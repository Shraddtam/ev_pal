from collections import Counter
from backend.data_access import number, read_csv
from backend.services.vehicles import catalog

def summary():
    vehicles=catalog(); stations=read_csv("charging/charging_stations.csv"); registrations=read_csv("market/registrations.csv")
    verified_dc = [v for v in vehicles if v['battery']['max_dc_power_kw'] is not None]
    return {"metrics":{"models":len(vehicles),"manufacturers":len({v['manufacturer'] for v in vehicles}),"average_range":round(sum(number(v['claimed_range_km']) for v in vehicles)/len(vehicles)),"average_battery":round(sum(number(v['battery']['battery_capacity_kwh']) for v in vehicles)/len(vehicles),1),"charging_stations":len(stations),"registration_total":sum(int(number(r['registrations'])) for r in registrations)},"charts":{"range":[{"label":v['model']+' '+v['variant'],"value":number(v['claimed_range_km'])} for v in vehicles],"chemistry":[{"label":k,"value":v} for k,v in Counter(x['battery']['chemistry'] for x in vehicles).items()],"charging":[{"label":v['model'],"value":number(v['battery']['max_dc_power_kw'])} for v in verified_dc]}}
