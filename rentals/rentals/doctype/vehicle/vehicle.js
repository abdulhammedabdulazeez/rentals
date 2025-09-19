// Copyright (c) 2025, HamidDev and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle", {
	// refresh(frm) {

	// },

	is_published(frm) {
		if (frm.doc.is_published && !frm.doc.route) {
			let display_name = `${frm.doc.make} ${frm.doc.model} ${frm.doc.year}`;
			let safe_display_name = encodeURIComponent(display_name.replace(/\s+/g, "-"));
			frm.set_value("route", "cars/" + safe_display_name);
		}
	},

	get_summary(frm) { 
		frm.get_field("summary").$wrapper.append('<h1>Here is your summary</h1>');
	}
});
