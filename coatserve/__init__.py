__version__ = "0.0.1"

import json
import frappe


@frappe.whitelist()
def get_total_cm(filters=None):

    filters = frappe.form_dict.get("filters")

    # Parse JSON string to dictionary
    if isinstance(filters, str):
        filters = json.loads(filters)

    from_date = filters["from_date"]
    to_date = filters["to_date"]

    data = frappe.db.sql(
        """
    SELECT 
        ROUND(SUM(total), 2) AS total_cm
    FROM (
        SELECT 
            (sii.rate - stock_entry_detail.basic_rate) * sii.qty AS total
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
        si.docstatus = 1
        AND si.posting_date >= %s
        AND si.posting_date <= %s
    GROUP BY
        si.name, sii.item_code, sii.qty
) AS cm_table;""",
        (from_date, to_date),
        as_dict=True,
    )

    # data = frappe.db.sql("""
    # SELECT
    # 	SUM((sii.rate - stock_entry_detail.basic_rate) * sii.qty, 2) as total_cm
    # FROM
    # 	`tabSales Invoice` si
    # INNER JOIN
    # 	`tabSales Invoice Item` sii ON si.name = sii.parent
    # LEFT JOIN
    # 	`tabStock Entry Detail` stock_entry_detail ON sii.item_code = stock_entry_detail.item_code
    # LEFT JOIN
    # 	`tabStock Entry` stock_entry ON stock_entry_detail.parent = stock_entry.name
    # 	AND stock_entry.stock_entry_type = 'Manufacture'
    # WHERE
    # 	si.docstatus = '1'
    # 	AND si.posting_date >= %s
    # 	AND si.posting_date <= %s
    # GROUP BY
    # si.name, sii.item_code, sii.qty;
    # """, (from_date, to_date), as_dict=True)

    return {"value": data[0].total_cm, "fieldtype": "Currency"}
