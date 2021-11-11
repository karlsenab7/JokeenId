# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Categories(models.Model):
    _name = "jokeen.transactions.categories"
    _description = "Jokeen Transaction Categories"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Category', required=True)
    note = fields.Text(string='Description')
