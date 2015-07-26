#!/usr/bin/env python

import database
import match
import time
import unittest


class BaseTestCase(unittest.TestCase):
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


class TestCreateNewPlayerCommandLineArgument(BaseTestCase):
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


class TestEditPlayer(BaseTestCase):
    def test_option_edit(self):
        """edit_player() edits player with new info provided"""
        r = database.search("players", "LATEST", "1")
        s = str(r[0][0])
        self.assertEquals(match.edit_player(option="edit", player=s,
                                            new_name="Johan Sebastian Bach",
                                            new_country="Guam"), 0)

    def test_option_delete(self):
        """edit_player() deletes player"""
        r = database.search("players", "LATEST", "1")
        s = str(r[0][0])
        self.assertEquals(match.edit_player(option="delete", player=s), 0)

    def test_check_bad_option(self):
        """edit_player() throws when passed a bad option"""
        with self.assertRaises(AttributeError):
            match.edit_player(option="bad")

    def test_check_edit_missing_new_info(self):
        """edit_player() throws when both new_name and new_country are not
        specified"""
        with self.assertRaises(AttributeError):
            match.edit_player(option="edit", new_name="Joan Jett")

    def test_check_no_player_id(self):
        """Script should reject if --edit-player argument is empty"""
        with self.assertRaises(SystemExit):
            self.parser.parse_args(["--edit-player"])

    def test_check_delete_invalid_player_id(self):
        """edit_player() should throw if the player ID is invalid"""
        with self.assertRaises(AttributeError):
            match.edit_player(option="delete", player="38471237401238")

    def test_check_edit_invalid_player_id(self):
        """edit_player() should throw if the player ID is invalid"""
        with self.assertRaises(AttributeError):
            match.edit_player(option="delete", player="38471237401238",
                              new_name="Michael Bay", new_country="Japan")
            

class TestListPlayers(BaseTestCase):
    def test_display_zero_matches(self):
        """list_players() returns 1 if the tournament.Players table is empty"""
        database.delete_all_players()
        self.assertEqual(match.list_players(), 1)

    def test_list_players(self):
        """list_players() returns 0 if it works."""
        player_name = "James Tester Rogan"
        player_country = "United States"
        match.new_player(player_name=player_name, country=player_country)
        self.assertEqual(match.list_players(), 0)

    def test_list_players_100(self):
        """list_players() displays 100 entries in tournament.Players"""
        for i in range(1, 101):
            player_name = "James Tester Rogan"
            player_country = "United States"
            self.assertEqual(match.new_player(player_name=player_name,
                                 country=player_country), 0)
        self.assertEqual(match.list_players(), 0)

    def test_list_players_1000(self):
        """list_players() displays 1000 entries in tournament.Players"""
        for i in range(1, 1001):
            player_name = "James Tester Rogan"
            player_country = "United States"
            self.assertEqual(match.new_player(player_name=player_name,
                                 country=player_country), 0)
        self.assertEqual(match.list_players(), 0)

    def test_list_players_limit5(self):
        """list_players() should honor a preset limit"""



if __name__ == '__main__':
    unittest.main()

