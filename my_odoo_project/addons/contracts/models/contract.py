# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Contract(models.Model):
    _name = 'contracts.contract'
    _description = 'Contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'sequence, id'

    name = fields.Char(string='Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    sequence = fields.Integer(string='Sequence', default=10)
    ht = fields.Float(string='HT', compute='_compute_amounts', store=True)
    ttc = fields.Float(string='TTC', compute='_compute_amounts', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('partial', 'Partial Payment'),
        ('paid', 'Full Payment')
    ], string='State', default='draft', track_visibility='onchange')

    contract_line_ids = fields.One2many('contracts.contract.line', 'contract_id', string='Contract Lines')
    payment_ids = fields.One2many('contracts.payment', 'contract_id', string='Payments')

    @api.depends('contract_line_ids.ht', 'contract_line_ids.ttc')
    def _compute_amounts(self):
        for contract in self:
            contract.ht = sum(contract.contract_line_ids.mapped('ht'))
            contract.ttc = sum(contract.contract_line_ids.mapped('ttc'))

    @api.onchange('payment_ids')
    def _onchange_payments(self):
        total_paid = sum(self.payment_ids.mapped('amount'))
        if total_paid >= self.ttc:
            self.state = 'paid'
        elif total_paid > 0:
            self.state = 'partial'
        else:
            self.state = 'draft'