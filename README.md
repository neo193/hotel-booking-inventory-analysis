# Hotel Booking & Inventory Analysis

Python/Pandas analysis of a **synthetic 13-unit resort** covering January 2025–August 2026.

## Technologies
Python • Pandas • Matplotlib

## Analysis
The project calculates booking volume, realised revenue, room nights, **Occupancy**, **ADR**, **RevPAR**, cancellation rate and booking lead time.

## Key Findings
- Highest monthly occupancy: **145.4% (2025-12)**.
- Lowest monthly occupancy: **71.3% (2026-04)**.
- **Agoda** had the highest cancellation rate at **18.7%**.
- Direct bookings had a cancellation rate of **7.2%** and shorter booking lead times than OTA-heavy channels.
- The analysis shows why inventory utilisation and realised room nights are more useful operational measures than booking count alone.

## KPI Definitions
- Occupancy % = Sold room nights / Available room nights
- ADR = Average realised nightly rate
- RevPAR = Realised room revenue / Available room nights

## Run
```bash
pip install -r requirements.txt
python analysis.py
```

## Repository
```text
hotel-booking-inventory-analysis/
├── README.md
├── analysis.py
├── Hotel_Booking_Inventory_Analysis.ipynb
├── requirements.txt
├── data/
└── images/
```

> Synthetic portfolio data; findings do not represent a real property.
