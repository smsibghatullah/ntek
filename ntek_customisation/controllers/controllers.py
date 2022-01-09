# -*- coding: utf-8 -*-
# from odoo import http


# class NtekCustomisation(http.Controller):
#     @http.route('/ntek_customisation/ntek_customisation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ntek_customisation/ntek_customisation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ntek_customisation.listing', {
#             'root': '/ntek_customisation/ntek_customisation',
#             'objects': http.request.env['ntek_customisation.ntek_customisation'].search([]),
#         })

#     @http.route('/ntek_customisation/ntek_customisation/objects/<model("ntek_customisation.ntek_customisation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ntek_customisation.object', {
#             'object': obj
#         })
