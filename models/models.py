# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from datetime import date
from odoo.tools import format_date
from odoo.exceptions import ValidationError

class ResCurrency(models.Model):
    _inherit = 'res.currency'

    def l10n_ar_action_get_afip_ws_currency_rate(self):
        usd = self.env['res.currency'].search([('name', '=', 'USD')], limit=1)
        rate = usd.get_pyafipws_currency_rate()[0]
        currentRate = usd.rate_ids.filtered(lambda r: r.name == date.today())
        if currentRate:
            currentRate[0].inverse_company_rate = rate
        else:
            usd.update({'rate_ids': [(0, 0, {'name': date.today(), 'inverse_company_rate': rate})]})
