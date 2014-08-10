import openerp
from openerp import http
import simplejson
from openerp.http import request, serialize_exception as _serialize_exception
from cStringIO import StringIO
from collections import deque

def get_id(seq):
    debut='data-oe-id="'
    pos=seq.index(debut)
    pos+=len(debut)
    result=""
    while seq[pos] !='"':
        result+=(seq[pos])
        pos+=1
    return int(result)

class TableExporter(http.Controller):

    @http.route('/request_model', type='json', auth='none')
    def check_xlwt(self, view_id):
        return "RPC ok!"
        
    @http.route(['/request_rpc'], type='json', auth="public", website=True)
    def publish_prix(self, prix):
        #from pudb import set_trace; set_trace()
        cr, uid, context = request.cr, openerp.SUPERUSER_ID, request.context
        #iuv = request.registry['ir.ui.view']
        mymodel=request.registry["skateshop.skate"]
        result=mymodel.search(cr, uid, [
            ('prix', '=', int(prix)),],context=request.context)
        return result

    @http.route(['/list_skates'], type='json', auth="public", website=True)
    def publish(self):
        #from pudb import set_trace; set_trace()
        cr, uid, context = request.cr, openerp.SUPERUSER_ID, request.context
        mymodel=request.registry["skateshop.skate"]
        result=mymodel.search(cr, uid, [], offset=0, limit=None, order=None, context=None, count=False)
        return result
        
    @http.route(['/get_product/<value>'], type='http', auth="public", website=True)
    def get_version(self,value):
        print 'ID={}'.format(value)
        return value