#!/usr/bin/env python

import database
import match
import time
import unittest


class CommandLineTestCase(unittest.TestCase):
    """Base TestCase class, sets up a CLI parser"""

    @classmethod
    def setUpClass(cls):
        parser = match.argument_parser()
        cls.parser = parser


class TestVerifyCheckVersionMessage(unittest.TestCase):
    def test_trivialArg(self):
        """check_version() is waiting the correct time (3.0s)"""
        start = time.time()
        match.check_version((2, 4))
        end = time.time()
        count = round(end - start, 1)
        self.assertEqual(count, 3.0)


class TestVerifyVersionTooLowStatusReportSuccess(unittest.TestCase):
    def test_older_python_version(self):
        """check_version() 1 if out of spec"""
        self.assertEqual(match.check_version((2, 4)), 1)

    def test_same_python_version(self):
        """check_version() 0 if in spec for same version"""
        self.assertEqual(match.check_version((2, 7)), 0)

    def test_newer_python_version(self):
        """check_version() 0 if in spec for same version"""
        self.assertEqual(match.check_version((2, 9)), 0)

    def test_newer_python3_version(self):
        """check_version() 0 if in spec for same version"""
        self.assertEqual(match.check_version((3, 4)), 0)


class TestCreateNewPlayerCommandLineArgument(CommandLineTestCase):
    def test_no_name(self):
        """Script should reject if --new-player argument is empty"""
        with self.assertRaises(SystemExit):
            self.parser.parse_args(["--new-player"])


class TestNewPlayer(unittest.TestCase):
    def test_catch_name_contains_integer(self):
        """new_player() should reject if name contains integer"""
        with self.assertRaises(AttributeError):
            match.new_player(player_name="1")

    def test_catch_name_less_two_characters(self):
        """new_player() should reject if name is less than two characters"""
        with self.assertRaises(AttributeError):
            match.new_player(player_name="a")

    def test_catch_name_contains_symbols(self):
        """new_player() should reject if name contains symbols"""
        with self.assertRaises(AttributeError):
            match.new_player(player_name="J!mes Dean")

    def test_check_name_first_and_last(self):
        """new_player() should reject if both a first and last name aren't
        present"""
        with self.assertRaises(AttributeError):
            match.new_player(player_name="James")

    def test_scenario_player_has_three_word_name(self):
        """new_player() should return 0 if player is given a middle name"""
        player_name = "James Dean Rogan"
        player_country = "United States"
        self.assertEqual(0, match.new_player(player_name=player_name,
                                             country=player_country))

    def test_add_new_player(self):
        """new_player() should return 0 if adding new player was successful"""
        player_name = "James Rogan"
        player_country = "United States"
        self.assertEqual(0, match.new_player(player_name=player_name,
                                             country=player_country))


class TestEditPlayer(unittest.TestCase):
    def test_option_edit(self):
        """edit_player() edits player with new info provided"""
        r = database.search("players", "LATEST", "1")
        s = str(r[0][0])
        self.assertEqual(match.edit_player(option="edit", player=s,
                         new_name="Johan Sebastian Bach",
                         new_country="Guam"), 0)

    def test_option_delete(self):
        """edit_player() deletes player"""
        r = database.search("players", "LATEST", "1")
        s = str(r[0][0])
        self.assertEqual(match.edit_player(option="delete", player=s), 0)

    def test_check_bad_option(self):
        """edit_player() throws when passed a bad option"""
        self.assertRaises(match.edit_player(option="bad"), 0)


if __name__ == '__main__':
    unittest.main()

