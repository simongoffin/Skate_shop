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
    def publish(self, id):
        #from pudb import set_trace; set_trace()
        _id = int(id)
        
        return _id
        #obj = _object.browse(request.cr, request.uid, _id)

#         values = {}
#         if 'website_published' in _object._all_columns:
#             values['website_published'] = not obj.website_published
#         _object.write(request.cr, request.uid, [_id],
#                       values, context=request.context)
# 
#         obj = _object.browse(request.cr, request.uid, _id)
#         return bool(obj.website_published)