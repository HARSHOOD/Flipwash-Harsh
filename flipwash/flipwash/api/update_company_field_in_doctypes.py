import frappe


@frappe.whitelist(allow_guest=True)
def update_company_field_in_doctypes():
    doctypes = frappe.get_all("DocType", filters={"issingle": 0})  # skip single doctypes

    updated_doctypes = []

    for doctype in doctypes:
        doctype_name = doctype.name
        meta = frappe.get_meta(doctype_name)

        for field in meta.fields:
            if field.fieldname == "company":
                # Load DocType JSON
                doc = frappe.get_doc("DocType", doctype_name)
                
                for f in doc.fields:
                    if f.fieldname == "company":
                        # Update only if needed
                        updated = False
                        if not f.in_list_view:
                            f.in_list_view = 1
                            updated = True
                        if not f.in_standard_filter:
                            f.in_standard_filter = 1
                            updated = True
                        
                        if updated:
                            doc.save(ignore_permissions=True)
                            updated_doctypes.append(doctype_name)
                        break
                break

    frappe.db.commit()
    print("✅ Updated Doctypes:", updated_doctypes)
