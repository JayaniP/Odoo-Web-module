### -*- coding: utf-8 -*-
from openerp import http,api
from openerp.http import request
import serial

#seri = serial.Serial('/dev/ttyUSB0',9600)


class web_demo(http.Controller):

    @http.route(['/main'], type = 'http', auth = 'public', website = True)
    def mainpage(self, **kwargs):
        main_iot_obj = request.env['main.iot'].search([])
#        if not iot_main_obj:
#            res = iot_main_obj.search_read([], ['name', 'channel'])
#            print "***********",res
        return http.request.render('IOT_web.main_page', {'res': main_iot_obj})

    @http.route(['/status'], type='http', auth="public", methods=['POST'], website = True)
    def check_status(self, **kwargs):
        main_iot_obj = request.env['main.iot']
        print "***Status***",kwargs
        res = main_iot_obj.search([('id', '=', kwargs['item_id'])])
#        res1 = iot_main_obj.search_read([], [ 'name','channel'])
        for x in res:
            print x.status
            pin = x.channel 
#          pro = iot_main_obj.search([],['name','channel'])
        if kwargs['status'] == 'true':
            sdata = res.write({'status' : True })
#            seri.write(pin,'1')
            
            print "+++++++++++",res
        else:
            sdata = res.write({'status' : False })
            print "+++++++++++",res
#            seri.write(pin,'0')
#            print pro
        return {}
    
    @http.route(['/statusval'], type='http', auth="public", methods=['POST'], website = True)
    def status(self, **kwargs):
        main_iot_obj = request.env['main.iot']
        print "***Status***",kwargs
        res = main_iot_obj.search_read([], ['name', 'channel'])
        print "***********",res
       
        return {}
        
    @http.route(['/config'], type = 'http', auth = 'public', website = True)
    def configpage(self, **kwargs):
        main_iot_obj = request.env['main.iot']
        r = main_iot_obj.search([])
        result = []
        for x in r:
            result.append(x.channel)
        val = main_iot_obj.search_read([], ['name', 'channel'])
        print "******Val****",val
        return http.request.render('IOT_web.config_page', {'res': result, 'key': val})

    @http.route(['/delete_record'], type='http', auth="public", methods=['POST','GET'], website = True)
    def delete_record(self, **kwargs):
        main_iot_obj = request.env['main.iot']
        res = main_iot_obj.sudo().browse(int(kwargs['item_id']))
        res.unlink()

    @http.route(['/create_record'], type='http', auth="public", methods=['POST'], website = True)
    def create_record(self, **kwargs):
        print '&&&&&&&&&&&&&&',kwargs
        main_iot_obj = request.env['main.iot']
        res = main_iot_obj.create(kwargs)
        print '@@@@@@@@@@@',res
        

