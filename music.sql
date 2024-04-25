--
-- PostgreSQL database dump
--

-- Dumped from database version 14.11 (Homebrew)
-- Dumped by pg_dump version 14.11 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: invitations; Type: TABLE; Schema: public; Owner: lilymcclain
--

CREATE TABLE public.invitations (
    id integer NOT NULL,
    creating_user_id integer,
    joining_user_id integer,
    accepted boolean,
    declined boolean
);


ALTER TABLE public.invitations OWNER TO lilymcclain;

--
-- Name: invitations_id_seq; Type: SEQUENCE; Schema: public; Owner: lilymcclain
--

CREATE SEQUENCE public.invitations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.invitations_id_seq OWNER TO lilymcclain;

--
-- Name: invitations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: lilymcclain
--

ALTER SEQUENCE public.invitations_id_seq OWNED BY public.invitations.id;


--
-- Name: shared_playlist_tracks; Type: TABLE; Schema: public; Owner: lilymcclain
--

CREATE TABLE public.shared_playlist_tracks (
    id integer NOT NULL,
    playlist_id integer,
    track_id integer
);


ALTER TABLE public.shared_playlist_tracks OWNER TO lilymcclain;

--
-- Name: shared_playlist_tracks_id_seq; Type: SEQUENCE; Schema: public; Owner: lilymcclain
--

CREATE SEQUENCE public.shared_playlist_tracks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shared_playlist_tracks_id_seq OWNER TO lilymcclain;

--
-- Name: shared_playlist_tracks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: lilymcclain
--

ALTER SEQUENCE public.shared_playlist_tracks_id_seq OWNED BY public.shared_playlist_tracks.id;


--
-- Name: shared_playlists; Type: TABLE; Schema: public; Owner: lilymcclain
--

CREATE TABLE public.shared_playlists (
    id integer NOT NULL,
    creating_user_id integer,
    joining_user_id integer,
    title character varying,
    public boolean
);


ALTER TABLE public.shared_playlists OWNER TO lilymcclain;

--
-- Name: shared_playlists_id_seq; Type: SEQUENCE; Schema: public; Owner: lilymcclain
--

CREATE SEQUENCE public.shared_playlists_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shared_playlists_id_seq OWNER TO lilymcclain;

--
-- Name: shared_playlists_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: lilymcclain
--

ALTER SEQUENCE public.shared_playlists_id_seq OWNED BY public.shared_playlists.id;


--
-- Name: solo_playlist_tracks; Type: TABLE; Schema: public; Owner: lilymcclain
--

CREATE TABLE public.solo_playlist_tracks (
    id integer NOT NULL,
    playlist_id integer,
    track_id integer
);


ALTER TABLE public.solo_playlist_tracks OWNER TO lilymcclain;

--
-- Name: solo_playlist_tracks_id_seq; Type: SEQUENCE; Schema: public; Owner: lilymcclain
--

CREATE SEQUENCE public.solo_playlist_tracks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.solo_playlist_tracks_id_seq OWNER TO lilymcclain;

--
-- Name: solo_playlist_tracks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: lilymcclain
--

ALTER SEQUENCE public.solo_playlist_tracks_id_seq OWNED BY public.solo_playlist_tracks.id;


--
-- Name: solo_playlists; Type: TABLE; Schema: public; Owner: lilymcclain
--

CREATE TABLE public.solo_playlists (
    id integer NOT NULL,
    creating_user_id integer,
    title character varying,
    public boolean
);


ALTER TABLE public.solo_playlists OWNER TO lilymcclain;

--
-- Name: solo_playlists_id_seq; Type: SEQUENCE; Schema: public; Owner: lilymcclain
--

CREATE SEQUENCE public.solo_playlists_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.solo_playlists_id_seq OWNER TO lilymcclain;

--
-- Name: solo_playlists_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: lilymcclain
--

ALTER SEQUENCE public.solo_playlists_id_seq OWNED BY public.solo_playlists.id;


--
-- Name: tracks; Type: TABLE; Schema: public; Owner: lilymcclain
--

CREATE TABLE public.tracks (
    id integer NOT NULL,
    title character varying,
    artist character varying,
    artist_id character varying,
    spotify_track_id character varying,
    genre character varying
);


ALTER TABLE public.tracks OWNER TO lilymcclain;

--
-- Name: tracks_id_seq; Type: SEQUENCE; Schema: public; Owner: lilymcclain
--

CREATE SEQUENCE public.tracks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tracks_id_seq OWNER TO lilymcclain;

--
-- Name: tracks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: lilymcclain
--

ALTER SEQUENCE public.tracks_id_seq OWNED BY public.tracks.id;


--
-- Name: user_tracks; Type: TABLE; Schema: public; Owner: lilymcclain
--

CREATE TABLE public.user_tracks (
    id integer NOT NULL,
    user_id integer,
    track_id integer,
    listened_to boolean
);


ALTER TABLE public.user_tracks OWNER TO lilymcclain;

