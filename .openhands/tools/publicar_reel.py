"""Publica un video ya montado y revisado.

Hace las tres cosas, en este orden:
  1. Crea la Release publica del MP4 en el repositorio de videos (openframes).
  2. Anade la entrada a la cola del publicador (hypervideo): queue.json y el CSV.
  3. Dispara la Action manual 'publish-reel' con la hora pedida.

Uso:
  python3 publicar_reel.py --slug mkt-02-google-ads-trafico-correcto \
      --title "Google Ads: llegar solo a los cinco que importan (caso Alec Brownstein, 2010)" \
      --caption-file videos/mkt-02-google-ads-trafico-correcto/PUBLICACION.md \
      --duration 38.9 --publish-at "2026-10-14T17:30:00+02:00"

Necesita GITHUB_TOKEN en el entorno. Para no publicar ahora mismo, --publish-at acepta una hora ISO
con desfase (o "now"). La publicacion la ejecuta n8n desde el servidor a esa hora: no hace falta que
nadie este conectado.
"""

import argparse
import base64
import csv
import datetime
import hashlib
import io
import json
import os
import pathlib
import time
import urllib.error
import urllib.request

OPEN = "specialcowboy69/openframes"
HYP = "specialcowboy69/hypervideo"
API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
RAIZ = pathlib.Path(__file__).resolve().parents[2]


def api(url, data=None, method=None, ctype="application/json"):
    req = urllib.request.Request(url, data=data, method=method or ("POST" if data is not None else "GET"))
    for k, v in (("Authorization", "Bearer " + TOKEN), ("Accept", "application/vnd.github+json"),
                 ("User-Agent", "openframes-agent")):
        req.add_header(k, v)
    if data is not None and ctype:
        req.add_header("Content-Type", ctype)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")[:500]


def leer(repo, path):
    code, d = api(f"{API}/repos/{repo}/contents/{path}")
    if code != 200:
        raise SystemExit(f"no puedo leer {path}: {d}")
    return base64.b64decode(d["content"]).decode("utf-8"), d["sha"]


def guardar(repo, path, texto, sha, mensaje):
    code, d = api(f"{API}/repos/{repo}/contents/{path}", method="PUT", data=json.dumps({
        "message": mensaje, "content": base64.b64encode(texto.encode()).decode(),
        "sha": sha, "branch": "main"}).encode())
    if code not in (200, 201):
        raise SystemExit(f"error {code} guardando {path}: {d}")
    print(f"  guardado {path} · commit {d.get('commit', {}).get('sha', '')[:9]}")


def insertar_en_cola(crudo, item):
    cola = json.loads(crudo)
    assert not [i for i in cola["items"] if i.get("slug") == item["slug"]], "ya existe una entrada con ese slug"
    dec = json.JSONDecoder()
    pos = crudo.index("[", crudo.index('"items"')) + 1
    fin = ini = None
    while True:
        while pos < len(crudo) and crudo[pos] in " \t\r\n,":
            pos += 1
        if crudo[pos] == "]":
            break
        ini = pos
        _, fin = dec.raw_decode(crudo, pos)
        pos = fin
    sangria = crudo[crudo.rfind("\n", 0, ini) + 1:ini]
    bloque = "\n".join(sangria + l for l in json.dumps(item, ensure_ascii=False, indent=2).splitlines())
    nuevo = crudo[:fin] + ",\n" + bloque + crudo[fin:]
    val = json.loads(nuevo)
    assert [i["slug"] for i in val["items"]][-1] == item["slug"]
    assert len(val["items"]) == len(cola["items"]) + 1
    return nuevo, len(val["items"])


