import openerp
from openerp import http
import simplejson
from openerp.http import request, serialize_exception as _serialize_exception
from cStringIO import StringIO
from collections import deque

class TableExporter(http.Controller):

    @http.route('/request_model', type='json', auth='none')
    def check_xlwt(self, view_id):
        return "RPC ok!"
        
    @http.route(['/request_rpc'], type='json', auth="public", website=True)
    def publish(self, prix):
        #from pudb import set_trace; set_trace()
        cr, uid, context = request.cr, openerp.SUPERUSER_ID, request.context
        #iuv = request.registry['ir.ui.view']
        mymodel=request.registry["skateshop.skate"]
        mimetype ='application/xml;charset=utf-8'
        result=mymodel.search(cr, uid, [
            ('prix', '=', int(prix)),],context=request.context)
        return result
