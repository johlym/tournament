#!/usr/bin/env python
#
# Test cases for tournament.py
################################################################################
# THE ORIGINAL TEST SUITE CREATED BY UDACITY. NEEDED TO MEET MAJOR FUNCTIONAL  #
# REQUIREMENTS FOR THIS PROJECT. ALL TESTS IN THIS SUITE ARE REPLICATED WITH   #
# BETTER TRACKING IN test.py.                                                  #
################################################################################

from tournament import *
import test

def testDeleteMatches():
    deleteMatches()
    print "1. Old matches can be deleted."


def testDelete():
    deleteMatches()
    deletePlayer(player="1")
    print "2. Player records can be deleted."


def testCount():
    deleteMatches()
    deletePlayers()
    c = countPlayers()
    if c == '0':
        raise TypeError(
            "countPlayers() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "3. After deleting, countPlayers() returns zero."


def testRegister():
    deleteMatches()
    deletePlayers()
    registerPlayer(player_name="Chandra Nalaar", country="United States")
    c = countPlayers()
    if c != 1:
        raise ValueError(
            "After one player registers, countPlayers() should be 1.")
    print "4. After registering a player, countPlayers() returns 1."


def testRegisterCountDelete():
    deleteMatches()
    deletePlayers()
    registerPlayer(player_name="Markov Chaney", country="Fictionland")
    registerPlayer(player_name="Joe Malik", country="Fictionland")
    registerPlayer(player_name="Mao Tsu-hsi", country="Fictionland")
    registerPlayer(player_name="Atlanta Hope", country="Fictionland")
    c = countPlayers()
    if c != 4:
        raise ValueError(
            "After registering four players, countPlayers should be 4.")
    deletePlayers()
    c = countPlayers()
    if c != 0:
        print c
        raise ValueError("After deleting, countPlayers should return zero.")
    print "5. Players can be registered and deleted."


def testStandingsBeforeMatches():
    deleteMatches()
    deletePlayers()
    registerPlayer(player_name="Melpomene Murray", country="Fictionland")
    registerPlayer(player_name="Randy Schwartz", country="Fictionland")
    standings = playerStandings()
    if len(standings) < 2:
        raise ValueError("Players should appear in playerStandings even before "
                         "they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 4:
        raise ValueError("Each playerStandings row should have three columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in standings, "
                         "even if they have no matches played.")
    print "6. Newly registered players appear in the standings with no matches."


def testReportMatches():
    deleteMatches()
    deletePlayers()
    registerPlayer(player_name="Bruno Walton", country="Fictionland")
    registerPlayer(player_name="Boots O'Neal", country="Fictionland")
    registerPlayer(player_name="Cathy Burton", country="Fictionland")
    registerPlayer(player_name="Diane Grant", country="Fictionland")
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    standings = playerStandings()
    for (i, n, w, m) in standings:
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each match loser should have zero wins recorded.")
    print "7. After a match, players have updated standings."


def testPairings():
    deleteMatches()
    deletePlayers()
    registerPlayer(player_name="Twilight Sparkle", country="Fictionland")
    registerPlayer(player_name="Flutter Shy", country="Fictionland")
    registerPlayer(player_name="Apple Jack", country="Fictionland")
    registerPlayer(player_name="Pinkie Pie", country="Fictionland")
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    pairings = swissPairings()
    if len(pairings) != 2:
        raise ValueError(
            "For four players, swissPairings should return two pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "8. After one match, players with one win are paired."


if __name__ == '__main__':
    test.create_dummy_data()
    testDeleteMatches()
    test.create_dummy_data()
    testDelete()
    test.create_dummy_data()
    testCount()
    test.create_dummy_data()
    testRegister()
    test.create_dummy_data()
    testRegisterCountDelete()
    test.create_dummy_data()
    testStandingsBeforeMatches()
    test.create_dummy_data()
    testReportMatches()
    test.create_dummy_data()
    testPairings()
    print "Success!  All tests pass!"


