# Copyright 2024 Dixmit
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Account Reconcile Model Oca",
    "summary": """
        Advanced invoice-matching & write-off rules for the OCA bank
        reconciliation widget (the engine 19.0 core moved to Enterprise)""",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "author": "Dixmit,Odoo,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/account-reconcile",
    "maintainers": ["dnplkndll"],
    "depends": ["account_reconcile_oca"],
    "excludes": ["account_accountant"],
    "data": [
        "security/ir.model.access.csv",
        "views/account_reconcile_model_views.xml",
    ],
    "demo": [],
}
