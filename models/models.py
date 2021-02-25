# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inventario(models.Model):
    _name = 'inventario.inventario'
    _description = 'Inventario'

    code = fields.Char(string="Código")
    name = fields.Char(string="Nombre")
    date_enter = fields.Datetime(string="Fecha de entrada")
    date_exit = fields.Datetime(string="Fecha de salida")
    type = fields.Selection(
        [('T', 'Torre'), ('P', 'Portátil'), ('R', 'Periférico'), ('S', 'Software'), ('A', 'Almacenamiento')],
        string="Tipo")
    in_use = fields.Boolean(string="En uso")
    number_units = fields.Integer(string="Nº de unidades")
    image_field = fields.Binary(string="Imagen")

    def f_change_in_use(self):
        self.in_use = not self.in_use

class DeviceReport(models.AbstractModel):
     _name='report.inventario.report_device_card'
     _description='Informe de dispositivo'
     @api.model
     def _get_report_values(self, docids, data=None):
          report_obj = self.env['ir.actions.report']
          report = report_obj._get_report_from_name('inventario.report_device_card')
          return {
               'doc_ids':docids,
               'doc_model':self.env['inventario.inventario'],
               'docs':self.env['inventario.inventario'].browse(docids)
          }