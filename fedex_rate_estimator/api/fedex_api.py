import frappe
import requests
from frappe import _

@frappe.whitelist()
def get_fedex_rates(dispatch_address, shipping_address, weight):
    try:
        # Convert stringified arguments to dicts (if needed)
        if isinstance(dispatch_address, str):
            import json
            dispatch_address = json.loads(dispatch_address)
        if isinstance(shipping_address, str):
            import json
            shipping_address = json.loads(shipping_address)

        # Prepare FedEx API payload
        payload = {
            "accountNumber": {"value": "XXXXX7354"},
            "requestedShipment": {
                "shipper": {"address": dispatch_address},
                "recipient": {"address": shipping_address},
                "pickupType": "DROPOFF_AT_FEDEX_LOCATION",
                "rateRequestType": ["ACCOUNT", "LIST"],
                "requestedPackageLineItems": [
                    {
                        "weight": {
                            "units": "LB",
                            "value": weight
                        }
                    }
                ]
            }
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_FEDEX_SANDBOX_TOKEN"  # Replace this
        }

        # Make the request to FedEx sandbox
        response = requests.post(
            "https://apis-sandbox.fedex.com/rate/v1/rates/quotes",
            headers=headers,
            json=payload
        )

        if response.status_code != 200:
            frappe.log_error(response.text, "FedEx Rate API Error")
            return []

        data = response.json()

        # Parse and return rates
        rates = []
        for detail in data.get("output", {}).get("rateReplyDetails", []):
            rate_type = detail["ratedShipmentDetails"][0]["rateType"]
            amount = detail["ratedShipmentDetails"][0]["totalNetCharge"]["amount"]
            rates.append({
                "type": rate_type,
                "amount": amount
            })

        return rates

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "FedEx Rate Fetch Failed")
        frappe.throw(_("Could not fetch rates. Please check your inputs."))
