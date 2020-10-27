# -*- coding: utf-8 -*-

# from odoo import models, fields, api


from odoo import models, fields 
from odoo.exceptions import ValidationError

###########################################################

class CategoriaIngreso(models.Model):
   _name = "categoria.ingreso"

descripcion = fields.Char('Descripcion', required=True)
activo = fields.Boolean('Activo?', default=True)

class CategoriaEgreso(models.Model):
   _name = "categoria.egreso"

descripcion = fields.Char('Descripcion', required=True)
activo = fields.Boolean('Activo?', default=True)

class CategoriaCliente(models.Model):
   _name = "categoria.cliente"

descripcion = fields.Char('Descripcion', required=True)
activo = fields.Boolean('Activo?', default=True)

###########################################################

class Cliente(models.Model):
   _name = "cliente"

descripcion  = fields.Char('Descripcion', required=True)
ruc          = fields.Char('RUC',required=True)
tipo_cliente = fields.Many2one('categoria.cliente', string='Tipo Cliente')
activo       = fields.Boolean('Activo?',default=True)

class Proveedor(models.Model):
   _name = "proveedor"

descripcion  = fields.Char('Descripcion', required=True)
ruc          = fields.Char('RUC',required=True)
activo       = fields.Boolean('Activo?',default=True)


###########################################################

class Ingreso(models.Model):
   _name = "ingreso"

cliente_id               = fields.Many2one('Cliente', string="Cliente")
comentario               = fields.Char('Descripcion', required=True)
fecha_provision_ingreso  = fields.Date('Fecha Ingreso')
periodo                  = fields.Selection([
                                             ('2020-08','2020-08'),
                                             ('2020-09','2020-09'),
                                             ('2020-10','2020-10')
                                            ])

class Egreso(models.Model):
   _name = "egreso"

proveedor_id             = fields.Many2one('Proveedor', string="Proveedor")
comentario               = fields.Char('Descripcion', required=True)
fecha_provision_egreso  = fields.Date('Fecha Egreso')
periodo                  = fields.Selection([
                                             ('2020-08','2020-08'),
                                             ('2020-09','2020-09'),
                                             ('2020-10','2020-10')
                                            ])

###########################################################


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