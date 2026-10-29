"""Reproducible synthetic data generator for EV PAL.

All values produced by this program are invented test data and must never be
represented as verified specifications, policies, measurements, or statistics.
"""
from __future__ import annotations

import csv
import json
import math
import random
from datetime import date, datetime, timedelta
from pathlib import Path

SEED = 1802026
rng = random.Random(SEED)
ROOT = Path(__file__).parent / "data"
NOW = "2026-09-20T00:00:00Z"
META = {
    "synthetic": "true", "source_type": "synthetic", "generated_at": NOW,
    "generation_method": "seeded_rule_based_simulation_v1", "source_reference": "",
}
VEHICLES = [
    ("EVP001","Aranya Electric","Aira","Base","hatchback",20.5,"LFP",1180,72,125,18.5,210,145),
    ("EVP002","Aranya Electric","Aira","Long Range","hatchback",29.0,"LFP",1260,95,155,15.2,315,185),
    ("EVP003","Nivara Mobility","Sutra","Urban","sedan",30.2,"NMC",1320,100,180,12.0,340,215),
    ("EVP004","Nivara Mobility","Sutra","Touring","sedan",42.0,"NMC",1480,125,230,9.4,465,250),
    ("EVP005","Tamas Auto","Rove","City","compact_suv",35.0,"LFP",1420,105,190,11.1,380,215),
    ("EVP006","Tamas Auto","Rove","Adventure","compact_suv",52.0,"NMC",1640,150,280,8.2,520,285),
    ("EVP007","Vayun Motors","Kite","Family","suv",48.0,"LFP",1710,130,250,9.6,490,270),
    ("EVP008","Vayun Motors","Kite","Premium","suv",62.0,"NMC",1880,180,340,7.1,570,330),
    ("EVP009","Prithvi EV","Mitra","Fleet","mpv",40.0,"LFP",1660,95,215,13.0,395,225),
    ("EVP010","Prithvi EV","Mitra","Executive","mpv",56.0,"NMC",1900,155,310,8.5,515,300),
    ("EVP011","Suryan Automotive","Nova","Sport","crossover",58.0,"NMC",1810,210,390,6.3,545,340),
    ("EVP012","Suryan Automotive","Nova","Grand","crossover",72.0,"NCA",2050,245,460,5.6,625,400),
]
CITIES = [("Bengaluru","Karnataka",12.9716,77.5946),("Mumbai","Maharashtra",19.0760,72.8777),("Pune","Maharashtra",18.5204,73.8567),("Delhi","Delhi",28.6139,77.2090),("Hyderabad","Telangana",17.3850,78.4867),("Chennai","Tamil Nadu",13.0827,80.2707),("Ahmedabad","Gujarat",23.0225,72.5714),("Kochi","Kerala",9.9312,76.2673)]

def n(x, digits=2): return round(float(x), digits)
def clamp(x, lo, hi): return max(lo, min(hi, x))
def iso(d): return d.isoformat() if hasattr(d, "isoformat") else str(d)

def write(name, rows, folder, ref="reference_only"):
    path = ROOT / folder / name
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = list(rows)
    if not rows: return
    fields = list(rows[0])
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    return {"path": str(path.relative_to(ROOT.parent)).replace("\\", "/"), "fields": fields, "rows": len(rows), "reference": ref}

def with_meta(row, reference="reference_only"):
    return {**row, **META, "real_source_type": reference}

