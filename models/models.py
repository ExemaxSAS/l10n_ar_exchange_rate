# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from datetime import date
from odoo.tools import format_date
import logging
_logger = logging.getLogger(__name__)

class ResCurrency(models.Model):
    _inherit = 'res.currency'

    def l10n_ar_action_get_afip_ws_currency_rate(self):
        usd = self.env['res.currency'].search([('name', '=', 'USD')], limit=1)
        rate = usd.get_pyafipws_currency_rate()[0]
        self.env['res.currency.rate'].create({'currency_id': usd.id, 'rate': 1 / rate, 'name': date.today()})
