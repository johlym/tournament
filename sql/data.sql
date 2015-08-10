--- This SQL file is used for unit testing to reproduce the proper
-- environment(s). Use tournament.sql for regular usage. This SQL file was
-- created based on a database dump from a pre-created database that
-- contained all the necessary bits of data.

--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: matches; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE matches (
    id integer NOT NULL,
    player_1 text NOT NULL,
    player_2 text NOT NULL,
    winner text NOT NULL,
    "timestamp" text NOT NULL
);

--
-- Name: matches_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE matches_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE matches_id_seq OWNER TO postgres;

--
-- Name: matches_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE matches_id_seq OWNED BY matches.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY matches ALTER COLUMN id SET DEFAULT nextval('matches_id_seq'::regclass);


--
-- Data for Name: matches; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (1, '1', '12', 'jame5814944', '2015-07-26 14:24:31.558');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (2, '2', '11', 'jame3615090', '2015-07-26 14:24:31.691');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (3, '3', '10', 'jame2590959', '2015-07-26 14:24:31.794');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (4, '4', '9', 'jame2332898', '2015-07-26 14:24:31.900');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (5, '5', '8', 'jame3542865', '2015-07-26 14:24:32.007');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (6, '6', '7', 'jame1385023', '2015-07-26 14:24:32.117');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (7, '7', '6', 'jame1385023', '2015-07-26 14:24:32.221');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (8, '8', '5', 'jame1328253', '2015-07-26 14:24:32.325');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (9, '9', '4', 'jame5917519', '2015-07-26 14:24:32.428');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (10, '10', '3', 'jame2590959', '2015-07-26 14:24:32.533');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (11, '11', '2', 'jame3615090', '2015-07-26 14:24:32.643');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (12, '12', '1', 'jame4762130', '2015-07-26 14:24:32.771');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (13, '1', '10', 'carl5937203', '2015-07-26 14:39:06.145');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (14, '2', '9', 'chik2539783', '2015-07-26 14:39:06.252');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (15, '3', '8', 'rich9928173', '2015-07-26 14:39:06.360');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (16, '4', '7', 'bigm0199743', '2015-07-26 14:39:06.467');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (17, '5', '6', 'rich8509380', '2015-07-26 14:39:06.573');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (18, '6', '5', 'rich8509380', '2015-07-26 14:39:06.681');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (19, '7', '4', 'lizz2016832', '2015-07-26 14:39:06.787');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (20, '8', '3', 'rich9928173', '2015-07-26 14:39:06.895');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (21, '9', '2', 'chik2539783', '2015-07-26 14:39:07.039');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (22, '10', '1', 'poro4440291', '2015-07-26 14:39:07.149');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (23, '1', '10', 'carl5937203', '2015-07-26 14:39:09.097');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (24, '2', '9', 'chik2539783', '2015-07-26 14:39:09.215');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (25, '3', '8', 'rich9928173', '2015-07-26 14:39:09.322');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (26, '4', '7', 'lizz2016832', '2015-07-26 14:39:09.428');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (27, '5', '6', 'samy3484530', '2015-07-26 14:39:09.574');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (28, '6', '5', 'rich8509380', '2015-07-26 14:39:09.683');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (29, '7', '4', 'lizz2016832', '2015-07-26 14:39:09.812');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (30, '8', '3', 'phis4561112', '2015-07-26 14:39:09.939');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (31, '9', '2', 'mike1101922', '2015-07-26 14:39:10.047');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (32, '10', '1', 'carl5937203', '2015-07-26 14:39:10.153');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (33, '1', '10', 'carl5937203', '2015-07-26 14:39:10.985');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (34, '2', '9', 'chik2539783', '2015-07-26 14:39:11.094');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (35, '3', '8', 'rich9928173', '2015-07-26 14:39:11.203');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (36, '4', '7', 'bigm0199743', '2015-07-26 14:39:11.314');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (37, '5', '6', 'rich8509380', '2015-07-26 14:39:11.420');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (38, '6', '5', 'samy3484530', '2015-07-26 14:39:11.548');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (39, '7', '4', 'lizz2016832', '2015-07-26 14:39:11.672');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (40, '8', '3', 'phis4561112', '2015-07-26 14:39:11.780');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (41, '9', '2', 'mike1101922', '2015-07-26 14:39:11.885');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (42, '10', '1', 'poro4440291', '2015-07-26 14:39:11.993');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (43, '1', '10', 'poro4440291', '2015-07-26 14:40:28.597');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (44, '2', '9', 'chik2539783', '2015-07-26 14:40:28.713');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (45, '3', '8', 'rich9928173', '2015-07-26 14:40:28.847');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (46, '4', '7', 'lizz2016832', '2015-07-26 14:40:28.956');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (47, '5', '6', 'samy3484530', '2015-07-26 14:40:29.091');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (48, '6', '5', 'rich8509380', '2015-07-26 14:40:29.204');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (49, '7', '4', 'lizz2016832', '2015-07-26 14:40:29.314');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (50, '8', '3', 'rich9928173', '2015-07-26 14:40:29.423');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (51, '9', '2', 'mike1101922', '2015-07-26 14:40:29.534');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (52, '10', '1', 'poro4440291', '2015-07-26 14:40:29.643');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (53, '1', '10', 'carl5937203', '2015-07-26 14:40:34.453');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (54, '2', '9', 'chik2539783', '2015-07-26 14:40:34.557');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (55, '3', '8', 'phis4561112', '2015-07-26 14:40:34.686');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (56, '4', '7', 'bigm0199743', '2015-07-26 14:40:34.830');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (57, '5', '6', 'samy3484530', '2015-07-26 14:40:34.938');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (58, '6', '5', 'rich8509380', '2015-07-26 14:40:35.046');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (59, '7', '4', 'lizz2016832', '2015-07-26 14:40:35.151');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (60, '8', '3', 'phis4561112', '2015-07-26 14:40:35.259');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (61, '9', '2', 'chik2539783', '2015-07-26 14:40:35.363');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (62, '10', '1', 'poro4440291', '2015-07-26 14:40:35.467');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (63, '1', '10', 'poro4440291', '2015-07-26 14:40:36.300');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (64, '2', '9', 'mike1101922', '2015-07-26 14:40:36.444');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (65, '3', '8', 'rich9928173', '2015-07-26 14:40:36.558');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (66, '4', '7', 'lizz2016832', '2015-07-26 14:40:36.667');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (67, '5', '6', 'rich8509380', '2015-07-26 14:40:36.779');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (68, '6', '5', 'rich8509380', '2015-07-26 14:40:36.894');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (69, '7', '4', 'lizz2016832', '2015-07-26 14:40:37.004');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (70, '8', '3', 'phis4561112', '2015-07-26 14:40:37.110');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (71, '9', '2', 'chik2539783', '2015-07-26 14:40:37.216');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (72, '10', '1', 'carl5937203', '2015-07-26 14:40:37.321');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (73, '1', '10', 'poro4440291', '2015-07-26 14:40:38.175');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (74, '2', '9', 'mike1101922', '2015-07-26 14:40:38.288');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (75, '3', '8', 'rich9928173', '2015-07-26 14:40:38.400');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (76, '4', '7', 'lizz2016832', '2015-07-26 14:40:38.951');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (77, '5', '6', 'rich8509380', '2015-07-26 14:40:39.061');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (78, '6', '5', 'samy3484530', '2015-07-26 14:40:39.168');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (79, '7', '4', 'bigm0199743', '2015-07-26 14:40:39.281');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (80, '8', '3', 'phis4561112', '2015-07-26 14:40:39.389');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (81, '9', '2', 'chik2539783', '2015-07-26 14:40:39.495');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (82, '10', '1', 'carl5937203', '2015-07-26 14:40:39.616');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (83, '1', '10', 'carl5937203', '2015-07-26 14:40:40.573');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (84, '2', '9', 'chik2539783', '2015-07-26 14:40:40.679');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (85, '3', '8', 'phis4561112', '2015-07-26 14:40:40.792');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (86, '4', '7', 'bigm0199743', '2015-07-26 14:40:40.907');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (87, '5', '6', 'samy3484530', '2015-07-26 14:40:41.016');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (88, '6', '5', 'rich8509380', '2015-07-26 14:40:41.124');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (89, '7', '4', 'bigm0199743', '2015-07-26 14:40:41.235');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (90, '8', '3', 'rich9928173', '2015-07-26 14:40:41.348');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (91, '9', '2', 'chik2539783', '2015-07-26 14:40:41.473');
INSERT INTO matches (id, player_1, player_2, winner, "timestamp") VALUES (92, '10', '1', 'poro4440291', '2015-07-26 14:40:41.581');


