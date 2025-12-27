from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    timbre_amount = fields.Float(
        string="Timbre fiscal",
        compute="_compute_timbre_amount",
        store=True
    )

    total_with_timbre = fields.Float(
        string="Total avec timbre",
        compute="_compute_total_with_timbre",
        store=True
    )

    @api.depends("partner_id")
    def _compute_timbre_amount(self):
        for order in self:
            if not order.partner_id:
                order.timbre_amount = 0.0
                continue

            timbre = self.env["tko.timbre"].get_timbre_for_partner(
                order.partner_id
            )
            order.timbre_amount = timbre

    @api.depends("amount_total", "timbre_amount")
    def _compute_total_with_timbre(self):
        for order in self:
            order.total_with_timbre = order.amount_total + order.timbre_amount
