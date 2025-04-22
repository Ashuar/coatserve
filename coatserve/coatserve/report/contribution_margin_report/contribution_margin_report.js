// Copyright (c) 2025, ashuar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Contribution Margin Report"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"lable": __("From Date"),
			"fieldtype": "Date",
			"width": "60",
			"reqd": 1,
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1)
		},
		{
			"fieldname": "to_date",
			"lable": __("To Date"),
			"fieldtype": "Date",
			"width": "60",
			"reqd": 1,
			"default": frappe.datetime.get_today()
		}
	]
};
