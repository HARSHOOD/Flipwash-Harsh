app_name = "flipwash"
app_title = "Flipwash"
app_publisher = "Harsh"
app_description = "Flipwash"
app_email = "harsh.rajput@oodles.io"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "flipwash",
# 		"logo": "/assets/flipwash/logo.png",
# 		"title": "Flipwash",
# 		"route": "/flipwash",
# 		"has_permission": "flipwash.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/flipwash/css/flipwash.css"
# app_include_js = "/assets/flipwash/js/flipwash.js"

# include js, css files in header of web template
# web_include_css = "/assets/flipwash/css/flipwash.css"
# web_include_js = "/assets/flipwash/js/flipwash.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "flipwash/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "flipwash/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "flipwash.utils.jinja_methods",
# 	"filters": "flipwash.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "flipwash.install.before_install"
# after_install = "flipwash.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "flipwash.uninstall.before_uninstall"
# after_uninstall = "flipwash.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "flipwash.utils.before_app_install"
# after_app_install = "flipwash.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "flipwash.utils.before_app_uninstall"
# after_app_uninstall = "flipwash.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "flipwash.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"flipwash.tasks.all"
# 	],
# 	"daily": [
# 		"flipwash.tasks.daily"
# 	],
# 	"hourly": [
# 		"flipwash.tasks.hourly"
# 	],
# 	"weekly": [
# 		"flipwash.tasks.weekly"
# 	],
# 	"monthly": [
# 		"flipwash.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "flipwash.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "flipwash.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "flipwash.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["flipwash.utils.before_request"]
# after_request = ["flipwash.utils.after_request"]

# Job Events
# ----------
# before_job = ["flipwash.utils.before_job"]
# after_job = ["flipwash.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"flipwash.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
 
fixtures = ["Custom Field"]

after_install = [ 
                    "flipwash.flipwash.api.Add_on_subscription_plan.create_all_groups_items_and_plans",
                    "flipwash.flipwash.api.create_companies.update_company_field_in_employee"
] 



doctype_js = {
    "Campaign": "public/js/campaign.js"
}


doc_events = {
    "User": {
        "before_insert": "flipwash.flipwash.api.roles_and_permission.before_insert_user",
        "after_insert": "flipwash.flipwash.api.roles_and_permission.after_insert_user"
    }
}
