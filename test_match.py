#!/usr/bin/env python

import createdb
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


class TestVerifyCheckVersionMessage(BaseTestCase):
    def test_trivialArg(self):
        """check_version() is waiting the correct time (3.0s)"""
        start = time.time()
        match.check_version((2, 4))
        end = time.time()
        count = round(end - start, 1)
        self.assertEqual(count, 3.0)


class TestVerifyVersionTooLowStatusReportSuccess(BaseTestCase):
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


class TestCommandLineArguments(BaseTestCase):
    def test_arg_new_player(self):
        """Script should reject if --new-player argument is empty"""
        with self.assertRaises(SystemExit):
            self.parser.parse_args(["--new-player"])

    def test_arg_edit_player(self):
        """Script should reject if --edit-player argument is empty"""
        with self.assertRaises(SystemExit):
            self.parser.parse_args(["--edit-player"])

    def test_arg_delete_player(self):
        """Script should reject if --edit-player argument is empty"""
        with self.assertRaises(SystemExit):
            self.parser.parse_args(["--delete-player"])

    def test_arg_lookup_match(self):
        """Script should reject if --edit-player argument is empty"""
        with self.assertRaises(SystemExit):
            self.parser.parse_args(["--lookup-match"])

    def test_arg_delete_match(self):
        """Script should reject if --edit-player argument is empty"""
        with self.assertRaises(SystemExit):
            self.parser.parse_args(["--delete-match"])


class TestNewPlayer(BaseTestCase):
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
    def setUp(self):
        createdb.drop()
        createdb.create()
        for i in range(1, 9):
            player_name = "James Tester Rogan"
            player_country = "United States"
            self.assertEqual(match.new_player(player_name=player_name,
                             country=player_country), 0)

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
    def setUp(self):
        createdb.drop()
        createdb.create()
        for i in range(1, 99):
            player_name = "James Tester Rogan"
            player_country = "United States"
            self.assertEqual(match.new_player(player_name=player_name,
                             country=player_country), 0)

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

    def test_100_players(self):
        """list_players() displays 100 entries in tournament.Players"""
        for i in range(1, 101):
            player_name = "James Tester Rogan"
            player_country = "United States"
            self.assertEqual(match.new_player(player_name=player_name,
                             country=player_country), 0)
        self.assertEqual(match.list_players(), 0)

    def test_1000_players(self):
        """list_players() displays 1000 entries in tournament.Players"""
        for i in range(1, 1001):
            player_name = "James Tester Rogan"
            player_country = "United States"
            self.assertEqual(match.new_player(player_name=player_name,
                             country=player_country), 0)
        self.assertEqual(match.list_players(), 0)

    def test_limit5_players(self):
        """list_players() should honor a preset limit"""
        for i in range(1, 6):
            player_name = "James Tester Rogan"
            player_country = "United States"
            self.assertEqual(match.new_player(player_name=player_name,
                             country=player_country), 0)
        self.assertEqual(match.list_players(limit="5"), 0)

    def test_limit_contains_letter(self):
        """list_players() throws if limit contains a letter"""
        with self.assertRaises(AttributeError):
            match.list_players(limit="A")

    def test_limit_contains_symbol(self):
        """list_players() throws if limit contains a symbol"""
        with self.assertRaises(AttributeError):
            match.list_players(limit="@")


class TestNewMatch(BaseTestCase):
    def test_new_match(self):
        """go_match() returns 0 when a match was successful"""
        database.delete_all_players()
        player_name = "James Tester Rogan"
        player_country = "United States"
        self.assertEqual(match.new_player(player_name=player_name,
                         country=player_country), 0)
        p = database.search("players", "LATEST", "null")
        i1 = str(p[0][0])
        player_name = "Ricky Tricky McDonalds"
        player_country = "South Africa"
        self.assertEqual(match.new_player(player_name=player_name,
                         country=player_country), 0)
        p = database.search("players", "LATEST", "null")
        i2 = str(p[0][0])
        self.assertEqual(match.go_match(player_1=i1, player_2=i2), 0)
        
    def test_less_than_two_players(self):
        """go_match() throws if both players are not provided"""
        with self.assertRaises(AttributeError):
            match.go_match(player_1=9, player_2="")
        
    def test_player_1_not_valid(self):
        """go_match() throws if player 1 is not valid"""
        database.delete_all_players()
        player_name = "James Tester Rogan"
        player_country = "United States"
        self.assertEqual(match.new_player(player_name=player_name,
                         country=player_country), 0)
        p = database.search("players", "LATEST", "null")
        i1 = p[0][0]
        player_name = "Ricky Tricky McDonalds"
        player_country = "South Africa"
        self.assertEqual(match.new_player(player_name=player_name,
                         country=player_country), 0)
        p = database.search("players", "LATEST", "null")
        i2 = str(p[0][0])
        i1 = str(i1 + 2)
        with self.assertRaises(LookupError):
            match.go_match(player_1=i1, player_2=i2)
        
    def test_player_2_not_valid(self):
        """go_match() throws if player 2 is not valid"""
        database.delete_all_players()
        player_name = "James Tester Rogan"
        player_country = "United States"
        self.assertEqual(match.new_player(player_name=player_name,
                         country=player_country), 0)
        p = database.search("players", "LATEST", "null")
        i1 = str(p[0][0])
        player_name = "Ricky Tricky McDonalds"
        player_country = "South Africa"
        self.assertEqual(match.new_player(player_name=player_name,
                         country=player_country), 0)
        p = database.search("players", "LATEST", "null")
        i2 = p[0][0]
        i2 = str(i2 + 2)
        with self.assertRaises(LookupError):
            match.go_match(player_1=i1, player_2=i2)
        
    def test_player_1_contains_letter(self):
        """go_match() throws if player 1 ID contains letter"""
        with self.assertRaises(AttributeError):
            match.go_match(player_1="A", player_2=1)
        
    def test_player_1_contains_symbol(self):
        """go_match() throws if player 1 ID contains symbol"""
        with self.assertRaises(AttributeError):
            match.go_match(player_1="$", player_2=1)
        
    def test_player_2_contains_letter(self):
        """go_match() throws if player 2 ID contains letter"""
        with self.assertRaises(AttributeError):
            match.go_match(player_1=2, player_2="A")
        
    def test_player_2_contains_symbol(self):
        """go_match() throws if player 2 ID contains symbol"""
        with self.assertRaises(AttributeError):
            match.go_match(player_1=2, player_2="%")


class TestSwissMatching(BaseTestCase):
    def setUp(self):
        createdb.drop()
        createdb.create()
        for i in range(1, 14):
            player_name = "James Tester Rogan"
            player_country = "United States"
            self.assertEqual(match.new_player(player_name=player_name,
                             country=player_country), 0)

    def test_swiss_match(self):
        """swiss_match() works properly"""
        self.assertEqual(match.swiss_match()[0], 0)

    def test_count_players(self):
        """number of players counted equals count(players) in database"""
        players_list1 = database.count_players()
        count = len(players_list1)
        self.assertEqual(match.swiss_match()[1], count)

    def test_modulo(self):
        """modulo properly detects an odd number of players"""
        self.assertTrue(match.swiss_match()[2])

    def test_no_players(self):
        """swiss_match() throws if there are no players in the database"""
        database.delete_all_players()
        with self.assertRaises(ValueError):
            match.swiss_match()


class TestDeleteMatch(BaseTestCase):
    def test_list_matches(self):
        """list_match() function executes without issue"""

    def test_no_matches_found(self):
        """list_match() throws SystemExit when no matches found"""

if __name__ == '__main__':
    unittest.main(verbosity=3, buffer=True)

