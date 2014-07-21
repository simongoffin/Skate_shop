# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class Skate(osv.Model):
    _name = "skateshop.skate"
    
    _columns = {
        'name' : fields.char(string="Title", size=256, required=True),
        'prix' : fields.integer(string="Prix"),
        'description' : fields.text(string="Description"),
        #Relational
        'proprietaire_id' : fields.many2one('skateshop.proprietaire',ondelete='cascade', string="Proprietaire", required=True),
    }
    