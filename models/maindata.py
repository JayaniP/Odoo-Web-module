# -*- coding: utf-8 -*-
from openerp import api, fields, models

channel_selection = [('1', '1'), ('2', '2'), ('3', '3'),
                                 ('4', '4'), ('5', '5'), ('6', '6'),
                                 ('7', '7'), ('8', '8')]

class iot_main(models.Model):
    _name = "main.iot"
    _description = 'IOT Main'

    name = fields.Char("Name")
    channel = fields.Selection(channel_selection, 'Channel')
    status = fields.Boolean("Status", default=True)