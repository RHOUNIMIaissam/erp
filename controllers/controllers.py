# -*- coding: utf-8 -*-
# from odoo import http


# class Auc(http.Controller):
#     @http.route('/auc/auc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/auc/auc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('auc.listing', {
#             'root': '/auc/auc',
#             'objects': http.request.env['auc.auc'].search([]),
#         })

#     @http.route('/auc/auc/objects/<model("auc.auc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('auc.object', {
#             'object': obj
#         })
