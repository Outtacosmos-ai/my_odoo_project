# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PaymentWizard(models.TransientModel):
    _name = 'contracts.payment.wizard'
    _description = 'Payment Wizard'

    contract_id = fields.Many2one('contracts.contract', string='Contract', required=True)
    amount = fields.Float(string='Amount', required=True)

    @api.multi
    def action_make_payment(self):
        self.ensure_one()
        self.env['contracts.payment'].create({
            'contract_id': self.contract_id.id,
            'amount': self.amount,
        })
        self.contract_id._onchange_payments()
        return {'type': 'ir.actions.act_window_close'}