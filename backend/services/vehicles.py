from backend.data_access import number
from backend.services.real_catalog import CATALOGUE

VEHICLE_FIELDS = ["vehicle_id","manufacturer","model","variant","body_type","ex_showroom_price","estimated_on_road_price","motor_power_kw","torque_nm","acceleration_0_100_sec","claimed_range_km","mixed_real_world_range_km","efficiency_kwh_per_100km","warranty_years","battery_warranty_years","adas_level","safety_features"]
BATTERY_FIELDS = ["vehicle_id","battery_capacity_kwh","usable_capacity_kwh","chemistry","thermal_management","cooling_type","battery_warranty_years","battery_warranty_km","max_ac_power_kw","max_dc_power_kw","charging_10_80_minutes","charging_20_80_minutes","fast_charging_supported","v2l_supported"]

def catalog():
    return CATALOGUE

def find(vehicle_id: str):
    return next((row for row in catalog() if row["vehicle_id"] == vehicle_id), None)

def search(query="", manufacturer="", body_type="", chemistry="", min_price=0, max_price=10**12, min_range=0, sort="price"):
    query=query.lower().strip()
    rows=[]
    for row in catalog():
        haystack=f"{row['manufacturer']} {row['model']} {row['variant']}".lower()
        if query and query not in haystack: continue
        if manufacturer and row["manufacturer"] != manufacturer: continue
        if body_type and row["body_type"] != body_type: continue
        if chemistry and row["battery"].get("chemistry") != chemistry: continue
        # The verified catalogue is deliberately not a city-specific retail-price feed.
        if row["ex_showroom_price"] is not None and not min_price <= number(row["ex_showroom_price"]) <= max_price: continue
        if number(row["claimed_range_km"]) < min_range: continue
        rows.append(row)
    key={"range":"claimed_range_km","efficiency":"efficiency_kwh_per_100km","price":"ex_showroom_price"}.get(sort,"claimed_range_km")
    return sorted(rows, key=lambda x:number(x.get(key)), reverse=sort=="range")

def detail(vehicle_id: str):
    vehicle=find(vehicle_id)
    if not vehicle: return None
    return {**vehicle, "ownership": None, "reviews": [],
            "ownership_note": "No verified ownership-cost, resale or owner-review data is currently attached to this model. Use the TCO calculator with your own inputs."}
