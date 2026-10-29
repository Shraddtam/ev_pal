from collections import defaultdict
from backend.data_access import number, read_csv

def insights(state="", manufacturer="", vehicle_id=""):
    rows=[r for r in read_csv("market/registrations.csv") if (not state or r['state']==state) and (not manufacturer or r['manufacturer']==manufacturer) and (not vehicle_id or r['vehicle_id']==vehicle_id)]
    monthly=defaultdict(float); states=defaultdict(float); makers=defaultdict(float)
    for r in rows: monthly[r['month']]+=number(r['registrations']); states[r['state']]+=number(r['registrations']); makers[r['manufacturer']]+=number(r['registrations'])
    series=lambda d:[{"label":k,"value":round(v)} for k,v in sorted(d.items())]
    return {"monthly":series(monthly),"states":series(states),"manufacturers":series(makers),"record_count":len(rows)}
