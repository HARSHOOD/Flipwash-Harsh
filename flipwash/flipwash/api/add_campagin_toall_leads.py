import frappe
from frappe import _

@frappe.whitelist()
def assign_campaign_to_leads(campaign_name):
    leads = frappe.get_all("Lead", filters={}, fields=["name"])
    print(leads)
    for lead in leads: 
        print("lead",lead)
        data = frappe.db.set_value("Lead", lead.name, "campaign_name", campaign_name) 
        print('data',data)

    frappe.db.commit()
    return _("Updated {0} leads").format(len(leads))


