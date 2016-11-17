# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = 'product.template'
    service_user_id = fields.Many2one(
        string='User',
        comodel_name='res.users',
        company_dependent=True,
    )
    service_duration = fields.Float()
