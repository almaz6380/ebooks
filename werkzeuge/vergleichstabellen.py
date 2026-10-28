"""Erzeugt Rohtabellen für Teil III aus recherche/vergleich/*.yaml."""
import pathlib, re, collections, yaml
B = pathlib.Path("/home/user/ebooks")
kap = {re.sub(r"^2[A-F]\d\d-", "", p.stem): p.stem[:4] for p in (B/"buch/kapitel").glob("2[A-F][0-9][0-9]-*.md")}
daten = []
for f in sorted((B/"recherche/vergleich").glob("*.yaml")):
    d = yaml.safe_load(f.read_text())
    d["slug"] = f.stem
    d["ord"] = kap.get(f.stem, "ZZZ")
    daten.append(d)
daten.sort(key=lambda d: d["ord"])
def z(n): return f"{n:,}".replace(",", ".")
for g in "ABCDEF":
    print(f"\n### Gruppe {g}\n")
    print("| Peptid | Evidenz | Zulassung EU / USA | Humanstudien / Register |\n|---|---|---|---|")
    for d in daten:
        if d["gruppe"] != g: continue
        print(f"| {d['name']} | {d['evidenz']} | EU: {d['zulassung_eu']}; USA: {d['zulassung_usa']} | {z(d['humanstudien'])} / {z(d['registerstudien'])} |")
    print("\n| Peptid | Kernergebnis | Hauptrisiko |\n|---|---|---|")
    for d in daten:
        if d["gruppe"] != g: continue
        print(f"| {d['name']} | {d['kernergebnis']} | {d['hauptrisiko']} |")
print()
c = collections.Counter(d["evidenz"] for d in daten); print("Evidenz gesamt", sorted(c.items()), len(daten))
for g in "ABCDEF":
    print(g, sorted(collections.Counter(d["evidenz"] for d in daten if d["gruppe"]==g).items()))
for d in daten:
    print("ZUL", d["evidenz"], d["name"], "|", d["zulassung_eu"], "|", d["zulassung_usa"])
for d in daten:
    print("WADA", d["name"], "|", d["wada"])
