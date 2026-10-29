"""Manufacturer-sourced vehicle catalogue snapshot.

This is intentionally a small editorial catalogue rather than a price feed.
Values are drawn from the linked manufacturer specification material and must
be rechecked whenever a model, variant or manufacturer page changes.
"""
from datetime import date

CHECKED = date.today().isoformat()

def source(title, url):
    return {
        "label": "Official manufacturer specification",
        "source_type": "official_manufacturer",
        "source_url": url,
        "source_title": title,
        "last_checked": CHECKED,
        "note": "Specifications and availability can differ by variant, city and model year. Confirm with the manufacturer or authorised dealer before purchase.",
    }

def vehicle(vehicle_id, manufacturer, model, variant, body_type, battery, chemistry,
            range_km, power, torque, acceleration, ac, dc, dc_time, warranty,
            source_title, source_url, **extra):
    return {
        "vehicle_id": vehicle_id, "manufacturer": manufacturer, "model": model,
        "variant": variant, "body_type": body_type, "vehicle_category": body_type,
        "ex_showroom_price": None, "price_status": "Check current official price",
        "motor_power_kw": power, "torque_nm": torque,
        "acceleration_0_100_sec": acceleration, "claimed_range_km": range_km,
        "mixed_real_world_range_km": None, "efficiency_kwh_per_100km": None,
        "warranty_years": None, "battery_warranty_years": warranty,
        "adas_level": extra.get("adas_level"), "safety_features": extra.get("safety_features", "See the variant-specific manufacturer feature list"),
        "battery": {"vehicle_id": vehicle_id, "battery_capacity_kwh": battery,
          "usable_capacity_kwh": None, "chemistry": chemistry,
          "thermal_management": extra.get("thermal_management", "See manufacturer source"),
          "cooling_type": extra.get("cooling_type", "See manufacturer source"),
          "battery_warranty_years": warranty, "battery_warranty_km": None,
          "max_ac_power_kw": ac, "max_dc_power_kw": dc,
          "charging_10_80_minutes": dc_time, "charging_20_80_minutes": None,
          "fast_charging_supported": "Yes", "v2l_supported": extra.get("v2l_supported", "See manufacturer source"),
          "connector": "CCS2"},
        "source": source(source_title, source_url),
    }

CATALOGUE = [
    vehicle("REAL001", "Tata Motors", "Tiago.ev", "Long Range", "hatchback", 24, "Lithium-ion", 315, 55, 114, None, 7.2, None, 58, 8,
      "Tata Tiago.ev technical specifications", "https://dealer-locator.cars.tatamotors.com/ev/assets/images/tiago-ev-brochure.pdf", thermal_management="Liquid cooled", v2l_supported="Not listed in source"),
    vehicle("REAL002", "Tata Motors", "Nexon.ev", "Long Range", "suv", 40.5, "Lithium-ion", 465, 106.4, 215, 8.9, 7.2, 50, 56, 8,
      "Tata Nexon.ev technical specifications", "https://dealer-locator.cars.tatamotors.com/ev/assets/images/nexon-ev-brochure.pdf", thermal_management="Liquid cooled", v2l_supported="Yes"),
    vehicle("REAL003", "Hyundai", "CRETA Electric", "Long Range", "suv", 51.4, "Liquid cooled lithium-ion", 510, 126, None, 7.9, 7.4, None, 39, None,
      "Hyundai CRETA Electric specifications", "https://www.hyundai.com/in/en/find-a-car/creta-electric/specification", thermal_management="Liquid cooled", v2l_supported="Yes", adas_level=2),
    vehicle("REAL004", "Mahindra", "BE 6", "79 kWh", "suv", 79, "LFP", 683, 210, 380, 6.7, 11, 175, 20, "Lifetime for eligible first private owner",
      "Mahindra BE 6 official launch specifications", "https://www.mahindraelectricsuv.com/press-releases/be6-and-xev9e-launched.html", thermal_management="See manufacturer source", v2l_supported="See manufacturer source"),
    vehicle("REAL005", "Mahindra", "XEV 9e", "79 kWh", "suv", 79, "LFP", 656, 210, 380, 6.8, 11, 175, 20, "Lifetime for eligible first private owner",
      "Mahindra XEV 9e official launch specifications", "https://www.mahindraelectricsuv.com/press-releases/be6-and-xev9e-launched.html", thermal_management="See manufacturer source", v2l_supported="See manufacturer source"),
    vehicle("REAL006", "BYD", "ATTO 3", "Extended Range", "suv", 60.48, "Blade Battery LFP", 420, 150, 310, 7.3, 7, 80, None, None,
      "BYD ATTO 3 vehicle specifications", "https://www.byd.com/material/byd-site/zm/product/atto3/atto3pdf/BYD%20ATTO%203%20Vehicle%20Specifications.pdf", thermal_management="See manufacturer source", v2l_supported="Yes"),
    vehicle("REAL007", "BYD", "SEALION 7", "RWD", "suv", 82.56, "Blade Battery", 482, 230, 380, 6.7, 11, 150, 60, None,
      "BYD SEALION 7 specification sheet", "https://www.byd.com/content/dam/byd-site/sc/BYD%20Sealion%207.pdf", thermal_management="See manufacturer source", v2l_supported="Yes"),
    vehicle("REAL008", "MG", "ZS EV", "50.3 kWh", "suv", 50.3, "Lithium-ion", 461, None, None, None, None, None, None, None,
      "MG ZS EV official launch release", "https://www.mgmotor.co.in/content/dam/mgmotor/documents/mg-dc-pdf-0267.pdf", thermal_management="See manufacturer source", v2l_supported="See manufacturer source"),
    vehicle("REAL009", "MG", "Comet EV", "17.3 kWh", "hatchback", 17.3, "Lithium-ion", 230, None, None, None, None, None, None, None,
      "MG Comet EV official brochure", "https://www.mgmotor.co.in/content/dam/mg-redesign/mg-comet-ev/documents/cm-dc-pdf-002.pdf", thermal_management="See manufacturer source", v2l_supported="See manufacturer source"),
]
