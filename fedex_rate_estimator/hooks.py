app_name = "fedex_rate_estimator"
app_title = "FedEx Rate Estimator"
app_publisher = "Muhsina"
app_description = "Frappe app to fetch FedEx shipping rates"
app_email = "muhsinavp1319@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "fedex_rate_estimator",
# 		"logo": "/assets/fedex_rate_estimator/logo.png",
# 		"title": "FedEx Rate Estimator",
# 		"route": "/fedex_rate_estimator",
# 		"has_permission": "fedex_rate_estimator.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/fedex_rate_estimator/css/fedex_rate_estimator.css"
# app_include_js = "/assets/fedex_rate_estimator/js/fedex_rate_estimator.js"

# include js, css files in header of web template
# web_include_css = "/assets/fedex_rate_estimator/css/fedex_rate_estimator.css"
# web_include_js = "/assets/fedex_rate_estimator/js/fedex_rate_estimator.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "fedex_rate_estimator/public/scss/website"

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
# app_include_icons = "fedex_rate_estimator/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }



fixture = [
    {
        'doctype' : 'Web Page',
        'filters' : {
            'name' : ['in', ['Shipment Rate Checker']]
        }
    }
]


# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "fedex_rate_estimator.utils.jinja_methods",
# 	"filters": "fedex_rate_estimator.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "fedex_rate_estimator.install.before_install"
# after_install = "fedex_rate_estimator.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "fedex_rate_estimator.uninstall.before_uninstall"
# after_uninstall = "fedex_rate_estimator.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "fedex_rate_estimator.utils.before_app_install"
# after_app_install = "fedex_rate_estimator.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "fedex_rate_estimator.utils.before_app_uninstall"
# after_app_uninstall = "fedex_rate_estimator.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "fedex_rate_estimator.notifications.get_notification_config"

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
# 		"fedex_rate_estimator.tasks.all"
# 	],
# 	"daily": [
# 		"fedex_rate_estimator.tasks.daily"
# 	],
# 	"hourly": [
# 		"fedex_rate_estimator.tasks.hourly"
# 	],
# 	"weekly": [
# 		"fedex_rate_estimator.tasks.weekly"
# 	],
# 	"monthly": [
# 		"fedex_rate_estimator.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "fedex_rate_estimator.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "fedex_rate_estimator.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "fedex_rate_estimator.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["fedex_rate_estimator.utils.before_request"]
# after_request = ["fedex_rate_estimator.utils.after_request"]

# Job Events
# ----------
# before_job = ["fedex_rate_estimator.utils.before_job"]
# after_job = ["fedex_rate_estimator.utils.after_job"]

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
# 	"fedex_rate_estimator.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

