--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

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
-- Name: advanced_workshop; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.advanced_workshop (
    id integer NOT NULL,
    clg_code character varying(250) DEFAULT NULL::character varying NOT NULL,
    name character varying(512) DEFAULT NULL::character varying NOT NULL,
    emailid character varying(250) DEFAULT NULL::character varying NOT NULL,
    gender character varying(250) DEFAULT NULL::character varying NOT NULL,
    contact_num character varying(11) DEFAULT NULL::character varying NOT NULL,
    alt_contact1 character varying(11) DEFAULT NULL::character varying,
    designation character varying(250) DEFAULT NULL::character varying NOT NULL,
    role character varying(50) DEFAULT NULL::character varying,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone
);


ALTER TABLE public.advanced_workshop OWNER TO postgres;

--
-- Name: advanced_workshop_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.advanced_workshop_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.advanced_workshop_id_seq OWNER TO postgres;

--
-- Name: advanced_workshop_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.advanced_workshop_id_seq OWNED BY public.advanced_workshop.id;


--
-- Name: alumni_email; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alumni_email (
    id integer NOT NULL,
    name character varying(50) DEFAULT NULL::character varying,
    username character varying(100) DEFAULT NULL::character varying,
    type character varying(50) DEFAULT NULL::character varying,
    year character varying(50) DEFAULT NULL::character varying,
    email_flag integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.alumni_email OWNER TO postgres;

--
-- Name: alumni_email_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.alumni_email_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.alumni_email_id_seq OWNER TO postgres;

--
-- Name: alumni_email_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.alumni_email_id_seq OWNED BY public.alumni_email.id;


--
-- Name: backup_elsi_college_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.backup_elsi_college_dtls (
    id integer NOT NULL,
    clg_code character varying(512) DEFAULT NULL::character varying,
    region_id integer,
    workshop_id integer DEFAULT 0 NOT NULL,
    college_name character varying(1024) DEFAULT NULL::character varying NOT NULL,
    abbreviation character varying(128) DEFAULT NULL::character varying,
    district character varying(256) DEFAULT NULL::character varying,
    address character varying(1024) DEFAULT NULL::character varying,
    state character varying(512) DEFAULT NULL::character varying,
    pincode character varying(10) DEFAULT NULL::character varying,
    college_type character varying(256) DEFAULT NULL::character varying,
    principal_meet integer DEFAULT 0 NOT NULL,
    robots_given integer DEFAULT 0,
    eyic_allowed integer DEFAULT 0 NOT NULL,
    eyrtc_allowed integer DEFAULT 0 NOT NULL,
    tbt_allowed integer DEFAULT 0 NOT NULL,
    content_allowed integer DEFAULT 0 NOT NULL,
    legal_docs integer DEFAULT 0,
    legal_docs_remarks character varying(1024) DEFAULT NULL::character varying,
    loi_status integer DEFAULT 0 NOT NULL,
    loi_format integer DEFAULT 0,
    loi_remarks character varying(1024) DEFAULT NULL::character varying,
    po_status integer DEFAULT 0,
    po_remark character varying(1024) DEFAULT NULL::character varying,
    wo_reg integer DEFAULT 0 NOT NULL,
    wo_invite integer DEFAULT 0 NOT NULL,
    wo_confirm integer DEFAULT 0 NOT NULL,
    wo_attend integer DEFAULT 0 NOT NULL,
    hardware_given character varying(1024) DEFAULT NULL::character varying,
    lab_inaugurated integer DEFAULT 0 NOT NULL,
    phase integer DEFAULT 0 NOT NULL,
    eys2016_invites integer DEFAULT 0 NOT NULL,
    team_verify integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.backup_elsi_college_dtls OWNER TO postgres;

--
-- Name: COLUMN backup_elsi_college_dtls.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.backup_elsi_college_dtls.id IS 'identifier';


--
-- Name: COLUMN backup_elsi_college_dtls.principal_meet; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.backup_elsi_college_dtls.principal_meet IS 'tbt+lab=3,tbt=0-lab=1==1';


--
-- Name: COLUMN backup_elsi_college_dtls.robots_given; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.backup_elsi_college_dtls.robots_given IS 'tbt_participated+lab=1,tbt+lab=3';


--
-- Name: COLUMN backup_elsi_college_dtls.eyrtc_allowed; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.backup_elsi_college_dtls.eyrtc_allowed IS '1=participated,2=tbt+eyrtc complete,3=eyrtc completed';


--
-- Name: backup_elsi_college_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.backup_elsi_college_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.backup_elsi_college_dtls_id_seq OWNER TO postgres;

--
-- Name: backup_elsi_college_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.backup_elsi_college_dtls_id_seq OWNED BY public.backup_elsi_college_dtls.id;


--
-- Name: colleges_to_contact_to_establish_elsi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.colleges_to_contact_to_establish_elsi (
    id integer NOT NULL,
    college_name character varying(512) DEFAULT NULL::character varying,
    name character varying(512) DEFAULT NULL::character varying,
    designation character varying(512) DEFAULT NULL::character varying,
    email character varying(512) DEFAULT NULL::character varying,
    rank integer
);


ALTER TABLE public.colleges_to_contact_to_establish_elsi OWNER TO postgres;

--
-- Name: con_feedback; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_feedback (
    id integer NOT NULL,
    tch_id integer,
    resources text,
    curriculum character varying(20) DEFAULT NULL::character varying,
    lab_exp character varying(20) DEFAULT NULL::character varying,
    comment text,
    lesson_id integer,
    lesson_plan_id integer,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT '-infinity'::timestamp without time zone NOT NULL
);


ALTER TABLE public.con_feedback OWNER TO postgres;

--
-- Name: con_feedback_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_feedback_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_feedback_id_seq OWNER TO postgres;

--
-- Name: con_feedback_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_feedback_id_seq OWNED BY public.con_feedback.id;


--
-- Name: con_latex; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_latex (
    id integer NOT NULL,
    tch_id integer,
    clg_id integer,
    down_date character varying(200) DEFAULT NULL::character varying,
    flag integer DEFAULT 0 NOT NULL,
    upload_date character varying(20) DEFAULT NULL::character varying,
    status character varying(100) DEFAULT NULL::character varying,
    accept_reject integer DEFAULT 0 NOT NULL,
    remark text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone
);


ALTER TABLE public.con_latex OWNER TO postgres;

--
-- Name: COLUMN con_latex.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.con_latex.id IS 'identifier';


--
-- Name: con_latex_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_latex_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_latex_id_seq OWNER TO postgres;

--
-- Name: con_latex_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_latex_id_seq OWNED BY public.con_latex.id;


--
-- Name: con_lesson_create; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_lesson_create (
    id integer NOT NULL,
    lp_name text,
    lp_plan character varying(100) DEFAULT NULL::character varying,
    refer_content text NOT NULL,
    available integer DEFAULT 0 NOT NULL,
    tch_count integer DEFAULT 0,
    i_agree integer DEFAULT 0 NOT NULL,
    phase integer DEFAULT 0 NOT NULL,
    launch_date character varying(200) DEFAULT NULL::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT '-infinity'::timestamp without time zone NOT NULL
);


ALTER TABLE public.con_lesson_create OWNER TO postgres;

--
-- Name: con_lesson_create_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_lesson_create_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_lesson_create_id_seq OWNER TO postgres;

--
-- Name: con_lesson_create_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_lesson_create_id_seq OWNED BY public.con_lesson_create.id;


--
-- Name: con_lesson_plan_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_lesson_plan_list (
    id integer NOT NULL,
    name character varying(1024) DEFAULT NULL::character varying NOT NULL,
    image_name character varying(1024) DEFAULT NULL::character varying,
    short_intro character varying(2048) DEFAULT NULL::character varying,
    intro_video_code character varying(512) DEFAULT NULL::character varying,
    available integer DEFAULT 0 NOT NULL,
    student_chk integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.con_lesson_plan_list OWNER TO postgres;

--
-- Name: con_lesson_plan_list_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_lesson_plan_list_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_lesson_plan_list_id_seq OWNER TO postgres;

--
-- Name: con_lesson_plan_list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_lesson_plan_list_id_seq OWNED BY public.con_lesson_plan_list.id;


--
-- Name: con_lesson_plan_long_content; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_lesson_plan_long_content (
    id integer NOT NULL,
    lesson_plan_id integer NOT NULL,
    long_intro text,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.con_lesson_plan_long_content OWNER TO postgres;

--
-- Name: con_lesson_plan_long_content_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_lesson_plan_long_content_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_lesson_plan_long_content_id_seq OWNER TO postgres;

--
-- Name: con_lesson_plan_long_content_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_lesson_plan_long_content_id_seq OWNED BY public.con_lesson_plan_long_content.id;


--
-- Name: con_lp_lessons; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_lp_lessons (
    id integer NOT NULL,
    lesson_plan_id integer NOT NULL,
    display_num integer NOT NULL,
    lesson_name character varying(512) DEFAULT NULL::character varying NOT NULL,
    video1_code character varying(512) DEFAULT NULL::character varying,
    video1_name character varying(1024) DEFAULT NULL::character varying,
    video2_code character varying(512) DEFAULT NULL::character varying,
    video2_name character varying(1024) DEFAULT NULL::character varying,
    html_content text,
    down_tm integer DEFAULT 0 NOT NULL,
    count_tm integer DEFAULT 0 NOT NULL,
    down_rr integer DEFAULT 0 NOT NULL,
    count_rr integer DEFAULT 0 NOT NULL,
    down_qb integer DEFAULT 0 NOT NULL,
    count_qb integer DEFAULT 0 NOT NULL,
    down_qbs integer DEFAULT 0 NOT NULL,
    count_qbs integer DEFAULT 0 NOT NULL,
    down_le integer DEFAULT 0 NOT NULL,
    count_le integer DEFAULT 0 NOT NULL,
    down_les integer DEFAULT 0 NOT NULL,
    count_les integer DEFAULT 0,
    available integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.con_lp_lessons OWNER TO postgres;

--
-- Name: con_lp_lessons_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_lp_lessons_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_lp_lessons_id_seq OWNER TO postgres;

--
-- Name: con_lp_lessons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_lp_lessons_id_seq OWNED BY public.con_lp_lessons.id;


--
-- Name: con_project_generic; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_project_generic (
    id integer NOT NULL,
    name character varying(1024) DEFAULT NULL::character varying NOT NULL,
    video_url character varying(1024) DEFAULT NULL::character varying,
    type integer DEFAULT 0 NOT NULL,
    available integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.con_project_generic OWNER TO postgres;

--
-- Name: con_project_generic_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_project_generic_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_project_generic_id_seq OWNER TO postgres;

--
-- Name: con_project_generic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_project_generic_id_seq OWNED BY public.con_project_generic.id;


--
-- Name: con_project_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_project_list (
    id integer NOT NULL,
    name character varying(1024) DEFAULT NULL::character varying NOT NULL,
    image_name character varying(1024) DEFAULT NULL::character varying,
    report_name character varying(50) DEFAULT NULL::character varying NOT NULL,
    available integer DEFAULT 0 NOT NULL,
    count_project integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.con_project_list OWNER TO postgres;

--
-- Name: con_project_list_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_project_list_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_project_list_id_seq OWNER TO postgres;

--
-- Name: con_project_list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_project_list_id_seq OWNED BY public.con_project_list.id;


--
-- Name: con_project_topics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_project_topics (
    id integer NOT NULL,
    proj_id integer NOT NULL,
    hardware text NOT NULL,
    software text,
    authors character varying(1024) DEFAULT NULL::character varying,
    description text,
    video_code character varying(512) DEFAULT NULL::character varying,
    code_link character varying(512) DEFAULT NULL::character varying,
    available integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.con_project_topics OWNER TO postgres;

--
-- Name: con_project_topics_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_project_topics_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_project_topics_id_seq OWNER TO postgres;

--
-- Name: con_project_topics_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_project_topics_id_seq OWNED BY public.con_project_topics.id;


--
-- Name: con_registration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_registration (
    id integer NOT NULL,
    tch_id integer,
    name character varying(200) DEFAULT NULL::character varying,
    designation character varying(200) DEFAULT NULL::character varying,
    photo character varying(100) DEFAULT NULL::character varying,
    name_cheq character varying(200) DEFAULT NULL::character varying,
    biography text,
    branch character varying(200) DEFAULT '0'::character varying NOT NULL,
    ifsc character varying(100) DEFAULT '0'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT '-infinity'::timestamp without time zone NOT NULL
);


ALTER TABLE public.con_registration OWNER TO postgres;

--
-- Name: COLUMN con_registration.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.con_registration.id IS 'identifier';


--
-- Name: con_registration_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_registration_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_registration_id_seq OWNER TO postgres;

--
-- Name: con_registration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_registration_id_seq OWNED BY public.con_registration.id;


--
-- Name: con_suggested_topic; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_suggested_topic (
    id integer NOT NULL,
    tch_id integer,
    topic character varying(200) DEFAULT NULL::character varying,
    description text,
    choice character varying(200) DEFAULT NULL::character varying,
    email_sent integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone
);


ALTER TABLE public.con_suggested_topic OWNER TO postgres;

--
-- Name: con_suggested_topic_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_suggested_topic_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_suggested_topic_id_seq OWNER TO postgres;

--
-- Name: con_suggested_topic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_suggested_topic_id_seq OWNED BY public.con_suggested_topic.id;


--
-- Name: con_template; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_template (
    id integer NOT NULL,
    tch_id integer,
    clg_id integer,
    lesson_id integer,
    i_agree integer DEFAULT 0 NOT NULL,
    start_date character varying(200) DEFAULT NULL::character varying,
    end_date character varying(200) DEFAULT NULL::character varying,
    flag integer DEFAULT 0 NOT NULL,
    upload_date character varying(20) DEFAULT NULL::character varying,
    status character varying(100) DEFAULT NULL::character varying,
    difficulty text,
    duration text,
    presentation text,
    lp8051 text,
    lparm text,
    down_rev_les integer DEFAULT 0 NOT NULL,
    upload_rev_date character varying(256) DEFAULT NULL::character varying,
    rev_upld_date character varying(200) DEFAULT NULL::character varying,
    rev_status text,
    rev_flag integer DEFAULT 0,
    accept_reject integer DEFAULT 0 NOT NULL,
    remark text,
    plag character varying(100) DEFAULT NULL::character varying,
    reg_status integer DEFAULT 0 NOT NULL,
    agreement integer DEFAULT 0,
    reviewer_name text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT '-infinity'::timestamp without time zone NOT NULL
);


ALTER TABLE public.con_template OWNER TO postgres;

--
-- Name: COLUMN con_template.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.con_template.id IS 'identifier';


--
-- Name: con_template_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_template_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_template_id_seq OWNER TO postgres;

--
-- Name: con_template_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_template_id_seq OWNED BY public.con_template.id;


--
-- Name: con_tutorial_create; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_tutorial_create (
    id integer NOT NULL,
    tut_name character varying(100) DEFAULT NULL::character varying,
    tut_plan character varying(100) DEFAULT NULL::character varying,
    refer_content text NOT NULL,
    available integer DEFAULT 0 NOT NULL,
    tch_count integer DEFAULT 0,
    i_agree integer DEFAULT 0 NOT NULL,
    phase integer DEFAULT 0 NOT NULL,
    launch_date character varying(200) DEFAULT NULL::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at date
);


ALTER TABLE public.con_tutorial_create OWNER TO postgres;

--
-- Name: con_tutorial_create_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_tutorial_create_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_tutorial_create_id_seq OWNER TO postgres;

--
-- Name: con_tutorial_create_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_tutorial_create_id_seq OWNED BY public.con_tutorial_create.id;


--
-- Name: con_tutorial_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_tutorial_list (
    id integer NOT NULL,
    name character varying(1024) DEFAULT NULL::character varying NOT NULL,
    image_name character varying(1024) DEFAULT NULL::character varying,
    short_intro character varying(2048) DEFAULT NULL::character varying,
    intro_video_code character varying(512) DEFAULT NULL::character varying,
    available integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.con_tutorial_list OWNER TO postgres;

--
-- Name: con_tutorial_list_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_tutorial_list_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_tutorial_list_id_seq OWNER TO postgres;

--
-- Name: con_tutorial_list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_tutorial_list_id_seq OWNED BY public.con_tutorial_list.id;


--
-- Name: con_tutorial_long_content; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_tutorial_long_content (
    id integer NOT NULL,
    tut_id integer NOT NULL,
    long_intro text,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.con_tutorial_long_content OWNER TO postgres;

--
-- Name: con_tutorial_long_content_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_tutorial_long_content_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_tutorial_long_content_id_seq OWNER TO postgres;

--
-- Name: con_tutorial_long_content_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_tutorial_long_content_id_seq OWNED BY public.con_tutorial_long_content.id;


--
-- Name: con_tutorial_topics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_tutorial_topics (
    id integer NOT NULL,
    tut_id integer NOT NULL,
    display_num integer NOT NULL,
    topic_name character varying(512) DEFAULT NULL::character varying NOT NULL,
    video_code character varying(512) DEFAULT NULL::character varying,
    html_content text,
    down_code integer DEFAULT 0 NOT NULL,
    down_ppt integer DEFAULT 0 NOT NULL,
    down_misc integer DEFAULT 0 NOT NULL,
    count_ppt integer DEFAULT 0 NOT NULL,
    count_code integer DEFAULT 0 NOT NULL,
    count_misc integer DEFAULT 0 NOT NULL,
    available integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.con_tutorial_topics OWNER TO postgres;

--
-- Name: con_tutorial_topics_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_tutorial_topics_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_tutorial_topics_id_seq OWNER TO postgres;

--
-- Name: con_tutorial_topics_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_tutorial_topics_id_seq OWNED BY public.con_tutorial_topics.id;


--
-- Name: con_video_stage0; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.con_video_stage0 (
    id integer NOT NULL,
    tch_id integer,
    video_link text,
    submit_date text NOT NULL,
    status character varying(50) DEFAULT NULL::character varying NOT NULL,
    remarks text,
    flag integer,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.con_video_stage0 OWNER TO postgres;

--
-- Name: con_video_stage0_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.con_video_stage0_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.con_video_stage0_id_seq OWNER TO postgres;

--
-- Name: con_video_stage0_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.con_video_stage0_id_seq OWNED BY public.con_video_stage0.id;


--
-- Name: content_count; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.content_count (
    id integer NOT NULL,
    clg_id integer NOT NULL,
    username character varying(512) DEFAULT NULL::character varying NOT NULL,
    content integer DEFAULT 0 NOT NULL,
    down_tm integer DEFAULT 0 NOT NULL,
    down_rr integer DEFAULT 0 NOT NULL,
    down_qb integer DEFAULT 0 NOT NULL,
    down_qbs integer DEFAULT 0 NOT NULL,
    down_le integer DEFAULT 0 NOT NULL,
    down_les integer DEFAULT 0 NOT NULL,
    ie_mod integer DEFAULT 0 NOT NULL,
    down_tut_ppt integer DEFAULT 0 NOT NULL,
    down_tut_code integer DEFAULT 0 NOT NULL,
    down_tut_misc integer DEFAULT 0 NOT NULL,
    count_lecture integer DEFAULT 0 NOT NULL,
    down_project integer DEFAULT 0 NOT NULL,
    down_lesson_temp integer DEFAULT 0 NOT NULL,
    down_latex integer DEFAULT 0 NOT NULL,
    down_video_res integer DEFAULT 0 NOT NULL,
    down_stg1_temp integer DEFAULT 0 NOT NULL,
    down_res_tutorial integer DEFAULT 0 NOT NULL,
    create_content integer DEFAULT 0 NOT NULL,
    blockly integer DEFAULT 0,
    suggest integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.content_count OWNER TO postgres;

--
-- Name: content_count_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.content_count_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.content_count_id_seq OWNER TO postgres;

--
-- Name: content_count_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.content_count_id_seq OWNED BY public.content_count.id;


--
-- Name: content_register; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.content_register (
    id integer NOT NULL,
    clg_id integer,
    name text,
    email text,
    contact character varying(50) DEFAULT NULL::character varying,
    gender character varying(10) DEFAULT NULL::character varying,
    designation integer,
    department integer,
    upload character varying(40) DEFAULT NULL::character varying,
    accept_reject text,
    email_flag integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


ALTER TABLE public.content_register OWNER TO postgres;

--
-- Name: content_register_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.content_register_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.content_register_id_seq OWNER TO postgres;

--
-- Name: content_register_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.content_register_id_seq OWNED BY public.content_register.id;


--
-- Name: create_tutorial; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.create_tutorial (
    id integer NOT NULL,
    tch_id integer,
    clg_id integer,
    tut_id integer,
    i_agree integer DEFAULT 0 NOT NULL,
    start_date character varying(200) DEFAULT NULL::character varying,
    end_date character varying(200) DEFAULT NULL::character varying,
    video_link text,
    rev_video_link text,
    tut_explain text,
    flag integer DEFAULT 0 NOT NULL,
    upload_date character varying(20) DEFAULT NULL::character varying,
    status character varying(100) DEFAULT NULL::character varying,
    difficulty text,
    duration text,
    presentation text,
    lp8051 text,
    lparm text,
    down_rev_tuto integer DEFAULT 0 NOT NULL,
    upload_rev_date character varying(256) DEFAULT NULL::character varying,
    rev_upld_date character varying(200) DEFAULT NULL::character varying,
    rev_status text,
    rev_flag integer DEFAULT 0 NOT NULL,
    accept_reject integer DEFAULT 0 NOT NULL,
    remark text,
    plag character varying(100) DEFAULT NULL::character varying,
    reg_status integer DEFAULT 0 NOT NULL,
    agreement integer DEFAULT 0 NOT NULL,
    reviewer_name text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT '-infinity'::timestamp without time zone NOT NULL
);


ALTER TABLE public.create_tutorial OWNER TO postgres;

--
-- Name: COLUMN create_tutorial.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.create_tutorial.id IS 'identifier';


--
-- Name: create_tutorial_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.create_tutorial_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.create_tutorial_id_seq OWNER TO postgres;

--
-- Name: create_tutorial_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.create_tutorial_id_seq OWNED BY public.create_tutorial.id;


--
-- Name: elsi_clg_contact_dtl; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.elsi_clg_contact_dtl (
    id integer NOT NULL,
    clg_id integer NOT NULL,
    name character varying(512) DEFAULT NULL::character varying,
    emailid character varying(256) DEFAULT NULL::character varying,
    gender character varying(12) DEFAULT NULL::character varying,
    branch character varying(128) DEFAULT NULL::character varying,
    alt_email1 character varying(256) DEFAULT NULL::character varying,
    alt_email2 character varying(256) DEFAULT NULL::character varying,
    alt_email3 character varying(256) DEFAULT NULL::character varying,
    contact_num character varying(50) DEFAULT NULL::character varying,
    alt_contact1 character varying(50) DEFAULT NULL::character varying,
    alt_contact2 character varying(50) DEFAULT NULL::character varying,
    "Active" character varying(50) DEFAULT NULL::character varying,
    designation character varying(256) DEFAULT NULL::character varying,
    type integer DEFAULT 1 NOT NULL,
    modified_by character varying(100) DEFAULT NULL::character varying,
    status_cnt character varying(10) DEFAULT NULL::character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.elsi_clg_contact_dtl OWNER TO postgres;

--
-- Name: elsi_clg_contact_dtl_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.elsi_clg_contact_dtl_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.elsi_clg_contact_dtl_id_seq OWNER TO postgres;

--
-- Name: elsi_clg_contact_dtl_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.elsi_clg_contact_dtl_id_seq OWNED BY public.elsi_clg_contact_dtl.id;


--
-- Name: elsi_college_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.elsi_college_dtls (
    id integer NOT NULL,
    clg_code character varying(512) DEFAULT NULL::character varying,
    region_id integer,
    workshop_id integer DEFAULT 0 NOT NULL,
    college_name character varying(1024) DEFAULT NULL::character varying NOT NULL,
    abbreviation character varying(128) DEFAULT NULL::character varying,
    district character varying(256) DEFAULT NULL::character varying,
    address character varying(1024) DEFAULT NULL::character varying,
    state character varying(512) DEFAULT NULL::character varying,
    pincode character varying(10) DEFAULT NULL::character varying,
    college_type character varying(256) DEFAULT NULL::character varying,
    principal_meet integer DEFAULT 0 NOT NULL,
    robots_given integer DEFAULT 0,
    eyic_allowed integer DEFAULT 0 NOT NULL,
    eyrtc_allowed integer DEFAULT 0 NOT NULL,
    tbt_allowed integer DEFAULT 0 NOT NULL,
    mooc_allowed integer,
    content_allowed integer DEFAULT 0 NOT NULL,
    legal_docs integer DEFAULT 0,
    legal_docs_remarks character varying(1024) DEFAULT NULL::character varying,
    loi_status integer DEFAULT 0 NOT NULL,
    loi_format integer DEFAULT 0,
    loi_remarks character varying(1024) DEFAULT NULL::character varying,
    po_status integer DEFAULT 0,
    po_remark character varying(1024) DEFAULT NULL::character varying,
    wo_reg integer DEFAULT 0 NOT NULL,
    wo_invite integer DEFAULT 0 NOT NULL,
    wo_confirm integer DEFAULT 0 NOT NULL,
    wo_attend integer DEFAULT 0 NOT NULL,
    hardware_given character varying(1024) DEFAULT NULL::character varying,
    lab_inaugurated integer DEFAULT 0 NOT NULL,
    phase integer DEFAULT 0 NOT NULL,
    eys2016_invites integer DEFAULT 0 NOT NULL,
    team_verify integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.elsi_college_dtls OWNER TO postgres;

--
-- Name: COLUMN elsi_college_dtls.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.elsi_college_dtls.id IS 'identifier';


--
-- Name: COLUMN elsi_college_dtls.principal_meet; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.elsi_college_dtls.principal_meet IS 'tbt+lab=3,tbt=0-lab=1==1';


--
-- Name: COLUMN elsi_college_dtls.robots_given; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.elsi_college_dtls.robots_given IS 'tbt_participated+lab=1,tbt+lab=3';


--
-- Name: COLUMN elsi_college_dtls.eyrtc_allowed; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.elsi_college_dtls.eyrtc_allowed IS '1=participated,2=tbt+eyrtc complete,3=eyrtc completed';


--
-- Name: elsi_college_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.elsi_college_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.elsi_college_dtls_id_seq OWNER TO postgres;

--
-- Name: elsi_college_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.elsi_college_dtls_id_seq OWNED BY public.elsi_college_dtls.id;


--
-- Name: elsi_competitions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.elsi_competitions (
    id integer NOT NULL,
    year character varying(12) DEFAULT NULL::character varying NOT NULL,
    name character varying(256) DEFAULT NULL::character varying,
    theme character varying(256) DEFAULT NULL::character varying,
    phase integer,
    type integer,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.elsi_competitions OWNER TO postgres;

--
-- Name: COLUMN elsi_competitions.type; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.elsi_competitions.type IS '1=eYRTC,2=TBT.3=Challenge,4=eYRDC';


--
-- Name: elsi_competitions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.elsi_competitions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.elsi_competitions_id_seq OWNER TO postgres;

--
-- Name: elsi_competitions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.elsi_competitions_id_seq OWNED BY public.elsi_competitions.id;


--
-- Name: elsi_departments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.elsi_departments (
    id integer NOT NULL,
    name character varying(512) DEFAULT NULL::character varying NOT NULL,
    main_branch character varying(512) DEFAULT NULL::character varying
);


ALTER TABLE public.elsi_departments OWNER TO postgres;

--
-- Name: elsi_departments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.elsi_departments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.elsi_departments_id_seq OWNER TO postgres;

--
-- Name: elsi_departments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.elsi_departments_id_seq OWNED BY public.elsi_departments.id;


--
-- Name: elsi_designations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.elsi_designations (
    id integer NOT NULL,
    name character varying(256) DEFAULT NULL::character varying NOT NULL,
    type character varying(256) DEFAULT NULL::character varying
);


ALTER TABLE public.elsi_designations OWNER TO postgres;

--
-- Name: elsi_designations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.elsi_designations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.elsi_designations_id_seq OWNER TO postgres;

--
-- Name: elsi_designations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.elsi_designations_id_seq OWNED BY public.elsi_designations.id;


--
-- Name: elsi_emails; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.elsi_emails (
    id integer NOT NULL,
    subject character varying(2054) DEFAULT NULL::character varying NOT NULL,
    email_msg character varying(5200) DEFAULT NULL::character varying,
    img character varying(1024) DEFAULT NULL::character varying,
    pdf character varying(1024) DEFAULT NULL::character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.elsi_emails OWNER TO postgres;

--
-- Name: elsi_emails_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.elsi_emails_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.elsi_emails_id_seq OWNER TO postgres;

--
-- Name: elsi_emails_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.elsi_emails_id_seq OWNED BY public.elsi_emails.id;


--
-- Name: elsi_mooc; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.elsi_mooc (
    id integer NOT NULL,
    clg_id integer,
    clg_code character varying(200) DEFAULT NULL::character varying,
    college_name character varying(200) DEFAULT NULL::character varying,
    name character varying(200) DEFAULT NULL::character varying,
    username character varying(200) DEFAULT NULL::character varying,
    contact character varying(100) DEFAULT NULL::character varying,
    slot character varying(200) DEFAULT NULL::character varying,
    email_flag integer DEFAULT 1 NOT NULL,
    updated_at timestamp without time zone
);


ALTER TABLE public.elsi_mooc OWNER TO postgres;

--
-- Name: elsi_mooc_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.elsi_mooc_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.elsi_mooc_id_seq OWNER TO postgres;

--
-- Name: elsi_mooc_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.elsi_mooc_id_seq OWNED BY public.elsi_mooc.id;


--
-- Name: elsi_region; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.elsi_region (
    id integer NOT NULL,
    region_name character varying(512) DEFAULT NULL::character varying NOT NULL,
    type integer DEFAULT 0 NOT NULL,
    active integer DEFAULT 0 NOT NULL,
    clg_id integer,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.elsi_region OWNER TO postgres;

--
-- Name: TABLE elsi_region; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.elsi_region IS 'Stores all the regions under eLSI';


--
-- Name: COLUMN elsi_region.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.elsi_region.id IS 'Identifier';


--
-- Name: COLUMN elsi_region.region_name; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.elsi_region.region_name IS 'region name';


--
-- Name: COLUMN elsi_region.type; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.elsi_region.type IS 'type of the region, 1-NC, 2-CC';


--
-- Name: elsi_region_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.elsi_region_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.elsi_region_id_seq OWNER TO postgres;

--
-- Name: elsi_region_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.elsi_region_id_seq OWNED BY public.elsi_region.id;


--
-- Name: elsi_state; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.elsi_state (
    id integer NOT NULL,
    code character varying(6) DEFAULT NULL::character varying,
    state character varying(100) DEFAULT NULL::character varying
);


ALTER TABLE public.elsi_state OWNER TO postgres;

--
-- Name: elsi_state_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.elsi_state_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.elsi_state_id_seq OWNER TO postgres;

--
-- Name: elsi_state_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.elsi_state_id_seq OWNED BY public.elsi_state.id;


--
-- Name: elsi_students_mooc; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.elsi_students_mooc (
    id integer NOT NULL,
    name character varying(255) DEFAULT NULL::character varying,
    clg_id integer,
    emailid character varying(255) DEFAULT NULL::character varying,
    contact_num character varying(12) DEFAULT NULL::character varying,
    alt_contact1 character varying(12) DEFAULT NULL::character varying,
    department character varying(100) DEFAULT NULL::character varying,
    current_year character varying(5) DEFAULT NULL::character varying,
    mooc_allowed integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone
);


ALTER TABLE public.elsi_students_mooc OWNER TO postgres;

--
-- Name: elsi_students_mooc_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.elsi_students_mooc_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.elsi_students_mooc_id_seq OWNER TO postgres;

--
-- Name: elsi_students_mooc_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.elsi_students_mooc_id_seq OWNED BY public.elsi_students_mooc.id;


--
-- Name: elsi_teachers_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.elsi_teachers_dtls (
    id integer NOT NULL,
    user_id integer,
    clg_id integer,
    name character varying(512) DEFAULT NULL::character varying,
    emailid character varying(256) DEFAULT NULL::character varying,
    alt_email1 character varying(256) DEFAULT NULL::character varying,
    alt_email2 character varying(256) DEFAULT NULL::character varying,
    contact_num character varying(25) DEFAULT NULL::character varying,
    alt_contact1 character varying(50) DEFAULT NULL::character varying,
    department character varying(128) DEFAULT NULL::character varying,
    designation character varying(30) DEFAULT NULL::character varying,
    gender character varying(15) DEFAULT NULL::character varying,
    coor_flag integer DEFAULT 0 NOT NULL,
    wo_flag integer DEFAULT 0 NOT NULL,
    mooc_allowed integer,
    workshop_id integer DEFAULT 0 NOT NULL,
    wo_attendee integer DEFAULT 0 NOT NULL,
    wo_count integer DEFAULT 0 NOT NULL,
    eyrtc_flag integer DEFAULT 0 NOT NULL,
    tbt_flag integer DEFAULT 0 NOT NULL,
    eyic_flag integer DEFAULT 0 NOT NULL,
    content_flag integer,
    "Status" character varying(150) DEFAULT NULL::character varying,
    status_flag integer,
    modified_by character varying(100) DEFAULT NULL::character varying,
    elsi_flag integer,
    remarks character varying(150) DEFAULT NULL::character varying,
    login_created integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.elsi_teachers_dtls OWNER TO postgres;

--
-- Name: COLUMN elsi_teachers_dtls.elsi_flag; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.elsi_teachers_dtls.elsi_flag IS '1: Coordinator, 2: Member';


--
-- Name: elsi_teachers_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.elsi_teachers_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.elsi_teachers_dtls_id_seq OWNER TO postgres;

--
-- Name: elsi_teachers_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.elsi_teachers_dtls_id_seq OWNED BY public.elsi_teachers_dtls.id;


--
-- Name: eyantra_cert_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eyantra_cert_dtls (
    id integer NOT NULL,
    workshop_id integer,
    tch_id integer,
    cert_num character varying(200) DEFAULT NULL::character varying,
    cert_date character varying(25) DEFAULT NULL::character varying,
    generated_at character varying(100) DEFAULT NULL::character varying,
    remarks character varying(10) DEFAULT NULL::character varying,
    type character varying(10) DEFAULT NULL::character varying,
    year integer,
    eyrtc_id integer,
    eyic_id character varying(10) DEFAULT NULL::character varying
);


ALTER TABLE public.eyantra_cert_dtls OWNER TO postgres;

--
-- Name: eyantra_cert_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.eyantra_cert_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eyantra_cert_dtls_id_seq OWNER TO postgres;

--
-- Name: eyantra_cert_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eyantra_cert_dtls_id_seq OWNED BY public.eyantra_cert_dtls.id;


--
-- Name: eyrtc_participation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eyrtc_participation (
    id integer NOT NULL,
    clg_id integer NOT NULL,
    comp_id integer NOT NULL,
    tl_id integer NOT NULL,
    tm1_id integer,
    tm2_id integer,
    tm3_id integer,
    year character varying(4) DEFAULT NULL::character varying NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.eyrtc_participation OWNER TO postgres;

--
-- Name: eyrtc_participation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.eyrtc_participation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eyrtc_participation_id_seq OWNER TO postgres;

--
-- Name: eyrtc_participation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eyrtc_participation_id_seq OWNED BY public.eyrtc_participation.id;


--
-- Name: eyrtc_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eyrtc_status (
    id integer NOT NULL,
    part_id integer NOT NULL,
    task0_uploaded integer DEFAULT 0 NOT NULL,
    task0_date timestamp without time zone,
    task0_file_name character varying(200) DEFAULT NULL::character varying,
    task0_marks real,
    task0_remark character varying(1024) DEFAULT NULL::character varying,
    task1_uploaded integer DEFAULT 0 NOT NULL,
    task1_date timestamp without time zone,
    task1_link character varying(1024) DEFAULT NULL::character varying,
    task1_marks real,
    task1_remark character varying(1024) DEFAULT NULL::character varying,
    task2_uploaded integer DEFAULT 0 NOT NULL,
    task2_date timestamp without time zone,
    task2_link1 character varying(2048) DEFAULT NULL::character varying,
    task2_link2 character varying(2048) DEFAULT NULL::character varying,
    task2_marks real,
    task2_remark character varying(1024) DEFAULT NULL::character varying,
    taskvideo_uploaded integer DEFAULT 0 NOT NULL,
    taskvideo_date timestamp without time zone,
    taskvideo_link character varying(2048) DEFAULT NULL::character varying,
    taskvideo_marks real,
    taskvideo_remark character varying(1024) DEFAULT NULL::character varying,
    taskcode_uploaded integer DEFAULT 0 NOT NULL,
    taskcode_date timestamp without time zone,
    taskcode_marks real,
    taskcode_remark character varying(1024) DEFAULT NULL::character varying,
    final_validatory_marks integer,
    final_validatory_remarks character varying(1024) DEFAULT NULL::character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.eyrtc_status OWNER TO postgres;

--
-- Name: eyrtc_status_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.eyrtc_status_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eyrtc_status_id_seq OWNER TO postgres;

--
-- Name: eyrtc_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eyrtc_status_id_seq OWNED BY public.eyrtc_status.id;


--
-- Name: eys_registration_2016; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eys_registration_2016 (
    id integer NOT NULL,
    part_id integer NOT NULL,
    clg_id integer NOT NULL,
    team_id character varying(2056) DEFAULT NULL::character varying,
    name character varying(512) DEFAULT NULL::character varying,
    emailid character varying(256) DEFAULT NULL::character varying,
    contact_num character varying(25) DEFAULT NULL::character varying,
    role character varying(30) DEFAULT NULL::character varying,
    gender character varying(15) DEFAULT NULL::character varying,
    arrival_date character varying(256) DEFAULT NULL::character varying,
    departure_date character varying(256) DEFAULT NULL::character varying,
    elsi_coor integer DEFAULT 0 NOT NULL,
    elsi_competition integer DEFAULT 0,
    category character varying(512) DEFAULT NULL::character varying,
    accommodation character varying(512) DEFAULT NULL::character varying,
    attendence character varying(512) DEFAULT NULL::character varying,
    reached_venue integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.eys_registration_2016 OWNER TO postgres;

--
-- Name: eys_registration_2016_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.eys_registration_2016_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eys_registration_2016_id_seq OWNER TO postgres;

--
-- Name: eys_registration_2016_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eys_registration_2016_id_seq OWNED BY public.eys_registration_2016.id;


--
-- Name: eys_registration_2017; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eys_registration_2017 (
    id integer NOT NULL,
    part_id integer NOT NULL,
    clg_id integer NOT NULL,
    team_id character varying(2056) DEFAULT NULL::character varying,
    name character varying(512) DEFAULT NULL::character varying,
    emailid character varying(256) DEFAULT NULL::character varying,
    contact_num character varying(25) DEFAULT NULL::character varying,
    role character varying(30) DEFAULT NULL::character varying,
    gender character varying(15) DEFAULT NULL::character varying,
    arrival_date character varying(256) DEFAULT NULL::character varying,
    arrival_time character varying(250) DEFAULT NULL::character varying,
    departure_date character varying(256) DEFAULT NULL::character varying,
    elsi_coor integer DEFAULT 0 NOT NULL,
    elsi_competition integer DEFAULT 0,
    category character varying(512) DEFAULT NULL::character varying,
    accommodation character varying(512) DEFAULT NULL::character varying,
    attendence character varying(512) DEFAULT NULL::character varying,
    account_number character varying(512) DEFAULT NULL::character varying,
    account_holder_name character varying(512) DEFAULT NULL::character varying,
    bank_name character varying(512) DEFAULT NULL::character varying,
    bank_address character varying(512) DEFAULT NULL::character varying,
    account_type character varying(512) DEFAULT NULL::character varying,
    "IFSC_code" character varying(512) DEFAULT NULL::character varying,
    reached_venue integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.eys_registration_2017 OWNER TO postgres;

--
-- Name: eys_registration_2017_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.eys_registration_2017_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eys_registration_2017_id_seq OWNER TO postgres;

--
-- Name: eys_registration_2017_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eys_registration_2017_id_seq OWNED BY public.eys_registration_2017.id;


--
-- Name: eys_registration_2018; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eys_registration_2018 (
    id integer NOT NULL,
    part_id integer NOT NULL,
    clg_id integer NOT NULL,
    team_id character varying(2056) DEFAULT NULL::character varying,
    name character varying(512) DEFAULT NULL::character varying,
    emailid character varying(256) DEFAULT NULL::character varying,
    contact_num character varying(25) DEFAULT NULL::character varying,
    role character varying(30) DEFAULT NULL::character varying,
    gender character varying(15) DEFAULT NULL::character varying,
    arrival_date character varying(256) DEFAULT NULL::character varying,
    arrival_time character varying(250) DEFAULT NULL::character varying,
    departure_date character varying(256) DEFAULT NULL::character varying,
    elsi_coor integer DEFAULT 0 NOT NULL,
    elsi_competition integer DEFAULT 0,
    category character varying(512) DEFAULT NULL::character varying,
    accommodation character varying(512) DEFAULT NULL::character varying,
    attendence character varying(512) DEFAULT NULL::character varying,
    account_number character varying(512) DEFAULT NULL::character varying,
    account_holder_name character varying(512) DEFAULT NULL::character varying,
    bank_name character varying(512) DEFAULT NULL::character varying,
    bank_address character varying(512) DEFAULT NULL::character varying,
    account_type character varying(512) DEFAULT NULL::character varying,
    "IFSC_code" character varying(512) DEFAULT NULL::character varying,
    reached_venue integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.eys_registration_2018 OWNER TO postgres;

--
-- Name: eys_registration_2018_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.eys_registration_2018_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eys_registration_2018_id_seq OWNER TO postgres;

--
-- Name: eys_registration_2018_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eys_registration_2018_id_seq OWNED BY public.eys_registration_2018.id;


--
-- Name: eys_registration_2019; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eys_registration_2019 (
    id integer NOT NULL,
    part_id integer DEFAULT 0 NOT NULL,
    clg_id integer,
    team_id character varying(2056) DEFAULT NULL::character varying,
    name character varying(512) DEFAULT NULL::character varying,
    emailid character varying(256) DEFAULT NULL::character varying,
    contact_num character varying(25) DEFAULT NULL::character varying,
    role character varying(30) DEFAULT NULL::character varying,
    gender character varying(15) DEFAULT NULL::character varying,
    arrival_date character varying(256) DEFAULT NULL::character varying,
    arrival_time character varying(250) DEFAULT NULL::character varying,
    departure_date character varying(256) DEFAULT NULL::character varying,
    elsi_coor integer DEFAULT 0 NOT NULL,
    elsi_competition integer DEFAULT 0,
    category character varying(512) DEFAULT NULL::character varying,
    accommodation character varying(512) DEFAULT NULL::character varying,
    attendence character varying(512) DEFAULT NULL::character varying,
    account_number character varying(512) DEFAULT NULL::character varying,
    account_holder_name character varying(512) DEFAULT NULL::character varying,
    bank_name character varying(512) DEFAULT NULL::character varying,
    bank_address character varying(512) DEFAULT NULL::character varying,
    account_type character varying(512) DEFAULT NULL::character varying,
    "IFSC_code" character varying(512) DEFAULT NULL::character varying,
    reached_venue integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.eys_registration_2019 OWNER TO postgres;

--
-- Name: eys_registration_2019_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.eys_registration_2019_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eys_registration_2019_id_seq OWNER TO postgres;

--
-- Name: eys_registration_2019_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eys_registration_2019_id_seq OWNED BY public.eys_registration_2019.id;


--
-- Name: eys_registration_2020; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eys_registration_2020 (
    id integer NOT NULL,
    part_id integer DEFAULT 0 NOT NULL,
    clg_id integer,
    team_id character varying(2056) DEFAULT NULL::character varying,
    name character varying(512) DEFAULT NULL::character varying,
    emailid character varying(256) DEFAULT NULL::character varying,
    contact_num character varying(25) DEFAULT NULL::character varying,
    role character varying(30) DEFAULT NULL::character varying,
    gender character varying(15) DEFAULT NULL::character varying,
    arrival_date character varying(256) DEFAULT NULL::character varying,
    arrival_time character varying(250) DEFAULT NULL::character varying,
    departure_date character varying(256) DEFAULT NULL::character varying,
    elsi_coor integer DEFAULT 0 NOT NULL,
    elsi_competition integer DEFAULT 0,
    category character varying(512) DEFAULT NULL::character varying,
    accommodation character varying(512) DEFAULT NULL::character varying,
    attendence character varying(512) DEFAULT NULL::character varying,
    account_number character varying(512) DEFAULT NULL::character varying,
    account_holder_name character varying(512) DEFAULT NULL::character varying,
    bank_name character varying(512) DEFAULT NULL::character varying,
    bank_address character varying(512) DEFAULT NULL::character varying,
    account_type character varying(512) DEFAULT NULL::character varying,
    "IFSC_code" character varying(512) DEFAULT NULL::character varying,
    reached_venue integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.eys_registration_2020 OWNER TO postgres;

--
-- Name: eys_registration_2020_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.eys_registration_2020_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eys_registration_2020_id_seq OWNER TO postgres;

--
-- Name: eys_registration_2020_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eys_registration_2020_id_seq OWNED BY public.eys_registration_2020.id;


--
-- Name: eysip_conduct; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eysip_conduct (
    id integer NOT NULL,
    stud_name character varying(100) DEFAULT NULL::character varying,
    email character varying(100) DEFAULT NULL::character varying,
    photograph character varying(100) DEFAULT NULL::character varying,
    pancard character varying(100) DEFAULT NULL::character varying,
    signature character varying(100) DEFAULT NULL::character varying,
    conduct integer,
    proj_id integer,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone
);


ALTER TABLE public.eysip_conduct OWNER TO postgres;

--
-- Name: eysip_conduct_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.eysip_conduct_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eysip_conduct_id_seq OWNER TO postgres;

--
-- Name: eysip_conduct_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eysip_conduct_id_seq OWNED BY public.eysip_conduct.id;


--
-- Name: ie_modules; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ie_modules (
    id integer NOT NULL,
    name character varying(1024) DEFAULT NULL::character varying NOT NULL,
    image_name character varying(1024) DEFAULT NULL::character varying,
    short_intro character varying(2048) DEFAULT NULL::character varying,
    video_code character varying(512) DEFAULT NULL::character varying,
    down_pdf character varying(1024) DEFAULT NULL::character varying,
    available integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.ie_modules OWNER TO postgres;

--
-- Name: ie_modules_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ie_modules_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ie_modules_id_seq OWNER TO postgres;

--
-- Name: ie_modules_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ie_modules_id_seq OWNED BY public.ie_modules.id;


--
-- Name: login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login (
    id bigint NOT NULL,
    name character varying(100) DEFAULT NULL::character varying,
    team_id integer NOT NULL,
    team_member_id integer NOT NULL,
    username character varying(100) DEFAULT NULL::character varying NOT NULL,
    password character varying(1024) DEFAULT NULL::character varying NOT NULL,
    role integer DEFAULT 0 NOT NULL,
    active integer DEFAULT 0 NOT NULL,
    theme character varying(20) DEFAULT NULL::character varying,
    email_flag integer,
    last_login timestamp without time zone DEFAULT '-infinity'::timestamp without time zone NOT NULL,
    login_count integer DEFAULT 0 NOT NULL,
    change_count integer DEFAULT 0 NOT NULL,
    forgot_count integer DEFAULT 0 NOT NULL,
    remember_token character varying(1024) DEFAULT NULL::character varying,
    verify_token character varying(100) DEFAULT NULL::character varying,
    token character varying(1024) DEFAULT NULL::character varying,
    email_verified_at timestamp without time zone,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.login OWNER TO postgres;

--
-- Name: login_emails; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login_emails (
    id bigint NOT NULL,
    name character varying(100) DEFAULT NULL::character varying,
    team_id integer,
    team_member_id integer,
    username character varying(100) DEFAULT NULL::character varying,
    password character varying(1024) DEFAULT NULL::character varying,
    role integer DEFAULT 0 NOT NULL,
    active integer DEFAULT 0 NOT NULL,
    theme character varying(20) DEFAULT NULL::character varying,
    email_flag integer,
    last_login timestamp without time zone,
    login_count integer DEFAULT 0 NOT NULL,
    change_count integer DEFAULT 0 NOT NULL,
    forgot_count integer DEFAULT 0 NOT NULL,
    remember_token character varying(1024) DEFAULT NULL::character varying,
    verify_token character varying(100) DEFAULT NULL::character varying,
    token character varying(1024) DEFAULT NULL::character varying,
    email_verified_at timestamp without time zone,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.login_emails OWNER TO postgres;

--
-- Name: login_emails_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.login_emails_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.login_emails_id_seq OWNER TO postgres;

--
-- Name: login_emails_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.login_emails_id_seq OWNED BY public.login_emails.id;


--
-- Name: login_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.login_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.login_id_seq OWNER TO postgres;

--
-- Name: login_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.login_id_seq OWNED BY public.login.id;


--
-- Name: mooc_colleges; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mooc_colleges (
    id integer NOT NULL,
    clg_id integer,
    tch_email character varying(200) DEFAULT NULL::character varying,
    students integer,
    updated_at timestamp without time zone
);


ALTER TABLE public.mooc_colleges OWNER TO postgres;

--
-- Name: mooc_colleges_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.mooc_colleges_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mooc_colleges_id_seq OWNER TO postgres;

--
-- Name: mooc_colleges_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.mooc_colleges_id_seq OWNED BY public.mooc_colleges.id;


--
-- Name: online_lab_inauguration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.online_lab_inauguration (
    id integer NOT NULL,
    clg_id integer NOT NULL,
    labinaug_date character varying(25) DEFAULT NULL::character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.online_lab_inauguration OWNER TO postgres;

--
-- Name: online_lab_inauguration_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.online_lab_inauguration_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.online_lab_inauguration_id_seq OWNER TO postgres;

--
-- Name: online_lab_inauguration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.online_lab_inauguration_id_seq OWNED BY public.online_lab_inauguration.id;


--
-- Name: principal_meet_attendee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.principal_meet_attendee (
    id integer NOT NULL,
    principal_meet_id integer,
    clg_id integer,
    name character varying(512) DEFAULT NULL::character varying,
    emailid character varying(250) DEFAULT NULL::character varying,
    contact_num character varying(100) DEFAULT NULL::character varying,
    alt_contact1 integer,
    gender character varying(16) DEFAULT NULL::character varying,
    designation character varying(512) DEFAULT NULL::character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.principal_meet_attendee OWNER TO postgres;

--
-- Name: principal_meet_attendee_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.principal_meet_attendee_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.principal_meet_attendee_id_seq OWNER TO postgres;

--
-- Name: principal_meet_attendee_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.principal_meet_attendee_id_seq OWNED BY public.principal_meet_attendee.id;


--
-- Name: principal_meet_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.principal_meet_dtls (
    id integer NOT NULL,
    region_id integer,
    clg_id integer,
    active integer DEFAULT 0 NOT NULL,
    start_date date
);


ALTER TABLE public.principal_meet_dtls OWNER TO postgres;

--
-- Name: principal_meet_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.principal_meet_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.principal_meet_dtls_id_seq OWNER TO postgres;

--
-- Name: principal_meet_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.principal_meet_dtls_id_seq OWNED BY public.principal_meet_dtls.id;


--
-- Name: principal_meet_participants; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.principal_meet_participants (
    id integer NOT NULL,
    principal_meet_id integer,
    data_table_id integer,
    clg_id integer,
    clg_contact_id integer NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.principal_meet_participants OWNER TO postgres;

--
-- Name: COLUMN principal_meet_participants.data_table_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.principal_meet_participants.data_table_id IS 'clg_contact_dtls = 1, principal_meet_attendee = 2';


--
-- Name: principal_meet_participants_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.principal_meet_participants_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.principal_meet_participants_id_seq OWNER TO postgres;

--
-- Name: principal_meet_participants_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.principal_meet_participants_id_seq OWNED BY public.principal_meet_participants.id;


--
-- Name: regional_finals_invite; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.regional_finals_invite (
    id integer NOT NULL,
    state character varying(100) DEFAULT NULL::character varying,
    college_name character varying(100) DEFAULT NULL::character varying,
    district character varying(300) DEFAULT NULL::character varying,
    regional character varying(100) DEFAULT NULL::character varying,
    name character varying(100) DEFAULT NULL::character varying,
    designation character varying(100) DEFAULT NULL::character varying,
    email character varying(100) DEFAULT NULL::character varying,
    contact character varying(100) DEFAULT NULL::character varying,
    attendees integer,
    lunch character varying(10) DEFAULT NULL::character varying,
    created_at date,
    updated_at date
);


ALTER TABLE public.regional_finals_invite OWNER TO postgres;

--
-- Name: regional_finals_invite_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.regional_finals_invite_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.regional_finals_invite_id_seq OWNER TO postgres;

--
-- Name: regional_finals_invite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.regional_finals_invite_id_seq OWNED BY public.regional_finals_invite.id;


--
-- Name: regional_finals_invite_to_be_sent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.regional_finals_invite_to_be_sent (
    id integer NOT NULL,
    college_name character varying(512) DEFAULT NULL::character varying,
    name character varying(512) DEFAULT NULL::character varying,
    designation character varying(512) DEFAULT NULL::character varying,
    email character varying(512) DEFAULT NULL::character varying,
    venue character varying(512) DEFAULT NULL::character varying,
    day2 character varying(512) DEFAULT NULL::character varying,
    daydate character varying(512) DEFAULT NULL::character varying,
    subject character varying(200) DEFAULT NULL::character varying NOT NULL,
    attach character varying(200) DEFAULT NULL::character varying NOT NULL,
    rsvpname character varying(100) DEFAULT NULL::character varying NOT NULL,
    rsvpemail character varying(100) DEFAULT NULL::character varying NOT NULL,
    rsvpcontact character varying(100) DEFAULT NULL::character varying NOT NULL,
    created_at date,
    updated_at date
);


ALTER TABLE public.regional_finals_invite_to_be_sent OWNER TO postgres;

--
-- Name: regional_finals_invite_to_be_sent_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.regional_finals_invite_to_be_sent_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.regional_finals_invite_to_be_sent_id_seq OWNER TO postgres;

--
-- Name: regional_finals_invite_to_be_sent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.regional_finals_invite_to_be_sent_id_seq OWNED BY public.regional_finals_invite_to_be_sent.id;


--
-- Name: talks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.talks (
    id integer NOT NULL,
    name character varying(1024) DEFAULT NULL::character varying,
    title text,
    image character varying(1024) DEFAULT NULL::character varying,
    image_alt character varying(128) DEFAULT NULL::character varying,
    short_intro text,
    visited_lecture integer DEFAULT 0 NOT NULL,
    available smallint NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.talks OWNER TO postgres;

--
-- Name: talks_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.talks_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.talks_id_seq OWNER TO postgres;

--
-- Name: talks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.talks_id_seq OWNED BY public.talks.id;


--
-- Name: talks_series; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.talks_series (
    id integer NOT NULL,
    display integer,
    image character varying(512) DEFAULT NULL::character varying,
    img_url character varying(512) DEFAULT NULL::character varying,
    available smallint NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.talks_series OWNER TO postgres;

--
-- Name: talks_series_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.talks_series_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.talks_series_id_seq OWNER TO postgres;

--
-- Name: talks_series_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.talks_series_id_seq OWNED BY public.talks_series.id;


--
-- Name: tbt_challenge_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_challenge_status (
    id integer NOT NULL,
    part_id integer NOT NULL,
    i_agree_challenge integer DEFAULT 0 NOT NULL,
    task1_uploaded integer DEFAULT 0 NOT NULL,
    task1_upload_time timestamp without time zone NOT NULL,
    task1_file_name character varying(64) DEFAULT NULL::character varying,
    task1_marks real,
    task1_remark character varying(1024) DEFAULT NULL::character varying,
    task2_uploaded integer DEFAULT 0 NOT NULL,
    task2_video_link character varying(256) DEFAULT NULL::character varying,
    task2_upload_time timestamp without time zone,
    task2_code_uploaded integer DEFAULT 0 NOT NULL,
    task2_code_upload_time timestamp without time zone,
    task2_marks real,
    task2_remark character varying(1024) DEFAULT NULL::character varying,
    challenge_result integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_challenge_status OWNER TO postgres;

--
-- Name: tbt_challenge_status_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_challenge_status_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_challenge_status_id_seq OWNER TO postgres;

--
-- Name: tbt_challenge_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_challenge_status_id_seq OWNED BY public.tbt_challenge_status.id;


--
-- Name: tbt_feedback; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_feedback (
    id integer NOT NULL,
    clg_id integer NOT NULL,
    usr_id integer NOT NULL,
    teacher_name character varying(1024) DEFAULT NULL::character varying NOT NULL,
    email_id character varying(1024) DEFAULT NULL::character varying,
    question1 text,
    question2 text,
    question3 text,
    question4 text,
    question5 text,
    question6 text,
    question7 character varying(8192) DEFAULT NULL::character varying,
    question8 character varying(8192) DEFAULT NULL::character varying,
    question9 character varying(8192) DEFAULT NULL::character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.tbt_feedback OWNER TO postgres;

--
-- Name: tbt_feedback_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_feedback_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_feedback_id_seq OWNER TO postgres;

--
-- Name: tbt_feedback_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_feedback_id_seq OWNED BY public.tbt_feedback.id;


--
-- Name: tbt_participation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_participation (
    id integer NOT NULL,
    clg_id integer NOT NULL,
    tbt_phase integer NOT NULL,
    tl_id integer NOT NULL,
    tm1_id integer,
    tm2_id integer,
    tm3_id integer,
    year character varying(4) DEFAULT NULL::character varying NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_participation OWNER TO postgres;

--
-- Name: tbt_participation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_participation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_participation_id_seq OWNER TO postgres;

--
-- Name: tbt_participation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_participation_id_seq OWNED BY public.tbt_participation.id;


--
-- Name: tbt_ques_ans_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_ques_ans_dtls (
    id integer NOT NULL,
    clg_id integer,
    part_id integer,
    ques_1 integer,
    ques_2 integer,
    ques_3 integer,
    ques_4 integer,
    ques_5 character varying(1024) DEFAULT NULL::character varying,
    task integer,
    marks real,
    bonus integer,
    total_marks real,
    save_count integer DEFAULT 0,
    submit integer DEFAULT 0,
    submit_time timestamp without time zone,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT '-infinity'::timestamp without time zone NOT NULL
);


ALTER TABLE public.tbt_ques_ans_dtls OWNER TO postgres;

--
-- Name: tbt_ques_ans_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_ques_ans_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_ques_ans_dtls_id_seq OWNER TO postgres;

--
-- Name: tbt_ques_ans_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_ques_ans_dtls_id_seq OWNED BY public.tbt_ques_ans_dtls.id;


--
-- Name: tbt_question_master; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_question_master (
    id integer NOT NULL,
    question integer,
    option_1 integer,
    option_2 integer,
    option_3 integer,
    option_4 integer,
    option_5 integer,
    correct_option integer,
    task integer,
    type integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.tbt_question_master OWNER TO postgres;

--
-- Name: tbt_question_master_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_question_master_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_question_master_id_seq OWNER TO postgres;

--
-- Name: tbt_question_master_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_question_master_id_seq OWNED BY public.tbt_question_master.id;


--
-- Name: tbt_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_status (
    id integer NOT NULL,
    part_id integer NOT NULL,
    task1_uploaded integer DEFAULT 0 NOT NULL,
    task1_upload_time timestamp without time zone NOT NULL,
    task1_marks real,
    task1_remark character varying(1024) DEFAULT NULL::character varying,
    task2_uploaded integer DEFAULT 0 NOT NULL,
    task2_upload_time timestamp without time zone,
    task2_marks real,
    task2_remark character varying(1024) DEFAULT NULL::character varying,
    task3_uploaded integer DEFAULT 0 NOT NULL,
    task3_upload_time timestamp without time zone NOT NULL,
    task3_marks real,
    task3_remark character varying(1024) DEFAULT NULL::character varying,
    task4_uploaded integer DEFAULT 0 NOT NULL,
    task4_upload_time timestamp without time zone NOT NULL,
    task4_marks real,
    task4_remark character varying(1024) DEFAULT NULL::character varying,
    task5_uploaded integer DEFAULT 0 NOT NULL,
    task5_upload_time timestamp without time zone NOT NULL,
    task5_marks real,
    task5_remark character varying(1024) DEFAULT NULL::character varying,
    task6_uploaded integer DEFAULT 0 NOT NULL,
    task6_upload_time timestamp without time zone NOT NULL,
    task6_marks real,
    task6_remark character varying(1024) DEFAULT NULL::character varying,
    award_grade character varying(64) DEFAULT NULL::character varying,
    names_ok integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_status OWNER TO postgres;

--
-- Name: tbt_status_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_status_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_status_id_seq OWNER TO postgres;

--
-- Name: tbt_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_status_id_seq OWNED BY public.tbt_status.id;


--
-- Name: tbt_temp_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_temp_data (
    id integer NOT NULL,
    region_id integer,
    college_name character varying(1024) DEFAULT NULL::character varying,
    abbreviated character varying(32) DEFAULT NULL::character varying,
    district character varying(512) DEFAULT NULL::character varying,
    state character varying(64) DEFAULT NULL::character varying,
    pincode character varying(8) DEFAULT NULL::character varying,
    polytech integer,
    principal_name character varying(256) DEFAULT NULL::character varying,
    principal_contact character varying(16) DEFAULT NULL::character varying,
    principal_email character varying(256) DEFAULT NULL::character varying,
    college_address character varying(2048) DEFAULT NULL::character varying,
    tm1_name character varying(256) DEFAULT NULL::character varying,
    tm1_email character varying(256) DEFAULT NULL::character varying,
    tm1_contact bigint,
    tm1_role integer,
    tm1_wrk integer,
    tm2_name character varying(256) DEFAULT NULL::character varying,
    tm2_email character varying(256) DEFAULT NULL::character varying,
    tm2_contact bigint,
    tm2_role integer,
    tm2_wrk integer,
    tm3_name character varying(256) DEFAULT NULL::character varying,
    tm3_email character varying(256) DEFAULT NULL::character varying,
    tm3_contact bigint,
    tm3_role integer,
    tm3_wrk integer,
    tm4_name character varying(256) DEFAULT NULL::character varying,
    tm4_email character varying(256) DEFAULT NULL::character varying,
    tm4_contact bigint,
    tm4_role integer,
    tm4_wrk integer,
    tm5_name character varying(256) DEFAULT NULL::character varying,
    tm5_email character varying(256) DEFAULT NULL::character varying,
    tm5_contact bigint,
    tm5_role integer,
    tm5_wrk integer,
    loi_status integer,
    robots_given integer,
    login_allowed integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.tbt_temp_data OWNER TO postgres;

--
-- Name: tbt_temp_data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_temp_data_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_temp_data_id_seq OWNER TO postgres;

--
-- Name: tbt_temp_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_temp_data_id_seq OWNED BY public.tbt_temp_data.id;


--
-- Name: team_email; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.team_email (
    id bigint NOT NULL,
    team_id bigint NOT NULL,
    name character varying(100) DEFAULT NULL::character varying NOT NULL,
    email character varying(100) DEFAULT NULL::character varying NOT NULL,
    contact character varying(15) DEFAULT NULL::character varying NOT NULL,
    discipline_id integer,
    department_id integer,
    year integer,
    gender character varying(6) DEFAULT NULL::character varying,
    address character varying(1000) DEFAULT NULL::character varying,
    role integer NOT NULL,
    eyrc_year character varying(1024) DEFAULT NULL::character varying,
    eyrc_theme character varying(1024) DEFAULT NULL::character varying,
    eyrc_cert character varying(1024) DEFAULT NULL::character varying,
    tracking character varying(250) DEFAULT NULL::character varying,
    dispatch_date text,
    email_flag integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.team_email OWNER TO postgres;

--
-- Name: team_email_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.team_email_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.team_email_id_seq OWNER TO postgres;

--
-- Name: team_email_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.team_email_id_seq OWNED BY public.team_email.id;


--
-- Name: team_member_detail; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.team_member_detail (
    id bigint NOT NULL,
    email character varying(100) DEFAULT NULL::character varying NOT NULL,
    flag integer,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.team_member_detail OWNER TO postgres;

--
-- Name: team_member_detail_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.team_member_detail_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.team_member_detail_id_seq OWNER TO postgres;

--
-- Name: team_member_detail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.team_member_detail_id_seq OWNED BY public.team_member_detail.id;


--
-- Name: temp_college; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.temp_college (
    id integer NOT NULL,
    clg_id integer,
    region_id integer NOT NULL,
    college_name character varying(256) DEFAULT NULL::character varying NOT NULL,
    address character varying(1024) DEFAULT NULL::character varying,
    principal_meet integer DEFAULT 0 NOT NULL,
    work_shop integer DEFAULT 0 NOT NULL,
    current_stat integer,
    "PrincipalName" character varying(512) DEFAULT NULL::character varying,
    "P_Number" character varying(256) DEFAULT NULL::character varying,
    "P_Number2" character varying(256) DEFAULT NULL::character varying,
    "P_emailID" character varying(512) DEFAULT NULL::character varying,
    loi_status integer DEFAULT 0 NOT NULL,
    college_updated integer,
    created_at timestamp without time zone DEFAULT '-infinity'::timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.temp_college OWNER TO postgres;

--
-- Name: temp_college_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.temp_college_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.temp_college_id_seq OWNER TO postgres;

--
-- Name: temp_college_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.temp_college_id_seq OWNED BY public.temp_college.id;


--
-- Name: temp_elsi_college_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.temp_elsi_college_dtls (
    id integer DEFAULT 0 NOT NULL,
    clg_code character varying(512) DEFAULT NULL::character varying,
    region_id integer,
    workshop_id integer DEFAULT 0 NOT NULL,
    college_name character varying(1024) DEFAULT NULL::character varying NOT NULL,
    abbreviation character varying(128) DEFAULT NULL::character varying,
    district character varying(256) DEFAULT NULL::character varying,
    address character varying(1024) DEFAULT NULL::character varying,
    state character varying(512) DEFAULT NULL::character varying,
    pincode character varying(10) DEFAULT NULL::character varying,
    college_type character varying(256) DEFAULT NULL::character varying,
    principal_meet integer DEFAULT 0 NOT NULL,
    robots_given integer DEFAULT 0,
    eyic_allowed integer DEFAULT 0 NOT NULL,
    eyrtc_allowed integer DEFAULT 0 NOT NULL,
    tbt_allowed integer DEFAULT 0 NOT NULL,
    content_allowed integer DEFAULT 0 NOT NULL,
    legal_docs integer DEFAULT 0,
    legal_docs_remarks character varying(1024) DEFAULT NULL::character varying,
    loi_status integer DEFAULT 0 NOT NULL,
    loi_format integer DEFAULT 0,
    loi_remarks character varying(1024) DEFAULT NULL::character varying,
    po_status integer DEFAULT 0,
    po_remark character varying(1024) DEFAULT NULL::character varying,
    wo_reg integer DEFAULT 0 NOT NULL,
    wo_invite integer DEFAULT 0 NOT NULL,
    wo_confirm integer DEFAULT 0 NOT NULL,
    wo_attend integer DEFAULT 0 NOT NULL,
    hardware_given character varying(1024) DEFAULT NULL::character varying,
    lab_inaugurated integer DEFAULT 0 NOT NULL,
    phase integer DEFAULT 0 NOT NULL,
    eys2016_invites integer DEFAULT 0 NOT NULL,
    team_verify integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.temp_elsi_college_dtls OWNER TO postgres;

--
-- Name: COLUMN temp_elsi_college_dtls.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.temp_elsi_college_dtls.id IS 'identifier';


--
-- Name: COLUMN temp_elsi_college_dtls.principal_meet; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.temp_elsi_college_dtls.principal_meet IS 'tbt+lab=3,tbt=0-lab=1==1';


--
-- Name: COLUMN temp_elsi_college_dtls.robots_given; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.temp_elsi_college_dtls.robots_given IS 'tbt_participated+lab=1,tbt+lab=3';


--
-- Name: COLUMN temp_elsi_college_dtls.eyrtc_allowed; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.temp_elsi_college_dtls.eyrtc_allowed IS '1=participated,2=tbt+eyrtc complete,3=eyrtc completed';


--
-- Name: temp_principal_meet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.temp_principal_meet (
    id integer NOT NULL,
    region_id integer NOT NULL,
    temp_clg_id integer,
    name character varying(512) DEFAULT NULL::character varying,
    email character varying(250) DEFAULT NULL::character varying,
    contact_num character varying(100) DEFAULT NULL::character varying,
    alt_contact_num1 integer,
    designation character varying(512) DEFAULT NULL::character varying,
    clg_type character varying(250) DEFAULT NULL::character varying,
    created_at timestamp without time zone DEFAULT '-infinity'::timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.temp_principal_meet OWNER TO postgres;

--
-- Name: temp_principal_meet_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.temp_principal_meet_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.temp_principal_meet_id_seq OWNER TO postgres;

--
-- Name: temp_principal_meet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.temp_principal_meet_id_seq OWNED BY public.temp_principal_meet.id;


--
-- Name: temp_workshop_attend; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.temp_workshop_attend (
    id integer NOT NULL,
    temp_clg_id integer NOT NULL,
    clg_id integer,
    region_id integer NOT NULL,
    name character varying(512) DEFAULT NULL::character varying NOT NULL,
    email character varying(256) DEFAULT NULL::character varying NOT NULL,
    contact_num character varying(256) DEFAULT NULL::character varying NOT NULL,
    alternate_email1 character varying(512) DEFAULT NULL::character varying,
    department character varying(216) DEFAULT NULL::character varying,
    role integer,
    workshop_attend integer,
    created_at timestamp without time zone DEFAULT '-infinity'::timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.temp_workshop_attend OWNER TO postgres;

--
-- Name: temp_workshop_attend_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.temp_workshop_attend_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.temp_workshop_attend_id_seq OWNER TO postgres;

--
-- Name: temp_workshop_attend_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.temp_workshop_attend_id_seq OWNED BY public.temp_workshop_attend.id;


--
-- Name: users_login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_login (
    id integer NOT NULL,
    clg_id integer NOT NULL,
    username character varying(512) DEFAULT NULL::character varying NOT NULL,
    password character varying(1024) DEFAULT NULL::character varying,
    admin integer DEFAULT 0 NOT NULL,
    content integer DEFAULT 0 NOT NULL,
    cont_flag integer DEFAULT 0 NOT NULL,
    eyrtc integer DEFAULT 0 NOT NULL,
    tbt integer DEFAULT 0 NOT NULL,
    active integer NOT NULL,
    agree integer DEFAULT 0 NOT NULL,
    token character varying(1024) DEFAULT NULL::character varying,
    last_login timestamp without time zone,
    login_count integer,
    change_count integer DEFAULT 0 NOT NULL,
    forgot_count integer DEFAULT 0 NOT NULL,
    incorrect_login_attempts integer,
    remember_token character varying(1024) DEFAULT NULL::character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.users_login OWNER TO postgres;

--
-- Name: users_login_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_login_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_login_id_seq OWNER TO postgres;

--
-- Name: users_login_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_login_id_seq OWNED BY public.users_login.id;


--
-- Name: verification_tokens; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.verification_tokens (
    id integer NOT NULL,
    email character varying(100) DEFAULT NULL::character varying,
    token character varying(50) DEFAULT NULL::character varying,
    expires_in integer DEFAULT 3600 NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone
);


ALTER TABLE public.verification_tokens OWNER TO postgres;

--
-- Name: verification_tokens_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.verification_tokens_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.verification_tokens_id_seq OWNER TO postgres;

--
-- Name: verification_tokens_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.verification_tokens_id_seq OWNED BY public.verification_tokens.id;


--
-- Name: workshop_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.workshop_dtls (
    id integer NOT NULL,
    region_id integer,
    clg_id integer,
    active integer DEFAULT 0 NOT NULL,
    workshop_team character varying(520) DEFAULT NULL::character varying NOT NULL,
    start_date date,
    end_date date
);


ALTER TABLE public.workshop_dtls OWNER TO postgres;

--
-- Name: workshop_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.workshop_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.workshop_dtls_id_seq OWNER TO postgres;

--
-- Name: workshop_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.workshop_dtls_id_seq OWNED BY public.workshop_dtls.id;


--
-- Name: workshop_participants; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.workshop_participants (
    id integer NOT NULL,
    workshop_id integer,
    clg_id integer,
    tch_id integer
);


ALTER TABLE public.workshop_participants OWNER TO postgres;

--
-- Name: workshop_participants_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.workshop_participants_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.workshop_participants_id_seq OWNER TO postgres;

--
-- Name: workshop_participants_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.workshop_participants_id_seq OWNED BY public.workshop_participants.id;


--
-- Name: workshop_shipment_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.workshop_shipment_dtls (
    id integer NOT NULL,
    workshop_id integer,
    clg_id integer,
    shipment_date date,
    tracking_no integer,
    mode_of_dispatch character varying(1024) DEFAULT NULL::character varying,
    delivery_date date,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.workshop_shipment_dtls OWNER TO postgres;

--
-- Name: workshop_shipment_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.workshop_shipment_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.workshop_shipment_dtls_id_seq OWNER TO postgres;

--
-- Name: workshop_shipment_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.workshop_shipment_dtls_id_seq OWNED BY public.workshop_shipment_dtls.id;


--
-- Name: workshop_team; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.workshop_team (
    id integer NOT NULL,
    "Name" character varying(255) DEFAULT NULL::character varying NOT NULL
);


ALTER TABLE public.workshop_team OWNER TO postgres;

--
-- Name: workshop_team_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.workshop_team_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.workshop_team_id_seq OWNER TO postgres;

--
-- Name: workshop_team_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.workshop_team_id_seq OWNED BY public.workshop_team.id;


--
-- Name: advanced_workshop id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.advanced_workshop ALTER COLUMN id SET DEFAULT nextval('public.advanced_workshop_id_seq'::regclass);


--
-- Name: alumni_email id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alumni_email ALTER COLUMN id SET DEFAULT nextval('public.alumni_email_id_seq'::regclass);


--
-- Name: backup_elsi_college_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backup_elsi_college_dtls ALTER COLUMN id SET DEFAULT nextval('public.backup_elsi_college_dtls_id_seq'::regclass);


--
-- Name: con_feedback id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_feedback ALTER COLUMN id SET DEFAULT nextval('public.con_feedback_id_seq'::regclass);


--
-- Name: con_latex id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_latex ALTER COLUMN id SET DEFAULT nextval('public.con_latex_id_seq'::regclass);


--
-- Name: con_lesson_create id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_lesson_create ALTER COLUMN id SET DEFAULT nextval('public.con_lesson_create_id_seq'::regclass);


--
-- Name: con_lesson_plan_list id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_lesson_plan_list ALTER COLUMN id SET DEFAULT nextval('public.con_lesson_plan_list_id_seq'::regclass);


--
-- Name: con_lesson_plan_long_content id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_lesson_plan_long_content ALTER COLUMN id SET DEFAULT nextval('public.con_lesson_plan_long_content_id_seq'::regclass);


--
-- Name: con_lp_lessons id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_lp_lessons ALTER COLUMN id SET DEFAULT nextval('public.con_lp_lessons_id_seq'::regclass);


--
-- Name: con_project_generic id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_project_generic ALTER COLUMN id SET DEFAULT nextval('public.con_project_generic_id_seq'::regclass);


--
-- Name: con_project_list id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_project_list ALTER COLUMN id SET DEFAULT nextval('public.con_project_list_id_seq'::regclass);


--
-- Name: con_project_topics id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_project_topics ALTER COLUMN id SET DEFAULT nextval('public.con_project_topics_id_seq'::regclass);


--
-- Name: con_registration id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_registration ALTER COLUMN id SET DEFAULT nextval('public.con_registration_id_seq'::regclass);


--
-- Name: con_suggested_topic id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_suggested_topic ALTER COLUMN id SET DEFAULT nextval('public.con_suggested_topic_id_seq'::regclass);


--
-- Name: con_template id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_template ALTER COLUMN id SET DEFAULT nextval('public.con_template_id_seq'::regclass);


--
-- Name: con_tutorial_create id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_tutorial_create ALTER COLUMN id SET DEFAULT nextval('public.con_tutorial_create_id_seq'::regclass);


--
-- Name: con_tutorial_list id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_tutorial_list ALTER COLUMN id SET DEFAULT nextval('public.con_tutorial_list_id_seq'::regclass);


--
-- Name: con_tutorial_long_content id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_tutorial_long_content ALTER COLUMN id SET DEFAULT nextval('public.con_tutorial_long_content_id_seq'::regclass);


--
-- Name: con_tutorial_topics id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_tutorial_topics ALTER COLUMN id SET DEFAULT nextval('public.con_tutorial_topics_id_seq'::regclass);


--
-- Name: con_video_stage0 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_video_stage0 ALTER COLUMN id SET DEFAULT nextval('public.con_video_stage0_id_seq'::regclass);


--
-- Name: content_count id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.content_count ALTER COLUMN id SET DEFAULT nextval('public.content_count_id_seq'::regclass);


--
-- Name: content_register id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.content_register ALTER COLUMN id SET DEFAULT nextval('public.content_register_id_seq'::regclass);


--
-- Name: create_tutorial id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.create_tutorial ALTER COLUMN id SET DEFAULT nextval('public.create_tutorial_id_seq'::regclass);


--
-- Name: elsi_clg_contact_dtl id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_clg_contact_dtl ALTER COLUMN id SET DEFAULT nextval('public.elsi_clg_contact_dtl_id_seq'::regclass);


--
-- Name: elsi_college_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_college_dtls ALTER COLUMN id SET DEFAULT nextval('public.elsi_college_dtls_id_seq'::regclass);


--
-- Name: elsi_competitions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_competitions ALTER COLUMN id SET DEFAULT nextval('public.elsi_competitions_id_seq'::regclass);


--
-- Name: elsi_departments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_departments ALTER COLUMN id SET DEFAULT nextval('public.elsi_departments_id_seq'::regclass);


--
-- Name: elsi_designations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_designations ALTER COLUMN id SET DEFAULT nextval('public.elsi_designations_id_seq'::regclass);


--
-- Name: elsi_emails id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_emails ALTER COLUMN id SET DEFAULT nextval('public.elsi_emails_id_seq'::regclass);


--
-- Name: elsi_mooc id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_mooc ALTER COLUMN id SET DEFAULT nextval('public.elsi_mooc_id_seq'::regclass);


--
-- Name: elsi_region id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_region ALTER COLUMN id SET DEFAULT nextval('public.elsi_region_id_seq'::regclass);


--
-- Name: elsi_state id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_state ALTER COLUMN id SET DEFAULT nextval('public.elsi_state_id_seq'::regclass);


--
-- Name: elsi_students_mooc id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_students_mooc ALTER COLUMN id SET DEFAULT nextval('public.elsi_students_mooc_id_seq'::regclass);


--
-- Name: elsi_teachers_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_teachers_dtls ALTER COLUMN id SET DEFAULT nextval('public.elsi_teachers_dtls_id_seq'::regclass);


--
-- Name: eyantra_cert_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eyantra_cert_dtls ALTER COLUMN id SET DEFAULT nextval('public.eyantra_cert_dtls_id_seq'::regclass);


--
-- Name: eyrtc_participation id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eyrtc_participation ALTER COLUMN id SET DEFAULT nextval('public.eyrtc_participation_id_seq'::regclass);


--
-- Name: eyrtc_status id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eyrtc_status ALTER COLUMN id SET DEFAULT nextval('public.eyrtc_status_id_seq'::regclass);


--
-- Name: eys_registration_2016 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eys_registration_2016 ALTER COLUMN id SET DEFAULT nextval('public.eys_registration_2016_id_seq'::regclass);


--
-- Name: eys_registration_2017 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eys_registration_2017 ALTER COLUMN id SET DEFAULT nextval('public.eys_registration_2017_id_seq'::regclass);


--
-- Name: eys_registration_2018 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eys_registration_2018 ALTER COLUMN id SET DEFAULT nextval('public.eys_registration_2018_id_seq'::regclass);


--
-- Name: eys_registration_2019 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eys_registration_2019 ALTER COLUMN id SET DEFAULT nextval('public.eys_registration_2019_id_seq'::regclass);


--
-- Name: eys_registration_2020 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eys_registration_2020 ALTER COLUMN id SET DEFAULT nextval('public.eys_registration_2020_id_seq'::regclass);


--
-- Name: eysip_conduct id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eysip_conduct ALTER COLUMN id SET DEFAULT nextval('public.eysip_conduct_id_seq'::regclass);


--
-- Name: ie_modules id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ie_modules ALTER COLUMN id SET DEFAULT nextval('public.ie_modules_id_seq'::regclass);


--
-- Name: login id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login ALTER COLUMN id SET DEFAULT nextval('public.login_id_seq'::regclass);


--
-- Name: login_emails id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_emails ALTER COLUMN id SET DEFAULT nextval('public.login_emails_id_seq'::regclass);


--
-- Name: mooc_colleges id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mooc_colleges ALTER COLUMN id SET DEFAULT nextval('public.mooc_colleges_id_seq'::regclass);


--
-- Name: online_lab_inauguration id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.online_lab_inauguration ALTER COLUMN id SET DEFAULT nextval('public.online_lab_inauguration_id_seq'::regclass);


--
-- Name: principal_meet_attendee id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.principal_meet_attendee ALTER COLUMN id SET DEFAULT nextval('public.principal_meet_attendee_id_seq'::regclass);


--
-- Name: principal_meet_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.principal_meet_dtls ALTER COLUMN id SET DEFAULT nextval('public.principal_meet_dtls_id_seq'::regclass);


--
-- Name: principal_meet_participants id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.principal_meet_participants ALTER COLUMN id SET DEFAULT nextval('public.principal_meet_participants_id_seq'::regclass);


--
-- Name: regional_finals_invite id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.regional_finals_invite ALTER COLUMN id SET DEFAULT nextval('public.regional_finals_invite_id_seq'::regclass);


--
-- Name: regional_finals_invite_to_be_sent id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.regional_finals_invite_to_be_sent ALTER COLUMN id SET DEFAULT nextval('public.regional_finals_invite_to_be_sent_id_seq'::regclass);


--
-- Name: talks id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.talks ALTER COLUMN id SET DEFAULT nextval('public.talks_id_seq'::regclass);


--
-- Name: talks_series id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.talks_series ALTER COLUMN id SET DEFAULT nextval('public.talks_series_id_seq'::regclass);


--
-- Name: tbt_challenge_status id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_challenge_status ALTER COLUMN id SET DEFAULT nextval('public.tbt_challenge_status_id_seq'::regclass);


--
-- Name: tbt_feedback id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_feedback ALTER COLUMN id SET DEFAULT nextval('public.tbt_feedback_id_seq'::regclass);


--
-- Name: tbt_participation id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_participation ALTER COLUMN id SET DEFAULT nextval('public.tbt_participation_id_seq'::regclass);


--
-- Name: tbt_ques_ans_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_ques_ans_dtls ALTER COLUMN id SET DEFAULT nextval('public.tbt_ques_ans_dtls_id_seq'::regclass);


--
-- Name: tbt_question_master id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_question_master ALTER COLUMN id SET DEFAULT nextval('public.tbt_question_master_id_seq'::regclass);


--
-- Name: tbt_status id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_status ALTER COLUMN id SET DEFAULT nextval('public.tbt_status_id_seq'::regclass);


--
-- Name: tbt_temp_data id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_temp_data ALTER COLUMN id SET DEFAULT nextval('public.tbt_temp_data_id_seq'::regclass);


--
-- Name: team_email id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team_email ALTER COLUMN id SET DEFAULT nextval('public.team_email_id_seq'::regclass);


--
-- Name: team_member_detail id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team_member_detail ALTER COLUMN id SET DEFAULT nextval('public.team_member_detail_id_seq'::regclass);


--
-- Name: temp_college id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.temp_college ALTER COLUMN id SET DEFAULT nextval('public.temp_college_id_seq'::regclass);


--
-- Name: temp_principal_meet id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.temp_principal_meet ALTER COLUMN id SET DEFAULT nextval('public.temp_principal_meet_id_seq'::regclass);


--
-- Name: temp_workshop_attend id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.temp_workshop_attend ALTER COLUMN id SET DEFAULT nextval('public.temp_workshop_attend_id_seq'::regclass);


--
-- Name: users_login id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_login ALTER COLUMN id SET DEFAULT nextval('public.users_login_id_seq'::regclass);


--
-- Name: verification_tokens id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.verification_tokens ALTER COLUMN id SET DEFAULT nextval('public.verification_tokens_id_seq'::regclass);


--
-- Name: workshop_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workshop_dtls ALTER COLUMN id SET DEFAULT nextval('public.workshop_dtls_id_seq'::regclass);


--
-- Name: workshop_participants id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workshop_participants ALTER COLUMN id SET DEFAULT nextval('public.workshop_participants_id_seq'::regclass);


--
-- Name: workshop_shipment_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workshop_shipment_dtls ALTER COLUMN id SET DEFAULT nextval('public.workshop_shipment_dtls_id_seq'::regclass);


--
-- Name: workshop_team id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workshop_team ALTER COLUMN id SET DEFAULT nextval('public.workshop_team_id_seq'::regclass);


--
-- Data for Name: advanced_workshop; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.advanced_workshop (id, clg_code, name, emailid, gender, contact_num, alt_contact1, designation, role, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: alumni_email; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alumni_email (id, name, username, type, year, email_flag, updated_at) FROM stdin;
\.


--
-- Data for Name: backup_elsi_college_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.backup_elsi_college_dtls (id, clg_code, region_id, workshop_id, college_name, abbreviation, district, address, state, pincode, college_type, principal_meet, robots_given, eyic_allowed, eyrtc_allowed, tbt_allowed, content_allowed, legal_docs, legal_docs_remarks, loi_status, loi_format, loi_remarks, po_status, po_remark, wo_reg, wo_invite, wo_confirm, wo_attend, hardware_given, lab_inaugurated, phase, eys2016_invites, team_verify, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: colleges_to_contact_to_establish_elsi; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.colleges_to_contact_to_establish_elsi (id, college_name, name, designation, email, rank) FROM stdin;
\.


--
-- Data for Name: con_feedback; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_feedback (id, tch_id, resources, curriculum, lab_exp, comment, lesson_id, lesson_plan_id, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_latex; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_latex (id, tch_id, clg_id, down_date, flag, upload_date, status, accept_reject, remark, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_lesson_create; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_lesson_create (id, lp_name, lp_plan, refer_content, available, tch_count, i_agree, phase, launch_date, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_lesson_plan_list; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_lesson_plan_list (id, name, image_name, short_intro, intro_video_code, available, student_chk, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_lesson_plan_long_content; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_lesson_plan_long_content (id, lesson_plan_id, long_intro, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_lp_lessons; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_lp_lessons (id, lesson_plan_id, display_num, lesson_name, video1_code, video1_name, video2_code, video2_name, html_content, down_tm, count_tm, down_rr, count_rr, down_qb, count_qb, down_qbs, count_qbs, down_le, count_le, down_les, count_les, available, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_project_generic; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_project_generic (id, name, video_url, type, available, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_project_list; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_project_list (id, name, image_name, report_name, available, count_project, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_project_topics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_project_topics (id, proj_id, hardware, software, authors, description, video_code, code_link, available, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_registration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_registration (id, tch_id, name, designation, photo, name_cheq, biography, branch, ifsc, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_suggested_topic; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_suggested_topic (id, tch_id, topic, description, choice, email_sent, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_template; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_template (id, tch_id, clg_id, lesson_id, i_agree, start_date, end_date, flag, upload_date, status, difficulty, duration, presentation, lp8051, lparm, down_rev_les, upload_rev_date, rev_upld_date, rev_status, rev_flag, accept_reject, remark, plag, reg_status, agreement, reviewer_name, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_tutorial_create; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_tutorial_create (id, tut_name, tut_plan, refer_content, available, tch_count, i_agree, phase, launch_date, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_tutorial_list; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_tutorial_list (id, name, image_name, short_intro, intro_video_code, available, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_tutorial_long_content; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_tutorial_long_content (id, tut_id, long_intro, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_tutorial_topics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_tutorial_topics (id, tut_id, display_num, topic_name, video_code, html_content, down_code, down_ppt, down_misc, count_ppt, count_code, count_misc, available, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: con_video_stage0; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.con_video_stage0 (id, tch_id, video_link, submit_date, status, remarks, flag, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: content_count; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.content_count (id, clg_id, username, content, down_tm, down_rr, down_qb, down_qbs, down_le, down_les, ie_mod, down_tut_ppt, down_tut_code, down_tut_misc, count_lecture, down_project, down_lesson_temp, down_latex, down_video_res, down_stg1_temp, down_res_tutorial, create_content, blockly, suggest, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: content_register; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.content_register (id, clg_id, name, email, contact, gender, designation, department, upload, accept_reject, email_flag, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: create_tutorial; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.create_tutorial (id, tch_id, clg_id, tut_id, i_agree, start_date, end_date, video_link, rev_video_link, tut_explain, flag, upload_date, status, difficulty, duration, presentation, lp8051, lparm, down_rev_tuto, upload_rev_date, rev_upld_date, rev_status, rev_flag, accept_reject, remark, plag, reg_status, agreement, reviewer_name, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: elsi_clg_contact_dtl; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.elsi_clg_contact_dtl (id, clg_id, name, emailid, gender, branch, alt_email1, alt_email2, alt_email3, contact_num, alt_contact1, alt_contact2, "Active", designation, type, modified_by, status_cnt, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: elsi_college_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.elsi_college_dtls (id, clg_code, region_id, workshop_id, college_name, abbreviation, district, address, state, pincode, college_type, principal_meet, robots_given, eyic_allowed, eyrtc_allowed, tbt_allowed, mooc_allowed, content_allowed, legal_docs, legal_docs_remarks, loi_status, loi_format, loi_remarks, po_status, po_remark, wo_reg, wo_invite, wo_confirm, wo_attend, hardware_given, lab_inaugurated, phase, eys2016_invites, team_verify, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: elsi_competitions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.elsi_competitions (id, year, name, theme, phase, type, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: elsi_departments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.elsi_departments (id, name, main_branch) FROM stdin;
\.


--
-- Data for Name: elsi_designations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.elsi_designations (id, name, type) FROM stdin;
\.


--
-- Data for Name: elsi_emails; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.elsi_emails (id, subject, email_msg, img, pdf, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: elsi_mooc; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.elsi_mooc (id, clg_id, clg_code, college_name, name, username, contact, slot, email_flag, updated_at) FROM stdin;
\.


--
-- Data for Name: elsi_region; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.elsi_region (id, region_name, type, active, clg_id, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: elsi_state; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.elsi_state (id, code, state) FROM stdin;
\.


--
-- Data for Name: elsi_students_mooc; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.elsi_students_mooc (id, name, clg_id, emailid, contact_num, alt_contact1, department, current_year, mooc_allowed, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: elsi_teachers_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.elsi_teachers_dtls (id, user_id, clg_id, name, emailid, alt_email1, alt_email2, contact_num, alt_contact1, department, designation, gender, coor_flag, wo_flag, mooc_allowed, workshop_id, wo_attendee, wo_count, eyrtc_flag, tbt_flag, eyic_flag, content_flag, "Status", status_flag, modified_by, elsi_flag, remarks, login_created, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: eyantra_cert_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.eyantra_cert_dtls (id, workshop_id, tch_id, cert_num, cert_date, generated_at, remarks, type, year, eyrtc_id, eyic_id) FROM stdin;
\.


--
-- Data for Name: eyrtc_participation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.eyrtc_participation (id, clg_id, comp_id, tl_id, tm1_id, tm2_id, tm3_id, year, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: eyrtc_status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.eyrtc_status (id, part_id, task0_uploaded, task0_date, task0_file_name, task0_marks, task0_remark, task1_uploaded, task1_date, task1_link, task1_marks, task1_remark, task2_uploaded, task2_date, task2_link1, task2_link2, task2_marks, task2_remark, taskvideo_uploaded, taskvideo_date, taskvideo_link, taskvideo_marks, taskvideo_remark, taskcode_uploaded, taskcode_date, taskcode_marks, taskcode_remark, final_validatory_marks, final_validatory_remarks, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: eys_registration_2016; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.eys_registration_2016 (id, part_id, clg_id, team_id, name, emailid, contact_num, role, gender, arrival_date, departure_date, elsi_coor, elsi_competition, category, accommodation, attendence, reached_venue, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: eys_registration_2017; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.eys_registration_2017 (id, part_id, clg_id, team_id, name, emailid, contact_num, role, gender, arrival_date, arrival_time, departure_date, elsi_coor, elsi_competition, category, accommodation, attendence, account_number, account_holder_name, bank_name, bank_address, account_type, "IFSC_code", reached_venue, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: eys_registration_2018; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.eys_registration_2018 (id, part_id, clg_id, team_id, name, emailid, contact_num, role, gender, arrival_date, arrival_time, departure_date, elsi_coor, elsi_competition, category, accommodation, attendence, account_number, account_holder_name, bank_name, bank_address, account_type, "IFSC_code", reached_venue, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: eys_registration_2019; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.eys_registration_2019 (id, part_id, clg_id, team_id, name, emailid, contact_num, role, gender, arrival_date, arrival_time, departure_date, elsi_coor, elsi_competition, category, accommodation, attendence, account_number, account_holder_name, bank_name, bank_address, account_type, "IFSC_code", reached_venue, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: eys_registration_2020; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.eys_registration_2020 (id, part_id, clg_id, team_id, name, emailid, contact_num, role, gender, arrival_date, arrival_time, departure_date, elsi_coor, elsi_competition, category, accommodation, attendence, account_number, account_holder_name, bank_name, bank_address, account_type, "IFSC_code", reached_venue, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: eysip_conduct; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.eysip_conduct (id, stud_name, email, photograph, pancard, signature, conduct, proj_id, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: ie_modules; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ie_modules (id, name, image_name, short_intro, video_code, down_pdf, available, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login (id, name, team_id, team_member_id, username, password, role, active, theme, email_flag, last_login, login_count, change_count, forgot_count, remember_token, verify_token, token, email_verified_at, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: login_emails; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login_emails (id, name, team_id, team_member_id, username, password, role, active, theme, email_flag, last_login, login_count, change_count, forgot_count, remember_token, verify_token, token, email_verified_at, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: mooc_colleges; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mooc_colleges (id, clg_id, tch_email, students, updated_at) FROM stdin;
\.


--
-- Data for Name: online_lab_inauguration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.online_lab_inauguration (id, clg_id, labinaug_date, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: principal_meet_attendee; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.principal_meet_attendee (id, principal_meet_id, clg_id, name, emailid, contact_num, alt_contact1, gender, designation, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: principal_meet_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.principal_meet_dtls (id, region_id, clg_id, active, start_date) FROM stdin;
\.


--
-- Data for Name: principal_meet_participants; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.principal_meet_participants (id, principal_meet_id, data_table_id, clg_id, clg_contact_id, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: regional_finals_invite; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.regional_finals_invite (id, state, college_name, district, regional, name, designation, email, contact, attendees, lunch, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: regional_finals_invite_to_be_sent; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.regional_finals_invite_to_be_sent (id, college_name, name, designation, email, venue, day2, daydate, subject, attach, rsvpname, rsvpemail, rsvpcontact, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: talks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.talks (id, name, title, image, image_alt, short_intro, visited_lecture, available, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: talks_series; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.talks_series (id, display, image, img_url, available, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_challenge_status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_challenge_status (id, part_id, i_agree_challenge, task1_uploaded, task1_upload_time, task1_file_name, task1_marks, task1_remark, task2_uploaded, task2_video_link, task2_upload_time, task2_code_uploaded, task2_code_upload_time, task2_marks, task2_remark, challenge_result, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_feedback; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_feedback (id, clg_id, usr_id, teacher_name, email_id, question1, question2, question3, question4, question5, question6, question7, question8, question9, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_participation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_participation (id, clg_id, tbt_phase, tl_id, tm1_id, tm2_id, tm3_id, year, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_ques_ans_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_ques_ans_dtls (id, clg_id, part_id, ques_1, ques_2, ques_3, ques_4, ques_5, task, marks, bonus, total_marks, save_count, submit, submit_time, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_question_master; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_question_master (id, question, option_1, option_2, option_3, option_4, option_5, correct_option, task, type, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_status (id, part_id, task1_uploaded, task1_upload_time, task1_marks, task1_remark, task2_uploaded, task2_upload_time, task2_marks, task2_remark, task3_uploaded, task3_upload_time, task3_marks, task3_remark, task4_uploaded, task4_upload_time, task4_marks, task4_remark, task5_uploaded, task5_upload_time, task5_marks, task5_remark, task6_uploaded, task6_upload_time, task6_marks, task6_remark, award_grade, names_ok, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_temp_data; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_temp_data (id, region_id, college_name, abbreviated, district, state, pincode, polytech, principal_name, principal_contact, principal_email, college_address, tm1_name, tm1_email, tm1_contact, tm1_role, tm1_wrk, tm2_name, tm2_email, tm2_contact, tm2_role, tm2_wrk, tm3_name, tm3_email, tm3_contact, tm3_role, tm3_wrk, tm4_name, tm4_email, tm4_contact, tm4_role, tm4_wrk, tm5_name, tm5_email, tm5_contact, tm5_role, tm5_wrk, loi_status, robots_given, login_allowed, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: team_email; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.team_email (id, team_id, name, email, contact, discipline_id, department_id, year, gender, address, role, eyrc_year, eyrc_theme, eyrc_cert, tracking, dispatch_date, email_flag, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: team_member_detail; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.team_member_detail (id, email, flag, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: temp_college; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.temp_college (id, clg_id, region_id, college_name, address, principal_meet, work_shop, current_stat, "PrincipalName", "P_Number", "P_Number2", "P_emailID", loi_status, college_updated, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: temp_elsi_college_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.temp_elsi_college_dtls (id, clg_code, region_id, workshop_id, college_name, abbreviation, district, address, state, pincode, college_type, principal_meet, robots_given, eyic_allowed, eyrtc_allowed, tbt_allowed, content_allowed, legal_docs, legal_docs_remarks, loi_status, loi_format, loi_remarks, po_status, po_remark, wo_reg, wo_invite, wo_confirm, wo_attend, hardware_given, lab_inaugurated, phase, eys2016_invites, team_verify, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: temp_principal_meet; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.temp_principal_meet (id, region_id, temp_clg_id, name, email, contact_num, alt_contact_num1, designation, clg_type, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: temp_workshop_attend; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.temp_workshop_attend (id, temp_clg_id, clg_id, region_id, name, email, contact_num, alternate_email1, department, role, workshop_attend, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: users_login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_login (id, clg_id, username, password, admin, content, cont_flag, eyrtc, tbt, active, agree, token, last_login, login_count, change_count, forgot_count, incorrect_login_attempts, remember_token, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: verification_tokens; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.verification_tokens (id, email, token, expires_in, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: workshop_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.workshop_dtls (id, region_id, clg_id, active, workshop_team, start_date, end_date) FROM stdin;
\.


--
-- Data for Name: workshop_participants; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.workshop_participants (id, workshop_id, clg_id, tch_id) FROM stdin;
\.


--
-- Data for Name: workshop_shipment_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.workshop_shipment_dtls (id, workshop_id, clg_id, shipment_date, tracking_no, mode_of_dispatch, delivery_date, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: workshop_team; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.workshop_team (id, "Name") FROM stdin;
\.


--
-- Name: advanced_workshop_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.advanced_workshop_id_seq', 1, false);


--
-- Name: alumni_email_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.alumni_email_id_seq', 1, false);


--
-- Name: backup_elsi_college_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.backup_elsi_college_dtls_id_seq', 1, false);


--
-- Name: con_feedback_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_feedback_id_seq', 1, false);


--
-- Name: con_latex_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_latex_id_seq', 1, false);


--
-- Name: con_lesson_create_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_lesson_create_id_seq', 1, false);


--
-- Name: con_lesson_plan_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_lesson_plan_list_id_seq', 1, false);


--
-- Name: con_lesson_plan_long_content_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_lesson_plan_long_content_id_seq', 1, false);


--
-- Name: con_lp_lessons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_lp_lessons_id_seq', 1, false);


--
-- Name: con_project_generic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_project_generic_id_seq', 1, false);


--
-- Name: con_project_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_project_list_id_seq', 1, false);


--
-- Name: con_project_topics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_project_topics_id_seq', 1, false);


--
-- Name: con_registration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_registration_id_seq', 1, false);


--
-- Name: con_suggested_topic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_suggested_topic_id_seq', 1, false);


--
-- Name: con_template_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_template_id_seq', 1, false);


--
-- Name: con_tutorial_create_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_tutorial_create_id_seq', 1, false);


--
-- Name: con_tutorial_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_tutorial_list_id_seq', 1, false);


--
-- Name: con_tutorial_long_content_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_tutorial_long_content_id_seq', 1, false);


--
-- Name: con_tutorial_topics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_tutorial_topics_id_seq', 1, false);


--
-- Name: con_video_stage0_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.con_video_stage0_id_seq', 1, false);


--
-- Name: content_count_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.content_count_id_seq', 1, false);


--
-- Name: content_register_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.content_register_id_seq', 1, false);


--
-- Name: create_tutorial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.create_tutorial_id_seq', 1, false);


--
-- Name: elsi_clg_contact_dtl_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.elsi_clg_contact_dtl_id_seq', 1, false);


--
-- Name: elsi_college_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.elsi_college_dtls_id_seq', 1, false);


--
-- Name: elsi_competitions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.elsi_competitions_id_seq', 1, false);


--
-- Name: elsi_departments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.elsi_departments_id_seq', 1, false);


--
-- Name: elsi_designations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.elsi_designations_id_seq', 1, false);


--
-- Name: elsi_emails_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.elsi_emails_id_seq', 1, false);


--
-- Name: elsi_mooc_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.elsi_mooc_id_seq', 1, false);


--
-- Name: elsi_region_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.elsi_region_id_seq', 1, false);


--
-- Name: elsi_state_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.elsi_state_id_seq', 1, false);


--
-- Name: elsi_students_mooc_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.elsi_students_mooc_id_seq', 1, false);


--
-- Name: elsi_teachers_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.elsi_teachers_dtls_id_seq', 1, false);


--
-- Name: eyantra_cert_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.eyantra_cert_dtls_id_seq', 1, false);


--
-- Name: eyrtc_participation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.eyrtc_participation_id_seq', 1, false);


--
-- Name: eyrtc_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.eyrtc_status_id_seq', 1, false);


--
-- Name: eys_registration_2016_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.eys_registration_2016_id_seq', 1, false);


--
-- Name: eys_registration_2017_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.eys_registration_2017_id_seq', 1, false);


--
-- Name: eys_registration_2018_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.eys_registration_2018_id_seq', 1, false);


--
-- Name: eys_registration_2019_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.eys_registration_2019_id_seq', 1, false);


--
-- Name: eys_registration_2020_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.eys_registration_2020_id_seq', 1, false);


--
-- Name: eysip_conduct_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.eysip_conduct_id_seq', 1, false);


--
-- Name: ie_modules_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ie_modules_id_seq', 1, false);


--
-- Name: login_emails_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.login_emails_id_seq', 1, false);


--
-- Name: login_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.login_id_seq', 1, false);


--
-- Name: mooc_colleges_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mooc_colleges_id_seq', 1, false);


--
-- Name: online_lab_inauguration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.online_lab_inauguration_id_seq', 1, false);


--
-- Name: principal_meet_attendee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.principal_meet_attendee_id_seq', 1, false);


--
-- Name: principal_meet_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.principal_meet_dtls_id_seq', 1, false);


--
-- Name: principal_meet_participants_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.principal_meet_participants_id_seq', 1, false);


--
-- Name: regional_finals_invite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.regional_finals_invite_id_seq', 1, false);


--
-- Name: regional_finals_invite_to_be_sent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.regional_finals_invite_to_be_sent_id_seq', 1, false);


--
-- Name: talks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.talks_id_seq', 1, false);


--
-- Name: talks_series_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.talks_series_id_seq', 1, false);


--
-- Name: tbt_challenge_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_challenge_status_id_seq', 1, false);


--
-- Name: tbt_feedback_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_feedback_id_seq', 1, false);


--
-- Name: tbt_participation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_participation_id_seq', 1, false);


--
-- Name: tbt_ques_ans_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_ques_ans_dtls_id_seq', 1, false);


--
-- Name: tbt_question_master_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_question_master_id_seq', 1, false);


--
-- Name: tbt_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_status_id_seq', 1, false);


--
-- Name: tbt_temp_data_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_temp_data_id_seq', 1, false);


--
-- Name: team_email_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.team_email_id_seq', 1, false);


--
-- Name: team_member_detail_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.team_member_detail_id_seq', 1, false);


--
-- Name: temp_college_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.temp_college_id_seq', 1, false);


--
-- Name: temp_principal_meet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.temp_principal_meet_id_seq', 1, false);


--
-- Name: temp_workshop_attend_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.temp_workshop_attend_id_seq', 1, false);


--
-- Name: users_login_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_login_id_seq', 1, false);


--
-- Name: verification_tokens_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.verification_tokens_id_seq', 1, false);


--
-- Name: workshop_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.workshop_dtls_id_seq', 1, false);


--
-- Name: workshop_participants_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.workshop_participants_id_seq', 1, false);


--
-- Name: workshop_shipment_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.workshop_shipment_dtls_id_seq', 1, false);


--
-- Name: workshop_team_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.workshop_team_id_seq', 1, false);


--
-- Name: advanced_workshop advanced_workshop_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.advanced_workshop
    ADD CONSTRAINT advanced_workshop_pkey PRIMARY KEY (id);


--
-- Name: alumni_email alumni_email_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alumni_email
    ADD CONSTRAINT alumni_email_pkey PRIMARY KEY (id);


--
-- Name: backup_elsi_college_dtls backup_elsi_college_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backup_elsi_college_dtls
    ADD CONSTRAINT backup_elsi_college_dtls_pkey PRIMARY KEY (id);


--
-- Name: con_feedback con_feedback_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_feedback
    ADD CONSTRAINT con_feedback_pkey PRIMARY KEY (id);


--
-- Name: con_latex con_latex_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_latex
    ADD CONSTRAINT con_latex_pkey PRIMARY KEY (id);


--
-- Name: con_lesson_create con_lesson_create_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_lesson_create
    ADD CONSTRAINT con_lesson_create_pkey PRIMARY KEY (id);


--
-- Name: con_lesson_plan_list con_lesson_plan_list_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_lesson_plan_list
    ADD CONSTRAINT con_lesson_plan_list_pkey PRIMARY KEY (id);


--
-- Name: con_lesson_plan_long_content con_lesson_plan_long_content_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_lesson_plan_long_content
    ADD CONSTRAINT con_lesson_plan_long_content_pkey PRIMARY KEY (id);


--
-- Name: con_lp_lessons con_lp_lessons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_lp_lessons
    ADD CONSTRAINT con_lp_lessons_pkey PRIMARY KEY (id);


--
-- Name: con_project_generic con_project_generic_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_project_generic
    ADD CONSTRAINT con_project_generic_pkey PRIMARY KEY (id);


--
-- Name: con_project_list con_project_list_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_project_list
    ADD CONSTRAINT con_project_list_pkey PRIMARY KEY (id);


--
-- Name: con_project_topics con_project_topics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_project_topics
    ADD CONSTRAINT con_project_topics_pkey PRIMARY KEY (id);


--
-- Name: con_registration con_registration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_registration
    ADD CONSTRAINT con_registration_pkey PRIMARY KEY (id);


--
-- Name: con_suggested_topic con_suggested_topic_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_suggested_topic
    ADD CONSTRAINT con_suggested_topic_pkey PRIMARY KEY (id);


--
-- Name: con_template con_template_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_template
    ADD CONSTRAINT con_template_pkey PRIMARY KEY (id);


--
-- Name: con_tutorial_create con_tutorial_create_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_tutorial_create
    ADD CONSTRAINT con_tutorial_create_pkey PRIMARY KEY (id);


--
-- Name: con_tutorial_list con_tutorial_list_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_tutorial_list
    ADD CONSTRAINT con_tutorial_list_pkey PRIMARY KEY (id);


--
-- Name: con_tutorial_long_content con_tutorial_long_content_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_tutorial_long_content
    ADD CONSTRAINT con_tutorial_long_content_pkey PRIMARY KEY (id);


--
-- Name: con_tutorial_topics con_tutorial_topics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_tutorial_topics
    ADD CONSTRAINT con_tutorial_topics_pkey PRIMARY KEY (id);


--
-- Name: con_video_stage0 con_video_stage0_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.con_video_stage0
    ADD CONSTRAINT con_video_stage0_pkey PRIMARY KEY (id);


--
-- Name: content_count content_count_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.content_count
    ADD CONSTRAINT content_count_pkey PRIMARY KEY (id);


--
-- Name: content_register content_register_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.content_register
    ADD CONSTRAINT content_register_pkey PRIMARY KEY (id);


--
-- Name: create_tutorial create_tutorial_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.create_tutorial
    ADD CONSTRAINT create_tutorial_pkey PRIMARY KEY (id);


--
-- Name: elsi_clg_contact_dtl elsi_clg_contact_dtl_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_clg_contact_dtl
    ADD CONSTRAINT elsi_clg_contact_dtl_pkey PRIMARY KEY (id);


--
-- Name: elsi_college_dtls elsi_college_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_college_dtls
    ADD CONSTRAINT elsi_college_dtls_pkey PRIMARY KEY (id);


--
-- Name: elsi_competitions elsi_competitions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_competitions
    ADD CONSTRAINT elsi_competitions_pkey PRIMARY KEY (id);


--
-- Name: elsi_departments elsi_departments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_departments
    ADD CONSTRAINT elsi_departments_pkey PRIMARY KEY (id);


--
-- Name: elsi_designations elsi_designations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_designations
    ADD CONSTRAINT elsi_designations_pkey PRIMARY KEY (id);


--
-- Name: elsi_emails elsi_emails_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_emails
    ADD CONSTRAINT elsi_emails_pkey PRIMARY KEY (id);


--
-- Name: elsi_mooc elsi_mooc_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_mooc
    ADD CONSTRAINT elsi_mooc_pkey PRIMARY KEY (id);


--
-- Name: elsi_region elsi_region_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_region
    ADD CONSTRAINT elsi_region_pkey PRIMARY KEY (id);


--
-- Name: elsi_state elsi_state_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_state
    ADD CONSTRAINT elsi_state_pkey PRIMARY KEY (id);


--
-- Name: elsi_students_mooc elsi_students_mooc_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_students_mooc
    ADD CONSTRAINT elsi_students_mooc_pkey PRIMARY KEY (id);


--
-- Name: elsi_teachers_dtls elsi_teachers_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_teachers_dtls
    ADD CONSTRAINT elsi_teachers_dtls_pkey PRIMARY KEY (id);


--
-- Name: eyantra_cert_dtls eyantra_cert_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eyantra_cert_dtls
    ADD CONSTRAINT eyantra_cert_dtls_pkey PRIMARY KEY (id);


--
-- Name: eyrtc_participation eyrtc_participation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eyrtc_participation
    ADD CONSTRAINT eyrtc_participation_pkey PRIMARY KEY (id);


--
-- Name: eyrtc_status eyrtc_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eyrtc_status
    ADD CONSTRAINT eyrtc_status_pkey PRIMARY KEY (id);


--
-- Name: eys_registration_2016 eys_registration_2016_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eys_registration_2016
    ADD CONSTRAINT eys_registration_2016_pkey PRIMARY KEY (id);


--
-- Name: eys_registration_2017 eys_registration_2017_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eys_registration_2017
    ADD CONSTRAINT eys_registration_2017_pkey PRIMARY KEY (id);


--
-- Name: eys_registration_2018 eys_registration_2018_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eys_registration_2018
    ADD CONSTRAINT eys_registration_2018_pkey PRIMARY KEY (id);


--
-- Name: eys_registration_2019 eys_registration_2019_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eys_registration_2019
    ADD CONSTRAINT eys_registration_2019_pkey PRIMARY KEY (id);


--
-- Name: eys_registration_2020 eys_registration_2020_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eys_registration_2020
    ADD CONSTRAINT eys_registration_2020_pkey PRIMARY KEY (id);


--
-- Name: eysip_conduct eysip_conduct_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eysip_conduct
    ADD CONSTRAINT eysip_conduct_pkey PRIMARY KEY (id);


--
-- Name: ie_modules ie_modules_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ie_modules
    ADD CONSTRAINT ie_modules_pkey PRIMARY KEY (id);


--
-- Name: login_emails login_emails_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_emails
    ADD CONSTRAINT login_emails_pkey PRIMARY KEY (id);


--
-- Name: login login_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login
    ADD CONSTRAINT login_pkey PRIMARY KEY (id);


--
-- Name: mooc_colleges mooc_colleges_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mooc_colleges
    ADD CONSTRAINT mooc_colleges_pkey PRIMARY KEY (id);


--
-- Name: online_lab_inauguration online_lab_inauguration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.online_lab_inauguration
    ADD CONSTRAINT online_lab_inauguration_pkey PRIMARY KEY (id);


--
-- Name: principal_meet_attendee principal_meet_attendee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.principal_meet_attendee
    ADD CONSTRAINT principal_meet_attendee_pkey PRIMARY KEY (id);


--
-- Name: principal_meet_dtls principal_meet_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.principal_meet_dtls
    ADD CONSTRAINT principal_meet_dtls_pkey PRIMARY KEY (id);


--
-- Name: principal_meet_participants principal_meet_participants_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.principal_meet_participants
    ADD CONSTRAINT principal_meet_participants_pkey PRIMARY KEY (id);


--
-- Name: talks talks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.talks
    ADD CONSTRAINT talks_pkey PRIMARY KEY (id);


--
-- Name: talks_series talks_series_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.talks_series
    ADD CONSTRAINT talks_series_pkey PRIMARY KEY (id);


--
-- Name: tbt_challenge_status tbt_challenge_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_challenge_status
    ADD CONSTRAINT tbt_challenge_status_pkey PRIMARY KEY (id);


--
-- Name: tbt_feedback tbt_feedback_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_feedback
    ADD CONSTRAINT tbt_feedback_pkey PRIMARY KEY (id);


--
-- Name: tbt_participation tbt_participation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_participation
    ADD CONSTRAINT tbt_participation_pkey PRIMARY KEY (id);


--
-- Name: tbt_ques_ans_dtls tbt_ques_ans_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_ques_ans_dtls
    ADD CONSTRAINT tbt_ques_ans_dtls_pkey PRIMARY KEY (id);


--
-- Name: tbt_question_master tbt_question_master_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_question_master
    ADD CONSTRAINT tbt_question_master_pkey PRIMARY KEY (id);


--
-- Name: tbt_status tbt_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_status
    ADD CONSTRAINT tbt_status_pkey PRIMARY KEY (id);


--
-- Name: team_email team_email_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team_email
    ADD CONSTRAINT team_email_pkey PRIMARY KEY (id);


--
-- Name: team_member_detail team_member_detail_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team_member_detail
    ADD CONSTRAINT team_member_detail_pkey PRIMARY KEY (id);


--
-- Name: temp_college temp_college_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.temp_college
    ADD CONSTRAINT temp_college_pkey PRIMARY KEY (id);


--
-- Name: temp_principal_meet temp_principal_meet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.temp_principal_meet
    ADD CONSTRAINT temp_principal_meet_pkey PRIMARY KEY (id);


--
-- Name: temp_workshop_attend temp_workshop_attend_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.temp_workshop_attend
    ADD CONSTRAINT temp_workshop_attend_pkey PRIMARY KEY (id);


--
-- Name: users_login users_login_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_login
    ADD CONSTRAINT users_login_pkey PRIMARY KEY (id);


--
-- Name: verification_tokens verification_tokens_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.verification_tokens
    ADD CONSTRAINT verification_tokens_pkey PRIMARY KEY (id);


--
-- Name: workshop_dtls workshop_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workshop_dtls
    ADD CONSTRAINT workshop_dtls_pkey PRIMARY KEY (id);


--
-- Name: workshop_participants workshop_participants_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workshop_participants
    ADD CONSTRAINT workshop_participants_pkey PRIMARY KEY (id);


--
-- Name: workshop_shipment_dtls workshop_shipment_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workshop_shipment_dtls
    ADD CONSTRAINT workshop_shipment_dtls_pkey PRIMARY KEY (id);


--
-- Name: workshop_team workshop_team_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workshop_team
    ADD CONSTRAINT workshop_team_pkey PRIMARY KEY (id);


--
-- Name: public_colleges_to_contact_to_establish_elsi_id0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_colleges_to_contact_to_establish_elsi_id0_idx ON public.colleges_to_contact_to_establish_elsi USING btree (id);


--
-- Name: public_content_count_username0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_content_count_username0_idx ON public.content_count USING btree (username);


--
-- Name: public_elsi_students_mooc_clg_id0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX public_elsi_students_mooc_clg_id0_idx ON public.elsi_students_mooc USING btree (clg_id);


--
-- Name: public_login_emails_username0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_login_emails_username0_idx ON public.login_emails USING btree (username);


--
-- Name: public_login_username0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_login_username0_idx ON public.login USING btree (username);


--
-- Name: public_regional_finals_invite_id0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_regional_finals_invite_id0_idx ON public.regional_finals_invite USING btree (id);


--
-- Name: public_regional_finals_invite_to_be_sent_id0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_regional_finals_invite_to_be_sent_id0_idx ON public.regional_finals_invite_to_be_sent USING btree (id);


--
-- Name: public_tbt_feedback_id0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_tbt_feedback_id0_idx ON public.tbt_feedback USING btree (id);


--
-- Name: public_tbt_temp_data_id0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_tbt_temp_data_id0_idx ON public.tbt_temp_data USING btree (id);


--
-- Name: public_team_email_contact1_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_team_email_contact1_idx ON public.team_email USING btree (contact);


--
-- Name: public_team_email_email0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_team_email_email0_idx ON public.team_email USING btree (email);


--
-- Name: public_team_member_detail_email0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_team_member_detail_email0_idx ON public.team_member_detail USING btree (email);


--
-- Name: public_users_login_username0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_users_login_username0_idx ON public.users_login USING btree (username);


--
-- Name: public_verification_tokens_email0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_verification_tokens_email0_idx ON public.verification_tokens USING btree (email);


--
-- Name: elsi_students_mooc elsi_students_mooc_clg_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_students_mooc
    ADD CONSTRAINT elsi_students_mooc_clg_id_fkey FOREIGN KEY (clg_id) REFERENCES public.elsi_college_dtls(id);


--
-- PostgreSQL database dump complete
--

