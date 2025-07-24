import frappe

def add_training_programs_to_employee(doc, method):
    # Only run when first time saved (status is 'Draft' and no child rows yet)
    if doc.status == "Inactive" and not doc.training_programs:
        training_programs = frappe.get_all("Training Program", fields=["name"])

        for tp in training_programs:
            doc.append("training_programs", {
                "training_program": tp.name,
                "status": "Scheduled",
            })
        doc.save(
            ignore_permissions=True, # ignore write permissions during save
        ) 
        frappe.db.commit()