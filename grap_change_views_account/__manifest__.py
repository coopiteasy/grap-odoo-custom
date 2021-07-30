# Copyright (C) 2013-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Quentin DUPONT <quentin.dupont@grap.coop>
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "GRAP - Change Views Account",
    "version": "12.0.1.1.4",
    "category": "GRAP - Custom",
    "author": "GRAP",
    "website": "http://www.grap.coop",
    "license": "AGPL-3",
    "depends": [
        "account",
        "account_group_menu",
        "account_invoice_triple_discount",
        "account_financial_report",
        "sale",
        "account_invoice_supplierinfo_update_standard_price",
        "web_tree_dynamic_colored_field",
        "account_subsequence_fiscal_year",
    ],
    "data": [
        "views/menu.xml",
        "views/view_account_account.xml",
        "views/view_account_account_template.xml",
        "views/view_account_account_type.xml",
        "views/view_account_invoice.xml",
        "views/view_account_journal.xml",
        "views/view_account_move.xml",
        "views/view_account_tax_group.xml",
        "views/view_wizard_update_invoice_supplierinfo.xml",
    ],
    "demo": [
        "demo/res_groups.xml",
    ],
    "installable": True,
}