--
-- Name: user_tracks_id_seq; Type: SEQUENCE; Schema: public; Owner: lilymcclain
--

CREATE SEQUENCE public.user_tracks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_tracks_id_seq OWNER TO lilymcclain;

--
-- Name: user_tracks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: lilymcclain
--

ALTER SEQUENCE public.user_tracks_id_seq OWNED BY public.user_tracks.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: lilymcclain
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying,
    password character varying,
    explicit_content boolean
);


ALTER TABLE public.users OWNER TO lilymcclain;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: lilymcclain
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO lilymcclain;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: lilymcclain
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: invitations id; Type: DEFAULT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.invitations ALTER COLUMN id SET DEFAULT nextval('public.invitations_id_seq'::regclass);


--
-- Name: shared_playlist_tracks id; Type: DEFAULT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.shared_playlist_tracks ALTER COLUMN id SET DEFAULT nextval('public.shared_playlist_tracks_id_seq'::regclass);


--
-- Name: shared_playlists id; Type: DEFAULT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.shared_playlists ALTER COLUMN id SET DEFAULT nextval('public.shared_playlists_id_seq'::regclass);


--
-- Name: solo_playlist_tracks id; Type: DEFAULT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.solo_playlist_tracks ALTER COLUMN id SET DEFAULT nextval('public.solo_playlist_tracks_id_seq'::regclass);


--
-- Name: solo_playlists id; Type: DEFAULT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.solo_playlists ALTER COLUMN id SET DEFAULT nextval('public.solo_playlists_id_seq'::regclass);


--
-- Name: tracks id; Type: DEFAULT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.tracks ALTER COLUMN id SET DEFAULT nextval('public.tracks_id_seq'::regclass);


