# -*- coding: utf-8 -*-
# 15.0 EE

from odoo import models, fields, api
from datetime import datetime
from odoo.tools import format_date

class ResCurrency(models.Model):
    _inherit = 'res.currency'

    def l10n_ar_action_get_afip_ws_currency_rate(self):
        date, rate = self._l10n_ar_get_afip_ws_currency_rate()
        date = datetime.strptime(date, '%Y%m%d').date()
        self.update({'rate_ids': [(0, 0, {'name': date, 'inverse_company_rate': rate})]})
