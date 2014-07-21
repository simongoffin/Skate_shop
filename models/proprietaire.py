# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class Proprietaire(osv.Model):
    _name = "skateshop.proprietaire"
    
    def _get_montant(self, cr, uid, ids, name, arg, context=None):
        result = {}
        for proprietaire in self.browse(cr, uid, ids, context=context):
            result[proprietaire.id] = 0
            for skate in proprietaire.skate_ids:
                    result[proprietaire.id] += skate.prix
        return result
        
    
    _columns = {
        'name' : fields.char(string="Title", size=256),
        #Relational
        'skate_ids': fields.one2many('skateshop.skate', 'proprietaire_id',string="Skates"),
        #Fonctional
        'montant' : fields.function(_get_montant,type='integer', string='Montant'),
    }