--
-- Name: user_tracks id; Type: DEFAULT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.user_tracks ALTER COLUMN id SET DEFAULT nextval('public.user_tracks_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: invitations; Type: TABLE DATA; Schema: public; Owner: lilymcclain
--

COPY public.invitations (id, creating_user_id, joining_user_id, accepted, declined) FROM stdin;
1	3	2	t	f
\.


--
-- Data for Name: shared_playlist_tracks; Type: TABLE DATA; Schema: public; Owner: lilymcclain
--

COPY public.shared_playlist_tracks (id, playlist_id, track_id) FROM stdin;
1	1	120
2	1	121
3	1	122
4	1	123
5	1	124
6	1	125
7	1	126
8	1	127
9	1	128
10	1	129
11	1	130
12	1	131
13	1	132
14	1	133
15	1	134
16	1	135
17	1	136
18	1	137
19	1	138
20	1	139
\.


--
-- Data for Name: shared_playlists; Type: TABLE DATA; Schema: public; Owner: lilymcclain
--

COPY public.shared_playlists (id, creating_user_id, joining_user_id, title, public) FROM stdin;
1	2	3	kylie & lily Playlist	f
\.


--
-- Data for Name: solo_playlist_tracks; Type: TABLE DATA; Schema: public; Owner: lilymcclain
--

COPY public.solo_playlist_tracks (id, playlist_id, track_id) FROM stdin;
1	1	21
2	1	22
3	1	23
4	1	24
5	1	25
6	1	26
7	1	27
8	1	28
9	1	29
10	1	30
11	1	31
12	1	32
13	1	33
14	1	34
15	1	35
16	1	36
17	1	37
18	1	38
19	1	39
20	1	40
21	2	61
22	2	62
23	2	63
24	2	64
25	2	65
26	2	66
27	2	67
28	2	68
29	2	69
30	2	70
31	2	71
32	2	72
33	2	73
34	2	74
35	2	75
36	2	76
37	2	77
38	2	78
39	2	79
40	2	80
41	3	100
42	3	101
43	3	102
44	3	103
45	3	104
46	3	105
47	3	106
48	3	107
49	3	108
50	3	109
51	3	110
52	3	111
53	3	112
54	3	113
55	3	114
56	3	115
57	3	116
58	3	117
59	3	118
60	3	119
\.


--
-- Data for Name: solo_playlists; Type: TABLE DATA; Schema: public; Owner: lilymcclain
--

COPY public.solo_playlists (id, creating_user_id, title, public) FROM stdin;
1	1	henry Playlist	f
2	2	kylie Playlist	f
3	3	lily Playlist	f
\.


--
-- Data for Name: tracks; Type: TABLE DATA; Schema: public; Owner: lilymcclain
--

COPY public.tracks (id, title, artist, artist_id, spotify_track_id, genre) FROM stdin;
1	M - 2006 Remaster	The Cure	7bu3H8JO7d0UbMoVzbo70s	6lGRiGJcWg1WiPLi7KoQvq	new wave
2	Just	Radiohead	4Z8W4fKeB5YxbusRsdQVPb	1dyTcli07c77mtQK3ahUZR	alternative rock
3	You Got It	Roy Orbison	0JDkhL4rjiPNEp92jAgJnS	6r20M5DWYdIoCDmDViBxuz	adult standards
4	Over You - Live	The Velvet Underground	1nJvji2KIlWSseXRSlNYsC	2chcBZsDQlN5sjoAkdaD28	alternative rock
5	Married With Children - Remastered	Oasis	2DaxqgrOhkeH0fpeiQq2f4	57bbMdaWpthoPTfuU9TFvQ	beatlesque
6	Warning Signs	Dorian Electra	202HZzqKvPsMHcbwnDZx7u	2F6cCKQn0vC0NUc47kBgzT	escape room
7	Dead!	My Chemical Romance	7FBcuc1gsnv6Y1nwFtNRCb	0uukw2CgEIApv4IWAjXrBC	emo
8	Idolize	Dorian Electra	202HZzqKvPsMHcbwnDZx7u	2MQ5VghlFqzGh5YsXBzVWZ	escape room
9	Sink to the Bottom	Fountains Of Wayne	1pgtr4nhBQjp9oCUBPyYWh	32uXfxJERzv4RK1gMLXbOA	pop rock
10	Best Buy	Bladee	2xvtxDNInKDV4AvGmjw6d1	1vaF8hvbUDMLowhVwEC3SS	cloud rap
11	Venus In Furs	The Velvet Underground	1nJvji2KIlWSseXRSlNYsC	29engDqjmMr3VLqMm0c0WE	alternative rock
12	All Tomorrow's Parties	The Velvet Underground	1nJvji2KIlWSseXRSlNYsC	1mL6q0gbifm2dBTvMBx4px	alternative rock
13	Waltz #2 (XO)	Elliott Smith	2ApaG60P4r0yhBoDCGD8YG	5AMrnF761nziCWUfjBgRUI	alternative rock
14	The Passenger	Iggy Pop	33EUXrFKGjpUSGacqEHhU4	15BQ7vEDv2LJuh8TxWIhtd	alternative rock
15	M.E.M.P.H.I.S.	Three 6 Mafia	26s8LSolLfCIY88ysQbIuT	1JfqLivyh8AfzlmZgMqJ0P	crunk
16	SNAIL'S PACE	Frost Children	6R1kfr0GIWnwxY4zW11Vag	0JUnfSjqpIvetC15lz1cgG	hyperpop
17	Goodbye Horses	Q Lazzarus	2EOrSEDPcZ9feKWSi8Fpdi	7I5eQZFdlPV8LZWH2FeqaW	new romantic
18	What’s Important	Beat Happening	1qHR9DMfOJQjvWLEfMZQlG	0wHAqXzMjoAeOC2aAFNVAS	alternative rock
19	Kiwi Maddog 20/20 (version 2 of 2)	Elliott Smith	2ApaG60P4r0yhBoDCGD8YG	5GwXU2PDHWykajNQ2Gaj8e	alternative rock
20	Hybrid Moments - C.I. Recording 1978	Misfits	1cXi8ALPQCBHZbf0EgP4Ey	7ap5NaoYRB6TJdrhX5Fej8	horror punk
21	One Of These Things First	Nick Drake	5c3GLXai8YOMid29ZEuR9y	0hNVjU6JKydHts0SAjHCno	british folk
22	This Strange Effect (Live at Aeolian Hall, 1965)	The Kinks	1SQRv42e4PjEYfPhS0Tk9E	1d1ecarY2bBa2orOcHFCIa	album rock
23	Her Black Wings	Danzig	34c4iQ5tkaZKu6Sv28BTde	4wM61bPrvM8HScuxtskTbd	alternative metal
24	Sound System - 2007 Remaster	Operation Ivy	18XRGxd1b484f2h06cwvJJ	4Pmo0mMgiyBCj1Zd7Axsi1	hardcore punk
25	Damaged Goods	Gang Of Four	3AmWjMXXtBJOmNGpUFSOAl	62uw0iWu8jLB4cYBQxjdcm	alternative rock
26	Na Na Na (Na Na Na Na Na Na Na Na Na)	My Chemical Romance	7FBcuc1gsnv6Y1nwFtNRCb	5BB0Jzw60KyfSTyjJqtely	emo
27	The Hanging Garden	The Cure	7bu3H8JO7d0UbMoVzbo70s	4aiCy98MqryFBPOKN8e9GP	new wave
28	I Don't Need Society	D.R.I.	6eKzDvHhJgMtcaOrvEXCTv	3ecrppPnloDWWI7XLxynjW	crossover thrash
29	Here Comes Your Man	Pixies	6zvul52xwTWzilBZl6BUbT	4IvZLDtwBHmBmwgDIUbuwa	alternative rock
30	Tear You Apart	She Wants Revenge	2zRt0sfxNnqI8gLR7d8gWt	3urJUvRhgMrwydaTQFVEg9	dark wave
31	I Don't Want to Get Over You	The Magnetic Fields	6RWjTQqILL7a1tQ0VapyLK	25N9PiAQnH5CxjKIa58MaN	alternative rock
32	Northern Sky	Nick Drake	5c3GLXai8YOMid29ZEuR9y	3EtIraJEHVSbBvLw5msioH	british folk
33	Helena	Misfits	1cXi8ALPQCBHZbf0EgP4Ey	1zNpX2LDasbtkryLNiphWN	horror punk
34	Love Like Blood	Killing Joke	0Zy4ncr8h1jd7Nzr9946fD	0SEfEDcVisRq8z4gU6r86b	gothic rock
35	Miserlou	Agent Orange	1pBsvSnrhmgDZqisT13SFA	1RhscZWFp75XvlJvbpbpYf	hardcore punk
36	Dirty Little Secret	The All-American Rejects	3vAaWhdBR38Q02ohXqaNHT	5lDriBxJd22IhOH9zTcFrV	alternative metal
37	Pet Sematary	Ramones	1co4F2pPNH8JjTutZkmgSm	2PN0JeaGtkHrlcmwZFWzBM	alternative rock
38	New Rose	The Damned	6VeL8VhaMjHTPc5uovFl3h	2RqX92TwDYaChAyfX9tKMH	new wave
39	half return	Adrianne Lenker	4aKWmkWAKviFlyvHYPTNQY	1i8dJGpKO0xQiKGCVslJqB	countrygaze
40	Unity - 2007 Remaster	Operation Ivy	18XRGxd1b484f2h06cwvJJ	2TncdAnbeRHID1yNR8YJC9	hardcore punk
41	Haircut	Ryan Beatty	60NNvDqsif0u40CXMV6jDQ	3UY4s7F4Ard3T6vm7xcJxQ	bedroom soul
42	Ant Pile	Dominic Fike	6USv9qhCn6zfxlBQIYJ9qs	2hR3npB7rQOqRXS4yISzFs	alternative pop rock
43	all-american bitch	Olivia Rodrigo	1McMsnEElThX1knmY4oliG	34sOdxWu9FljH84UXdRwu1	pop
44	Femininomenon	Chappell Roan	7GlBOeep6PqTfFi59PTUUN	53IRnAWx13PYmoVYtemUBS	indie pop
45	Why Don't We Go There	One Direction	4AK6F7OLvEQ5QYCBNiQWHq	2pFEbA6GdNxBOMn9Egvowm	boy band
46	Brando	Lucy Dacus	07D1Bjaof0NFlU32KXiqUP	4LAyHW59Qkj42ZMbas3Di4	indie pop
47	Mandinka	Sinéad O'Connor	4sD9znwiVFx9cgRPZ42aQ1	4x4e63yL8r7tOFcZ0n6KHe	lilith
48	Hot & Heavy	Lucy Dacus	07D1Bjaof0NFlU32KXiqUP	6SIooImkHGKCIwgUZ3WDvD	indie pop
49	rot in love	ratbag	6v6OE9MQreCmwuAqF0NfzQ	7oj0HfhX4PY8zmUR4kBxfe	\N
50	Scratching	Dijon	0knGpCTbmG4ctl1wzYRZs4	2F8SyDwcgNJaM7fo5poRzn	bedroom soul
51	Montezuma	Fleet Foxes	4EVpmkEwrLYEg6jIsiPMIb	5Civg4JEWHLe2gqMG5vW6E	chamber pop
52	Bodies	Dominic Fike	6USv9qhCn6zfxlBQIYJ9qs	59JXLBosh2OFLMCARkINnB	alternative pop rock
53	One Of Your Girls	Troye Sivan	3WGpXCj9YhhfX11TToZcXP	5Eh1nj7IjV9lwpcKAkidyY	australian pop
54	Expert In A Dying Field	The Beths	7DjwIxbe8kpw4pqnzAMoin	1bPcxJHusTrlr2Kj4kjK7e	auckland indie
55	Seventyseven dog years	underscores	7HfUJxeVTgrvhk0eWHFzV7	3irkFAVOrI6hy6PB0C725w	hyperpop
56	Being In Love	Wet Leg	2TwOrUcYnAlIiKmVQkkoSZ	4VBE0mwU8Nmm8hiqfCe4Ve	crank wave
57	Sick	Dominic Fike	6USv9qhCn6zfxlBQIYJ9qs	6OklSp2KgnW8RWNdQ7n8o1	alternative pop rock
58	Daylight	Harry Styles	6KImCVD70vtIoJWnq6nGn3	51Zw1cKDgkad0CXv23HCMU	pop
59	Come on over Baby (All I Want Is You) - Radio Version	Christina Aguilera	1l7ZsJRRS8wlW3WfJfPfNS	7A0apkTSTvMbSI7yplcmlh	dance pop
60	Circles	Mac Miller	4LLpKhyESsyAXpc4laK94U	4jXl6VtkFFKIt3ycUQc5LT	hip hop
61	So Hot You're Hurting My Feelings	Squirrel Flower	7bI1v9NGBBhq8iGfytctni	6LHioVAsFPLjupnl8ikW7H	boston indie
62	Cayendo (Side A - Acoustic)	Frank Ocean	2h93pZq0e7k5yf4dywlkpM	72794Eag03xdy7TO0KNuid	lgbtq+ hip hop
63	Under The Table	Fiona Apple	3g2kUQ6tHLLbmkV7T4GPtL	12WhIX6MvI93bS3wPSStSY	art pop
64	Ryd	Steve Lacy	57vWImR43h4CaDao012Ofp	5Ha9IheRrkDyr7ZdhaRsWb	afrofuturism
65	Temper Temper	Lime Cordiale	6yrtCy4XJHXM6tczo4RlTs	3DCU0R5FFaB9GKxZERb5wr	australian surf rock
66	Thoroughfare	Ethel Cain	0avMDS4HyoCEP6RqZJWpY2	04P1ylRDzyxBIl9W0UNWXC	countrygaze
67	Something	Julien Baker	12zbUHbPHL5DGuJtiUfsip	0BhM0Kr7Gc4uOIdVE3lXvt	ambient folk
68	Little Trouble	Better Oblivion Community Center	3NBmfDV6Yh3hjuQUBVvYgO	3CEexkaj6vOPQISc9B2S3h	indie pop
69	Pink Pony Club	Chappell Roan	7GlBOeep6PqTfFi59PTUUN	1k2pQc5i348DCHwbn5KTdc	indie pop
70	Moved On	LAUNDRY DAY	0SwK6bwzmGkViNoxSbJ5Mk	6WyIAjQg3ANwrWsYCO1vMB	bedroom pop
71	Body to Flame	Lucy Dacus	07D1Bjaof0NFlU32KXiqUP	3LW6Yh52Xtc6bmmzTVpkD0	indie pop
72	Traingazing	Sam Wills	7JFinw4LobpCUjapyKvsjo	49QEJdbU9mf4VUXReOpZ9u	uk contemporary r&b
73	Isabella (with Lucy Dacus)	Hamilton Leithauser	3ZXXJ9nO1Dn9B0AJ25eAQY	1yyLZ36akxy4Bf3RqLZhtG	indie rock
74	Lil Baby Crush	Jordan Ward	3DGlTwdM5Dim9XQipb3jMf	6nXiaXqSZAJuOG6q66mZV1	indie hip hop
75	Softly	Clairo	3l0CmX0FuQjFxr8SK7Vqag	4PvbbMYL4fkToni5BLaYRb	bedroom pop
76	More Than Friends	Aidan Bissett	4XQI4hyuy5xun1ou3SM8Oe	0AAKAJfciQhdYlEZLwxwMg	gen z singer-songwriter
77	Go Home	Julien Baker	12zbUHbPHL5DGuJtiUfsip	2Yl6jU0pWLyMP9XUlGsZAD	ambient folk
78	Electric Feel	MGMT	0SwO7SWeDHJijQ3XNS7xEE	3FtYbEfBqAlGO46NUDQSAt	alternative rock
79	Meet Me At Our Spot	THE ANXIETY	64H8UqGLbJFHwKtGxiV8OP	07MDkzWARZaLEdKxo6yArG	modern alternative pop
80	Annie	Dijon	0knGpCTbmG4ctl1wzYRZs4	1UuyxrM0UxKxLht6vWf3lZ	bedroom soul
81	Oxbow	Waxahatchee	5IWCU0V9evBlW4gIeGY4zF	5NHAAgIFC3IDVCbOAewHlw	alabama indie
82	Fire	Waxahatchee	5IWCU0V9evBlW4gIeGY4zF	2lBEWXP11gpEySIXgA5ALH	alabama indie
83	The Emperor's New Clothes	Sinéad O'Connor	4sD9znwiVFx9cgRPZ42aQ1	0HSmS7KsbOpB3K4UFdOSx9	lilith
84	Without You Without Them	boygenius	1hLiboQ98IQWhpKeP9vRFw	12EkF8uGofptstVIX7Oc0C	indie pop
85	212	Azealia Banks	7gRhy3MIPHQo5CXYfWaw9I	16EMONl2vH3rt9f4ehTG8g	escape room
86	Hell	Waxahatchee	5IWCU0V9evBlW4gIeGY4zF	5MSyyBEPMrYFyiYP51B9du	alabama indie
87	Out Alpha The Alpha	Megan Thee Stallion	181bsRPaVXVlUKXrxwZfHK	5buJqlSc56jXbmcoHqkeIO	houston rap
88	Lilacs	Waxahatchee	5IWCU0V9evBlW4gIeGY4zF	69Akwuscu16hdYN637eTis	alabama indie
89	Wet	Dazey and the Scouts	3J8YGHzxEZzHRYVxGmQCvJ	7yBjQ29XKxHlxuqycHuvmm	boston indie
90	The Eye	Waxahatchee	5IWCU0V9evBlW4gIeGY4zF	4BtThAVSnU1wZqupmcnnps	alabama indie
91	vampire	Olivia Rodrigo	1McMsnEElThX1knmY4oliG	3k79jB4aGmMDUQzEwa46Rz	pop
92	Pedestrian at Best	Courtney Barnett	4OOlG5eBXSkSAAEeKjJb5Y	7gsn3NxWLA0s0g9TmQlMri	art pop
93	Witches	Waxahatchee	5IWCU0V9evBlW4gIeGY4zF	1g5PJ4SMxVgCTy6uYLzgu4	alabama indie
94	Can’t Do Much	Waxahatchee	5IWCU0V9evBlW4gIeGY4zF	0sEJmxTlb2SZNxdjzBATPK	alabama indie
95	I Love You, Honeybear	Father John Misty	2kGBy2WHvF0VdZyqiVCkDT	5jLMFDMUkGpzIgPF2sxWkB	art pop
96	Birthday	The Sugarcubes	1G0Xwj8mza6b03iYkVdzDP	55MEbqyxZphjB0beZ7YT0f	alternative rock
97	Avant Gardener	Courtney Barnett	4OOlG5eBXSkSAAEeKjJb5Y	3LueS3mbuB1yaJNN0Ale6U	art pop
98	War	Waxahatchee	5IWCU0V9evBlW4gIeGY4zF	1Ga3pLsq3HgflHNPvBvnNC	alabama indie
99	Saturday in the Park - 2002 Remaster	Chicago	3iDD7bnsjL9J4fO298r0L0	4OJFkrRQqol4FsPesF8eu4	album rock
100	My Kind	Rosali	2WpwNw5EKb52c1QlvnGqfs	3lK0biBfR1N04pp7J3GOqJ	alternative americana
101	Linger	The Cranberries	7t0rwkOPGlDPEhaOcVtOt9	0gEyKnHvgkrkBM6fbeHdwK	irish rock
102	How Can You Really	Foxygen	55LHFEtIplWhsfyWZUwkf4	0XyUYupoEzHVHjYJcIwBIm	baroque pop
103	Make Ya Proud	Hovvdy	59RNNqeEfkq3X5pfOQxZ3C	22OlNU4xTgKvTekYCyvYmj	austindie
104	Never Get Old	Sinéad O'Connor	4sD9znwiVFx9cgRPZ42aQ1	0obVv1fEGQcWrTpCiEDjja	lilith
105	Blue Moon Revisited (Song For Elvis)	Cowboy Junkies	3CYSRCHfilgR8DSbkCMp5j	1RszdaPPEyHMoTyy0pRBrv	alternative country
106	You Can Have It All	Yo La Tengo	5hAhrnb0Ch4ODwWu4tsbpi	5s91S8hSrJXqYdhwHOEioV	alternative rock
107	Still Can’t Believe	Dr. Dog	4mLJ3XfOM5FPjSAWdQ2Jk7	1qCiSESOXPmjgVeuC6UH3o	chamber pop
108	First Love/Late Spring	Mitski	2uYWxilOVlUdk4oV9DvwqK	3sslYZcFKtUvIEWN9lADgr	brooklyn indie
109	Impossible Germany	Wilco	2QoU3awHVdcHS8LrZEKvSM	6L0BBPYeWnaQJeDa0ox0IA	alternative country
110	Swim and Sleep (Like a Shark)	Unknown Mortal Orchestra	1LeVJ5GPeYDOVUjxx1y7Rp	265ehI4I7NfR8PmAXdpspn	art pop
111	Free Treasure	Adrianne Lenker	4aKWmkWAKviFlyvHYPTNQY	3zGhR60NOVSgtzNEQNcHav	countrygaze
112	Revival	Deerhunter	38zTZcuN7nFvVJ6auhc6V3	2h1tUggJBTBYNbi2SqM4tK	alternative rock
113	Ophelia	The Lumineers	16oZKvXb6WkQlVAjwo2Wbg	7gUvAzKQ651eGm16AqcTbP	folk-pop
114	Forever Young - 2019 Remaster	Alphaville	0xliTEbFfy5HQHvsTknTkX	6XHNIbru8xGohLzHNgxQvF	new romantic
115	Fade	Waxahatchee	5IWCU0V9evBlW4gIeGY4zF	3IpGVvLgtjOcImeblhzh31	alabama indie
116	Someday - triple j Like A Version / Live	Julia Jacklin	12fRkVfO2fUsz1QHgDAG3g	5oWJxP0sIsHRge6LWR9sIs	chamber pop
117	The Logical Song - Remastered 2010	Supertramp	3JsMj0DEzyWc0VDlHuy9Bx	6mHOcVtsHLMuesJkswc0GZ	album rock
118	You're So Vain	Carly Simon	4FtSnMlCVxCswABUmdhwpm	2DnJjbjNTV9Nd5NOa1KGba	classic rock
119	The Boy	Shannon & The Clams	6A5Ns1SpGWTt8SzXPwiqVE	1WypLBcOgtNO0meaWKBkVQ	bay area indie
120	Florida	Dominic Fike	6USv9qhCn6zfxlBQIYJ9qs	4N6jSDQb5PaR9d1IYM2aBz	alternative pop rock
121	Infrunami	Steve Lacy	57vWImR43h4CaDao012Ofp	0f8eRy9A0n6zXpKSHSCAEp	afrofuturism
122	Defenceless	Louis Tomlinson	57WHJIHrjOE3iAxpihhMnp	74YzCrLzu7fw0AasX3CEwv	pop
123	It's Called: Freefall	Rainbow Kitten Surprise	4hz8tIajF2INpgM0qzPJz2	474uVhyGgK5MtY9gMcDgGl	pov: indie
124	One Thing	One Direction	4AK6F7OLvEQ5QYCBNiQWHq	5G2c6FsfTzgYUzageCmfXY	boy band
125	Dead Girl Walking	Jensen McRae	11dABkjSoOjcP9p3TFSNRj	3yvfF8a3MEpoE58lrIARnX	gen z singer-songwriter
126	Payphone	Maroon 5	04gDigrS5kc9YWfZHwBETP	1XGmzt0PVuFgQYYnV2It7A	pop
127	8 Letters	Why Don't We	2jnIB6XdLvnJUeNTy5A0J2	4zRZAmBQP8vhNPf9i9opXt	boy band
128	Bruises Off The Peach - Live Performance	Ryan Beatty	60NNvDqsif0u40CXMV6jDQ	5NKuBQQKo1yo5EB8QTx2FX	bedroom soul
129	Chateau (Feel Alright)	Djo	5p9HO3XC5P3BLxJs5Mtrhm	3vjs2MDHoF9xhylNg6Y9un	pov: indie
130	It's Sad to Belong - Single Version	England Dan & John Ford Coley	01W8kYNqFHyKicPfR0pLwO	3zqvox7nyhykHe7WS8w9Rm	mellow gold
131	Forever Young - 2019 Remaster	Alphaville	0xliTEbFfy5HQHvsTknTkX	6XHNIbru8xGohLzHNgxQvF	new romantic
132	An Everlasting Love	Andy Gibb	4YPqbAiLzBg5DIfsgQZ8QK	30IpEYZRHYmS8yZyMM5aYK	disco
133	Moving Out	Kacey Musgraves	70kkdajctXSbqSMJbQO424	1LwT9Pou0rRCXPpXVWy5iA	classic texas country
134	Pressure To Party	Julia Jacklin	12fRkVfO2fUsz1QHgDAG3g	0WpSiLSFPVarFJ03SJJQUu	chamber pop
135	I Know You Know	Bonny Light Horseman	0Qi9Fcmn1DJAoG8Agf5ibb	5OQ8VuPNOJm0UR3FGbGo6U	indie folk
136	Botox	ïago	6nKAEx9XhIKHw2mSpMOVvX	2a7NY1gKqosJTcaFxxH8te	\N
137	Peace and Quiet	Waxahatchee	5IWCU0V9evBlW4gIeGY4zF	3IjZ2SHO7YijUFEn18SFbi	alabama indie
138	Chasing Time	Azealia Banks	7gRhy3MIPHQo5CXYfWaw9I	0KghTfieEzsuB4KkPwxhei	escape room
139	Alone	Heart	34jw2BbxjoYalTp8cJFCPv	54b8qPFqYqIndfdxiLApea	album rock
\.


--
-- Data for Name: user_tracks; Type: TABLE DATA; Schema: public; Owner: lilymcclain
--

COPY public.user_tracks (id, user_id, track_id, listened_to) FROM stdin;
1	1	1	t
2	1	2	t
3	1	3	t
4	1	4	t
5	1	5	t
6	1	6	t
7	1	7	t
8	1	8	t
9	1	9	t
10	1	10	t
11	1	11	t
12	1	12	t
13	1	13	t
14	1	14	t
15	1	15	t
16	1	16	t
17	1	17	t
18	1	18	t
19	1	19	t
20	1	20	t
21	2	41	t
22	2	42	t
23	2	43	t
24	2	44	t
25	2	45	t
26	2	46	t
27	2	47	t
28	2	48	t
29	2	49	t
30	2	50	t
31	2	51	t
32	2	52	t
33	2	53	t
34	2	54	t
35	2	55	t
36	2	56	t
37	2	57	t
38	2	58	t
39	2	59	t
40	2	60	t
41	3	81	t
42	3	82	t
43	3	83	t
44	3	84	t
45	3	85	t
46	3	86	t
47	3	87	t
48	3	88	t
49	3	89	t
50	3	90	t
51	3	91	t
52	3	92	t
53	3	93	t
54	3	94	t
55	3	95	t
56	3	96	t
57	3	97	t
58	3	98	t
59	3	99	t
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: lilymcclain
--

COPY public.users (id, username, password, explicit_content) FROM stdin;
1	henry	henry	t
2	kylie	kylie	t
3	lily	lily	t
\.


--
-- Name: invitations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: lilymcclain
--

SELECT pg_catalog.setval('public.invitations_id_seq', 1, true);


--
-- Name: shared_playlist_tracks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: lilymcclain
--

SELECT pg_catalog.setval('public.shared_playlist_tracks_id_seq', 20, true);


--
-- Name: shared_playlists_id_seq; Type: SEQUENCE SET; Schema: public; Owner: lilymcclain
--

SELECT pg_catalog.setval('public.shared_playlists_id_seq', 1, true);


--
-- Name: solo_playlist_tracks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: lilymcclain
--

SELECT pg_catalog.setval('public.solo_playlist_tracks_id_seq', 60, true);


--
-- Name: solo_playlists_id_seq; Type: SEQUENCE SET; Schema: public; Owner: lilymcclain
--

SELECT pg_catalog.setval('public.solo_playlists_id_seq', 3, true);


--
-- Name: tracks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: lilymcclain
--

SELECT pg_catalog.setval('public.tracks_id_seq', 139, true);


--
-- Name: user_tracks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: lilymcclain
--

SELECT pg_catalog.setval('public.user_tracks_id_seq', 59, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: lilymcclain
--

SELECT pg_catalog.setval('public.users_id_seq', 3, true);


--
-- Name: invitations invitations_pkey; Type: CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.invitations
    ADD CONSTRAINT invitations_pkey PRIMARY KEY (id);


--
-- Name: shared_playlist_tracks shared_playlist_tracks_pkey; Type: CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.shared_playlist_tracks
    ADD CONSTRAINT shared_playlist_tracks_pkey PRIMARY KEY (id);


--
-- Name: shared_playlists shared_playlists_pkey; Type: CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.shared_playlists
    ADD CONSTRAINT shared_playlists_pkey PRIMARY KEY (id);


--
-- Name: solo_playlist_tracks solo_playlist_tracks_pkey; Type: CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.solo_playlist_tracks
    ADD CONSTRAINT solo_playlist_tracks_pkey PRIMARY KEY (id);


--
-- Name: solo_playlists solo_playlists_pkey; Type: CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.solo_playlists
    ADD CONSTRAINT solo_playlists_pkey PRIMARY KEY (id);


--
-- Name: tracks tracks_pkey; Type: CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.tracks
    ADD CONSTRAINT tracks_pkey PRIMARY KEY (id);


--
-- Name: user_tracks user_tracks_pkey; Type: CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.user_tracks
    ADD CONSTRAINT user_tracks_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: invitations invitations_creating_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.invitations
    ADD CONSTRAINT invitations_creating_user_id_fkey FOREIGN KEY (creating_user_id) REFERENCES public.users(id);


--
-- Name: invitations invitations_joining_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.invitations
    ADD CONSTRAINT invitations_joining_user_id_fkey FOREIGN KEY (joining_user_id) REFERENCES public.users(id);


--
-- Name: shared_playlist_tracks shared_playlist_tracks_playlist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.shared_playlist_tracks
    ADD CONSTRAINT shared_playlist_tracks_playlist_id_fkey FOREIGN KEY (playlist_id) REFERENCES public.shared_playlists(id);


--
-- Name: shared_playlist_tracks shared_playlist_tracks_track_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.shared_playlist_tracks
    ADD CONSTRAINT shared_playlist_tracks_track_id_fkey FOREIGN KEY (track_id) REFERENCES public.tracks(id);


--
-- Name: shared_playlists shared_playlists_creating_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.shared_playlists
    ADD CONSTRAINT shared_playlists_creating_user_id_fkey FOREIGN KEY (creating_user_id) REFERENCES public.users(id);


--
-- Name: shared_playlists shared_playlists_joining_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.shared_playlists
    ADD CONSTRAINT shared_playlists_joining_user_id_fkey FOREIGN KEY (joining_user_id) REFERENCES public.users(id);


--
-- Name: solo_playlist_tracks solo_playlist_tracks_playlist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.solo_playlist_tracks
    ADD CONSTRAINT solo_playlist_tracks_playlist_id_fkey FOREIGN KEY (playlist_id) REFERENCES public.solo_playlists(id);


--
-- Name: solo_playlist_tracks solo_playlist_tracks_track_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.solo_playlist_tracks
    ADD CONSTRAINT solo_playlist_tracks_track_id_fkey FOREIGN KEY (track_id) REFERENCES public.tracks(id);


--
-- Name: solo_playlists solo_playlists_creating_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.solo_playlists
    ADD CONSTRAINT solo_playlists_creating_user_id_fkey FOREIGN KEY (creating_user_id) REFERENCES public.users(id);


--
-- Name: user_tracks user_tracks_track_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.user_tracks
    ADD CONSTRAINT user_tracks_track_id_fkey FOREIGN KEY (track_id) REFERENCES public.tracks(id);


--
-- Name: user_tracks user_tracks_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lilymcclain
--

ALTER TABLE ONLY public.user_tracks
    ADD CONSTRAINT user_tracks_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

