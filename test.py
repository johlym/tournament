#!/usr/bin/env python

""" The master Unit test set up. Each set of tests below should cover all
functional aspects of tournament.py. The original file tournament_test.py has
been rolled in here and its tests exist below. Most tests below are YAY/NAY
in that we're expecitng very specific results. In most cases, each function
in tournament.py returns a status code based on its behavior. These codes are
returned when non-critical events take place such as "no players found" when
trying to search for players.
"""

import time
import unittest
import psycopg2
import tournament
import tools


def connect():
    # Connect to the PostgreSQL tools.  Returns a database connection.
    return psycopg2.connect(database='tournament', user='postgres')


def drop():
    co = connect()
    cu = co.cursor()
    cu.execute("DROP TABLE IF EXISTS players CASCADE;")
    cu.execute("DROP TABLE IF EXISTS matches CASCADE;")
    co.commit()
    cu.close()
    co.close()
    return 0


def truncate(table):
    co = connect()
    cu = co.cursor()
    cu.execute("TRUNCATE " + table + ";")
    co.commit()
    cu.close()
    co.close()


# Create database contents
def create():
    co = connect()
    cu = co.cursor()
    cu.execute("CREATE TABLE players(id serial NOT NULL,"
               "name text NOT NULL, country text "
               "NOT NULL, code text, CONSTRAINT players_pkey PRIMARY KEY (id))"
               "WITH (OIDS=FALSE);")
    cu.execute("ALTER TABLE players OWNER TO postgres;")
    cu.execute("CREATE TABLE matches (id serial NOT NULL, "
               "p1 text NOT NULL, p2 "
               "text NOT NULL, "
               "\"timestamp\" text NOT NULL,"
               "CONSTRAINT matches_pkey PRIMARY KEY (id))"
               "WITH (OIDS=FALSE);")
    cu.execute("ALTER TABLE matches OWNER TO postgres;")
    co.commit()
    cu.close()
    co.close()
    return 0


def create_dummy_data():
    drop()
    tools.bulksql(open("sql/data.sql", "r").read())


def dummy_player(player_name="", country=""):
    s = tournament.registerPlayer(player_name=player_name, country=country)
    return s


class TestCreateDatabaseTable(unittest.TestCase):
    def test_connect_to_database(self):
        """test connection to database 'tournament'"""
        connect()

    def test_drop_database_tables_if_exist(self):
        """setup process: drop tables from database if they exist"""
        self.assertEqual(drop(), 0)

    def test_create_database_tables(self):
        """create database tables 'players', 'matches'"""
        self.assertEqual(drop(), 0)
        self.assertEqual(create(), 0)


class TestMainDatabaseConnector(unittest.TestCase):
    def test_connect_to_database(self):
        """test connection to database 'tournament'"""
        tools.connect()


class BaseTestCase(unittest.TestCase):
    """Base TestCase class, sets up a CLI parser"""
        
    @classmethod
    def setUpClass(cls):
        parser = tournament.argument_parser()
        cls.parser = parser


class TestVerifyCheckVersionMessage(BaseTestCase):
    def test_wait_time(self):
        """check_version() is waiting the correct time (3.0s)"""
        start = time.time()
        tournament.check_version((2, 4))
        end = time.time()
        count = round(end - start, 1)
        self.assertEqual(count, 3.0)


class TestVerifyVersionTooLowStatusReportSuccess(BaseTestCase):
    def test_older_python_version(self):
        """check_version() 1 if out of spec"""
        self.assertEqual(tournament.check_version((2, 4)), 1)

    def test_same_python_version(self):
        """check_version() 0 if in spec for same version"""
        self.assertEqual(tournament.check_version((2, 7)), 0)

    def test_newer_python_version(self):
        """check_version() 0 if in spec for same version"""
        self.assertEqual(tournament.check_version((2, 9)), 0)

    def test_newer_python3_version(self):
        """check_version() 0 if in spec for same version"""
        self.assertEqual(tournament.check_version((3, 4)), 0)


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

    def test_arg_delete_match(self):
        """Script should reject if --edit-player argument is empty"""
        with self.assertRaises(SystemExit):
            self.parser.parse_args(["--delete-match"])


class TestNewPlayer(BaseTestCase):
    def test_name_contains_integer(self):
        """registerPlayer() should reject if name contains integer"""
        with self.assertRaises(AttributeError):
            tournament.registerPlayer(player_name="1")

    def test_name_less_two_characters(self):
        """registerPlayer() should reject if name is less than two characters"""
        with self.assertRaises(AttributeError):
            tournament.registerPlayer(player_name="a")

    def test_name_contains_symbols(self):
        """registerPlayer() should reject if name contains symbols"""
        with self.assertRaises(AttributeError):
            tournament.registerPlayer(player_name="J!mes Dean")

    def test_name_first_and_last(self):
        """registerPlayer() should reject if both a first and last name aren't
        present"""
        with self.assertRaises(AttributeError):
            tournament.registerPlayer(player_name="James")

    def test_player_has_three_word_name(self):
        """registerPlayer() should return 0 if player is given a middle name"""
        self.assertEqual(0, dummy_player(player_name="James Dean Rogan",
                                         country="United States"))

    def test_country_not_provided(self):
        """registerPlayer() should return 0 if player is given a middle name"""
        with self.assertRaises(SystemExit):
            dummy_player(player_name="James Rogan", country="")

    def test_add_new_player(self):
        """registerPlayer() should return 0 if adding new player was successful"""
        self.assertEqual(0, dummy_player(player_name="Christoph Waltz",
                                         country="Germany"))


