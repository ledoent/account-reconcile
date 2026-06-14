To configure an invoice-matching rule:

1. Go to *Accounting > Configuration > Banks > Reconciliation Models* and create
   or open a model.
2. Set **Type** to *Rule to match invoices/bills*. The invoice-matching options
   appear once this type is selected.
3. In the left column, restrict the rule with the matching criteria you need:
   journals, amount nature (received/paid), amount range, partner / partner
   categories, same currency, search-months limit, candidate ordering
   (oldest/newest first) and unique-match.
4. In the **Invoice Matching** tab, choose where to search the
   invoice/payment reference (label, notes, reference) and configure the
   note/transaction-type filters and the payment tolerance (fixed amount or
   percentage).
5. Tick **Auto-validate** to let the model reconcile automatically when a
   confident match is found.
6. Optionally, in the **Partner Mapping** tab, add regular expressions on the
   statement label / notes to derive the partner when it is not set.

When reconciling a bank statement in the OCA reconciliation widget, applicable
models propose (or auto-validate) the matching invoices/bills.
