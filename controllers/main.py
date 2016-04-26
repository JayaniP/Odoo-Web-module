### -*- coding: utf-8 -*-
from openerp import http,api
from openerp.http import request


class web_demo(http.Controller):

    @http.route(['/main'], type = 'http', auth = 'public', website = True)
    def mainpage(self, **kwargs):
        iot_main_obj = request.env['iot.main']
        if not iot_main_obj:
            res = iot_main_obj.search_read([], ['name', 'channel'])
        return http.request.render('IOT_web.main_page', {'res': res})

    @http.route(['/status'], type='http', auth="public", methods=['POST'], website = True)
    def check_status(self, **kwargs):
        iot_main_obj = request.env['iot.main']
        print kwargs
        res = iot_main_obj.search([('id', '=', kwargs['item_id'])])
        if kwargs['status'] == 'true':
            sdata = res.write({'status' : True })
        else:
            sdata = res.write({'status' : False })
        return {}

    @http.route(['/config'], type = 'http', auth = 'public', website = True)
    def configpage(self, **kwargs):
        iot_main_obj = request.env['iot.main']
        r = iot_main_obj.search([])
        result = []
        for x in r:
            result.append(x.channel)
        val = iot_main_obj.search_read([], ['name', 'channel'])
        return http.request.render('IOT_web.config_page', {'res': result, 'key': val})

    @http.route(['/delete_record'], type='http', auth="public", methods=['POST','GET'], website = True)
    def delete_record(self, **kwargs):
        iot_main_obj = request.env['iot.main']
        res = iot_main_obj.sudo().browse(int(kwargs['item_id']))
        res.unlink()

    @http.route(['/create_record'], type='http', auth="public", methods=['POST'], website = True)
    def create_record(self, **kwargs):
        iot_main_obj = request.env['iot.main']
        res = iot_main_obj.create(kwargs)
        print res

