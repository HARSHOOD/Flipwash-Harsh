import frappe
from frappe.model.document import Document
from frappe.exceptions import ValidationError




@frappe.whitelist(allow_guest=True)
def create_flipwash_subscription_plans():
    print("[STEP: START] Starting creation of Flipwash subscription plans...")

    plans = [
        {"plan_name": "Flip Wash - Small", "price": 70},
        {"plan_name": "Flip Wash - Medium", "price": 80},
        {"plan_name": "Flip Wash - Large", "price": 90},
        {"plan_name": "Flip Express Detail - Small", "price": 100},
        {"plan_name": "Flip Express Detail - Medium", "price": 120},
        {"plan_name": "Flip Express Detail - Large", "price": 140},
    ]

    for plan in plans:
        try:
            print(f"\n[STEP: PLAN] Processing plan: {plan['plan_name']}")
            item = get_or_create_item(plan["plan_name"])
            plan =  create_subscription_plan(plan["plan_name"], item.name, plan["price"]) 
            # return {"plan":plan,"item":item}
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), f"[ERROR] Subscription creation failed for: {plan['plan_name']}")
            print(f"[ERROR] Subscription creation failed for: {plan['plan_name']} -> {e}")

    print("[STEP: DONE] Finished creating Flipwash subscription plans.")


def get_or_create_item(item_name):
    print(f"[STEP: CHECK ITEM] Checking if Item exists: {item_name}")
    item = frappe.db.exists("Item", item_name)
    if item:
        print(f"[STEP: ITEM EXISTS] Found existing Item: {item_name}")
        return frappe.get_doc("Item", item_name)
    else:
        print(f"[STEP: ITEM CREATE] Creating new Item: {item_name}")
        return create_item(item_name)


def create_item(item_name):
    doc = frappe.new_doc("Item")
    doc.item_code = generate_item_code(item_name)
    doc.item_name = item_name
    doc.item_group = "Services"
    doc.is_sales_item = 1
    doc.stock_uom = "Nos"
    doc.description = f"Subscription service for {item_name}"
    doc.is_stock_item = 0

    print(f"[STEP: VALIDATE ITEM] Validating Item: {item_name}")
    try :  
         doc.insert(ignore_permissions=True)
         frappe.db.commit()  
         print(f"[STEP: SAVED ITEM] Created Item: {doc.name} with code: {doc.item_code}")
    except Exception as e : 
         print("error while creating inserting doc",e)
    return doc


def generate_item_code(item_name):
    return item_name.lower().replace(" ", "-")


def create_subscription_plan(plan_name, item_code, price):
    print(f"[STEP: CHECK PLAN] Checking if Subscription Plan exists: {plan_name}")
    if frappe.db.exists("Subscription Plan", plan_name):
        print(f"[SKIP] Subscription Plan already exists: {plan_name}")
        return

    plan = frappe.new_doc("Subscription Plan")
    plan.plan_name = plan_name
    # plan.description = f"Auto-created subscription plan for {plan_name}"
    plan.billing_interval = "Month"
    plan.item = item_code
    plan.currency = "USD"
    plan.price_determination = "Fixed Rate"
    plan.cost = price

    try :  
         plan.insert(ignore_permissions=True)
         frappe.db.commit()  
         print(f"[STEP: SAVED ITEM] Created Item: {plan.name} with code: {plan.item}")
    except Exception as e : 
         print("error while creating inserting doc",e) 
        
    return plan 
