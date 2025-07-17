# apps/flipwash/flipwash/flipwash_management/doctype/vehicle_wash_entry/vehicle_wash_entry.py

import frappe
from frappe.model.document import Document

class VehicleWashEntry(Document): 
    def autoname(self):
        if self.customer and self.service_datetime:
            # Format datetime as YYYY-MM-DD-HH-MM
            formatted_datetime = frappe.utils.format_datetime(self.service_datetime, "yyyy-MM-dd-HH-mm")
            self.name = f"{self.customer}-{formatted_datetime}"
        else:
            frappe.throw("Customer and Service DateTime are required to generate the name.")
            
            
            
    def validate(self):
        # Count all previous PAID (non-free) visits of this customer
        previous_visits = frappe.db.count('Vehicle Wash Entry', {
            'customer': self.customer,
            'docstatus': ['<', 2]  # Exclude cancelled if any
        })

        # Add +1 for current visit
        self.visit_count = previous_visits + 1

        # Loyalty logic: every 6th visit is free
        if self.visit_count % 6 == 0:
            self.free_service = 1
            self.amount_charged = 0  # Make wash free
            frappe.msgprint("🎉 Loyalty Reward! This wash is free.")
        else:
            self.free_service = 0

        # Optional fallback: ensure amount is not null
        if not self.amount_charged:
            self.amount_charged = 0
