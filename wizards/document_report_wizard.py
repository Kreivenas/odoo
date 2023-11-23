from odoo import models, fields, api

class DocumentReportWizard(models.TransientModel):
    _name = 'document.report.wizard'
    _description = 'Dokumentų Ataskaitos Vedlys'

    date_from = fields.Date(string='Data nuo')
    date_to = fields.Date(string='Data iki')

    def button_generate_report(self):
        data = {
            'ids': self.ids,
            'model': 'document.management',
            'form': {
                'date_from': self.date_from,
                'date_to': self.date_to,
            },
        }

        return self.env.ref('your_module.report_document').report_action(self, data=data)

