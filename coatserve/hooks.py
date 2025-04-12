from . import __version__ as app_version

app_name = "coatserve"
app_title = "Coatserve"
app_publisher = "ashuar"
app_description = "coarserve customaization"
app_email = "ashuarchughtai@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/coatserve/css/coatserve.css"
# app_include_js = "/assets/coatserve/js/coatserve.js"

# include js, css files in header of web template
# web_include_css = "/assets/coatserve/css/coatserve.css"
# web_include_js = "/assets/coatserve/js/coatserve.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "coatserve/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Sales Order" : "public/js/sales_order.js",
    "Delivery Note": "public/js/delivery_note.js",
    "Sales Invoice": "public/js/sales_invoice.js",
    }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "coatserve.utils.jinja_methods",
#	"filters": "coatserve.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "coatserve.install.before_install"
# after_install = "coatserve.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "coatserve.uninstall.before_uninstall"
# after_uninstall = "coatserve.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "coatserve.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"coatserve.tasks.all"
#	],
#	"daily": [
#		"coatserve.tasks.daily"
#	],
#	"hourly": [
#		"coatserve.tasks.hourly"
#	],
#	"weekly": [
#		"coatserve.tasks.weekly"
#	],
#	"monthly": [
#		"coatserve.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "coatserve.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "coatserve.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "coatserve.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["coatserve.utils.before_request"]
# after_request = ["coatserve.utils.after_request"]

# Job Events
# ----------
# before_job = ["coatserve.utils.before_job"]
# after_job = ["coatserve.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"coatserve.auth.validate"
# ]
fixtures = [
    {
        "dt": "Custom Field",
        "filters": {
            "name": ["IN", ["Sales Order Item-pack_size",
            "Sales Order Item-sale_tax_value",
            "Sales Order Item-total_inclusive_sales_tax",
            "Sales Order Item-price_per_lt_or_kg",
            "Sales Order Item-total_cost",
            "Sales Order Item-quantity_ltr_k",
            "Sales Order-total_qty_ltr_kg",
            "Delivery Note Item-pack_size",
            "Delivery Note Item-sale_tax_value",
            "Delivery Note Item-total_inclusive_sales_tax",
            "Delivery Note Item-price_per_lt_or_kg",
            "Delivery Note Item-total_cost",
            "Delivery Note Item-quantity_ltr_k",
            "Delivery Note-total_qty_ltr_kg",
            "Sales Invoice Item-pack_size",
            "Sales Invoice Item-sale_tax_value",
            "Sales Invoice Item-total_inclusive_sales_tax",
            "Sales Invoice Item-price_per_lt_or_kg",
            "Sales Invoice Item-total_cost",
            "Sales Invoice Item-quantity_ltr_k",
            ]]
        }
    }
]