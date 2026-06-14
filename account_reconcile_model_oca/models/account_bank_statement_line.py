# Copyright 2023 Dixmit
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models
from odoo.tools import html2plaintext


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    def _retrieve_partner(self):
        # Try the advanced reconcile-model regex partner mapping first, setting
        # partner_id on the matched lines, then defer to account_reconcile_oca's
        # own batch retrieval (bank account / name) for the remaining lines.
        to_retrieve = self.filtered(
            lambda line: not line.partner_id and not line.is_reconciled
        )
        if to_retrieve:
            rec_models = self.env["account.reconcile.model"].search(
                [
                    ("rule_type", "!=", "writeoff_button"),
                    ("company_id", "in", to_retrieve.company_id.ids),
                ]
            )
            for line in to_retrieve:
                for rec_model in rec_models.filtered(
                    lambda m, line=line: m.company_id == line.company_id
                ):
                    partner = rec_model._get_partner_from_mapping(line)
                    if partner and rec_model._is_applicable_for(line, partner):
                        line.partner_id = partner
                        break
        return super()._retrieve_partner()

    def _get_st_line_strings_for_matching(self, allowed_fields=None):
        """Collect the strings that could be used on the statement line to perform some
        matching.
        :param allowed_fields: A explicit list of fields to consider.
        :return: A list of strings.
        """
        self.ensure_one()

        st_line_text_values = []
        if not allowed_fields or "payment_ref" in allowed_fields:
            if self.payment_ref:
                st_line_text_values.append(self.payment_ref)
        if not allowed_fields or "narration" in allowed_fields:
            value = html2plaintext(self.narration or "")
            if value:
                st_line_text_values.append(value)
        if not allowed_fields or "ref" in allowed_fields:
            if self.ref:
                st_line_text_values.append(self.ref)
        return st_line_text_values
