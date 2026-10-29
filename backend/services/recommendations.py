from backend.data_access import number
from backend.services.vehicles import catalog
from backend.observability.logging import log_event

def recommend(payload):
    daily=number(payload.get("daily_distance"),40); needs_range=number(payload.get("preferred_range"),300); home=str(payload.get("home_charging","true")).lower()=="true"; high=number(payload.get("highway_usage"),30); fast_priority=number(payload.get("fast_charging_priority"),3); longevity=number(payload.get("battery_longevity_priority"),3)
    scored=[]
    for v in catalog():
        b=v['battery']; r=number(v['claimed_range_km']); score=0
        score += max(0,25-abs(r-needs_range)/max(needs_range,1)*20)
        score += 15 if r >= daily*2.5 else 3
        score += (number(b['max_dc_power_kw'])/175)*fast_priority*3
        score += (4 if b['chemistry']=="LFP" else 2)*longevity
        if not home: score += number(b['max_dc_power_kw'])/10
        if high>55: score += number(v['motor_power_kw'])/35
        charging = f"{b['max_dc_power_kw']} kW DC capability" if b['max_dc_power_kw'] is not None else "DC charging specification unavailable in this catalogue entry"
        reasons=[f"{r:.0f} km claimed range for a {daily:.0f} km daily input",f"{b['chemistry']} battery chemistry",charging]
        trade=[]
        if r<needs_range: trade.append("Range is below the preferred range.")
        if b['chemistry']!="LFP": trade.append("Chemistry trade-off: this configuration is not LFP.")
        scored.append({"vehicle":v,"score":round(score,1),"reasons":reasons,"tradeoffs":trade or ["No major rule-based trade-off for these inputs."]})
    result=sorted(scored,key=lambda x:x['score'],reverse=True)[:3]
    log_event("app", "recommendations_generated", "Rule-based vehicle recommendations generated", data={"candidate_count":len(scored),"result_ids":[x["vehicle"]["vehicle_id"] for x in result],"engine":"rule_based_v1"})
    return result
