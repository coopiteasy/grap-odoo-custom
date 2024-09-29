# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    name = fields.Char(translate=False)

    description = fields.Text(translate=False)

    legend_priority = fields.Char(translate=False)

    legend_blocked = fields.Char(translate=False)

    legend_done = fields.Char(translate=False)

    legend_normal = fields.Char(translate=False)
