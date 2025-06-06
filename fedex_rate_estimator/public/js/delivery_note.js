frappe.ui.form.on('Delivery Note', {
  refresh: function (frm) {
    //if (frm.doc.docstatus === 1) {  // Only on submitted documents
      frm.add_custom_button('Get FedEx Rates', () => {
        frappe.prompt(
          [
            {
              label: 'Weight (LB)',
              fieldname: 'weight',
              fieldtype: 'Float',
              default: 10
            }
          ],
          (values) => {
            frappe.call({
              method: "fedex_rate_estimator.api.fedex_api.get_fedex_rates",
              args: {
                dispatch_address: {
                  streetLines: ["Company Address Line 1", "Line 2"], // You can customize this logic
                  city: "Your City",
                  stateOrProvinceCode: "ST",
                  postalCode: "00000",
                  countryCode: "US",
                  residential: false
                },
                shipping_address: {
                  streetLines: [frm.doc.address_display || "Customer Address"],
                  city: "Customer City",
                  stateOrProvinceCode: "ST",
                  postalCode: "00000",
                  countryCode: "US",
                  residential: false
                },
                weight: values.weight
              },
              callback: function (r) {
                if (r.message) {
                  let html = `<table class="table table-bordered"><thead><tr><th>Rate Type</th><th>Amount</th></tr></thead><tbody>`;
                  for (let rate of r.message) {
                    html += `<tr><td>${rate.type}</td><td>$${rate.amount}</td></tr>`;
                  }
                  html += "</tbody></table>";

                  frappe.msgprint({
                    title: 'FedEx Rates',
                    indicator: 'blue',
                    message: html
                  });
                } else {
                  frappe.msgprint("No rates found.");
                }
              }
            });
          },
          'Enter Weight'
        );
      });
    //}
  }
});
