# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ContractLine(models.Model):
    _name = 'contracts.contract.line'
    _description = 'Contract Line'

    contract_id = fields.Many2one('contracts.contract', string='Contract', required=True)
    language = fields.Char(string='Language')
    language_formalized = fields.Char(string='Language Formalized')
    value_added_tax = fields.Float(string='Value Added Tax', default=20.0)
    ht = fields.Float(string='HT')
    ttc = fields.Float(string='TTC', compute='_compute_ttc', store=True)

    @api.depends('ht', 'value_added_tax')
    def _compute_ttc(self):
        for line in self:
            line.ttc = line.ht * (1 + line.value_added_tax / 100)