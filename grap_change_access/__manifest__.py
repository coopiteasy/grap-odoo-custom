# Copyright (C) 2013 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "GRAP - Change Accesses",
    "version": "12.0.1.1.0",
    "summary": "Add new groups for specific models"
    " and change accesses for a number of models.",
    "category": "GRAP - Custom",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-custom",
    "license": "AGPL-3",
    "depends": [
        "mrp",
        "sales_team",
        "point_of_sale",
        "purchase",
        "pos_restaurant",
        "project",
        # OCA
        "attachment_delete_restrict",
        "product_margin_classification",
        "crm_security_group",
        # GRAP
        "product_print_category_food_report",
    ],
    "data": [
        "security/ir_rule.xml",
        "security/ir_model_access.xml",
        "security/ir_module_category.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "data/ir_model.xml",
    ],
    "qweb": [
        "static/src/xml/grap_change_access.xml",
    ],
    "installable": True,
}
