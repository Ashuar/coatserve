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
		si.posting_date as invoice_date,
		si.customer,
		si.customer_name,
		sii.item_code,
		sii.item_name,
		sii.pack_size,
		sii.qty as order_qty,
		sii.rate,
		stock_entry_detail.basic_rate,
		sii.quantity_ltr_kg,
		ROUND((sii.rate - stock_entry_detail.basic_rate), 2) as cm_per_pack,
		ROUND((sii.rate - stock_entry_detail.basic_rate) / sii.pack_size, 2) as cm_per_ltr,
		sii.amount,
		ROUND(stock_entry_detail.basic_rate * sii.qty, 2) as total_cost,
		ROUND((sii.rate - stock_entry_detail.basic_rate) * sii.qty, 2) as total_cm,
		ROUND((sii.rate - stock_entry_detail.basic_rate) / sii.rate * 100, 2) as cm_percentage
	FROM
		`tabSales Invoice` si
	INNER JOIN
		`tabSales Invoice Item` sii ON si.name = sii.parent
	LEFT JOIN
		`tabStock Entry Detail` stock_entry_detail ON sii.item_code = stock_entry_detail.item_code
	LEFT JOIN
		`tabStock Entry` stock_entry ON stock_entry_detail.parent = stock_entry.name 
		AND stock_entry.stock_entry_type = 'Manufacture'
	WHERE    
		si.docstatus = '1'
		AND si.posting_date >= %(from_date)s 
		AND si.posting_date <= %(to_date)s
    GROUP BY
	si.name, sii.item_code, sii.qty;
	"""
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