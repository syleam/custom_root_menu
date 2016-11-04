# -*- coding: utf-8 -*-
##############################################################################
#
#    custom_root_menu module for OpenERP, Allows to define a custom root menu per user
#    Copyright (C) 2016 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sylvain Garancher <sylvain.garancher@syleam.fr>
#
#    This file is a part of custom_root_menu
#
#    custom_root_menu is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    custom_root_menu is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.tests import common


class TestProductProduct(common.TransactionCase):
    def setUp(self):
        super(TestProductProduct, self).setUp()

        self.user = self.env.user

    def test_00_no_custom_menu(self):
        """
        Check that all menus without parent are taken when the user has no custom root menu
        """
        self.user.menu_id = False
        root_menus = self.env['ir.ui.menu'].sudo(self.user).get_user_roots()
        all_root_menus = self.env['ir.ui.menu'].search([('parent_id', '=', False)])
        self.assertEqual(root_menus, all_root_menus)

    def test_01_with_custom_menu(self):
        """
        Check that all menus without parent are taken when the user has no custom root menu
        """
        self.user.menu_id = self.env['ir.ui.menu'].search([('child_id', '!=', False)], limit=1)
        root_menus = self.env['ir.ui.menu'].sudo(self.user).get_user_roots()
        all_root_menus = self.user.menu_id.child_id
        self.assertEqual(root_menus, all_root_menus)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: