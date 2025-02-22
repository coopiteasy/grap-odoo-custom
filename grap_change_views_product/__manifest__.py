# Copyright (C) 2013-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "GRAP - Change Views Product",
    "version": "12.0.0.4.0",
    "category": "GRAP - Custom",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-custom",
    "license": "AGPL-3",
    "depends": [
        # Coop It Easy
        "account_customer_wallet",
        # Odoo
        "product",
        "purchase",
        "sale",
        "point_of_sale",
        "product_supplierinfo_qty_multiplier",
        "stock",
        "sale_invoice_policy",
        "mrp",
        # OCA
        "product_margin_classification",
        "product_price_history",
        "product_pricelist_margin",
        "barcodes_generator_product",
        "product_form_purchase_link",
        "pos_meal_voucher",
        "pos_product_mergeable_line",
        "pos_tare",
        "product_net_weight",
        "purchase_discount",
        "purchase_triple_discount",
        "product_standard_price_tax_included",
        "product_sale_tax_price_included",
        "web_widget_numeric_step",
        "product_category_global_account_setting",
        # GRAP
        "grap_change_views_mrp",
        "fiscal_company_product",
        "stock_preparation_category",
        "recurring_consignment",
        "product_to_scale_bizerba",
        "sale_eshop",
        "product_food",
        "product_food_certification",
        "product_label",
        "product_main_seller",
        "product_print_category",
        "product_simple_pricelist",
        "product_print_category_food_report",
        "product_origin",
        "l10n_fr_department_product_origin",
        "account_invoice_supplierinfo_update_standard_price",
        "pos_sector",
        "intercompany_trade_product",
        "joint_buying_product",
        "mrp_food",
        "mrp_business",
        "mrp_bom_tag",
        "product_supplierinfo_standard_price",
    ],
    "data": [
        "views/menu.xml",
        "views/view_product_margin_classification.xml",
        "views/view_product_pricelist.xml",
        "views/view_product_pricelist_item.xml",
        "views/view_product_supplierinfo.xml",
        "views/view_product_product_stock.xml",
        "views/view_product_product_tree.xml",
        "views/view_product_product_form.xml",
        "views/view_product_product_search.xml",
    ],
    "installable": True,
}
