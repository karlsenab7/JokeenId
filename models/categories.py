# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Categories(models.Model):
    _name = "jokeen.transactions.categories"
    _description = "Jokeen Transaction Categories"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    reference = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    transType = fields.Selection([
            ('income', 'Income'),
            ('expenditure', 'Expenditure'),
        ], string='Type', default='expenditure', required=True)
    name = fields.Char(string='Category', required=True)
    note = fields.Text(string='Description')

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Category'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('jokeen.transactions.categories.sequence')
        res = super(Categories, self).create(vals)
        return res