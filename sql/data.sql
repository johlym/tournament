CREATE TABLE auditlog (
    id integer NOT NULL,
    entry text NOT NULL,
    action text NOT NULL,
    unique_id text NOT NULL,
    "timestamp" text NOT NULL
);

--
-- Name: auditlog_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auditlog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

--
-- Name: auditlog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auditlog_id_seq OWNED BY auditlog.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auditlog ALTER COLUMN id SET DEFAULT nextval('auditlog_id_seq'::regclass);


--
-- Data for Name: auditlog; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (1, 'Retrieved 10 rows from the tournament.players.', 'trn.count_players()', '40625f24-0648-41c1-8970-b13c078b8ff5', '2015-07-26 19:12:33.012');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (2, 'Found 10 players in list for swiss matchups.', 'swiss_match()', '6e75ff6b-d608-4545-92f2-60f54f8066c6', '2015-07-26 19:12:33.023');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (3, 'Generated MASTER table for display.', 'swiss_match()', 'e5a443d6-ba2f-4181-aef3-5c430885e290', '2015-07-26 19:12:33.049');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (4, 'Generated SLAVE A table for display.', 'swiss_match()', 'da8eff78-2416-4907-81ae-26dd6218aa4a', '2015-07-26 19:12:33.059');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (5, 'Generated SLAVE B table for display.', 'swiss_match()', '9d7a8e13-f7e2-4745-a5da-8544d052639f', '2015-07-26 19:12:33.068');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (6, 'Generated COMPLETE table for display', 'swiss_match()', '7cb7533e-2b2f-41a3-b338-ffb8e969eb89', '2015-07-26 19:12:33.078');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (7, 'Initiating round 1 against go_match()', 'swiss_match()', '5500bdc7-86f6-4b02-a257-8a0eb738e4e5', '2015-07-26 19:12:33.096');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (8, 'Starting match between 1 and 10', 'go_match()', 'd80adfe8-e728-44f0-bb36-8e851c06530e', '2015-07-26 19:12:33.118');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (9, 'Generated random number 2', 'go_match()', '9364be36-324d-4487-9993-b49460a2e61b', '2015-07-26 19:12:33.167');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (10, 'Stated that player 1 wins.', 'go_match()', 'dc3234dd-0b9a-4279-952b-4d0067d971ca', '2015-07-26 19:12:33.176');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (11, 'Reported win to database.', 'go_match()', 'da1ecdd3-6463-47d4-a598-40f8578bf011', '2015-07-26 19:12:33.196');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (12, 'Completed round 1 against go_match()', 'swiss_match()', 'ed9157ce-d483-4b6d-9391-e8cf16781e8e', '2015-07-26 19:12:33.226');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (13, 'Initiating round 2 against go_match()', 'swiss_match()', '5278b042-7b84-4df6-82d9-60510ff3e30f', '2015-07-26 19:12:33.239');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (14, 'Starting match between 2 and 9', 'go_match()', '50391b64-7e89-4315-b960-4b2878818dde', '2015-07-26 19:12:33.248');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (15, 'Generated random number 1', 'go_match()', 'ea1fe2a8-179f-47ad-bf83-bdf4675148f0', '2015-07-26 19:12:33.298');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (16, 'Stated that player 2 wins.', 'go_match()', 'eb28ef9e-dfbf-4337-8fba-489ce8e87173', '2015-07-26 19:12:33.309');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (17, 'Reported win to database.', 'go_match()', '767c298a-44db-42cd-b185-87978a5ad810', '2015-07-26 19:12:33.328');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (18, 'Completed round 2 against go_match()', 'swiss_match()', '840a5045-1ff9-4cb3-8a36-bdd9173f91ac', '2015-07-26 19:12:33.341');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (19, 'Initiating round 3 against go_match()', 'swiss_match()', 'c3861d63-b125-45a5-af6f-127920543c53', '2015-07-26 19:12:33.352');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (20, 'Starting match between 3 and 8', 'go_match()', '89a9672f-a72e-45e6-aac9-4a277c26b733', '2015-07-26 19:12:33.361');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (21, 'Generated random number 1', 'go_match()', 'f8b9c697-7881-4405-ae07-db9ae1352d8e', '2015-07-26 19:12:33.408');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (22, 'Stated that player 2 wins.', 'go_match()', '7b136a48-efa1-4305-b5c7-0fd7898908ed', '2015-07-26 19:12:33.417');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (23, 'Reported win to database.', 'go_match()', '65bb7cf7-63f0-44fb-b60b-f2b1cac7c1a4', '2015-07-26 19:12:33.437');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (24, 'Completed round 3 against go_match()', 'swiss_match()', 'c1370824-31cc-4921-82c4-30e338d046f1', '2015-07-26 19:12:33.447');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (25, 'Initiating round 4 against go_match()', 'swiss_match()', 'be8967fe-84e6-4698-9692-d1cc80dc6e12', '2015-07-26 19:12:33.457');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (26, 'Starting match between 4 and 7', 'go_match()', '893a0630-41b9-4bb4-88ca-aa0a4b1fbec8', '2015-07-26 19:12:33.467');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (27, 'Generated random number 2', 'go_match()', '3190dd6c-8b64-4527-9bd3-95c67834a6a1', '2015-07-26 19:12:33.514');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (28, 'Stated that player 1 wins.', 'go_match()', '45d50ac3-4685-45bc-b6fc-2e8fe57ac3a7', '2015-07-26 19:12:33.524');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (29, 'Reported win to database.', 'go_match()', 'aa2771ea-4438-414a-8ad9-c256649a0a55', '2015-07-26 19:12:33.542');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (30, 'Completed round 4 against go_match()', 'swiss_match()', 'f92f58f5-596a-4add-b18c-ffc09bef17be', '2015-07-26 19:12:33.552');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (31, 'Initiating round 5 against go_match()', 'swiss_match()', 'ae2a8fb3-174b-4e7f-b94e-8460c8b393cb', '2015-07-26 19:12:33.563');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (32, 'Starting match between 5 and 6', 'go_match()', '79b9b227-6599-43a2-9156-d4ec05fde96a', '2015-07-26 19:12:33.573');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (33, 'Generated random number 1', 'go_match()', 'be6522b4-d396-49a3-99ec-bbe9ffa2804c', '2015-07-26 19:12:33.620');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (34, 'Stated that player 2 wins.', 'go_match()', '3b904cfb-deb8-40ce-aa20-26c2ae8c3430', '2015-07-26 19:12:33.630');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (35, 'Reported win to database.', 'go_match()', 'ff5f0198-f816-42f2-bd7f-e45f05ab5080', '2015-07-26 19:12:33.650');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (36, 'Completed round 5 against go_match()', 'swiss_match()', 'cb01046e-2808-4c2c-af67-466413f1020f', '2015-07-26 19:12:33.660');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (37, 'Initiating round 6 against go_match()', 'swiss_match()', '89dea69b-ef28-4bcb-9f6e-f0978405dd95', '2015-07-26 19:12:33.670');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (38, 'Starting match between 6 and 5', 'go_match()', '1499ff6a-260f-41b5-931e-4c43f6dfd10f', '2015-07-26 19:12:33.680');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (39, 'Generated random number 1', 'go_match()', '5d710c6a-6046-4c5d-a5ae-9d4b58509e0f', '2015-07-26 19:12:33.735');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (40, 'Stated that player 2 wins.', 'go_match()', 'abc30bc1-2580-40f1-8669-1c11ce0c2fbe', '2015-07-26 19:12:33.745');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (41, 'Reported win to database.', 'go_match()', '44126a60-63ee-4900-be1f-12f1059e9b02', '2015-07-26 19:12:33.765');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (42, 'Completed round 6 against go_match()', 'swiss_match()', '361d3b22-fd8d-4978-8b6e-d52a94848ec0', '2015-07-26 19:12:33.775');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (43, 'Initiating round 7 against go_match()', 'swiss_match()', '10073fd9-ad58-4523-8f61-5478293664e2', '2015-07-26 19:12:33.785');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (44, 'Starting match between 7 and 4', 'go_match()', '226f83ca-d8d7-4a77-a39a-111c532c9f82', '2015-07-26 19:12:33.795');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (45, 'Generated random number 2', 'go_match()', '07e0416e-b8c8-4451-abdc-3abc2703f136', '2015-07-26 19:12:33.842');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (46, 'Stated that player 1 wins.', 'go_match()', '3fe3fb0f-4c78-49ab-a23b-f42b04c14f11', '2015-07-26 19:12:33.852');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (47, 'Reported win to database.', 'go_match()', '6131f388-fa42-4f9a-8510-557350c06b37', '2015-07-26 19:12:33.871');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (48, 'Completed round 7 against go_match()', 'swiss_match()', '674d12f2-a90c-4d5a-8817-02365b4797a4', '2015-07-26 19:12:33.881');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (49, 'Initiating round 8 against go_match()', 'swiss_match()', '6c523a86-06ce-44e9-b757-9327f186dc4d', '2015-07-26 19:12:33.891');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (50, 'Starting match between 8 and 3', 'go_match()', '1c5df44f-3b89-4f45-be63-c37291eb7206', '2015-07-26 19:12:33.901');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (51, 'Generated random number 1', 'go_match()', '022b458e-c6c4-49d9-ad86-bec88d3f9cd1', '2015-07-26 19:12:33.949');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (52, 'Stated that player 2 wins.', 'go_match()', 'd6c7451f-deea-49fa-884e-17b70a106e27', '2015-07-26 19:12:33.958');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (53, 'Reported win to database.', 'go_match()', '789249ba-2389-4d77-9ff5-e4016bbac956', '2015-07-26 19:12:33.982');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (54, 'Completed round 8 against go_match()', 'swiss_match()', 'f6eceb4f-1164-4815-b802-79acaa1f4bdd', '2015-07-26 19:12:33.991');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (55, 'Initiating round 9 against go_match()', 'swiss_match()', 'f53ec511-4ad6-4725-b6af-b4bb6e4a35de', '2015-07-26 19:12:34.000');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (56, 'Starting match between 9 and 2', 'go_match()', '2e76672e-f7ca-4328-8b5a-43c31a288fb6', '2015-07-26 19:12:34.010');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (57, 'Generated random number 2', 'go_match()', 'f37bfdb7-1775-4827-9626-9e1d5406ae5d', '2015-07-26 19:12:34.057');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (58, 'Stated that player 1 wins.', 'go_match()', '4827ac75-e56f-42f1-b44c-f7ebb8cdf27f', '2015-07-26 19:12:34.072');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (59, 'Reported win to database.', 'go_match()', 'f347b923-feb7-45ba-853b-5111b2111208', '2015-07-26 19:12:34.094');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (60, 'Completed round 9 against go_match()', 'swiss_match()', '21142133-727e-44f9-b6c3-991813fce67b', '2015-07-26 19:12:34.104');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (61, 'Initiating round 10 against go_match()', 'swiss_match()', 'cf423ec5-48b4-41f6-b334-7f2106e2b701', '2015-07-26 19:12:34.131');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (62, 'Starting match between 10 and 1', 'go_match()', '9068c7c8-77f8-4a85-bb75-37cedbc6de57', '2015-07-26 19:12:34.141');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (63, 'Generated random number 2', 'go_match()', '38c3ee37-a6ff-457a-9fce-ef2b78f54655', '2015-07-26 19:12:34.190');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (64, 'Stated that player 1 wins.', 'go_match()', '58d7d933-5ac6-4bfe-ad23-56d0591feafd', '2015-07-26 19:12:34.216');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (65, 'Reported win to database.', 'go_match()', '9e6e5b8d-b1a3-40de-af98-fe3aa13323c4', '2015-07-26 19:12:34.247');
INSERT INTO auditlog (id, entry, action, unique_id, "timestamp") VALUES (66, 'Completed round 10 against go_match()', 'swiss_match()', '3b2cf7c1-a906-41dd-b3d9-f98858bee5df', '2015-07-26 19:12:34.256');


--
-- Name: auditlog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auditlog_id_seq', 66, true);


--
-- Name: auditlog_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auditlog
    ADD CONSTRAINT auditlog_pkey PRIMARY KEY (id);


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

