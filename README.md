# Tournament 
[![Build Status](https://travis-ci.org/jelyman2/tournament.svg?branch=master)](https://travis-ci.org/jelyman2/tournament)

A Python application to simulate 1-on-1 matchups and rank each player by the 
number of wins and other data.

## Overview

The purpose of this application is to demonstrate basic interaction with a 
relational database management system via Python. This was a project crafted 
for the "Full Stack Developer" Udacity Nanodegree program in which I enrolled.

## How it Works

I was faced with two options: let the user run the script and have it behave 
in a demo-like fashion with pre-defined events OR allow the user to have 
direct control over the meaty portions of the application (a.k.a. the user 
database).

Run the script on the command line with a 2.7x python interpreter with one of
 the following arguments. If you do not, you'll be prompted that you forgot 
 to do so and will receive a list of arguments, anyway.

### Requirements

- Python >= 2.7
- PostgreSQL >= 9.3

## Installation

### Pre-requisites

Use `pip` and install:
- psycopg2 (`pip install psycopg2`)
- PrettyTable (`pip install PrettyTable`)

If you don't have `pip`, follow [these](https://pip.pypa
.io/en/latest/installing.html) instructions.

Make sure you have PostgreSQL already installed. Using the command line, run 
the following:

`psql -f sql/tournament.sql`

If you have the pgAdmin installed, you can open `tournament.sql` and paste 
its contents into a new SQL query within the UI and run from there.

## Using the App 

### Arguments

Here's a breakdown of all the arguments that can be passed by the user:

#### Player

`--new-player`: Creates a new player. You'll be prompted for a name and 
country of origin.

`--delete-player`: Delete an existing player. You'll be prompted for an `ID`.

`--edit-player`: Update the information for an existing player. You'll be 
prompted for an `ID`.

`--list-players`: List all players in the database.

#### Match

`--new-match`: Create a new match. Provide the IDs of two players.

`--swiss-match`: Activates the swiss-style matchup function. This is an 
automated behavior.

## Noteworthy

* Since player `ID` numbers are unique, an `ID` of a deleted player will never 
belong to another player so in its place you'll see `[DELETED]`.

* Missing data will likely always return an exception.

* I opted to do some of the data manipulation in the app for the swiss 
pairings, versus in the database query. My testing shows there was no 
performance improvement using the latter.

* Previous versions of this app included audit logging. It was more for my 
usage than anything else. Since we're past that point, I pulled it.