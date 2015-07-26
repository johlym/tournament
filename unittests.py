#!/usr/bin/env python

# import database
import match
import unittest


class CommandLineTestCase(unittest.TestCase):
    """Base TestCase class, sets up a CLI parser"""

    @classmethod
    def setUpClass(cls):
        parser = match.argument_parser()
        cls.parser = parser


class TestVerifyVersionMessage(unittest.TestCase):
    def test(self):
        """message should print if version is below 2.7"""
        self.assertGreaterEqual(match.req_version, (2, 7))


class TestCreateNewPlayerCommandLineArgument(CommandLineTestCase):
    def test_no_name(self):
        """Script should reject if --new-player argument is empty"""
        with self.assertRaises(SystemExit):
            self.parser.parse_args(["--new-player"])


class TestNewPlayerCatches(unittest.TestCase):
    def test_name_contains_integer(self):
        """new_player() should reject if name contains integer"""
        with self.assertRaises(AttributeError):
            match.new_player(player_name="1")

    def test_name_less_two_characters(self):
        """new_player() should reject if name is less than two characters"""
        with self.assertRaises(AttributeError):
            match.new_player(player_name="a")

    def test_name_contains_symbols(self):
        """new_player() should reject if name contains symbols"""
        with self.assertRaises(AttributeError):
            match.new_player(player_name="J!mes Dean")

    def test_name_not_first_and_last(self):
        """new_player() should reject if both a first and last name aren't
        present"""
        with self.assertRaises(AttributeError):
            match.new_player(player_name="James")

    def test_add_player(self):
        """new_player() should return 0 if adding new player was successful"""
        player_name = "James Rogan"
        player_country = "United States"
        self.assertEqual(0, match.new_player(player_name=player_name,
                                             country=player_country))

    def test_player_has_three_word_name(self):
        """new_player() should return 0 if player is given a middle name"""
        player_name = "James Dean Rogan"
        player_country = "United States"
        self.assertEqual(0, match.new_player(player_name=player_name,
                                             country=player_country))

if __name__ == '__main__':
    unittest.main()

