from odoo import models, fields, api

class Document(models.Model):
    _name = 'document.management'
    _description = 'Dokumentų Valdymas'

    name = fields.Char(string='Pavadinimas', required=True)
    description = fields.Text(string='Aprašymas')
    company_id = fields.Many2one('res.company', string='Įmonė')
    date = fields.Date(string='Data')

@api.model
def _get_menu_action(self):
    return {
        "type": "ir.actions.act_window",
        "name": "Document",
        "res_model": self._name,
        "view_mode": "tree,form",
    } 