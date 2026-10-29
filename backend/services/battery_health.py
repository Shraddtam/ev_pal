from backend.data_access import number
from backend.services.vehicles import catalog, find
from backend.observability.logging import log_event
from backend.observability.metrics import record_operation_latency
from time import perf_counter

def estimate(payload):
    started=perf_counter()
    vehicle=find(payload.get("vehicle_id", "")) or catalog()[0]
    age=number(payload.get("age_months"),36); mileage=number(payload.get("mileage_km"),36000); temp=number(payload.get("temperature_c"),28); cycles=number(payload.get("charging_cycles"),300); fast=number(payload.get("fast_charge_percentage"),20); soc=number(payload.get("average_soc"),60); dod=number(payload.get("depth_of_discharge"),55)
    loss=.55+age*.026+mileage/1000*.010+fast*.018+max(temp-30,0)*.055+max(soc-80,0)*.07+max(dod-75,0)*.025+cycles*.0015
    soh=max(50,min(100,100-loss)); usable=number(vehicle['battery'].get('usable_capacity_kwh') or vehicle['battery'].get('battery_capacity_kwh')); factors=[]
    for label,val in [("Calendar age",age*.026),("Mileage",mileage/1000*.010),("Fast charging",fast*.018),("High temperature",max(temp-30,0)*.055),("High average SOC",max(soc-80,0)*.07)]:
        if val>.5: factors.append({"factor":label,"impact":round(val,2)})
    result={"estimate_label":"Development estimate — not a BMS measurement","vehicle":vehicle['model']+' '+vehicle['variant'],"soh_percent":round(soh,1),"remaining_capacity_kwh":round(usable*soh/100,1),"degradation_percent":round(100-soh,1),"degradation_rate_percent_per_year":round((100-soh)/max(age/12,.25),2),"confidence":"moderate" if 6<=age<=108 else "low","factors":factors or [{"factor":"Inputs are within low-stress bands","impact":0}]}
    duration_ms=round((perf_counter()-started)*1000,2)
    record_operation_latency("soh_inference", duration_ms)
    log_event("ml", "soh_estimated", "Battery-health development estimate completed", duration_ms=duration_ms, data={"model_name":"physics_inspired_heuristic","model_version":"0.1","vehicle_id":vehicle["vehicle_id"],"feature_count":10,"prediction_soh_percent":result["soh_percent"],"interval_available":False,"shap_computed":False})
    return result