def make_vehicles():
    rows=[]; batteries=[]
    for i,(vid,mfr,model,var,cat,cap,chem,weight,power,torque,accel,claim,price) in enumerate(VEHICLES):
        usable=n(cap*(.92 if chem=="LFP" else .90)); eff=n(15.2 + weight/470 + (power-80)/70 + rng.uniform(-.7,.7),1)
        mixed=n(usable/eff*100); city=n(mixed*1.10); highway=n(mixed*.87)
        dimensions = (3800+i*38, 1735+i*14, 1580+i*12, 2450+i*28)
        rows.append(with_meta({"vehicle_id":vid,"manufacturer":mfr,"model":model,"variant":var,"vehicle_category":cat,"body_type":cat,"launch_year":2023+i%4,"model_year":2026,"ex_showroom_price":price*100000,"estimated_on_road_price":n(price*1.13,2)*100000,"motor_type":"permanent_magnet_synchronous","motor_power_kw":power,"motor_power_bhp":n(power*1.341),"torque_nm":torque,"drive_type":"FWD" if i<9 else "RWD","kerb_weight_kg":weight,"length_mm":dimensions[0],"width_mm":dimensions[1],"height_mm":dimensions[2],"wheelbase_mm":dimensions[3],"ground_clearance_mm":170+(i%4)*8,"boot_capacity_l":280+(i%5)*42,"seating_capacity":5 if cat != "mpv" else 7,"top_speed_kmph":135+power//4,"acceleration_0_100_sec":accel,"claimed_range_km":claim,"city_range_km":city,"highway_range_km":highway,"mixed_real_world_range_km":mixed,"efficiency_kwh_per_100km":eff,"warranty_years":3,"warranty_km":100000,"battery_warranty_years":8,"battery_warranty_km":160000,"safety_features":"ABS|ESC|6_airbags|TPMS","adas_level":0 if i<7 else 2,"infotainment_features":"10in_display|Android_Auto|CarPlay","connected_features":"remote_lock|charge_status|trip_history"}))
        density={"LFP":145,"NMC":185,"NCA":205}[chem]; battwt=n(cap*1000/density*1.10,1); dc=25 if cap<35 else (60 if cap<55 else 110)
        batteries.append(with_meta({"battery_id":"BAT"+vid[-3:],"vehicle_id":vid,"battery_capacity_kwh":cap,"usable_capacity_kwh":usable,"chemistry":chem,"cell_format":"prismatic" if chem=="LFP" else "pouch","nominal_voltage":400 if cap<60 else 800,"energy_density_wh_kg":density,"battery_weight_kg":battwt,"thermal_management":"liquid" if chem!="LFP" or cap>40 else "air_assisted","cooling_type":"liquid" if chem!="LFP" or cap>40 else "forced_air","manufacturer_if_known":"Synthetic Cellworks","battery_warranty_years":8,"battery_warranty_km":160000,"max_ac_power_kw":7.2 if cap<55 else 11,"max_dc_power_kw":dc,"charging_10_80_minutes":round(cap*.7/dc*60+8),"charging_20_80_minutes":round(cap*.6/dc*60+7),"recommended_soc_range":"20-80","fast_charging_supported":"true","v2l_supported":"true" if i in (5,7,11) else "false","battery_pack_architecture":"cell_to_pack" if i>6 else "module_based"}))
    return rows,batteries

def make_soh():
    base={v[0]:v for v in VEHICLES}; rows=[]
    for j in range(24000):
        vid = VEHICLES[j%len(VEHICLES)][0]; v=base[vid]; chem=v[6]; age=rng.randint(2,108); monthly=max(250,rng.gauss(1150,480)); odo=max(300,int(monthly*age*rng.uniform(.86,1.14))); fast=clamp(rng.betavariate(2,7)*100,0,75); temp=clamp(rng.gauss(28,7),8,48); high=clamp(rng.gauss(95,22),5,240); cycles=max(5,int(odo/(v[5]/(16+rng.random()*5))*1.15)); chem_pen={"LFP":.0,"NMC":.45,"NCA":.7}[chem]; deg=.55+age*.026+(odo/1000)*.010+fast*.018+max(temp-30,0)*.055+high*.008+chem_pen+rng.gauss(0,.9)
        # rare controlled edge cases, still physically valid
        if j%997==0: deg*=.42
        if j%991==0: deg+=10
        soh=clamp(100-deg,50,100); cap=n(v[5]*(.92 if chem=="LFP" else .90)*soh/100)
        rows.append(with_meta({"observation_id":f"SOH{j:06d}","battery_instance_id":f"{vid}_B{j%80:02d}","vehicle_id":vid,"battery_chemistry":chem,"vehicle_age_months":age,"odometer_km":odo,"ambient_temperature_c":n(temp),"average_temperature_c":n(temp+rng.uniform(2,8)),"average_soc_percent":n(rng.uniform(42,68)),"minimum_soc_percent":n(rng.uniform(5,22)),"maximum_soc_percent":n(rng.uniform(80,100)),"average_depth_of_discharge":n(rng.uniform(35,78)),"charging_cycles":cycles,"fast_charge_cycles":round(cycles*fast/100),"fast_charge_percentage":n(fast),"slow_charge_percentage":n(100-fast),"average_charge_power_kw":n(3.3+fast/100*40),"average_discharge_power_kw":n(13+rng.uniform(0,12)),"daily_distance_km":n(monthly/30),"monthly_distance_km":n(monthly),"highway_usage_percentage":n(rng.uniform(15,75)),"city_usage_percentage":n(rng.uniform(25,85)),"energy_consumption_kwh_per_100km":n(16+v[7]/550+rng.uniform(-2,2)),"charging_efficiency":n(clamp(rng.gauss(.91,.025),.80,.97),3),"time_at_high_soc_hours":n(high),"time_at_low_soc_hours":n(rng.uniform(2,100)),"thermal_events":0 if rng.random()>.06 else rng.randint(1,3),"calendar_age_months":age,"estimated_capacity_kwh":cap,"capacity_retention_percent":n(soh),"soh_percent":n(soh),"degradation_rate_percent_per_year":n((100-soh)/max(age/12,.25)),"remaining_useful_life_months":round(clamp((soh-70)*7.2+rng.gauss(0,8),0,180))}))
    return rows

def make_sessions():
    rows=[]; start=datetime(2024,1,1)
    types=[("home_ac",7.2,"home"),("workplace_ac",7.2,"workplace"),("public_ac",11,"public"),("public_dc",60,"public")]
    for i in range(5000):
        vid=VEHICLES[i%12][0]; typ,power,loc=rng.choices(types,[42,12,24,22])[0]; soc=rng.randint(8,65); end=rng.randint(max(soc+10,55),98); cap=next(x[5] for x in VEHICLES if x[0]==vid); delivered=n(cap*(end-soc)/100/rng.uniform(.86,.95)); success=rng.random()>.035
        rows.append(with_meta({"session_id":f"CS{i:06d}","vehicle_id":vid,"timestamp":iso(start+timedelta(hours=i*9+rng.randint(0,8))),"start_soc":soc,"end_soc":end,"energy_delivered_kwh":delivered,"charging_type":typ,"charger_power_kw":power,"duration_minutes":round(delivered/power*60+rng.uniform(3,15)),"ambient_temperature_c":n(rng.gauss(29,6)),"location_type":loc,"fast_charge":"true" if "dc" in typ else "false","charging_cost":n(delivered*(10.5 if "public" in typ else 7.0)),"battery_temperature_c":n(rng.gauss(34 if "dc" in typ else 29,4)),"charging_efficiency":n(rng.uniform(.84,.96),3),"session_success":str(success).lower(),"interruption_reason":"" if success else rng.choice(["connector_fault","payment_timeout","grid_interruption"])}))
    return rows

def make_trips():
    rows=[]
    for i in range(5000):
        vid=VEHICLES[i%12][0]; dist=n(clamp(rng.lognormvariate(3.35,.65),5,420)); road=rng.choice(["urban","highway","mixed"]); speed=n({"urban":rng.uniform(22,45),"highway":rng.uniform(65,105),"mixed":rng.uniform(40,75)}[road]); ac=rng.random()<.70; temp=n(rng.gauss(28,7)); factor=1+(speed>80)*.17+ac*.10+(temp<15)*.12+rng.uniform(-.08,.10); eff=n((15+next(v[7] for v in VEHICLES if v[0]==vid)/600)*factor,2); used=n(dist*eff/100); start_soc=rng.randint(45,100); end=max(4,round(start_soc-used/next(v[5] for v in VEHICLES if v[0]==vid)*100))
        rows.append(with_meta({"trip_id":f"TR{i:06d}","vehicle_id":vid,"date":iso(date(2024,1,1)+timedelta(days=i%900)),"distance_km":dist,"starting_soc":start_soc,"ending_soc":end,"energy_used_kwh":used,"average_speed_kmph":speed,"maximum_speed_kmph":n(speed+rng.uniform(15,45)),"ambient_temperature_c":temp,"traffic_level":rng.choice(["low","medium","high"]),"road_type":road,"city_highway_ratio":n(rng.random()),"occupancy":rng.randint(1,5),"air_conditioning_used":str(ac).lower(),"tyre_pressure_condition":rng.choices(["normal","low"],[.91,.09])[0],"driving_style":rng.choice(["calm","normal","aggressive"]),"rain":str(rng.random()<.18).lower(),"elevation_change_m":rng.randint(-180,420),"calculated_efficiency":eff,"estimated_range_km":n(next(v[5] for v in VEHICLES if v[0]==vid)/eff*100)}))
    return rows

def simple_sets():
    stations=[]; tariffs=[]; climate=[]; registrations=[]; policies=[]; regulations=[]; warranties=[]; tco=[]; resale=[]; reviews=[]; safety=[]; users=[]; cells=[]
    for ci,(city,state,lat,lon) in enumerate(CITIES):
        for k in range(5): stations.append(with_meta({"station_id":f"ST{ci:02d}{k:02d}","operator":"Synthetic Charge Network","state":state,"city":city,"latitude":n(lat+rng.uniform(-.08,.08),5),"longitude":n(lon+rng.uniform(-.08,.08),5),"station_type":"public","charger_type":"DC" if k%2 else "AC","connector_type":"CCS2","power_kw":60 if k%2 else 11,"number_of_ports":rng.randint(2,8),"availability":n(rng.uniform(.72,.99)),"operating_hours":"24x7","price_per_kwh":n(rng.uniform(13,22)),"price_per_minute":0,"payment_methods":"UPI|card|app","network_status":"operational","installation_year":2023+k}))
        tariffs.append(with_meta({"tariff_id":f"TAR{ci:02d}","state":state,"discom":f"Synthetic {state} Distribution","consumer_category":"residential_ev_estimate","fixed_charge":n(rng.uniform(60,180)),"energy_charge_per_kwh":n(rng.uniform(5.5,8.8)),"tod_peak_rate":n(rng.uniform(8,13)),"tod_offpeak_rate":n(rng.uniform(4,6.5)),"ev_specific_rate":n(rng.uniform(5,8)),"taxes":n(rng.uniform(.2,1.2)),"surcharge":n(rng.uniform(0,.8)),"effective_from":"2026-01-01","effective_until":"2026-12-31"},"tariff_reference_only"))
        for month in range(1,13): climate.append(with_meta({"city":city,"state":state,"month":month,"average_temperature":n(25+7*math.sin((month-3)/12*math.tau)+rng.uniform(-3,3)),"minimum_temperature":n(17+rng.uniform(-5,6)),"maximum_temperature":n(34+rng.uniform(-4,8)),"humidity":round(rng.uniform(40,90)),"rainfall":n(rng.uniform(0,350)),"extreme_temperature_days":rng.randint(0,10)}))
    for p,(vid,mfr,model,var,cat,cap,*_) in enumerate(VEHICLES):
        warranties.append(with_meta({"manufacturer":mfr,"vehicle_id":vid,"basic_warranty_years":3,"basic_warranty_km":100000,"battery_warranty_years":8,"battery_warranty_km":160000,"battery_warranty_soh_threshold":70,"roadside_assistance":"3 years","service_interval_km":15000,"service_interval_months":12,"warranty_exclusions":"misuse|unauthorized_modification","extended_warranty":"available_synthetic_scenario","software_support_years":6,"battery_replacement_policy":"synthetic assessment process"}))
        for years in (3,5,8,10):
            purchase=(1400000+p*160000); annual=12000+9000*1.8; charging=12000*(16+p/2)/100*(.8*7+.2*16)*years; resale_pct=max(.18,.72-years*.055-p*.005); total=purchase+80000+charging+annual*years+purchase*.09*years-purchase*resale_pct
            tco.append(with_meta({"vehicle_id":vid,"ownership_years":years,"purchase_price":purchase,"subsidy":0,"registration_cost":purchase*.08,"insurance_annual":purchase*.022,"home_charger_cost":45000,"charger_installation_cost":15000,"annual_distance_km":12000,"electricity_price":7,"public_charging_percentage":20,"public_charging_price":16,"home_charging_price":7,"energy_efficiency":16+p/2,"charging_losses":10,"annual_maintenance":9000,"annual_tyre_cost":7000,"annual_insurance":purchase*.022,"financing_rate":9.5,"loan_period":5,"expected_resale_percentage":n(resale_pct*100),"purchase_cost":purchase,"running_cost":n(charging),"charging_cost":n(charging),"maintenance_cost":annual*years,"insurance":n(purchase*.022*years),"financing":n(purchase*.09*years),"depreciation":n(purchase*(1-resale_pct)),"resale_value":n(purchase*resale_pct),"total_ownership_cost":n(total),"cost_per_km":n(total/(12000*years)),"monthly_ownership_cost":n(total/(years*12))}))
        for age in range(1,9):
            soh=clamp(98-age*2.8+rng.gauss(0,2),62,100); price=purchase*(.86**age)*(0.85+soh/100*.15)*rng.uniform(.88,1.10)
            resale.append(with_meta({"vehicle_id":vid,"vehicle_age_years":age,"odometer_km":round(age*rng.uniform(9000,19000)),"soh_percent":n(soh),"warranty_remaining_months":max(0,96-age*12),"condition":rng.choice(["excellent","good","fair"]),"accident_history":str(rng.random()<.12).lower(),"service_history":rng.choice(["complete","partial"]),"location":rng.choice(CITIES)[0],"original_price":purchase,"used_market_price":n(price),"market_demand_index":n(rng.uniform(35,90)),"resale_percentage":n(price/purchase*100)}))
        for r in range(12): reviews.append(with_meta({"review_id":f"RV{p:02d}{r:02d}","vehicle_id":vid,"review_date":f"2026-{r+1:02d}-15","ownership_months":rng.randint(1,36),"odometer_km":rng.randint(500,50000),"rating":rng.randint(2,5),"range_experience":rng.choice(["above_expected","as_expected","below_expected"]),"charging_experience":rng.choice(["easy","mixed","difficult"]),"service_experience":rng.choice(["good","mixed","poor"]),"battery_experience":rng.choice(["stable","adequate","concern"]),"software_experience":rng.choice(["smooth","minor_bugs","issues"]),"comfort":rng.randint(2,5),"reliability":rng.randint(2,5),"pros":"synthetic positive observation","cons":"synthetic improvement request","complaint_category":rng.choice(["none","range","charging","service","software"]),"sentiment":rng.choice(["positive","neutral","mixed","negative"]),"severity":rng.choice(["low","medium","high"])}))
        if p%3==0: safety.append(with_meta({"event_id":f"SE{p:03d}","vehicle_id":vid,"event_type":rng.choice(["service_campaign","software_issue","charging_issue","thermal_event"]),"component":"synthetic_component","severity":rng.choice(["low","medium","high"]),"date":"2026-06-01","affected_units":rng.randint(10,500),"description":"Fictional test safety event; not an actual recall.","resolution":"synthetic inspection or software update","status":"closed","officially_confirmed":"false"}))
    for i in range(12): policies.append(with_meta({"policy_id":f"POL{i:03d}","policy_name":f"Synthetic {CITIES[i%8][1]} EV Incentive 2026","jurisdiction":"state","state":CITIES[i%8][1],"vehicle_category":"passenger_ev","eligible_vehicle":"synthetic eligible model","eligibility_conditions":"synthetic test condition","incentive_type":"rebate","incentive_amount":rng.choice([25000,40000,60000]),"battery_capacity_condition":"minimum 20 kWh","vehicle_price_condition":"below synthetic cap","income_condition":"none","registration_condition":"state registration required","start_date":"2026-01-01","end_date":"2026-12-31","application_process":"synthetic test workflow","document_requirements":"synthetic proof list","status":"active" if i<8 else "expired","last_verified":"2026-09-20","official_source_url":"","source_type":"synthetic"},"policy_reference_only"))
    # Controlled conflicting versions: policy resolution logic should select the latest valid record.
    prior = dict(policies[1]); prior.update({"policy_id":"POL012","incentive_amount":25000,"end_date":"2026-06-30","status":"expired","last_verified":"2026-05-01"}); policies.append(prior)
    for i,cat in enumerate(["vehicle_registration","charging_infrastructure","battery_safety","battery_recycling","battery_waste","manufacturing","vehicle_testing","homologation","insurance","scrappage","environmental_compliance","charging_station_requirements"]): regulations.append(with_meta({"regulation_id":f"REG{i:03d}","title":f"Synthetic {cat.replace('_',' ').title()} Scenario","jurisdiction":"India scenario","category":cat,"effective_date":"2026-01-01","expiry_date":"2027-01-01","summary":"Synthetic RAG test scenario, not a law or official document.","requirements":"Fictional test requirements only.","applicability":"synthetic test records","document_version":"v1.0","last_updated":"2026-09-20"},"regulation_reference_only"))
    for m in range(24):
        for vid,mfr,*rest in VEHICLES:
            seasonal=1+.18*math.sin((m%12-8)/12*math.tau); reg=max(3,round((30+VEHICLES.index(next(v for v in VEHICLES if v[0]==vid))*5)*seasonal*rng.uniform(.75,1.25))); registrations.append(with_meta({"month":(date(2025,1,1)+timedelta(days=30*m)).strftime("%Y-%m"),"state":CITIES[m%8][1],"city":CITIES[m%8][0],"manufacturer":mfr,"vehicle_id":vid,"vehicle_category":"passenger_ev","registrations":reg,"market_share":n(rng.uniform(1,14)),"year_on_year_growth":n(rng.uniform(-8,55))}))
    for i in range(120):
        chem=rng.choice(["LFP","NMC","NCA"]); cyc=i%500; ret=clamp(100-.015*cyc-max(0,rng.gauss(0,1)),55,100); cells.append(with_meta({"cell_id":f"CELL{i//500:03d}","chemistry":chem,"cycle_number":cyc,"temperature":n(rng.uniform(20,45)),"charge_current":n(rng.uniform(.5,2)),"discharge_current":n(rng.uniform(.5,2.5)),"charge_capacity":n(3.1*ret/100),"discharge_capacity":n(3.0*ret/100),"internal_resistance":n(.04+cyc*.00008,4),"voltage":n(rng.uniform(3.2,4.2),3),"capacity_retention":n(ret),"soh":n(ret)},"public_dataset_structure_reference_only"))
    for i in range(100): users.append(with_meta({"user_id":f"USR{i:03d}","budget":rng.randint(12,45)*100000,"monthly_distance":rng.randint(300,3000),"daily_distance":rng.randint(10,120),"city":CITIES[i%8][0],"state":CITIES[i%8][1],"home_charging":str(rng.random()<.7).lower(),"workplace_charging":str(rng.random()<.35).lower(),"highway_usage":rng.randint(0,90),"preferred_range":rng.randint(200,550),"performance_priority":rng.randint(1,5),"safety_priority":rng.randint(1,5),"comfort_priority":rng.randint(1,5),"low_running_cost_priority":rng.randint(1,5),"fast_charging_priority":rng.randint(1,5),"battery_longevity_priority":rng.randint(1,5),"ownership_years":rng.choice([3,5,8,10]),"family_size":rng.randint(1,7),"recommendation_target_vehicle_id":rng.choice(VEHICLES)[0]}))
    return locals()

def docs(manifest):
    d=ROOT/"documentation"; d.mkdir(exist_ok=True)
    (d/"generation_methodology.md").write_text("# Generation methodology\n\nSeed `%d` drives rule-based simulations with correlated battery, vehicle, charging, climate and cost variables. Deliberate noise, missing source references, duplicate/conflicting test records and stale synthetic policy versions exercise validation paths. No record is real-world data.\n"%SEED,encoding="utf-8")
    (d/"relationships.md").write_text("# Relationships\n\n`vehicles.vehicle_id` joins batteries, sessions, trips, SOH observations, TCO, resale, reviews, warranties and safety events. `state` joins policies, tariffs, climate, stations and registrations. `manufacturer` joins vehicle, warranty and registration records.\n",encoding="utf-8")
    (d/"data_quality_report.md").write_text("# Intentional data quality conditions\n\n- SOH observations include rare unusually healthy and heavily degraded records, but SOH stays 50–100.\n- Charging sessions include failed connector, payment and grid interruption scenarios.\n- `schemes.csv` contains a controlled conflicting older version (`POL012`) of the Maharashtra scenario; it has a lower incentive and expired date. Use `last_verified`, dates and status when testing reconciliation.\n- Source references are empty or reference-only by design.\n- Synthetic review sentiment and safety events deliberately vary; safety events are fictional and not confirmed recalls.\n- Dataset rows carry synthetic metadata. Controlled duplicate-like observations and measurement noise support validation testing.\n",encoding="utf-8")
    lines=["# Data dictionary\n", "Every CSV is synthetic. Metadata fields mean: `synthetic` = true; `source_type` = synthetic; `generated_at` = generation timestamp; `generation_method` = seeded simulation; `source_reference` = blank; `real_source_type` identifies only the normal real-source category.\n"]
    for m in manifest:
        lines += [f"## {m['path']}\n", f"Rows: {m['rows']}. Reference class: `{m['reference']}`.\n", "| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |\n|---|---|---|---|---|---|---|---|\n"]
        for field in m['fields']:
            sample="metadata" if field in META or field in ("real_source_type",) else "synthetic value"
            lines.append(f"| {field} | string or numeric | Synthetic `{field}` field | varies | synthetic valid values | yes where applicable | {sample} | seeded rule based simulation |\n")
    (d/"data_dictionary.md").write_text("".join(lines),encoding="utf-8")
    (ROOT.parent/"README.md").write_text("# EV PAL synthetic data pack\n\nRun `python generate_evpal_data.py` to reproduce the datasets. Use these records only for development, test, demonstrations, RAG and ML experimentation.\n\n**All generated values are synthetic and must not be presented as real vehicle specifications, government policies, manufacturer claims, market statistics, battery measurements, or official data.**\n",encoding="utf-8")

def main():
    manifest=[]
    vehicles,batteries=make_vehicles(); manifest += [write("vehicles.csv",vehicles,"vehicles"),write("batteries.csv",batteries,"vehicles")]
    soh=make_soh(); manifest += [write("soh_dataset.csv",soh,"battery"),write("degradation_dataset.csv",soh,"battery")]
    # Split by battery instance prevents leakage. OOD consists of NCA instances not in training.
    groups=sorted({r["battery_instance_id"] for r in soh}); train=set(groups[:60*len(groups)//100]); valid=set(groups[60*len(groups)//100:80*len(groups)//100]); test=set(groups[80*len(groups)//100:]);
    manifest += [write("train.csv",(r for r in soh if r["battery_instance_id"] in train),"ml"),write("validation.csv",(r for r in soh if r["battery_instance_id"] in valid),"ml"),write("test.csv",(r for r in soh if r["battery_instance_id"] in test),"ml"),write("ood_test.csv",(r for r in soh if r["battery_chemistry"]=="NCA" and r["battery_instance_id"] in test),"ml")]
    manifest += [write("charging_sessions.csv",make_sessions(),"charging"),write("range_trips.csv",make_trips(),"battery")]
    sets=simple_sets()
    mapping={"stations":("charging_stations.csv","charging"),"tariffs":("electricity_tariffs.csv","economics"),"climate":("climate.csv","market"),"registrations":("registrations.csv","market"),"policies":("schemes.csv","policies"),"regulations":("regulations.csv","policies"),"warranties":("manufacturer_policies.csv","policies"),"tco":("tco_inputs.csv","economics"),"resale":("resale_market.csv","economics"),"reviews":("owner_reviews.csv","reviews"),"safety":("safety_events.csv","safety"),"users":("user_profiles.csv","users"),"cells":("experimental_cells.csv","battery")}
    for key,(name,folder) in mapping.items(): manifest.append(write(name,sets[key],folder))
    source=[with_meta({"source_id":"SRC001","source_name":"Synthetic generator","source_type":"synthetic","organization":"EV PAL development","url":"","document_title":"Synthetic data generation metadata","publication_date":"2026-09-20","collection_date":"2026-09-20","last_verified":"2026-09-20","valid_from":"2026-09-20","valid_until":"","reliability_level":"not_real_world","data_categories":"all"})]
    manifest.append(write("source_metadata.csv",source,"sources"))
    examples=ROOT/"examples"; examples.mkdir(exist_ok=True)
    (examples/"api_vehicle.json").write_text(json.dumps(vehicles[0],indent=2),encoding="utf-8")
    (examples/"rag_policy_scenario.md").write_text("# Synthetic policy scenario\n\nSynthetic Maharashtra EV Incentive 2026 is a fictional RAG test document. It is not an official policy, notification, scheme or claim. Example eligibility: state registration, passenger EV category and a synthetic price cap.\n",encoding="utf-8")
    docs(manifest)
    print(f"Generated {len(manifest)} CSV datasets under {ROOT}")
if __name__ == "__main__": main()
