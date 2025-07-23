# apps/flipwash/flipwash/flipwash/api/test_case_vehicale_wash_entry.py

import frappe
from frappe.utils import now_datetime
from datetime import timedelta

@frappe.whitelist(allow_guest=True)
def create_bulk_vehicle_wash_entries():
    customer_name = "Grant Plastics Ltd."

    vehicle_types = ["Car", "SUV", "Truck"]
    service_types = ["Wash", "Polish", "Full Service"]
    payment_statuses = ["Paid", "Unpaid"]
    statuses = ["Draft", "In Progress", "Completed"]

    base_time = now_datetime()

    entries_created = []

    for i in range(25):
        # Add i * 10 minutes to base time
        service_time = base_time + timedelta(minutes=i * 10)

        try:
            doc = frappe.get_doc({
                "doctype": "Vehicle Wash Entry",
                "customer": customer_name,
                "vehicle_number": f"GP-{1000 + i}",
                "vehicle_type": vehicle_types[i % len(vehicle_types)],
                "service_type": service_types[i % len(service_types)],
                "service_datetime": service_time,
                "amount_charged": 100 + (i * 10),
                "payment_status": payment_statuses[i % len(payment_statuses)],
                "status": statuses[i % len(statuses)],
                "notes": f"Auto-generated test entry #{i+1}"
            })

            doc.save(ignore_permissions=True)
            entries_created.append(doc.name)

        except Exception as e:
            frappe.log_error(f"Error creating entry #{i+1}: {str(e)}")

    frappe.db.commit()

    return {
        "message": f"{len(entries_created)} entries created successfully.",
        "entries": entries_created
    }
