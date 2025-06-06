# FedEx Rate Estimator — Frappe Developer Assignment

This Frappe app allows logged-in users to input a **dispatch** and **shipping address**, fetch **FedEx shipping rates** using the FedEx Rate API, and display the rates in both a **custom page** and a **Delivery Note dialog**.


##  Features

- Custom Desk Web Page at `/shipment-rate-checker`
- Integration with FedEx Rate API
- Delivery Note Button to fetch and display rates
- Bootstrap classes like form-control, form-group, btn, card, etc.
- Two-column responsive layout with spacing and sections
- Uses `frappe.call()` to connect frontend with backend



## Setup Instructions

### 1. Install App

cd ~/frappe-bench
bench get-app fedex_rate_estimator https://github.com/Muhsina-V-P/fedex-rate-estimator.git
bench --site your-site-name install-app fedex_rate_estimator




