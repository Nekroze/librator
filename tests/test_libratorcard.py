#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for ``libratorcard`` command line tool."""

import os
import shutil
import unittest

from librator import librator


class TestLibratorCard(unittest.TestCase):

    def setUp(self):
        librator.cardmain("test".split())

    def test_something(self):
        import yaml
        with open("test.crd") as test:
            loaded = yaml.safe_load(test)

        from librarian.card import Card
        card = Card(name="card")
        card.add_attribute("alive")
        card.add_ability("open", "attack")
        card.set_info("art", "")

        expected = card.save()

        self.assertEqual(loaded, expected)

    def tearDown(self):
        os.remove("test.crd")

if __name__ == "__main__":
    unittest.main()
