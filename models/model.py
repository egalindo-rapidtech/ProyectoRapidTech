# -*- coding: utf-8 -*-

# from odoo import models, fields, api


from odoo import models, fields, api
from odoo.exceptions import ValidationError

###########################################################

class CategoriaIngreso(models.Model):
   _name = 'modulo1.categoria.ingreso'

   descripcion = fields.Char('Descripcion', required=True)
   activo = fields.Boolean('Activo?', default=True)

class CategoriaEgreso(models.Model):
   _name = 'modulo1.categoria.egreso'

   descripcion = fields.Char('Descripcion', required=True)
   activo = fields.Boolean('Activo?', default=True)




###########################################################

class Cliente(models.Model):
   _name = 'modulo1.cliente'

   descripcion    = fields.Char('Descripcion', required=True)
   ruc            = fields.Char('RUC', required=True)
   cel_contacto   = fields.Char('Contacto', required=True)
   #tipo_entidad   = fields.Selection([('Cliente','Proveedor')])
   activo         = fields.Boolean('Activo?',default=True)

class Proveedor(models.Model):
   _name = 'modulo1.proveedor'

   descripcion    = fields.Char('Descripcion', required=True)
   ruc            = fields.Char('RUC', required=True)
   cel_contacto   = fields.Char('Contacto', required=True)
   #tipo_entidad   = fields.Selection([('Cliente','Proveedor')])
   activo         = fields.Boolean('Activo?',default=True)

   #def filtrar_tipo_entidad(self):

###########################################################

class Ingreso(models.Model):
   _name = 'modulo1.ingreso'
   #Quiero enlazar una entidad de tipo cliente que debo hacer para filtrar a los datos de entidad
   cliente_id               = fields.Many2one('Cliente', string='Cliente') 
   comentario               = fields.Char('Descripcion', required=True)
   fecha_provision_ingreso  = fields.Date('Fecha Ingreso')
   igv                      = fields.Boolean('Con IGV', default=True)
   monto_provision_ingreso  = fields.Float('SubTotal', required=True)
   periodo                  = fields.Selection([
                                                ('2020-08','2020-08'),
                                                ('2020-09','2020-09'),
                                                ('2020-10','2020-10')
                                             ])
   


   #def recaudar(self):
      


class Egreso(models.Model):
   _name = 'modulo1.egreso'

   proveedor_id             = fields.Many2one('Proveedor', string='Proveedor')
   comentario               = fields.Char('Descripcion', required=True)
   fecha_provision_egreso   = fields.Date('Fecha Egreso')
   igv                      = fields.Boolean('Con IGV', default=True)
   monto_provision_egreso   = fields.Float('Sub Total', required=True)
   periodo                  = fields.Selection([
                                                ('2020-08','2020-08'),
                                                ('2020-09','2020-09'),
                                                ('2020-10','2020-10')
                                             ])

   #def desembolsar(self):


###########################################################

class Pago(models.Model):
   _name = 'modulo1.pago'

   @api.onchange('monto_pago')
   def CalcularTotal(self):
      self.monto_pago_igv   =  monto_pago * 0.12 
      self.monto_pago_total =  monto_pago_igv + monto_pago

   #origen_id   = fields.Char
   comentario  = fields.Char('Comentario', required=False)
   fecha_pago  = fields.Date('Fecha Pago')
   metodo_pago = fields.Selection([('Transferencia','Deposito')])
   monto_pago       = fields.Float('SubTotal', required=True)
   monto_pago_igv   = fields.Float('SubTotal IGV')
   monto_pago_total = fields.Float('Total')
   


"""
class GrupoEgreso(models.Model):
   _name = "grupo.egreso"

descripcion = fields.Char('Description', required=True)
activo = fields.Boolean('Active?', default=True)
"""

"""
class Mesa(models.Model):
   _name = "testing.mesa"

   name = fields.Char(string='Nombre')
   testing_silla_ids = fields.One2many('testing.silla', 'testing_mesa_id', string='Mesa')


class Silla(models.Model):
   _name = "testing.silla"

   name = fields.Char(string='Nombre')
   testing_mesa_id = fields.Many2one(comodel_name='testing.mesa', string='Mesa')
"""
# class modulo1(models.Model):
#     _name = 'modulo1.modulo1'
#     _description = 'modulo1.modulo1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

"""
class TodoTask2(models.Model):
    _name = 'todo.task2'
    _description = 'To-do Task2'
    
    def action_test2(self):
        raise ValidationError("Esta ventana se abrio desde con TodoTask2 y una vista diferente")


    name_2 = fields.Char('Description_2', required = True)
    is_done_2 = fields.Boolean('Done_2?') 
    active_2 = fields.Boolean('Active_2?', default=True)
"""