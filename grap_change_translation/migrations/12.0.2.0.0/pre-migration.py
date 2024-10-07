# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade

# pylint: disable=odoo-addons-relative-import
from odoo.addons.grap_change_translation import preserve_translation

_NO_TRANSLATABLE_LIST = [
    ("project_project", "label_tasks", "project.project"),
    ("project_task_type", "name", "project.task.type"),
    ("project_task_type", "description", "project.task.type"),
    ("project_task_type", "legend_priority", "project.task.type"),
    ("project_task_type", "legend_blocked", "project.task.type"),
    ("project_task_type", "legend_done", "project.task.type"),
    ("project_task_type", "legend_normal", "project.task.type"),
]


@openupgrade.migrate()
def migrate(env, version):
    for item in _NO_TRANSLATABLE_LIST:
        preserve_translation(env, openupgrade.logged_query, item[0], item[1], item[2])
