import json, glob, collections, os
LAUFEND={"RECRUITING","ACTIVE_NOT_RECRUITING","NOT_YET_RECRUITING","ENROLLING_BY_INVITATION"}
AUSSCHLUSS_DATEI={'gonadorelin'}  # GnRH-Analoga dominieren
alle={}; hud=set(); gnrh=set(); proPep=collections.defaultdict(set); grp={}
gesamt_eintraege=0
for f in sorted(glob.glob('recherche/studien/*.json')):
    k=os.path.basename(f)[:-5]; d=json.load(open(f)); grp[k]=d.get('gruppe')
    for s in d.get('ctgov',[]):
        gesamt_eintraege+=1
        if 'hudson' in (s.get('sponsor') or '').lower(): hud.add(s['nct']); continue
        if k in AUSSCHLUSS_DATEI:
            gnrh.add(s['nct']); continue
        alle.setdefault(s['nct'],s); proPep[s['nct']].add(k)
print('Einträge gesamt (mit Doppelungen):',gesamt_eintraege,'eindeutig nach Ausschluss:',len(alle),'Hudson:',len(hud),'Gonadorelin-Datei:',len(gnrh))
lauf={n:s for n,s in alle.items() if s['status'] in LAUFEND and s.get('typ')=='INTERVENTIONAL'}
print('laufend interventionell:',len(lauf))
def ph(p):
    return {'PHASE3':'Phase 3','PHASE2,PHASE3':'Phase 2/3','PHASE2':'Phase 2','PHASE1,PHASE2':'Phase 1/2','PHASE1':'Phase 1','EARLY_PHASE1':'Phase 1','PHASE4':'Phase 4','':'ohne Phase','NA':'ohne Phase'}.get(p or '', p)
c=collections.Counter(ph(s['phase']) for s in lauf.values()); print(c)
st=collections.Counter((ph(s['phase']),s['status']) for s in lauf.values())
for k in sorted(st): print(k,st[k])
# nach Gruppe
G=collections.defaultdict(collections.Counter)
for n,s in lauf.items():
    gs={grp[k] for k in proPep[n]}
    for g in gs: G[g][ph(s['phase'])]+=1
for g in sorted(G, key=str): print(g, dict(G[g]))
# gruppe A phase3 list
json.dump({n:dict(s,peptide=sorted(proPep[n])) for n,s in lauf.items()}, open('/tmp/claude-0/-home-user-ebooks/29fe1b24-a774-5c4a-92e4-dd1d1dc503f0/scratchpad/lauf.json','w'),ensure_ascii=False)