def fila_csv(crudo, plano):
    filas = list(csv.reader(io.StringIO(crudo)))
    cab = filas[0]
    fila = [str(plano.get(c.strip().lower().replace(" ", "_"), "")) for c in cab]
    fin = "\r\n" if "\r\n" in crudo else "\n"
    nuevo = crudo.rstrip("\r\n") + fin + ",".join(
        '"' + x.replace('"', '""') + '"' if any(c in x for c in ',"\n\r') else x for x in fila) + fin
    comp = list(csv.reader(io.StringIO(nuevo)))
    assert len(comp) == len(filas) + 1
    assert comp[-1][cab.index("slug")] == plano["slug"]
    return nuevo, len(comp) - 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--caption-file", required=True)
    ap.add_argument("--duration", type=float, required=True)
    ap.add_argument("--publish-at", required=True, help='ISO con desfase, p.ej. 2026-10-14T17:30:00+02:00')
    ap.add_argument("--platforms", default="instagram,facebook,tiktok,youtube")
    args = ap.parse_args()

    if not TOKEN:
        raise SystemExit("falta GITHUB_TOKEN")
    slug = args.slug
    tag = f"video-{slug}"
    hoy = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    caption = (RAIZ / args.caption_file).read_text(encoding="utf-8").strip()
    mp4 = RAIZ / "videos" / slug / "renders" / "video.mp4"
    if not mp4.exists():
        raise SystemExit(f"no encuentro el MP4: {mp4}")

    h = hashlib.sha256()
    with mp4.open("rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    sha = h.hexdigest()
    print(f"mp4: {mp4.stat().st_size} bytes · sha256 {sha}")
    print(f"publicacion programada para: {args.publish_at}")

    # 1) Release publica
    code, rel = api(f"{API}/repos/{OPEN}/releases/tags/{tag}")
    if code != 200:
        cuerpo = json.dumps({"tag_name": tag, "name": f"Video · {slug}", "draft": False, "prerelease": False,
                             "body": f"Video de la serie de casos de estudio.\n\n- 9:16 · 1080x1920 · {args.duration} s · voz es-ES\n"
                                     f"- `{slug}.mp4` · sha256 `{sha}`\n"}).encode()
        code, rel = api(f"{API}/repos/{OPEN}/releases", data=cuerpo)
        if code not in (200, 201):
            raise SystemExit(f"no se pudo crear la Release: {code} {rel}")
        print("Release creada:", rel["html_url"])
    else:
        print("la Release ya existia:", rel["html_url"])
    if f"{slug}.mp4" not in {a["name"] for a in rel.get("assets", [])}:
        code, sub = api(f"https://uploads.github.com/repos/{OPEN}/releases/{rel['id']}/assets?name={slug}.mp4",
                        data=mp4.read_bytes(), ctype="video/mp4")
        if code not in (200, 201):
            raise SystemExit(f"no se pudo subir el asset: {code} {sub}")
        print("asset subido · digest segun GitHub:", sub.get("digest"))
    url_mp4 = f"https://github.com/{OPEN}/releases/download/{tag}/{slug}.mp4"
    req = urllib.request.Request(url_mp4, headers={"User-Agent": "openframes-agent"})
    with urllib.request.urlopen(req, timeout=300) as r:
        h2 = hashlib.sha256(r.read()).hexdigest()
    print("descarga publica:", "HASH COINCIDE" if h2 == sha else "¡HASH DISTINTO!")

    # 2) cola
    item = {"slug": slug, "title": args.title, "status": "needs_review", "created_at": hoy, "updated_at": hoy,
            "template": "faceless-explainer", "duration_target_s": args.duration, "persona": "", "caption": caption,
            "review": {"status": "needs_review"},
            "outputs": {"content_folder": "", "project_folder": f"videos/{slug}", "zip": "", "render": url_mp4,
                        "preview": "", "cover": ""},
            "render_sha256": sha}
    crudo, sha_json = leer(HYP, "content/video-queue/queue.json")
    nuevo, n = insertar_en_cola(crudo, item)
    print(f"queue.json: {n} items · el nuevo al final")
    guardar(HYP, "content/video-queue/queue.json", nuevo, sha_json, f"chore: enqueue {slug} scheduled for {args.publish_at}")

    crudo_csv, sha_csv = leer(HYP, "content/video-queue/video-queue.csv")
    plano = {"slug": slug, "status": "needs_review", "title": args.title, "cta": "Guarda esto",
             "template": "faceless-explainer", "duration_target_s": str(args.duration), "voiceover_status": "generated",
             "render_mode": "draft", "render_url": url_mp4,
             "notes": f"MP4 en la Release publica de openframes; sha256 {sha[:16]}… Programada para {args.publish_at}.",
             "content_folder": f"videos/{slug}", "last_updated": hoy}
    nuevo_csv, filas = fila_csv(crudo_csv, plano)
    print(f"csv: {filas} filas · la nueva con slug y estado correctos")
    guardar(HYP, "content/video-queue/video-queue.csv", nuevo_csv, sha_csv, f"chore: enqueue {slug} in the csv")

    # 3) Action programada
    payload = {"ref": "main", "inputs": {"slug": slug, "caption": caption, "publish_at": args.publish_at,
                                         "platforms": args.platforms, "include_cover": "false",
                                         "confirmation": f"PUBLICAR {slug}"}}
    code, resp = api(f"{API}/repos/{HYP}/actions/workflows/publish-reel.yml/dispatches",
                     data=json.dumps(payload).encode())
    print(f"dispatch -> HTTP {code} {resp if code >= 300 else 'aceptado'}")
    if code != 204:
        raise SystemExit(1)
    time.sleep(20)
    code, runs = api(f"{API}/repos/{HYP}/actions/workflows/publish-reel.yml/runs?event=workflow_dispatch&per_page=1")
    r = (runs.get("workflow_runs") or [{}])[0]
    print(f"run {r.get('run_number')} · {r.get('status')}/{r.get('conclusion')} · {r.get('html_url')}")
    print("la publicacion la ejecuta n8n desde el servidor; no hace falta que nadie este conectado")


if __name__ == "__main__":
    main()
