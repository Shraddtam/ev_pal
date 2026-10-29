# EV PAL synthetic data pack and MVP

The project now includes a functional FastAPI + responsive frontend MVP. It loads the existing CSV data directly through a modular data access and service layer—no datasets are recreated or replaced.

## Run the app

Use Python 3.11+ in a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn backend.app:app --reload
```

Open `http://127.0.0.1:8000`. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Architecture

`frontend/` is the responsive application shell. `backend/app.py` defines the API surface. `backend/services/` holds dashboard, vehicle, recommendation, battery-health, TCO, policy, charging and market logic. `backend/data_access.py` is the CSV repository boundary intended to be replaced by PostgreSQL repositories later.

## Vehicle catalogue

The active EV Explorer, vehicle detail pages, comparison and buying guide use the source-linked catalogue in `backend/services/real_catalog.py`. It currently contains real Tata, Hyundai, Mahindra, BYD and MG models, with links to manufacturer specification material and a last-checked date. It deliberately does not show an unsourced city-specific price or generated ownership/review data as if it belonged to those models.

The policy, charging, market, TCO and battery-health screens retain a visible `DEMO DATA` or estimate notice until they are connected to verified sources or diagnostics.

See [API examples](docs/api.md) for the endpoint list and request samples.

Run `python generate_evpal_data.py` to reproduce the datasets. Use these records only for development, test, demonstrations, RAG and ML experimentation.

**All generated values are synthetic and must not be presented as real vehicle specifications, government policies, manufacturer claims, market statistics, battery measurements, or official data.**
