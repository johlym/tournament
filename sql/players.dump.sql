--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.4
-- Dumped by pg_dump version 9.4.4
-- Started on 2015-08-12 18:51:45 PDT

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
-- TOC entry 173 (class 1259 OID 48708)
-- Name: players; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE players (
    id integer NOT NULL,
    name text NOT NULL,
    country text NOT NULL,
    code text
);

--
-- TOC entry 172 (class 1259 OID 48706)
-- Name: players_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE players_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

--
-- TOC entry 2271 (class 0 OID 0)
-- Dependencies: 172
-- Name: players_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE players_id_seq OWNED BY players.id;


--
-- TOC entry 2153 (class 2604 OID 48711)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY players ALTER COLUMN id SET DEFAULT nextval('players_id_seq'::regclass);


--
-- TOC entry 2266 (class 0 OID 48708)
-- Dependencies: 173
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
-- TOC entry 2272 (class 0 OID 0)
-- Dependencies: 172
-- Name: players_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('players_id_seq', 7, true);


--
-- TOC entry 2155 (class 2606 OID 48716)
-- Name: players_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY players
    ADD CONSTRAINT players_pkey PRIMARY KEY (id);


-- Completed on 2015-08-12 18:51:45 PDT

--
-- PostgreSQL database dump complete
--

