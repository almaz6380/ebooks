"""Erzeugt das KDP-Cover (1600 x 2560 px, JPG).

Ohne --hintergrund wird eine Peptidkette prozedural gezeichnet.
Mit --hintergrund wird ein (KI-)Bild verwendet und nur die Schrift gesetzt.

python3 werkzeuge/cover.py --sprache de [--hintergrund cover/bild.png]
Texte je Sprache: cover/texte.yaml
"""
import argparse
import math
import pathlib
import random

import yaml
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BASIS = pathlib.Path(__file__).resolve().parent.parent
B, H = 1600, 2560
S = 2  # Supersampling
FONT = "/usr/share/fonts/truetype/inter/InterDisplay-{}.ttf"


def schrift(gewicht, groesse):
    for kandidat in (FONT.format(gewicht), f"/usr/share/fonts/opentype/inter/InterDisplay-{gewicht}.otf"):
        if pathlib.Path(kandidat).exists():
            return ImageFont.truetype(kandidat, groesse * S)
    import subprocess
    pfad = subprocess.run(["fc-match", "-f", "%{file}", f"Inter Display:style={gewicht}"],
                          capture_output=True, text=True).stdout
    return ImageFont.truetype(pfad, groesse * S)


def hintergrund_zeichnen():
    w, h = B * S, H * S
    bild = Image.new("RGB", (w, h))
    px = bild.load()
    oben, unten = (8, 18, 38), (3, 8, 20)
    for y in range(h):
        t = y / h
        farbe = tuple(int(oben[i] * (1 - t) + unten[i] * t) for i in range(3))
        for x in range(0, w):
            px[x, y] = farbe
    # weicher Lichtfleck
    licht = Image.new("L", (w, h), 0)
    ImageDraw.Draw(licht).ellipse((w * 0.0, h * 0.50, w * 1.0, h * 0.92), fill=120)
    licht = licht.filter(ImageFilter.GaussianBlur(260 * S))
    bild = Image.composite(Image.new("RGB", (w, h), (20, 70, 90)), bild, licht)

    # Peptidkette entlang einer Kurve
    rnd = random.Random(7)
    punkte = []
    n = 17
    for i in range(n):
        t = i / (n - 1)
        x = w * (-0.05 + 1.1 * t)
        y = h * (0.79 - 0.15 * t) + math.sin(t * math.pi * 2.3) * h * 0.04
        r = (34 + 22 * math.sin(t * math.pi)) * S * (0.85 + 0.3 * rnd.random())
        punkte.append((x, y, r))

    glow = Image.new("RGB", (w, h), (0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for (x1, y1, _), (x2, y2, _) in zip(punkte, punkte[1:]):
        gd.line((x1, y1, x2, y2), fill=(60, 200, 210), width=10 * S)
    for x, y, r in punkte:
        gd.ellipse((x - r * 1.8, y - r * 1.8, x + r * 1.8, y + r * 1.8), fill=(40, 150, 170))
    glow = glow.filter(ImageFilter.GaussianBlur(40 * S))
    bild = Image.blend(bild, Image.composite(glow, bild, glow.convert("L")), 0.55)

    d = ImageDraw.Draw(bild)
    for (x1, y1, _), (x2, y2, _) in zip(punkte, punkte[1:]):
        d.line((x1, y1, x2, y2), fill=(150, 225, 230), width=4 * S)
    gold = (226, 178, 92)
    for i, (x, y, r) in enumerate(punkte):
        # Seitenkette
        winkel = (-1) ** i * (math.pi / 2.6)
        sx, sy = x + math.cos(winkel) * r * 2.2, y - math.sin(winkel) * r * 2.2
        d.line((x, y, sx, sy), fill=(150, 225, 230), width=3 * S)
        rs = r * 0.42
        d.ellipse((sx - rs, sy - rs, sx + rs, sy + rs), fill=gold if i % 3 == 0 else (90, 190, 200))
        # Kugel mit Glanz
        for k in range(int(r), 0, -1):
            t = k / r
            farbe = (int(30 + 120 * (1 - t)), int(120 + 110 * (1 - t)), int(140 + 100 * (1 - t)))
            versatz = (1 - t) * r * 0.35
            d.ellipse((x - k - versatz, y - k - versatz, x + k - versatz, y + k - versatz), fill=farbe)
    return bild


def text_mittig(d, y, text, font, farbe, sperrung=0):
    if sperrung:
        breite = sum(d.textlength(c, font=font) for c in text) + sperrung * S * (len(text) - 1)
        x = (B * S - breite) / 2
        for c in text:
            d.text((x, y), c, font=font, fill=farbe)
            x += d.textlength(c, font=font) + sperrung * S
    else:
        breite = d.textlength(text, font=font)
        d.text(((B * S - breite) / 2, y), text, font=font, fill=farbe)
    box = d.textbbox((0, y), text, font=font)
    return box[3]


def umbrechen(d, text, font, max_breite):
    zeilen, zeile = [], ""
    for wort in text.split():
        probe = (zeile + " " + wort).strip()
        if d.textlength(probe, font=font) <= max_breite * S:
            zeile = probe
        else:
            zeilen.append(zeile)
            zeile = wort
    zeilen.append(zeile)
    return zeilen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sprache", default="de")
    ap.add_argument("--hintergrund")
    a = ap.parse_args()
    t = yaml.safe_load((BASIS / "cover/texte.yaml").read_text())[a.sprache]

    if a.hintergrund:
        bild = Image.open(a.hintergrund).convert("RGB")
        f = max(B * S / bild.width, H * S / bild.height)
        bild = bild.resize((int(bild.width * f), int(bild.height * f)), Image.LANCZOS)
        l, o = (bild.width - B * S) // 2, (bild.height - H * S) // 2
        bild = bild.crop((l, o, l + B * S, o + H * S))
    else:
        bild = hintergrund_zeichnen()

    # Abdunkeln oben und unten für Lesbarkeit
    maske = Image.new("L", (1, H * S))
    for y in range(H * S):
        t_ = y / (H * S)
        maske.putpixel((0, y), int(200 * max(0, 1 - t_ / 0.42) ** 1.4 + 210 * max(0, (t_ - 0.80) / 0.20) ** 1.2))
    maske = maske.resize((B * S, H * S))
    bild = Image.composite(Image.new("RGB", bild.size, (2, 6, 16)), bild, maske)

    d = ImageDraw.Draw(bild)
    gold, weiss, grau = (226, 184, 104), (246, 244, 238), (176, 196, 206)

    y = 230 * S
    y = text_mittig(d, y, t["oben"].upper(), schrift("SemiBold", 34), gold, sperrung=8) + 70 * S
    for zeile in t["titel"]:
        y = text_mittig(d, y, zeile, schrift("Bold", t.get("titelgroesse", 168)), weiss) + 34 * S
    y += 40 * S
    d.line(((B / 2 - 90) * S, y, (B / 2 + 90) * S, y), fill=gold, width=4 * S)
    y += 60 * S
    for zeile in umbrechen(d, t["untertitel"], schrift("Medium", 64), 1300):
        y = text_mittig(d, y, zeile, schrift("Medium", 64), weiss) + 22 * S
    y += 30 * S
    for zeile in umbrechen(d, t["zeile"], schrift("Regular", 46), 1300):
        y = text_mittig(d, y, zeile, schrift("Regular", 46), grau) + 18 * S

    if t.get("autor"):
        text_mittig(d, (H - 300) * S, t["badge"].upper(), schrift("SemiBold", 34), gold, sperrung=6)
        text_mittig(d, (H - 210) * S, t["autor"], schrift("SemiBold", 84), weiss, sperrung=4)
    else:  # ohne Autorennamen: nur das Stand-Band unten
        text_mittig(d, (H - 190) * S, t["badge"].upper(), schrift("SemiBold", 38), gold, sperrung=6)

    bild = bild.resize((B, H), Image.LANCZOS)
    ziel = BASIS / f"cover/cover_{a.sprache}.jpg"
    bild.save(ziel, quality=92, dpi=(300, 300))
    print(ziel)


if __name__ == "__main__":
    main()
