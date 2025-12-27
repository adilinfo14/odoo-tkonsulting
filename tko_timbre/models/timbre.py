from odoo import models, fields

class TkTimbre(models.Model):
    _name = "tko.timbre"
    _description = "Timbre fiscal"

    name = fields.Char(required=True)
    country_id = fields.Many2one("res.country", string="Pays", required=True)
    amount = fields.Float(string="Montant", required=True)
    active = fields.Boolean(default=True)