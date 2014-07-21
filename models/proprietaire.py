# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class Proprietaire(osv.Model):
    _name = "skateshop.proprietaire"
    
    _columns = {
        'name' : fields.char(string="Title", size=256),
        #Relational
        'skate_ids': fields.one2many('skateshop.skate', 'proprietaire_id',string="Skates"),
    }