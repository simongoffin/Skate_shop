# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class Skate(osv.Model):
    _name = "skateshop.skate"
    
    _columns = {
        'name' : fields.char(string="Title", size=256, required=True),
        'description' : fields.text(string="Description"),
    }
    