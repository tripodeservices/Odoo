from odoo import http
from odoo.http import request

class DisableBenchmarks(http.Controller):
    @http.route('/web/benchmarks', type='http', auth='none', csrf=False)
    def disable_benchmarks(self, **kwargs):
        # Renvoyer une erreur 404 pour cette route
        return request.not_found()
