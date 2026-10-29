"""Satzvorbereitung beim Bauen (die Manuskripte selbst bleiben unverändert):

1. Klammern, die nur Quellenangaben enthalten, werden zu Fußnoten (auf dem Kindle als Popup).
2. Der Vorsichtshinweis „Stand 2026, bitte aktuell prüfen“ bleibt nur in Rechtslage-Abschnitten,
   im Kapitel Rechtlicher Rahmen und in Zeilen zum Dopingstatus; sonst wird er entfernt
   (ein allgemeiner Hinweis steht im Impressum).
"""
import re

# Eine Quellenangabe: optional „Autor [et al.] Jahr, “ + PMID, oder eine NCT-Nummer
_ZITAT = r"(?:(?:[^\s(),;:][^(),;:]{0,80}?,?\s+(?:19|20)\d\d[a-z]?,\s*)?(?:PMID\s*\d{6,9})|NCT\d{8})"
_NUR_ZITATE = re.compile(rf"\s?\(\s*({_ZITAT}(?:\s*[;,]\s*{_ZITAT})*)\s*\)")

HINWEIS = {
    "de": r"Stand 2026,? bitte (?:aktuell )?prüfen",
    "en": r"(?:status )?as of 2026[,;]? please check(?: for (?:updates|current (?:status|information)))?",
    "es": r"(?:situación|estado) en 2026[,;]? compru[ée]b(?:ese|elo|e)(?: (?:en su|la) (?:versión|información) actual(?:izada)?)?",
    "fr": r"état 2026,? à vérifier",
    "it": r"aggiornato al 2026,? da verificare",
    "nl": r"stand 2026,? (?:actuele situatie )?controleren",
    "pt": r"situação em 2026,? verificar(?: atualização)?",
}
RECHT = {
    "de": "Rechtslage", "en": "Legal status", "es": "Situación legal", "fr": "Statut juridique",
    "it": "Quadro normativo", "nl": "Juridische status", "pt": "Situação legal",
}


def fussnoten(text):
    aus = []
    for zeile in text.splitlines():
        if zeile.lstrip().startswith(("|", "#")):
            aus.append(zeile)
            continue
        aus.append(_NUR_ZITATE.sub(lambda m: f"^[{m.group(1).strip()}.]", zeile))
    return "\n".join(aus) + ("\n" if text.endswith("\n") else "")


def _entfernen(z, h):
    z = re.sub(rf"^\s*\*?\s*{h}\.?\s*\*?\s*$", "", z, flags=re.I)              # eigener Absatz
    z = re.sub(rf"\s*\(\s*{h}\.?\s*\)", "", z, flags=re.I)                       # (Hinweis)
    z = re.sub(rf"\s*[,;–—-]\s*\*?{h}\*?(?=[.)\s;,]|$)", "", z, flags=re.I)       # …, Hinweis
    z = re.sub(rf"\*?{h}\.\*?\s*", "", z, flags=re.I)                            # Hinweis. (Satz)
    return re.sub(r"\(\s*\)", "", z)


def hinweise(text, sprache, dateiname):
    """Pro Rechtslage-Abschnitt bleibt nur der letzte Hinweis; alle anderen werden entfernt."""
    if dateiname.startswith("15-") or sprache not in HINWEIS:
        return text
    h = HINWEIS[sprache]
    recht = RECHT[sprache].lower()
    zeilen = text.splitlines()
    behalten = set()
    abschnitt_recht, letzte = False, None
    for i, z in enumerate(zeilen + ["#"]):
        if z.startswith("#"):
            if abschnitt_recht and letzte is not None:
                behalten.add(letzte)
            abschnitt_recht = z.lstrip("# ").strip().lower().startswith(recht)
            letzte = None
        elif abschnitt_recht and re.search(h, z, re.I):
            letzte = i
    aus = [z if (i in behalten or not re.search(h, z, re.I)) else _entfernen(z, h)
           for i, z in enumerate(zeilen)]
    return "\n".join(aus) + ("\n" if text.endswith("\n") else "")


def vorbereiten(text, sprache, dateiname):
    return fussnoten(hinweise(text, sprache, dateiname))
