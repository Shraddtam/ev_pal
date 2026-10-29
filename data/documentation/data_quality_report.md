# Intentional data quality conditions

- SOH observations include rare unusually healthy and heavily degraded records, but SOH stays 50–100.
- Charging sessions include failed connector, payment and grid interruption scenarios.
- `schemes.csv` contains a controlled conflicting older version (`POL012`) of the Maharashtra scenario; it has a lower incentive and expired date. Use `last_verified`, dates and status when testing reconciliation.
- Source references are empty or reference-only by design.
- Synthetic review sentiment and safety events deliberately vary; safety events are fictional and not confirmed recalls.
- Dataset rows carry synthetic metadata. Controlled duplicate-like observations and measurement noise support validation testing.