class TestEditPlayer(BaseTestCase):
    def setUp(self):
        create_dummy_data()

    def test_option_edit(self):
        """editPlayer() edits player with new info provided"""
        q = "SELECT * FROM matches ORDER BY id LIMIT 1"
        r = tools.query(q)
        s = str(r[0][0])
        self.assertEquals(tournament.editPlayer(player=s,
                                                 new_name="Johan Bach",
                                                 new_country="Guam"), 0)

    def test_option_delete(self):
        """editPlayer() deletes player"""
        q = "SELECT * FROM matches ORDER BY id LIMIT 1"
        r = tools.query(q)
        s = str(r[0][0])
        self.assertEquals(tournament.deletePlayer(player=s), 0)

    def test_edit_missing_new_info(self):
        """editPlayer() throws when both new_name and new_country are not
        specified"""
        with self.assertRaises(AttributeError):
            tournament.editPlayer(new_name="Joan Jett")

    def test_no_player_id(self):
        """Script should reject if --edit-player argument is empty"""
        with self.assertRaises(SystemExit):
            self.parser.parse_args(["--edit-player"])

    def test_delete_invalid_player_id(self):
        """editPlayer() should throw if the player ID is invalid"""
        with self.assertRaises(LookupError):
            tournament.deletePlayer(player="0")

    def test_edit_invalid_player_id(self):
        """editPlayer() should throw if the player ID is invalid"""
        with self.assertRaises(LookupError):
            tournament.editPlayer(player="0",
                                   new_name="Michael Bay", new_country="Japan")


class TestListPlayers(BaseTestCase):
    def setUp(self):
        create_dummy_data()

    def test_display_zero_matches(self):
        """listPlayers() returns 1 if the tournament.Players table is empty"""
        q = "TRUNCATE TABLE players;"
        tools.query(q)
        self.assertEqual(tournament.listPlayers(), 1)

    def test_list_players(self):
        """listPlayers() returns 0 if it works."""
        dummy_player(player_name="Mark German", country="Germany")
        self.assertEqual(tournament.listPlayers(), 0)


class TestNewMatch(BaseTestCase):
    def setUp(self):
        create_dummy_data()
        
    def test_less_than_two_players(self):
        """reportMatch() throws if both players are not provided"""
        with self.assertRaises(AttributeError):
            tournament.reportMatch(p1=9, p2="")
        
    def test_p1_not_valid(self):
        """reportMatch() throws if player 1 is not valid"""
        q = "TRUNCATE TABLE players;"
        tools.query(q)
        self.assertEqual(dummy_player(player_name="Double Quarder",
                                      country="Playland"), 0)
        q = "SELECT * FROM matches ORDER BY id LIMIT 1"
        p = tools.query(q)
        i1 = p[0][0]
        self.assertEqual(dummy_player(player_name="Big Mac Sauce",
                                      country="Playland"), 0)
        q = "SELECT * FROM matches ORDER BY id LIMIT 1"
        p = tools.query(q)
        i2 = str(p[0][0])
        i1 = str(i1 + 2)
        with self.assertRaises(LookupError):
            tournament.reportMatch(p1=i1, p2=i2)
        
    def test_p2_not_valid(self):
        """reportMatch() throws if player 2 is not valid"""
        q = "TRUNCATE TABLE players;"
        tools.query(q)
        self.assertEqual(dummy_player(player_name="Fissh Fillay",
                                      country="Playland"), 0)
        q = "SELECT * FROM matches ORDER BY id LIMIT 1"
        p = tools.query(q)
        i1 = str(p[0][0])
        self.assertEqual(dummy_player(player_name="Kulv Sangwich",
                                      country="Playland"), 0)
        q = "SELECT * FROM matches ORDER BY id LIMIT 1"
        p = tools.query(q)
        i2 = p[0][0]
        i2 = str(i2 + 2)
        with self.assertRaises(LookupError):
            tournament.reportMatch(p1=i1, p2=i2)
        
    def test_p1_contains_letter(self):
        """reportMatch() throws if player 1 ID contains letter"""
        with self.assertRaises(AttributeError):
            tournament.reportMatch(p1="A", p2=1)
        
    def test_p1_contains_symbol(self):
        """reportMatch() throws if player 1 ID contains symbol"""
        with self.assertRaises(AttributeError):
            tournament.reportMatch(p1="$", p2=1)
        
    def test_p2_contains_letter(self):
        """reportMatch() throws if player 2 ID contains letter"""
        with self.assertRaises(AttributeError):
            tournament.reportMatch(p1=2, p2="A")
        
    def test_p2_contains_symbol(self):
        """reportMatch() throws if player 2 ID contains symbol"""
        with self.assertRaises(AttributeError):
            tournament.reportMatch(p1=2, p2="%")


class TestSwissMatching(BaseTestCase):
    def setUp(self):
        create_dummy_data()

    def test_no_players(self):
        """swissPairings() throws if there are no players in the database"""
        q = "TRUNCATE TABLE players;"
        tools.query(q)
        with self.assertRaises(ValueError):
            tournament.swissPairings()


class TestLatestMatch(BaseTestCase):
    def setUp(self):
        create_dummy_data()

    def test_latest_match(self):
        """latest_match() function executes without issue"""

    def test_latest_match_not_found(self):
        """latestMatch() throws SystemExit when no match is found"""


class TestListWinRanking(BaseTestCase):
    def setUp(self):
        create_dummy_data()

    def test_list_win_ranking(self):
        """playerStandings() function executes without issue"""
        self.assertTrue(tournament.playerStandings())



if __name__ == '__main__':
    unittest.main(verbosity=3, buffer=True)
