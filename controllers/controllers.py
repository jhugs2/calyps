# -*- coding: utf-8 -*-
from odoo import http

# class Calyps(http.Controller):
#     @http.route('/calyps/calyps/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/calyps/calyps/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('calyps.listing', {
#             'root': '/calyps/calyps',
#             'objects': http.request.env['calyps.calyps'].search([]),
#         })

#     @http.route('/calyps/calyps/objects/<model("calyps.calyps"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('calyps.object', {
#             'object': obj
#         })