This module adds an **advanced invoice-matching engine** to the OCA bank
reconciliation widget (`account_reconcile_oca`).

Odoo 19.0 stripped the reconciliation-model matching configuration out of
Community core (it now lives in Enterprise). This module restores it for
Community: it extends `account.reconcile.model` with the rules needed to
automatically match bank statement lines against open invoices/bills, and
plugs the result into the `account_reconcile_oca` widget.

It provides:

- **Invoice matching** by text tokens found in the statement label, notes or
  reference, by amount (exact or within a configurable payment tolerance),
  partner, partner category, journal, currency and transaction nature.
- **Payment tolerance** (fixed amount or percentage), with optional
  auto-validation.
- **Regex partner mapping**: derive the partner of a statement line from its
  label/notes when none is set.
- **Unique-match** enforcement and **oldest/newest-first** ordering of
  candidates.
