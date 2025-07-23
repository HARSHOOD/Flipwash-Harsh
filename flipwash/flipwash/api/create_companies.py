import frappe
from frappe.model.document import Document

@frappe.whitelist(allow_guest=True)
def create_flipwash_companies():
    parent_company = "Flipwash India Pvt Ltd"

    # First create the parent company if not already created
    if not frappe.db.exists("Company", parent_company):
        doc = frappe.new_doc("Company")
        doc.company_name = parent_company
        doc.abbr = "FIP"
        doc.default_currency = "INR"
        doc.country = "India"
        doc.is_group=1
        doc.save(ignore_permissions=True)
        frappe.db.commit()
        print(f"✅ Parent company '{parent_company}' created.")
    else:
        print(f"ℹ️ Parent company '{parent_company}' already exists.")

    # List of franchises to be created
    company_list = [
        {"company_name": "Flipwash Gurgaon Franchise", "abbr": "FGF"},
        {"company_name": "Flipwash Delhi Franchise", "abbr": "FDF"},
        {"company_name": "Flipwash Mumbai Franchise", "abbr": "FMF"}
    ]

    for company in company_list:
        if not frappe.db.exists("Company", company["company_name"]):
            doc = frappe.new_doc("Company")
            doc.company_name = company["company_name"]
            doc.abbr = company["abbr"]
            doc.default_currency = "INR"
            doc.country = "India"
            doc.parent_company = parent_company  # Linking to parent
            doc.save(ignore_permissions=True)
            frappe.db.commit()
            print(f"✅ Company '{company['company_name']}' created.")
        else:
            print(f"⚠️ Company '{company['company_name']}' already exists.")


# create employee for each company 

import random
company_list = [
    "Flipwash India Pvt Ltd",
    "Flipwash Gurgaon Franchise",
    "Flipwash Delhi Franchise",
    "Flipwash Mumbai Franchise"
]

first_names = ["Aman", "Ravi", "Priya", "Neha", "Ankit", "Pooja", "Rohan", "Suman", "Vikas", "Divya"]
last_names = ["Sharma", "Kumar", "Verma", "Joshi", "Singh", "Choudhary", "Patel", "Yadav"]
genders = ["Male", "Female", "Other"]
    
@frappe.whitelist(allow_guest=True)
def create_employees_for_flipwash_companies():
    # 🔹 Hardcoded list of companies
   
    for company_name in company_list:
        num_employees = random.randint(10, 15)
        print(f"👷 Creating {num_employees} employees for {company_name}...")

        for _ in range(num_employees):
            first = random.choice(first_names)
            last = random.choice(last_names)
            full_name = f"{first} {last}"
            personal_email = f"{first.lower()}.{last.lower()}{random.randint(1, 999)}@flipwash.com"
            emp_id = f"{first[0].upper()}{last[0].upper()}{random.randint(1000, 9999)}"

            # Avoid duplicates (same name under same company)
            if not frappe.db.exists("Employee", {"employee_name": full_name, "company": company_name}):
                emp = frappe.new_doc("Employee")
                emp.first_name = first
                emp.last_name = last
                emp.employee_name = full_name
                emp.employee_number = emp_id
                emp.company = company_name
                emp.date_of_birth = "1995-01-01"
                emp.date_of_joining = "2023-01-01"
                emp.gender = random.choice(genders)
                emp.personal_email = personal_email
                emp.status = "Active"
                emp.save(ignore_permissions=True)

        frappe.db.commit()
        print(f"✅ Done creating employees for {company_name}")

    return "✅ Employees created for all companies" 


# this function is required , to set company field in list view and standered filters 
@frappe.whitelist(allow_guest=True)
def update_company_field_in_employee():
    try:
        doc = frappe.get_doc("DocType", "Employee")
        updated = False

        for f in doc.fields:
            if f.fieldname == "company":
                if not f.in_list_view:
                    f.in_list_view = 1
                    updated = True
                if not f.in_standard_filter:
                    f.in_standard_filter = 1
                    updated = True
                break  # Exit loop after finding 'company' field

        if updated:
            doc.save(ignore_permissions=True)
            frappe.db.commit()
            return {"status": "success", "message": "Company field updated in Employee doctype"}
        else:
            return {"status": "skipped", "message": "Company field already updated"}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "update_company_field_in_employee")
        return {"status": "error", "message": str(e)}

