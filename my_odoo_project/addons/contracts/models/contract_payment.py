# -*- coding: utf-8 -*-

from odoo import models, fields

class ContractPayment(models.Model):
    _name = 'contracts.payment'
    _description = 'Contract Payment'

    contract_id = fields.Many2one('contracts.contract', string='Contract', required=True)
    amount = fields.Float(string='Amount', required=True)