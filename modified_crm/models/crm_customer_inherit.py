from odoo import models, fields, api
from odoo.exceptions import UserError


class CrmCustomerInherit(models.Model):
    _inherit = 'res.partner'

    # It should be relation one2one !!!!!!!
    related_patient_id = fields.Many2one("hms.patient")
    # related_patient_id = fields.Integer()

    # @api.constrains()

    def unlink(self):
        for cus in self:
            if cus.related_patient_id:
                raise UserError("You can not delete Customer related to patient")
        super().unlink()

    @api.constrains('email')
    def _check_customer_email(self):
        patient = self.env['hms.patient'].search([('email', '=', self.email)])
        if patient:
            raise UserError(f"{self.email} is already exists for patient")

