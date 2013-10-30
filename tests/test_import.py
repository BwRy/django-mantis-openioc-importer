#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-mantis-stix-importer
------------

Tests for `django-mantis-stix-importer` modules module.
"""


from utils import deltaCalc

from django import test

from mantis_openioc_importer.management.commands.mantis_openioc_import import Command

from custom_test_runner import CustomSettingsTestCase

import pprint

pp = pprint.PrettyPrinter(indent=2)


class XML_Import_Tests(CustomSettingsTestCase):

    new_settings = dict(
        INSTALLED_APPS=(
           'dingos',
        )
    )

    def setUp(self):
        self.command = Command()

    def test_import(self):

        @deltaCalc
        def t_import(*args,**kwargs):
            return self.command.handle(*args,**kwargs)


        (delta,result) = t_import('tests/testdata/xml/zeus.ioc',
                                  placeholder_fillers=[('source', 'Example_import')],
                                  identifier_ns_uri="example.com",
                                  marking_json='tests/testdata/markings/import_info.json')

        #pp.pprint(delta)

        expected = [ ('DataTypeNameSpace', 2),
                     ('Fact', 43),
                     ('FactDataType', 3),
                     ('FactTerm', 24),
                     ('FactTerm2Type', 24),
                     ('FactValue', 28),
                     ('Identifier', 14),
                     ('IdentifierNameSpace', 2),
                     ('InfoObject', 14),
                     ('InfoObject2Fact', 54),
                     ('InfoObjectFamily', 2),
                     ('InfoObjectType', 4),
                     ('Marking2X', 13),
                     ('NodeID', 32),
                     ('Revision', 3)]

        self.assertEqual(delta,expected)

        (delta,result) = t_import('tests/testdata/xml/zeus.ioc',
                                  placeholder_fillers=[('source', 'Example_import')],
                                  identifier_ns_uri="example.com",
                                  marking_json='tests/testdata/markings/import_info.json')


        #pp.pprint(delta)

        expected = [('Identifier', 1), ('InfoObject', 1), ('InfoObject2Fact', 6)]

        self.assertEqual(delta,expected)


