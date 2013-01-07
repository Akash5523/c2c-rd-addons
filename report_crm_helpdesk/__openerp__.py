# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2010 Camptocamp SA (http://www.camptocamp.com) 
# All Right Reserved
#
# Author : Ferdinand Gassauer (Camptocamp Austria)
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################
{ "name"         : "CRM Helpdesk Report"
, "description"  : """This module provides a report displaying history of crm_helpdesk"""
, "version"      : "0.9"
, "depends"      : ["crm_helpdesk", "report_webkit"]
, "category"     : 'CRM & SRM'
, "author"       : "Camptocamp Austria"
, "website"      : "http://www.camptocamp.at/"
, "data"         : ["report_crm_helpdesk_view.xml"]
, "installable"  : True
, 'application'  : False
, "auto_install" : False
}
