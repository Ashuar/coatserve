# Copyright (c) 2025, ashuar and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns, data = get_columns(), get_data(filters)
    return columns, data


def get_data(filters=None):
    query = """
		SELECT
		si.name,
		si.posting_date AS invoice_date,
		si.customer,
		si.customer_name,
		sii.item_code,
		sii.item_name,
		sii.pack_size,
		sii.qty AS order_qty,
		sii.rate,
		sii.amount,
		sii.quantity_ltr_kg,
		sed.basic_rate,
		ROUND((sii.rate - sed.basic_rate), 2) AS cm_per_pack,
		ROUND((sii.rate - sed.basic_rate) / sii.pack_size, 2) AS cm_per_ltr,
		ROUND(sed.basic_rate * sii.qty, 2) AS total_cost,
		ROUND((sii.rate - sed.basic_rate) * sii.qty, 2) AS total_cm,
		ROUND((sii.rate - sed.basic_rate) / sii.rate * 100, 2) AS cm_percentage,
		sed.stock_entry_name AS stock_entry
	FROM
		`tabSales Invoice` si
	INNER JOIN
		`tabSales Invoice Item` sii ON si.name = sii.parent
	LEFT JOIN (
		SELECT
			sed1.item_code,
			sed1.basic_rate,
			sed1.parent AS stock_entry_name,
			se1.posting_date,
			se1.name AS se_name
		FROM
			`tabStock Entry Detail` sed1
		INNER JOIN
			`tabStock Entry` se1 ON sed1.parent = se1.name
		WHERE
			se1.docstatus = 1
			AND se1.stock_entry_type = 'Manufacture'
	) AS sed ON
		sed.item_code = sii.item_code
		AND sed.posting_date = (
			SELECT MAX(se2.posting_date)
			FROM `tabStock Entry` se2
			INNER JOIN `tabStock Entry Detail` sed2 ON sed2.parent = se2.name
			WHERE
				se2.docstatus = 1
				AND se2.stock_entry_type = 'Manufacture'
				AND sed2.item_code = sii.item_code
				AND se2.posting_date <= si.posting_date
		)
	WHERE
		si.docstatus = 1
		AND si.posting_date >= %(from_date)s
		AND si.posting_date <= %(to_date)s
    GROUP BY
    	si.posting_date, sii.item_code, sii.qty
		ORDER BY si.posting_date;"""
    data = frappe.db.sql(query, filters, as_dict=True)
    return data


def get_columns():
    return [
        {
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Sales Invoice",
            "label": _("Sales Invoice"),
        },
        {
            "fieldname": "stock_entry",
            "fieldtype": "Link",
            "options": "Stock Entry",
            "label": _("Voucher No"),
        },
        {"fieldname": "invoice_date", "fieldtype": "Date", "label": "Invoice Date"},
        {
            "fieldname": "customer",
            "fieldtype": "Link",
            "options": "Customer",
            "label": "Customer",
        },
        {
            "fieldname": "customer_name",
            "fieldtype": "Link",
            "options": "Customer",
            "label": "Customer Name",
        },
        {
            "fieldname": "item_code",
            "fieldtype": "Link",
            "options": "Item",
            "label": ("Item Code"),
        },
        {
            "fieldname": "item_name",
            "fieldtype": "Data",
            "label": "Item Name",
        },
        {
            "fieldname": "pack_size",
            "fieldtype": "Float",
            "label": "Pack Size",
        },
        {
            "fieldname": "order_qty",
            "fieldtype": "Float",
            "label": "Order Qty",
        },
        {
            "fieldname": "rate",
            "fieldtype": "Float",
            "label": "Sale Price(RS)",
        },
        {
            "fieldname": "amount",
            "fieldtype": "Float",
            "label": "Total Sales Value (RS)",
        },
        {
            "fieldname": "basic_rate",
            "fieldtype": "Float",
            "label": "Cost Price(RS)",
        },
        {
            "fieldname": "quantity_ltr_kg",
            "fieldtype": "Float",
            "label": "Quantity Ltr Kg",
        },
        {
            "fieldname": "cm_per_pack",
            "fieldtype": "Float",
            "label": "CM Per Pack",
        },
        {
            "fieldname": "cm_per_ltr",
            "fieldtype": "Float",
            "label": "CM Per Liter",
        },
        {
            "fieldname": "total_cost",
            "fieldtype": "Float",
            "label": "Total Cost",
        },
        {
            "fieldname": "total_cm",
            "fieldtype": "Float",
            "label": "Total CM",
        },
        {
            "fieldname": "cm_percentage",
            "fieldtype": "Float",
            "label": "CM Percentage",
        },
    ]
