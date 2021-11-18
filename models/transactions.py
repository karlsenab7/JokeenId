# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class Transactions(models.Model):
    _name = "jokeen.transactions"
    _description = "Jokeen Transaction"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # sequence
    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    transType = fields.Selection([
            ('income', 'Income'),
            ('expenditure', 'Expenditure'),
        ], string='Type', default='expenditure', required=True)
    category = fields.Many2one(comodel_name="jokeen.transactions.categories", string="Category", required=True)
    
    transDate = fields.Date(string="Date", required=True, track_visibility='onchange')
    nominal = fields.Integer(string='Nominal', required=True, track_visibility='onchange')
    note = fields.Text(string='Description', track_visibility='onchange')

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Transaction'
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('jokeen.transactions.sequence')
        res = super(Transactions, self).create(vals)
        return res

    @api.constrains('nominal')
    def check_nominal(self):
        for rec in self:
            if rec.nominal < 0:
                raise ValidationError(_('Nominal can not be less than zero !'))