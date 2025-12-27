from odoo import models, fields, api

class TkTimbre(models.Model):
    _name = "tko.timbre"
    _description = "Timbre fiscal"

    name = fields.Char(required=True)

    country_id = fields.Many2one(
        "res.country",
        string="Pays",
        required=True
    )

    partner_id = fields.Many2one(
        "res.partner",
        string="Client",
        help="Si renseigné, ce timbre s'applique uniquement à ce client"
    )

    amount = fields.Float(
        string="Montant du timbre",
        required=True
    )

    active = fields.Boolean(default=True)
        @api.model
    def get_timbre_for_partner(self, partner):
        """Retourne le timbre applicable à un client"""

        # 1️⃣ Timbre spécifique client
        timbre = self.search([
            ("partner_id", "=", partner.id),
            ("active", "=", True)
        ], limit=1)

        if timbre:
            return timbre.amount

        # 2️⃣ Timbre par pays
        timbre = self.search([
            ("partner_id", "=", False),
            ("country_id", "=", partner.country_id.id),
            ("active", "=", True)
        ], limit=1)

        return timbre.amount if timbre else 0.0
