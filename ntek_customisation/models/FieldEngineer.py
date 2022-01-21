from odoo import models, fields, api


class FieldEngineer(models.Model):
    _name = 'field.engineer'

    name = fields.Char(string = 'First Name', required = 'True')
    last_name = fields.Char(string = 'Last Name', required = 'True')
    country = fields.Char(string = 'Country')
    city = fields.Char(string='City')
    email = fields.Char(string = 'E-mail')
    mobile = fields.Char(string = 'Mobile No.')
    user_id = fields.Char(string = 'User ID', required = 'True')
    user_password = fields.Char(string = 'Password', required = 'True')

    @api.model
    def create(self, vals):
        print(vals)
        fe = super(FieldEngineer, self).create(vals)
        pos_groups = self.env['res.groups'].with_context(lang='en_US').search([('category_id.name', '=', 'Project')], order="id")
        pos_groups_name =  'sel_groups_' + '_'.join(str(it) for it in pos_groups.ids)
        fe_groups = self.env['res.groups'].with_context(lang='en_US').search([('name', '=', 'Field Engineer')], order="id")
        fe_group_name = 'in_group_' + str(fe_groups.id)

        for pos_group_item in pos_groups:
            if pos_group_item.name == 'Administrator':
                pos_admin = pos_group_item.id
            elif pos_group_item.name == 'User':
                pos_user = pos_group_item.id

        user_vals = {
            'name': fe.name + " " + fe.last_name,
            'login': fe.user_id,
            'password': fe.user_password,
            pos_groups_name: pos_user,
            fe_group_name: True
        }
        user_id = self.env['res.users'].create(user_vals)
        return fe

    def write(self, vals):
        fe = super(FieldEngineer, self).write(vals)
        user_vals = {
            'password': self.user_password,
        }
        user = self.env['res.users'].search([('login','=',self.user_id)])
        user.write({'password':self.user_password})
        return fe




