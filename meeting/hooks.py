# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "meeting"
app_title = "Meeting"
app_publisher = "New Indictrans Technologies Pvt. Ltd."
app_description = "Meeting Details"
app_icon = "octicon octicon-organization"
app_color = "#B03656"
app_email = "rohit.w@indictranstech.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/meeting/css/meeting.css"
# app_include_js = "/assets/meeting/js/meeting.js"

# include js, css files in header of web template
# web_include_css = "/assets/meeting/css/meeting.css"
# web_include_js = "/assets/meeting/js/meeting.js"

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

# Installation
# ------------

# before_install = "meeting.install.before_install"
# after_install = "meeting.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "meeting.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"meeting.tasks.all"
# 	],
# 	"daily": [
# 		"meeting.tasks.daily"
# 	],
# 	"hourly": [
# 		"meeting.tasks.hourly"
# 	],
# 	"weekly": [
# 		"meeting.tasks.weekly"
# 	]
# 	"monthly": [
# 		"meeting.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "meeting.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "meeting.event.get_events"
# }

