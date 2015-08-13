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
INSERT INTO matches VALUES (1, 'cars5806229', 'jami9933934', '2015-08-12 18:43:42.560');
INSERT INTO matches VALUES (2, 'john7691185', 'rich3513992', '2015-08-12 18:43:42.586');
INSERT INTO matches VALUES (3, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:42.598');
INSERT INTO matches VALUES (4, 'cars5806229', 'jami9933934', '2015-08-12 18:43:43.813');
INSERT INTO matches VALUES (5, 'rich3513992', 'john7691185', '2015-08-12 18:43:43.825');
INSERT INTO matches VALUES (6, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:43.838');
INSERT INTO matches VALUES (7, 'jami9933934', 'cars5806229', '2015-08-12 18:43:44.621');
INSERT INTO matches VALUES (8, 'john7691185', 'rich3513992', '2015-08-12 18:43:44.633');
INSERT INTO matches VALUES (9, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:44.645');
INSERT INTO matches VALUES (10, 'cars5806229', 'jami9933934', '2015-08-12 18:43:45.285');
INSERT INTO matches VALUES (11, 'john7691185', 'rich3513992', '2015-08-12 18:43:45.297');
INSERT INTO matches VALUES (12, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:45.309');
INSERT INTO matches VALUES (13, 'cars5806229', 'jami9933934', '2015-08-12 18:43:45.909');
INSERT INTO matches VALUES (14, 'rich3513992', 'john7691185', '2015-08-12 18:43:45.920');
INSERT INTO matches VALUES (15, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:45.932');
INSERT INTO matches VALUES (16, 'jami9933934', 'cars5806229', '2015-08-12 18:43:46.430');
INSERT INTO matches VALUES (17, 'john7691185', 'rich3513992', '2015-08-12 18:43:46.442');
INSERT INTO matches VALUES (18, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:46.454');
INSERT INTO matches VALUES (19, 'jami9933934', 'cars5806229', '2015-08-12 18:43:46.943');
INSERT INTO matches VALUES (20, 'rich3513992', 'john7691185', '2015-08-12 18:43:46.957');
INSERT INTO matches VALUES (21, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:46.968');
INSERT INTO matches VALUES (22, 'cars5806229', 'jami9933934', '2015-08-12 18:43:47.426');
INSERT INTO matches VALUES (23, 'john7691185', 'rich3513992', '2015-08-12 18:43:47.438');
INSERT INTO matches VALUES (24, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:47.450');
INSERT INTO matches VALUES (25, 'jami9933934', 'cars5806229', '2015-08-12 18:43:47.902');
INSERT INTO matches VALUES (26, 'rich3513992', 'john7691185', '2015-08-12 18:43:47.915');
INSERT INTO matches VALUES (27, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:47.927');
INSERT INTO matches VALUES (28, 'cars5806229', 'jami9933934', '2015-08-12 18:43:48.346');
INSERT INTO matches VALUES (29, 'rich3513992', 'john7691185', '2015-08-12 18:43:48.358');
INSERT INTO matches VALUES (30, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:48.370');
INSERT INTO matches VALUES (31, 'cars5806229', 'jami9933934', '2015-08-12 18:43:48.786');
INSERT INTO matches VALUES (32, 'john7691185', 'rich3513992', '2015-08-12 18:43:48.799');
INSERT INTO matches VALUES (33, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:48.811');
INSERT INTO matches VALUES (34, 'jami9933934', 'cars5806229', '2015-08-12 18:43:49.235');
INSERT INTO matches VALUES (35, 'rich3513992', 'john7691185', '2015-08-12 18:43:49.248');
INSERT INTO matches VALUES (36, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:49.260');
INSERT INTO matches VALUES (37, 'cars5806229', 'jami9933934', '2015-08-12 18:43:49.660');
INSERT INTO matches VALUES (38, 'rich3513992', 'john7691185', '2015-08-12 18:43:49.673');
INSERT INTO matches VALUES (39, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:49.686');
INSERT INTO matches VALUES (40, 'cars5806229', 'jami9933934', '2015-08-12 18:43:50.058');
INSERT INTO matches VALUES (41, 'rich3513992', 'john7691185', '2015-08-12 18:43:50.069');
INSERT INTO matches VALUES (42, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:50.082');
INSERT INTO matches VALUES (43, 'cars5806229', 'jami9933934', '2015-08-12 18:43:50.465');
INSERT INTO matches VALUES (44, 'rich3513992', 'john7691185', '2015-08-12 18:43:50.476');
INSERT INTO matches VALUES (45, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:50.488');
INSERT INTO matches VALUES (46, 'jami9933934', 'cars5806229', '2015-08-12 18:43:50.867');
INSERT INTO matches VALUES (47, 'john7691185', 'rich3513992', '2015-08-12 18:43:50.878');
INSERT INTO matches VALUES (48, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:50.890');
INSERT INTO matches VALUES (49, 'cars5806229', 'jami9933934', '2015-08-12 18:43:51.253');
INSERT INTO matches VALUES (50, 'rich3513992', 'john7691185', '2015-08-12 18:43:51.265');
INSERT INTO matches VALUES (51, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:51.277');
INSERT INTO matches VALUES (52, 'jami9933934', 'cars5806229', '2015-08-12 18:43:51.673');
INSERT INTO matches VALUES (53, 'john7691185', 'rich3513992', '2015-08-12 18:43:51.684');
INSERT INTO matches VALUES (54, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:51.698');
INSERT INTO matches VALUES (55, 'cars5806229', 'jami9933934', '2015-08-12 18:43:52.051');
INSERT INTO matches VALUES (56, 'rich3513992', 'john7691185', '2015-08-12 18:43:52.063');
INSERT INTO matches VALUES (57, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:52.075');
INSERT INTO matches VALUES (58, 'jami9933934', 'cars5806229', '2015-08-12 18:43:52.420');
INSERT INTO matches VALUES (59, 'john7691185', 'rich3513992', '2015-08-12 18:43:52.432');
INSERT INTO matches VALUES (60, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:52.444');
INSERT INTO matches VALUES (61, 'cars5806229', 'jami9933934', '2015-08-12 18:43:52.817');
INSERT INTO matches VALUES (62, 'john7691185', 'rich3513992', '2015-08-12 18:43:52.829');
INSERT INTO matches VALUES (63, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:52.841');
INSERT INTO matches VALUES (64, 'jami9933934', 'cars5806229', '2015-08-12 18:43:53.189');
INSERT INTO matches VALUES (65, 'john7691185', 'rich3513992', '2015-08-12 18:43:53.200');
INSERT INTO matches VALUES (66, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:53.213');
INSERT INTO matches VALUES (67, 'jami9933934', 'cars5806229', '2015-08-12 18:43:53.622');
INSERT INTO matches VALUES (68, 'john7691185', 'rich3513992', '2015-08-12 18:43:53.634');
INSERT INTO matches VALUES (69, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:53.646');
INSERT INTO matches VALUES (70, 'cars5806229', 'jami9933934', '2015-08-12 18:43:53.985');
INSERT INTO matches VALUES (71, 'john7691185', 'rich3513992', '2015-08-12 18:43:53.997');
INSERT INTO matches VALUES (72, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:54.008');
INSERT INTO matches VALUES (73, 'cars5806229', 'jami9933934', '2015-08-12 18:43:54.411');
INSERT INTO matches VALUES (74, 'john7691185', 'rich3513992', '2015-08-12 18:43:54.423');
INSERT INTO matches VALUES (75, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:54.435');
INSERT INTO matches VALUES (76, 'cars5806229', 'jami9933934', '2015-08-12 18:43:54.772');
INSERT INTO matches VALUES (77, 'rich3513992', 'john7691185', '2015-08-12 18:43:54.784');
INSERT INTO matches VALUES (78, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:54.796');
INSERT INTO matches VALUES (79, 'jami9933934', 'cars5806229', '2015-08-12 18:43:55.176');
INSERT INTO matches VALUES (80, 'rich3513992', 'john7691185', '2015-08-12 18:43:55.188');
INSERT INTO matches VALUES (81, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:55.199');
INSERT INTO matches VALUES (82, 'cars5806229', 'jami9933934', '2015-08-12 18:43:55.546');
INSERT INTO matches VALUES (83, 'rich3513992', 'john7691185', '2015-08-12 18:43:55.558');
INSERT INTO matches VALUES (84, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:55.570');
INSERT INTO matches VALUES (85, 'cars5806229', 'jami9933934', '2015-08-12 18:43:55.899');
INSERT INTO matches VALUES (86, 'rich3513992', 'john7691185', '2015-08-12 18:43:55.911');
INSERT INTO matches VALUES (87, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:55.922');
INSERT INTO matches VALUES (88, 'jami9933934', 'cars5806229', '2015-08-12 18:43:56.312');
INSERT INTO matches VALUES (89, 'john7691185', 'rich3513992', '2015-08-12 18:43:56.329');
INSERT INTO matches VALUES (90, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:56.341');
INSERT INTO matches VALUES (91, 'cars5806229', 'jami9933934', '2015-08-12 18:43:56.632');
INSERT INTO matches VALUES (92, 'john7691185', 'rich3513992', '2015-08-12 18:43:56.643');
INSERT INTO matches VALUES (93, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:56.655');
INSERT INTO matches VALUES (94, 'cars5806229', 'jami9933934', '2015-08-12 18:43:56.973');
INSERT INTO matches VALUES (95, 'john7691185', 'rich3513992', '2015-08-12 18:43:56.985');
INSERT INTO matches VALUES (96, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:56.998');
INSERT INTO matches VALUES (97, 'jami9933934', 'cars5806229', '2015-08-12 18:43:57.331');
INSERT INTO matches VALUES (98, 'rich3513992', 'john7691185', '2015-08-12 18:43:57.342');
INSERT INTO matches VALUES (99, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:57.366');
INSERT INTO matches VALUES (100, 'jami9933934', 'cars5806229', '2015-08-12 18:43:57.694');
INSERT INTO matches VALUES (101, 'rich3513992', 'john7691185', '2015-08-12 18:43:57.706');
INSERT INTO matches VALUES (102, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:57.719');
INSERT INTO matches VALUES (103, 'jami9933934', 'cars5806229', '2015-08-12 18:43:58.073');
INSERT INTO matches VALUES (104, 'rich3513992', 'john7691185', '2015-08-12 18:43:58.086');
INSERT INTO matches VALUES (105, 'jimm9256061', 'nick5579800', '2015-08-12 18:43:58.097');
INSERT INTO matches VALUES (106, 'cars5806229', 'jami9933934', '2015-08-12 18:43:58.452');
INSERT INTO matches VALUES (107, 'rich3513992', 'john7691185', '2015-08-12 18:43:58.464');
INSERT INTO matches VALUES (108, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:58.476');
INSERT INTO matches VALUES (109, 'jami9933934', 'cars5806229', '2015-08-12 18:43:58.773');
INSERT INTO matches VALUES (110, 'rich3513992', 'john7691185', '2015-08-12 18:43:58.784');
INSERT INTO matches VALUES (111, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:58.796');
INSERT INTO matches VALUES (112, 'jami9933934', 'cars5806229', '2015-08-12 18:43:59.137');
INSERT INTO matches VALUES (113, 'john7691185', 'rich3513992', '2015-08-12 18:43:59.148');
INSERT INTO matches VALUES (114, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:59.160');
INSERT INTO matches VALUES (115, 'cars5806229', 'jami9933934', '2015-08-12 18:43:59.512');
INSERT INTO matches VALUES (116, 'rich3513992', 'john7691185', '2015-08-12 18:43:59.524');
INSERT INTO matches VALUES (117, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:59.537');
INSERT INTO matches VALUES (118, 'cars5806229', 'jami9933934', '2015-08-12 18:43:59.845');
INSERT INTO matches VALUES (119, 'john7691185', 'rich3513992', '2015-08-12 18:43:59.856');
INSERT INTO matches VALUES (120, 'nick5579800', 'jimm9256061', '2015-08-12 18:43:59.868');
INSERT INTO matches VALUES (121, 'cars5806229', 'jami9933934', '2015-08-12 18:44:00.144');
INSERT INTO matches VALUES (122, 'john7691185', 'rich3513992', '2015-08-12 18:44:00.156');
INSERT INTO matches VALUES (123, 'nick5579800', 'jimm9256061', '2015-08-12 18:44:00.169');
INSERT INTO matches VALUES (124, 'cars5806229', 'mall5387374', '2015-08-12 18:47:01.244');
INSERT INTO matches VALUES (125, 'jami9933934', 'john7691185', '2015-08-12 18:47:01.255');
INSERT INTO matches VALUES (126, 'rich3513992', 'jimm9256061', '2015-08-12 18:47:01.267');
INSERT INTO matches VALUES (127, 'cars5806229', 'jami9933934', '2015-08-12 18:47:03.029');
INSERT INTO matches VALUES (128, 'rich3513992', 'john7691185', '2015-08-12 18:47:03.040');
INSERT INTO matches VALUES (129, 'jimm9256061', 'nick5579800', '2015-08-12 18:47:03.052');
INSERT INTO matches VALUES (130, 'cars5806229', 'mall5387374', '2015-08-12 18:47:04.281');
INSERT INTO matches VALUES (131, 'john7691185', 'jami9933934', '2015-08-12 18:47:04.293');
INSERT INTO matches VALUES (132, 'nick5579800', 'rich3513992', '2015-08-12 18:47:04.305');
INSERT INTO matches VALUES (133, 'jami9933934', 'cars5806229', '2015-08-12 18:47:05.155');
INSERT INTO matches VALUES (134, 'rich3513992', 'john7691185', '2015-08-12 18:47:05.167');
INSERT INTO matches VALUES (135, 'jimm9256061', 'nick5579800', '2015-08-12 18:47:05.182');
INSERT INTO matches VALUES (136, 'mall5387374', 'cars5806229', '2015-08-12 18:47:06.001');
INSERT INTO matches VALUES (137, 'jami9933934', 'nick5579800', '2015-08-12 18:47:06.013');
INSERT INTO matches VALUES (138, 'jimm9256061', 'rich3513992', '2015-08-12 18:47:06.025');
INSERT INTO matches VALUES (139, 'cars5806229', 'mall5387374', '2015-08-12 18:47:06.891');
INSERT INTO matches VALUES (140, 'john7691185', 'jami9933934', '2015-08-12 18:47:06.902');
INSERT INTO matches VALUES (141, 'jimm9256061', 'rich3513992', '2015-08-12 18:47:06.913');
INSERT INTO matches VALUES (142, 'john7691185', 'mall5387374', '2015-08-12 18:47:07.755');
INSERT INTO matches VALUES (143, 'nick5579800', 'jami9933934', '2015-08-12 18:47:07.768');
INSERT INTO matches VALUES (144, 'jimm9256061', 'rich3513992', '2015-08-12 18:47:07.780');
INSERT INTO matches VALUES (145, 'mall5387374', 'cars5806229', '2015-08-12 18:47:09.095');
INSERT INTO matches VALUES (146, 'jami9933934', 'john7691185', '2015-08-12 18:47:09.107');
INSERT INTO matches VALUES (147, 'nick5579800', 'rich3513992', '2015-08-12 18:47:09.119');
INSERT INTO matches VALUES (148, 'john7691185', 'mall5387374', '2015-08-12 18:48:17.633');
INSERT INTO matches VALUES (149, 'jami9933934', 'nick5579800', '2015-08-12 18:48:17.645');
INSERT INTO matches VALUES (150, 'jimm9256061', 'cars5806229', '2015-08-12 18:48:17.657');
INSERT INTO matches VALUES (151, 'cars5806229', 'jami9933934', '2015-08-12 18:48:18.499');
INSERT INTO matches VALUES (152, 'rich3513992', 'nick5579800', '2015-08-12 18:48:18.510');
INSERT INTO matches VALUES (153, 'jimm9256061', 'john7691185', '2015-08-12 18:48:18.522');
INSERT INTO matches VALUES (154, 'mall5387374', 'john7691185', '2015-08-12 18:48:19.279');
INSERT INTO matches VALUES (155, 'jami9933934', 'cars5806229', '2015-08-12 18:48:19.291');
INSERT INTO matches VALUES (156, 'jimm9256061', 'rich3513992', '2015-08-12 18:48:19.303');
INSERT INTO matches VALUES (157, 'jami9933934', 'nick5579800', '2015-08-12 18:48:20.070');
INSERT INTO matches VALUES (158, 'john7691185', 'rich3513992', '2015-08-12 18:48:20.082');
INSERT INTO matches VALUES (159, 'cars5806229', 'jimm9256061', '2015-08-12 18:48:20.094');
INSERT INTO matches VALUES (160, 'mall5387374', 'rich3513992', '2015-08-12 18:48:38.821');
INSERT INTO matches VALUES (161, 'jimm9256061', 'nick5579800', '2015-08-12 18:48:38.833');
INSERT INTO matches VALUES (162, 'john7691185', 'jami9933934', '2015-08-12 18:48:38.845');
INSERT INTO matches VALUES (163, 'mall5387374', 'jimm9256061', '2015-08-12 18:48:40.411');
INSERT INTO matches VALUES (164, 'nick5579800', 'cars5806229', '2015-08-12 18:48:40.423');
INSERT INTO matches VALUES (165, 'john7691185', 'rich3513992', '2015-08-12 18:48:40.434');
INSERT INTO matches VALUES (166, 'jami9933934', 'mall5387374', '2015-08-12 18:48:41.174');
INSERT INTO matches VALUES (167, 'jimm9256061', 'nick5579800', '2015-08-12 18:48:41.186');
INSERT INTO matches VALUES (168, 'rich3513992', 'john7691185', '2015-08-12 18:48:41.198');
INSERT INTO matches VALUES (169, 'mall5387374', 'jami9933934', '2015-08-12 18:48:41.916');
INSERT INTO matches VALUES (170, 'jimm9256061', 'rich3513992', '2015-08-12 18:48:41.928');
INSERT INTO matches VALUES (171, 'john7691185', 'nick5579800', '2015-08-12 18:48:41.940');
INSERT INTO matches VALUES (172, 'mall5387374', 'nick5579800', '2015-08-12 18:48:42.685');
INSERT INTO matches VALUES (173, 'jami9933934', 'john7691185', '2015-08-12 18:48:42.697');
INSERT INTO matches VALUES (174, 'cars5806229', 'jimm9256061', '2015-08-12 18:48:42.710');
INSERT INTO matches VALUES (175, 'jimm9256061', 'rich3513992', '2015-08-12 18:48:44.047');
INSERT INTO matches VALUES (176, 'nick5579800', 'cars5806229', '2015-08-12 18:48:44.059');
INSERT INTO matches VALUES (177, 'mall5387374', 'john7691185', '2015-08-12 18:48:44.071');
INSERT INTO matches VALUES (178, 'nick5579800', 'mall5387374', '2015-08-12 18:48:44.852');
INSERT INTO matches VALUES (179, 'john7691185', 'jimm9256061', '2015-08-12 18:48:44.864');
INSERT INTO matches VALUES (180, 'cars5806229', 'rich3513992', '2015-08-12 18:48:44.875');
INSERT INTO matches VALUES (181, 'cars5806229', 'jami9933934', '2015-08-12 18:48:45.646');
INSERT INTO matches VALUES (182, 'rich3513992', 'jimm9256061', '2015-08-12 18:48:45.657');
INSERT INTO matches VALUES (183, 'nick5579800', 'john7691185', '2015-08-12 18:48:45.669');
INSERT INTO matches VALUES (184, 'mall5387374', 'jami9933934', '2015-08-12 18:48:46.408');
INSERT INTO matches VALUES (185, 'nick5579800', 'john7691185', '2015-08-12 18:48:46.419');
INSERT INTO matches VALUES (186, 'cars5806229', 'rich3513992', '2015-08-12 18:48:46.431');
INSERT INTO matches VALUES (187, 'mall5387374', 'jimm9256061', '2015-08-12 18:48:47.137');
INSERT INTO matches VALUES (188, 'rich3513992', 'cars5806229', '2015-08-12 18:48:47.149');
INSERT INTO matches VALUES (189, 'john7691185', 'nick5579800', '2015-08-12 18:48:47.161');
INSERT INTO matches VALUES (190, 'rich3513992', 'jami9933934', '2015-08-12 18:48:47.884');
INSERT INTO matches VALUES (191, 'nick5579800', 'cars5806229', '2015-08-12 18:48:47.898');
INSERT INTO matches VALUES (192, 'john7691185', 'jimm9256061', '2015-08-12 18:48:47.910');
INSERT INTO matches VALUES (193, 'mall5387374', 'jami9933934', '2015-08-12 18:48:48.685');
INSERT INTO matches VALUES (194, 'john7691185', 'jimm9256061', '2015-08-12 18:48:48.697');
INSERT INTO matches VALUES (195, 'cars5806229', 'rich3513992', '2015-08-12 18:48:48.709');
INSERT INTO matches VALUES (196, 'john7691185', 'jami9933934', '2015-08-12 18:48:49.429');
INSERT INTO matches VALUES (197, 'mall5387374', 'nick5579800', '2015-08-12 18:48:49.441');
INSERT INTO matches VALUES (198, 'rich3513992', 'cars5806229', '2015-08-12 18:48:49.453');

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

INSERT INTO players VALUES (1, 'Carson Palmer', 'USA', 'cars5806229');
INSERT INTO players VALUES (2, 'Johnny Carson', 'USA', 'john7691185');
INSERT INTO players VALUES (3, 'Nick Cannon', 'USA', 'nick5579800');
INSERT INTO players VALUES (4, 'Jimmy Fallon', 'USA', 'jimm9256061');
INSERT INTO players VALUES (5, 'Richarg Geere', 'USA', 'rich3513992');
INSERT INTO players VALUES (6, 'Jamie Curtis', 'USA', 'jami9933934');
INSERT INTO players VALUES (7, 'Mallory Mallorson', 'USA', 'mall5387374');


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

