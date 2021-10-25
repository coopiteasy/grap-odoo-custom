# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Stock - Fix Stock Move Lines",
    "version": "12.0.1.1.1",
    "category": "Tools",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-custom",
    "license": "AGPL-3",
    # Depends on this module only to add a button in the correct place
    "depends": ["grap_change_views_product"],
    "data": [
        "data/ir_cron.xml",
        "views/view_product_product.xml",
    ],
    "installable": True,
}
