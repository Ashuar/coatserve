frappe.ui.form.on('Delivery Note Item', {
    item_code: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];
        frappe.db.get_value('Item', child.item_code, 'pack_size', function(response) {
            if (response && response.pack_size) {
                frappe.model.set_value(cdt, cdn, 'pack_size', response.pack_size);
            }
        });
    }
});
// upper function is to retrive data of pack size with item wise

frappe.ui.form.on('Delivery Note Item', {
    rate: function(frm, cdt, cdn) {
        updateQtyLtrKg(frm, cdt, cdn);
        updateSalesTaxValue(frm, cdt, cdn);
        totalInclusiveSalesTax(frm, cdt, cdn);
        pricePerLtOrKg(frm, cdt, cdn);
    },
    qty: function(frm, cdt, cdn) {
        updateQtyLtrKg(frm, cdt, cdn);
        updateSalesTaxValue(frm, cdt, cdn);
        totalInclusiveSalesTax(frm, cdt, cdn);
        pricePerLtOrKg(frm, cdt, cdn);
    }
});

function updateQtyLtrKg(frm, cdt, cdn) {
    var child = locals[cdt][cdn];
    var a = child.qty || 0;
    var packSize = child.pack_size || 0;
    var calculatedValue = (a * packSize).toFixed(2);
    frappe.model.set_value(cdt, cdn, 'quantity_ltr_kg', calculatedValue);
}

function updateSalesTaxValue(frm, cdt, cdn) {
    var child = locals[cdt][cdn];
    var a = 18 || 0;
    var e = child.qty || 0;
    var f = child.rate || 0;
    var g = e*f;
    var c = (g/100)*a;
    var round = c.toFixed(2);
    frappe.model.set_value(cdt, cdn, 'sale_tax_value', c);
}

function totalInclusiveSalesTax(frm, cdt, cdn) {
    var child = locals[cdt][cdn];
    var x = child.sale_tax_value || 0;
    var y = child.qty || 0;
    var w = child.rate || 0;
    var v = y*w;
    var z = x+v;
    var roundedValues = z.toFixed(2);
        
    frappe.model.set_value(cdt, cdn, 'total_inclusive_sales_tax', roundedValues);
}

function pricePerLtOrKg(frm, cdt, cdn) {
    var child = locals[cdt][cdn];
    var rates = child.rate || 0;
    var packSize = child.pack_size || 0;
        
    var calculatedValue = (rates / packSize).toFixed(2);
        
    frappe.model.set_value(cdt, cdn, 'price_per_lt_or_kg', calculatedValue);
}

frappe.ui.form.on('Delivery Note', {
	validate: function(frm) {
        function calculateQtyLtrKg() {
            var totalQty = 0;
            
            frm.doc.items.forEach(function(item){
                totalQty += parseFloat(item.quantity_ltr_kg) || 0;
            });
            
            frm.set_value('total_qty_ltr_kg', totalQty);
        }
        calculateQtyLtrKg();
	}
});