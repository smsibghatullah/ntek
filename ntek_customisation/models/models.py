# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ProjectTask(models.Model):
    _inherit = 'project.task'

    contract_id = fields.Many2one('contract', string='Contract')


class Contract(models.Model):
    _name = 'contract'

    name = fields.Char('name')