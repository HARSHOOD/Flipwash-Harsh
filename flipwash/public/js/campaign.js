frappe.ui.form.on('Campaign', {
    refresh: function(frm) {
        frm.add_custom_button(__('Assign to All Leads'), function() {
            frappe.call({
                method: 'flipwash.flipwash.api.add_campagin_toall_leads.assign_campaign_to_leads',
                args: {
                    campaign_name: frm.doc.name
                },
                callback: function(r) {
                    if (!r.exc) {
                        frappe.msgprint(__('Campaign assigned to all leads successfully.'));
                    }
                }
            });
        });
    }
});

