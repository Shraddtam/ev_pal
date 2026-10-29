from backend.data_access import number
from backend.services.vehicles import find
from backend.observability.logging import log_event

def calculate(payload):
    vehicle=find(payload.get("vehicle_id","EVP001")) or find("EVP001")
    years=int(number(payload.get("ownership_years"),5)); km=number(payload.get("annual_km"),12000); price=number(payload.get("purchase_price"),number(vehicle['ex_showroom_price'])); subsidy=number(payload.get("subsidy"),0); electricity=number(payload.get("electricity_price"),7); public_share=number(payload.get("public_charging_percent"),20)/100; public_price=number(payload.get("public_charging_price"),16); efficiency=number(vehicle.get('efficiency_kwh_per_100km'),18); maintenance=number(payload.get("annual_maintenance"),9000); insurance=number(payload.get("annual_insurance"),price*.022); tyres=number(payload.get("annual_tyre_cost"),7000); rate=number(payload.get("financing_rate"),9.5)/100; resale_pct=number(payload.get("resale_percent"),max(18,72-years*5.5))/100
    initial=price-subsidy+price*.08+60000; energy=km*years*efficiency/100*(electricity*(1-public_share)+public_price*public_share)*1.1; maint=(maintenance+tyres)*years; ins=insurance*years; finance=price*rate*years; resale=price*resale_pct; total=initial+energy+maint+ins+finance-resale
    alternatives=[]
    for kind,consumption,fuel in [("Petrol",7.0,105),("Diesel",5.5,94),("Hybrid",4.5,105)]:
        running=km*years/100*consumption*fuel; alt_total=price*1.05+running+maint*1.25+ins+finance-price*resale_pct*.9; alternatives.append({"type":kind,"total":round(alt_total),"cost_per_km":round(alt_total/(km*years),2)})
    yearly=[{"year":y,"cost":round(initial if y==1 else 0)+round(energy/years*y+maint/years*y+ins/years*y+finance/years*y)} for y in range(1,years+1)]
    result={"vehicle":vehicle['model']+' '+vehicle['variant'],"breakdown":{"initial_cost":round(initial),"electricity_cost":round(energy),"maintenance_and_tyres":round(maint),"insurance":round(ins),"financing":round(finance),"resale_value":round(resale),"total_ownership_cost":round(total),"cost_per_km":round(total/(km*years),2),"monthly_cost":round(total/(years*12))},"yearly":yearly,"alternatives":alternatives}
    log_event("app", "tco_calculated", "TCO scenario calculated", data={"vehicle_id":vehicle["vehicle_id"],"ownership_years":years,"annual_km":km,"total_cost":result["breakdown"]["total_ownership_cost"]})
    return result
