# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    updated_c24_date = fields.Datetime(
        string="Updated C24 Date",
        store=True,
        compute="_update_c24_date"
    )

    currency_price_change_date = fields.Datetime(
        string="Update Currency Amount Price",
        store=True,
    )

    @api.multi
    @api.depends('chrono')
    def _update_c24_date(self):
        for p in self:
            self.updated_c24_date = fields.Datetime.now()