def calculate_total_qty_ltr_kg(doc, event):
    # print(doc.items)
    total_qty = 0
    for item in doc.items:
        total_qty += float(item.quantity_ltr_kg)
    
    doc.total_qty_ltr_kg = total_qty