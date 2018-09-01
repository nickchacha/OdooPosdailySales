# -*- coding: utf-8 -*-
import json
import logging
import werkzeug.utils

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class DailyPosController(http.Controller):
	@http.route('/pos/daily_sale_details_report', type='http', auth='user')
    def print_sale_details(self, date_start=False, date_stop=False, **kw):
        r = request.env['point_of_salereport.pos_dairyorders_report_view']
        pdf, _ = request.env.ref('point_of_salereport.pos_dairyorders_report_view').with_context(date_start=date_start, date_stop=date_stop).render_qweb_pdf(r)
        pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf))]
        return request.make_response(pdf, headers=pdfhttpheaders)
