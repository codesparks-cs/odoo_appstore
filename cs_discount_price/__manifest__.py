# -*- coding: utf-8 -*-
{
    "name": "Discount On Price",
    "version": "16.0.0.0",
    "category": "Invoicing",
    "summary": "Calculates Discount percentage on change of Discount Price.",
    'sequence': 1,
    "discription": """
        The Discount Calculator Application is designed to effortlessly compute discount percentages based on changes in price, as well as determine the discounted price from a given discount percentage.
    """,
    "author": "Code Sparks",
    "company": "Code Sparks",
    "maintainer": "Code Sparks",
    "website": "",
    "depends": ["base", "account", "sale_management"],
    "data": [
        "views/sale_account_inherit.xml"
    ],
    "images": ['static/description/banner.png'],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True,
}