--
-- Name: matches_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('matches_id_seq', 92, true);


--
-- Name: matches_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY matches
    ADD CONSTRAINT matches_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: players; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE players (
    id integer NOT NULL,
    name text NOT NULL,
    country text NOT NULL,
    code text
);

--
-- Name: players_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE players_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE players_id_seq OWNER TO postgres;

--
-- Name: players_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE players_id_seq OWNED BY players.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY players ALTER COLUMN id SET DEFAULT nextval('players_id_seq'::regclass);


--
-- Data for Name: players; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO players (id, name, country, code) VALUES (1, 'Carl Isenhower', 'United States', 'carl5937203');
INSERT INTO players (id, name, country, code) VALUES (2, 'Mike Donalds', 'Canada', 'mike1101922');
INSERT INTO players (id, name, country, code) VALUES (3, 'Richard Gears', 'France', 'rich9928173');
INSERT INTO players (id, name, country, code) VALUES (4, 'Lizzard Beth', 'South Africa', 'lizz2016832');
INSERT INTO players (id, name, country, code) VALUES (5, 'Rich Mond', 'Canada', 'rich8509380');
INSERT INTO players (id, name, country, code) VALUES (6, 'Sam You Ell', 'Japan', 'samy3484530');
INSERT INTO players (id, name, country, code) VALUES (7, 'Big Mac', 'Playland', 'bigm0199743');
INSERT INTO players (id, name, country, code) VALUES (8, 'Phish Fill Aye', 'South Playland', 'phis4561112');
INSERT INTO players (id, name, country, code) VALUES (9, 'Chi Ken Club', 'North Playmand', 'chik2539783');
INSERT INTO players (id, name, country, code) VALUES (10, 'Po Rotland', 'Eastland', 'poro4440291');
INSERT INTO players (id, name, country, code) VALUES (11, 'Cal Ifo Rina',
                                                      'Westland',
                                                      'cali9557582');


--
-- Name: players_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('players_id_seq', 13, true);


--
-- Name: players_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY players
    ADD CONSTRAINT players_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

