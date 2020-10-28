# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

###########################################################

class CobroIngreso(models.TransientModel):
   _name = 'modulo1.cobro.ingreso'

   monto = fields.Float('Monto')
   monto_igv = fields.Float('Monto IGV?')
   monto_total = fields.Float('Monto Total')

   def cobrar_ingreso(self):
      ingreso_id = self.env['modulo1.ingreso'].browse(self._context.get('active_id'))
      monto_max = ingreso_id.monto_provision_ingreso
      if self.monto <= monto_max :
         print('SE valido que es menor a monto max')
      else:
         raise UserError('Se ingreso un monto de pago mayor al del ingreso')



