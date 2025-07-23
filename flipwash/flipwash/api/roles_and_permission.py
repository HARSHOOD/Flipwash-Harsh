import frappe
from frappe import _

role_name =  "Franchise User" 
# this is creating role in role doctype, which will assign to franchise user 
# @frappe.whitelist(allow_guest=True)
# def create_franchise_role():
    
#     # Check if the role already exists
#     if frappe.db.exists("Role", role_name):
#         print(f"Role '{role_name}' already exists.")
#         return {"message": f"Role '{role_name}' already exists."}

#     try:
#         # Create a new Role document using new_doc
#         role_doc = frappe.new_doc("Role")
#         role_doc.role_name = role_name
#         role_doc.desk_access = 1  # 1 = has Desk access; use 0 to disable Desk

#         # Insert the role and commit
#         role_doc.save(ignore_permissions=True)
#         frappe.db.commit()
     
#         return {"message": f"Role '{role_name}' created successfully."}

#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), "Create Franchise Role Failed")
#         return {"error": str(e)}

def before_insert_user(doc, method):
    try:
        check_employee_exists(doc.email) 
        print("before_insert_user check",doc)
       
        if not hasattr(doc, "company") or not doc.company:
            frappe.throw("Company must be selected on User.")

        

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "User Creation Failed")
        raise


@frappe.whitelist(allow_guest=True)
def check_employee_exists(email):
    if not frappe.db.exists("Employee", {"personal_email": email}) and not frappe.db.exists("Employee", {"company_email": email}):
        frappe.throw(_("No Employee found with email: {0}").format(email))


@frappe.whitelist(allow_guest=True)
def assign_roles_for_group_company(user):
    
    all_roles = frappe.get_all("Role", filters={"disabled": 0}, pluck="name")
    roles_to_assign = [r for r in all_roles if r != role_name]

    user.roles = []
    for role in roles_to_assign:
        user.append("roles", {"role": role})




@frappe.whitelist(allow_guest=True)
def assign_franchise_role_only(user):
    user.roles = []
    user.append("roles", {"role": role_name})



@frappe.whitelist(allow_guest=True)
def create_user_permission_for_company(user): 
    print("create_user_permission_for_company for user",user)
    try:
        if user.company:
            user_permission = frappe.get_doc({
                "doctype": "User Permission",
                "user": user.name,
                "allow": "Company",
                "for_value": user.company, 
                "is_default":1
            })
            user_permission.insert(ignore_permissions=True)
            frappe.db.commit()
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "User Permission Creation Failed")

@frappe.whitelist(allow_guest=True)
def link_user_to_employee(user):
    try: 
        print("linking user to employee")
        employee_name = frappe.get_value("Employee", {"personal_email": user.email})  
        if not employee_name :
         employee_name = frappe.get_value("Employee", {"company_email": user.email})  
        
        print("employee_name",employee_name)
        if employee_name:
            frappe.db.set_value("Employee", employee_name, "user_id", user.name)
            frappe.db.set_value("Employee", employee_name, "create_user_permission",0)
            frappe.db.commit()
    except Exception as e: 

        print("Linking User to Employee Failed",e) 
        return 



@frappe.whitelist(allow_guest=True)
def after_insert_user(doc,method):
    try:
        link_user_to_employee(doc)
        is_group = frappe.db.get_value("Company", doc.company, "is_group") 
        print("is_group",is_group)  
        if not is_group:
            create_user_permission_for_company(doc)
        assign_roles_for_group_company(doc)
        # Save role assignments
        doc.save(ignore_permissions=True)

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "User After Insert Hook Failed")
        raise
