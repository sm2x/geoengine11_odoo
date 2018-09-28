# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import anthem
from ..common import load_csv

""" File for a sample dataset

These songs will be called when the mode is 'sample', we should import only
excerpt of data, while the full data is only imported in the 'full' mode.

This dataset must be lighter to have fast build for dev and test instances.


"""


@anthem.log
def import_customers(ctx):
    """ Importing customers from csv """
    load_csv(ctx, 'data/sample/customers.csv', 'res.partner')


@anthem.log
def main(ctx):
    """ Loading sample data """
    import_customers(ctx)
