from backend.data_access import read_csv

def stations(city="", state="", charger_type="", operator=""):
    rows=read_csv("charging/charging_stations.csv")
    return [r for r in rows if (not city or r['city']==city) and (not state or r['state']==state) and (not charger_type or r['charger_type']==charger_type) and (not operator or r['operator']==operator)]
