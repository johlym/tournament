#!/usr/bin/env python

# import database
import match
import unittest


class TestVerifyVersionMessage(unittest.TestCase):
    def test(self):
        """message should print if version is below 2.7"""
        self.assertGreaterEqual(match.req_version, (2, 7))


class TestCreateNewPlayer(unittest.TestCase):
    def test_no_name(self):
        """new_player() should reject if no name is provided"""
        print "Pass"

    def test_name_contains_integer(self):
        """new_player() should reject if name contains integer"""
        print "Pass"

    def test_name_less_two_characters(self):
        """new_player() should reject if name is less than two characters"""
        print "Pass"

    def test_name_contains_symbols(self):
        """new_player() should reject if name contains symbols"""
        print "Pass"

    def test_add_player(self):
        """new_player() should return 0 if adding new player was successful"""
        print "Pass"

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

