# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json

class InventarioController(http.Controller):
    @http.route('/api/inventario',auth='public', method=['GET'],csrf=False)
    def get_inventario(self, **kw):
        try:
            items = http.request.env['inventario.inventario'].sudo().search_read([],['code', 'name', 'type', 'number_units'])
            res = json.dumps(items,ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error':str(e)}), content_type='application/json;charset=utf-8', status=505)



# class Inventario(http.Controller):
#     @http.route('/inventario/inventario/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventario/inventario/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventario.listing', {
#             'root': '/inventario/inventario',
#             'objects': http.request.env['inventario.inventario'].search([]),
#         })

#     @http.route('/inventario/inventario/objects/<model("inventario.inventario"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventario.object', {
#             'object': obj
#         })
