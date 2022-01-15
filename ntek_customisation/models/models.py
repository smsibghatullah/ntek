# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class ProjectTask(models.Model):
    _inherit = 'project.task'

    date_deadline = fields.Date(string='Ticket Date')
    contract_id = fields.Many2one('contract', string='Contract')
    ticket_no = fields.Char(string = 'Ticket No.')
    scope_of_work = fields.Char(string = 'Scope Of Work')
    travel_start = fields.Datetime(string = 'Travel Start') #Leaving For SITE
    arrival_on_site = fields.Datetime(string = 'Arrival On Site') #Arrival On SITE
    repair_start = fields.Datetime(string = 'Repair Start') #Work Start
    repair_stop = fields.Datetime(string = 'Repair Stop') #Work Stop
    sign_off_taken = fields.Datetime(string='Sign Off Taken') #Sign Off Taken
    sign_off_submitted = fields.Datetime(string='Sign Off Submitted') #Sign Off Submitted
    leave_site = fields.Datetime(string = 'Leave Site') #Levae Site
    travel_stop = fields.Datetime(string = 'Travel Stop')
    km_start = fields.Float(string = 'KM Start')
    km_till_date = fields.Float(string = 'KM Till Date')
    km_end = fields.Float(string = 'KM End')
    field_engineer_note = fields.Char(string = 'Field Engineer Note')
    # end_client = fields.Char(string = 'End Client')
    # site_address = fields.Char(string = 'Site Address')
    # city = fields.Char(string = 'City')
    # country = fields.Char(string = 'Country')
    # point_of_contact = fields.Char(string = 'Point Of Contact (POC)')
    # mobile = fields.Char(string = 'Mobile Number')


class Contract(models.Model):
    _name = 'contract'

    name = fields.Char('name')

class ProjectType(models.Model):
    _name = 'project.type'

    name = fields.Char(string = 'Project Type')

class ProjectSubType(models.Model):
    _name = 'project.sub.type'

    project_type = fields.Many2one('project.type', string='Project Type')
    name = fields.Char(string='Project Sub Type')

class Project(models.Model):
    _inherit = 'project.project'

    project_type = fields.Many2one('project.type', string='Project Type')
    project_sub_type = fields.Many2one('project.sub.type', string="Project Sub Type", domain="[('project_type', '=', project_type)]")
    description = fields.Char(string='Description')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

