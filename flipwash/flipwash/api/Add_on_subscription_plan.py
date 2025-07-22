import frappe
group_data = {   
    "Main":[  
        {"name":"Flip Wash","prices":{"small":70,"medium":80,"large":90}},
        {"name":"Flip Express Details","prices":{"small":100,"medium":120,"large":140}},
        ],
    "Exterior":[ 
        {"name":"Hand Wash|Soft 99","prices":{"small":40,"medium":50,"large":60}},
        {"name":"Buffer Wax","prices":{"small":20,"medium":30,"large":40}},
        {"name":"Clay Bar","prices":{"small":25,"medium":30,"large":40}},
        {"name":"Ceremic Spray","prices":{"small":30,"medium":40,"large":50}},
                 ] ,
    "Interior": [
        {"name": "Interior Deep Cleaning", "prices": {"Small": 119, "Medium": 139, "Large": 159}},
        {"name": "Leather Treatment", "prices": {"Small": 29, "Medium": 39, "Large": 59}}
                  ], 
    "Painting Care": [
        {"name": "Ceramic Coating", "prices": {"Small": 699, "Medium": 899, "Large": 999}},
        {"name": "Painting Correction", "prices": {"Small": 219, "Medium": 249, "Large": 279}},
        {"name": "Polishing", "prices": {"Per Panel": 50}}  # flat price
                  ],
    "Enhance": [
        {"name": "Headlight Restoration", "prices":90},
        {"name": "Engine Cleaning", "prices":60},
        {"name": "Plastic and Vinyl Restoration", "prices": 50}
             ] ,
    "Detailing":[  
        {"name":"Full Detailing","prices":{"Small": 399, "Medium": 459, "Large": 529}},
        {"name":"Exterior Detailing","prices":{"Small": 349, "Medium": 399, "Large": 459}}
        ]
}

# Entry function to create everything from structured data 
@frappe.whitelist(allow_guest=True)
def create_all_groups_items_and_plans():
    for group_name, items in group_data.items():
        create_item_group(group_name)
        create_items_for_group(group_name, items)

# 1. Create Item Group
def create_item_group(group_name):
    if not frappe.db.exists("Item Group", group_name):
        group = frappe.new_doc("Item Group")
        group.item_group_name = group_name
        group.parent_item_group = "All Item Groups"
        group.save(ignore_permissions=True)
        frappe.db.commit()
        print(f"Created Item Group: {group_name}")
    else:
        print(f"Document already exists in database: Item Group -> {group_name}")



# 2. Create Items under a group
def create_items_for_group(group_name, items):
    for item in items:
        item_name = item["name"]
        existing_item = frappe.db.exists("Item", item_name)
 
        if not existing_item:
            new_item = frappe.new_doc("Item")
            new_item.item_code = item_name
            new_item.item_name = item_name
            new_item.item_group = group_name
            new_item.stock_uom = "Nos"
            new_item.is_stock_item = 0
            new_item.save(ignore_permissions=True)
            frappe.db.commit()
            print(f"✅ Created Item: {item_name}")
            item_code = new_item.name
        else:
            print(f"❌ Document already exists in database: Item -> {item_name}")
            item_code = item_name
 
        # Now create subscription plans for this item
        create_subscription_plans(item_code, item_name, group_name, item["prices"]) 


 
# 2. Create Items under a group
def create_items_for_group(group_name, items):
    for item in items:
        item_name = item["name"]
        existing_item = frappe.db.exists("Item", item_name)
 
        if not existing_item:
            new_item = frappe.new_doc("Item")
            new_item.item_code = item_name
            new_item.item_name = item_name
            new_item.item_group = group_name
            new_item.stock_uom = "Nos"
            new_item.is_stock_item = 0
            new_item.save(ignore_permissions=True)
            frappe.db.commit()
            print(f"✅ Created Item: {item_name}")
            item_code = new_item.name
        else:
            print(f"❌ Document already exists in database: Item -> {item_name}")
            item_code = item_name
 
        # Now create subscription plans for this item
        create_subscription_plans(item_code, item_name, group_name, item["prices"])
 
# 3. Create Subscription Plan
def create_subscription_plans(item_code, item_name, group_name, prices):
    
    
    if isinstance(prices,dict) :
        for size, price in prices.items(): 
            if group_name == "main": 
                plan_name = f"{group_name}-{item_name}-{size}" 
            else :
                plan_name = f"{item_name}-{size}"  
                
            if not frappe.db.exists("Subscription Plan", {"plan_name": plan_name}):
                plan = frappe.new_doc("Subscription Plan")
                plan.plan_name = plan_name
                # plan.description = f"Auto-created subscription plan for {plan_name}"
                plan.billing_interval = "Month"
                plan.item = item_code
                plan.currency = "USD"
                plan.price_determination = "Fixed Rate"
                plan.cost = price
                plan.save(ignore_permissions=True)
                frappe.db.commit()
                print(f"✅ Created Subscription Plan: {plan_name}")
            else:
                print(f"❌ Document already exists in database: Subscription Plan -> {plan_name}")
    
    else:   
            plan_name = f"{group_name}-{item_name}"
            if not frappe.db.exists("Subscription Plan", {"plan_name": plan_name}):
                plan = frappe.new_doc("Subscription Plan")
                plan.plan_name = plan_name
                # plan.description = f"Auto-created subscription plan for {plan_name}"
                plan.billing_interval = "Month"
                plan.item = item_code
                plan.currency = "USD"
                plan.price_determination = "Fixed Rate"
                plan.cost = prices
                plan.save(ignore_permissions=True)
                frappe.db.commit()
                print(f"✅ Created Subscription Plan: {plan_name}")
            else:
                print(f"❌ Document already exists in database: Subscription Plan -> {plan_name}")
    
 
 
 
 