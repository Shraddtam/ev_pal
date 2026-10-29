# EV PAL API reference

The server serves synthetic prototype data only. Interactive OpenAPI documentation is available at `/docs` when the app is running.

| Endpoint | Purpose |
|---|---|
| `GET /api/dashboard` | Dashboard metrics and chart series |
| `GET /api/vehicles` | Vehicle catalogue with search and filters |
| `GET /api/vehicles/{vehicle_id}` | Vehicle, battery, ownership and review detail |
| `POST /api/recommendations` | Transparent rule-based buying matches |
| `POST /api/battery-health/estimate` | Labelled prototype SOH estimate |
| `POST /api/tco/calculate` | Deterministic EV and alternative-fuel cost scenario |
| `GET /api/policies` | Synthetic policy scenarios |
| `POST /api/policies/ask` | Local retrieval placeholder for future RAG |
| `GET /api/charging/stations` | Synthetic station filter endpoint |
| `GET /api/market` | Registration trend series |

## Example requests

```powershell
Invoke-RestMethod http://127.0.0.1:8000/api/vehicles?chemistry=LFP

Invoke-RestMethod -Method Post -ContentType 'application/json' `
  -Uri http://127.0.0.1:8000/api/battery-health/estimate `
  -Body '{"vehicle_id":"EVP001","age_months":36,"mileage_km":36000,"fast_charge_percentage":25}'
```

The SOH endpoint is a rule-based prototype calibrated to the synthetic dataset relationships. It must not be interpreted as BMS or diagnostic measurement.
