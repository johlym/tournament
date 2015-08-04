#!/usr/bin/env python

import unittest

import tcdbfunc
import database


class TestCreateDatabaseTable(unittest.TestCase):
    def test_connect_to_database(self):
        """test connection to database 'tournament'"""
        tcdbfunc.connect()

    def test_drop_database_tables_if_exist(self):
        """setup process: drop tables from database if they exist"""
        self.assertEqual(tcdbfunc.drop(), 0)

    def test_create_database_tables(self):
        """create database tables 'players', 'matches', 'auditlog'"""
        self.assertEqual(tcdbfunc.drop(), 0)
        self.assertEqual(tcdbfunc.create(), 0)


class TestMainDatabaseConnector(unittest.TestCase):
    def test_connect_to_database(self):
        """test connection to database 'tournament'"""
        database.connect()

if __name__ == '__main__':
    unittest.main()

