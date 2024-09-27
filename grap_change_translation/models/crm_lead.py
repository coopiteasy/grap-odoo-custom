# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Tag(models.Model):
    _inherit = "crm.lead.tag"

    name = fields.Char(translate=False)
