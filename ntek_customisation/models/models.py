# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class ProjectTask(models.Model):
    _inherit = 'project.task'

    contract_id = fields.Many2one('contract', string='Contract')
    ticket_no = fields.Char(string = 'Ticket No.')
    scope_of_work = fields.Char(string = 'Scope Of Work')
    travel_start = fields.Datetime(string = 'Travel Start')
    arrival_on_site = fields.Datetime(string = 'Arrival On Site')
    repair_start = fields.Datetime(string = 'Repair Start')
    repair_stop = fields.Datetime(string = 'Repair Stop')
    leave_site = fields.Datetime(string = 'Leave Site')
    travel_stop = fields.Datetime(string = 'Travel Stop')
    km_start = fields.Float(string = 'KM Start')
    km_till_date = fields.Float(string = 'KM Till Date')
    km_end = fields.Float(string = 'KM End')
    # end_client = fields.Char(string = 'End Client')
    # site_address = fields.Char(string = 'Site Address')
    # city = fields.Char(string = 'City')
    # country = fields.Char(string = 'Country')
    # point_of_contact = fields.Char(string = 'Point Of Contact (POC)')
    # mobile = fields.Char(string = 'Mobile Number')


class Contract(models.Model):
    _name = 'contract'

    name = fields.Char('name')