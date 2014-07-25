from openerp import http
import simplejson
from openerp.http import request, serialize_exception as _serialize_exception
from cStringIO import StringIO
from collections import deque

class TableExporter(http.Controller):

    @http.route('/web_graph/check_xlwt', type='json', auth='none')
    def check_xlwt(self):
        return "RPC ok!"