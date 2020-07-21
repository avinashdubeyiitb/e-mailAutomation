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
-- Name: departments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.departments (
    id integer NOT NULL,
    name character varying(512) DEFAULT NULL::character varying NOT NULL,
    main_branch character varying(512) DEFAULT NULL::character varying
);


ALTER TABLE public.departments OWNER TO postgres;

--
-- Name: departments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.departments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.departments_id_seq OWNER TO postgres;

--
-- Name: departments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.departments_id_seq OWNED BY public.departments.id;


--
-- Name: designations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.designations (
    id integer NOT NULL,
    name character varying(256) DEFAULT NULL::character varying NOT NULL,
    type character varying(256) DEFAULT NULL::character varying
);


ALTER TABLE public.designations OWNER TO postgres;

--
-- Name: designations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.designations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.designations_id_seq OWNER TO postgres;

--
-- Name: designations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.designations_id_seq OWNED BY public.designations.id;


--
-- Name: elsi_region; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.elsi_region (
    id integer NOT NULL,
    region_name character varying(512) DEFAULT NULL::character varying NOT NULL,
    type integer DEFAULT 0 NOT NULL,
    active integer DEFAULT 0 NOT NULL,
    clg_id integer,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
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
-- Name: region; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.region (
    id integer NOT NULL,
    region_name character varying(512) DEFAULT NULL::character varying NOT NULL,
    type integer DEFAULT 0 NOT NULL,
    active integer DEFAULT 0 NOT NULL,
    clg_id integer,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.region OWNER TO postgres;

--
-- Name: TABLE region; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.region IS 'Stores all the regions under eLSI';


--
-- Name: COLUMN region.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.region.id IS 'Identifier';


--
-- Name: COLUMN region.region_name; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.region.region_name IS 'region name';


--
-- Name: COLUMN region.type; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.region.type IS 'type of the region, 1-NC, 2-CC';


--
-- Name: region_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.region_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.region_id_seq OWNER TO postgres;

--
-- Name: region_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.region_id_seq OWNED BY public.region.id;


--
-- Name: state; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.state (
    id integer NOT NULL,
    state character varying(100) DEFAULT NULL::character varying
);


ALTER TABLE public.state OWNER TO postgres;

--
-- Name: state_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.state_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.state_id_seq OWNER TO postgres;

--
-- Name: state_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.state_id_seq OWNED BY public.state.id;


--
-- Name: tbt_challenge_master; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_challenge_master (
    id integer NOT NULL,
    theme character varying(255) DEFAULT NULL::character varying NOT NULL,
    description character varying(1020) DEFAULT NULL::character varying,
    create_at timestamp without time zone NOT NULL,
    update_at timestamp without time zone NOT NULL
);


ALTER TABLE public.tbt_challenge_master OWNER TO postgres;

--
-- Name: tbt_challenge_master_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_challenge_master_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_challenge_master_id_seq OWNER TO postgres;

--
-- Name: tbt_challenge_master_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_challenge_master_id_seq OWNED BY public.tbt_challenge_master.id;


--
-- Name: tbt_challenge_team_schedule; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_challenge_team_schedule (
    id integer NOT NULL,
    team_id integer NOT NULL,
    theme_id integer NOT NULL,
    launch_date timestamp without time zone NOT NULL,
    task1_deadline timestamp without time zone NOT NULL,
    task2_deadline timestamp without time zone NOT NULL,
    tbt_phase integer NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


ALTER TABLE public.tbt_challenge_team_schedule OWNER TO postgres;

--
-- Name: tbt_challenge_team_schedule_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_challenge_team_schedule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_challenge_team_schedule_id_seq OWNER TO postgres;

--
-- Name: tbt_challenge_team_schedule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_challenge_team_schedule_id_seq OWNED BY public.tbt_challenge_team_schedule.id;


--
-- Name: tbt_clg_contact_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_clg_contact_dtls (
    id integer NOT NULL,
    tbt_clg_id integer NOT NULL,
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
    alt_contact3 character varying(50) DEFAULT NULL::character varying,
    designation character varying(256) DEFAULT NULL::character varying,
    type integer DEFAULT 1 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_clg_contact_dtls OWNER TO postgres;

--
-- Name: tbt_clg_contact_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_clg_contact_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_clg_contact_dtls_id_seq OWNER TO postgres;

--
-- Name: tbt_clg_contact_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_clg_contact_dtls_id_seq OWNED BY public.tbt_clg_contact_dtls.id;


--
-- Name: tbt_college_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_college_dtls (
    id integer NOT NULL,
    elsi_clg_id integer,
    region_id integer,
    college_name character varying(1024) DEFAULT NULL::character varying NOT NULL,
    abbreviation character varying(128) DEFAULT NULL::character varying,
    district character varying(256) DEFAULT NULL::character varying,
    address character varying(1024) DEFAULT NULL::character varying,
    state character varying(512) DEFAULT NULL::character varying,
    pincode character varying(10) DEFAULT NULL::character varying,
    college_type character varying(256) DEFAULT NULL::character varying,
    principal_meet integer DEFAULT 0 NOT NULL,
    robots_given integer DEFAULT 0,
    tbt_allowed integer DEFAULT 0 NOT NULL,
    tbt_count integer,
    completed integer,
    legal_docs integer DEFAULT 0,
    legal_docs_remarks character varying(1024) DEFAULT NULL::character varying,
    loi_status integer DEFAULT 0,
    po_status integer DEFAULT 0,
    po_remark character varying(1024) DEFAULT NULL::character varying,
    wo_reg integer DEFAULT 0 NOT NULL,
    wo_invite integer DEFAULT 0 NOT NULL,
    wo_confirm integer DEFAULT 0 NOT NULL,
    wo_attend integer DEFAULT 0 NOT NULL,
    phase integer DEFAULT 0 NOT NULL,
    lab_inaugrated integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_college_dtls OWNER TO postgres;

--
-- Name: COLUMN tbt_college_dtls.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.tbt_college_dtls.id IS 'identifier';


--
-- Name: tbt_college_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_college_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_college_dtls_id_seq OWNER TO postgres;

--
-- Name: tbt_college_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_college_dtls_id_seq OWNED BY public.tbt_college_dtls.id;


--
-- Name: tbt_competition; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_competition (
    id integer DEFAULT 0 NOT NULL,
    year character varying(16) DEFAULT NULL::character varying NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_competition OWNER TO postgres;

--
-- Name: tbt_experiment_master; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_experiment_master (
    id integer NOT NULL,
    task_id integer NOT NULL,
    ex_version_id integer NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.tbt_experiment_master OWNER TO postgres;

--
-- Name: tbt_experiment_master_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_experiment_master_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_experiment_master_id_seq OWNER TO postgres;

--
-- Name: tbt_experiment_master_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_experiment_master_id_seq OWNED BY public.tbt_experiment_master.id;


--
-- Name: tbt_feedback; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_feedback (
    id integer NOT NULL,
    team_id integer NOT NULL,
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
-- Name: tbt_mcq_master; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_mcq_master (
    id integer NOT NULL,
    question_id integer,
    mcq_version_id integer,
    question_text text,
    option_1 character varying(2048) DEFAULT NULL::character varying,
    option_2 character varying(2048) DEFAULT NULL::character varying,
    option_3 character varying(2048) DEFAULT NULL::character varying,
    option_4 character varying(2048) DEFAULT NULL::character varying,
    option_5 character varying(2048) DEFAULT NULL::character varying,
    correct_option integer,
    answer_explanation character varying(8192) DEFAULT NULL::character varying,
    task integer,
    tbt_phase integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.tbt_mcq_master OWNER TO postgres;

--
-- Name: tbt_mcq_master_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_mcq_master_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_mcq_master_id_seq OWNER TO postgres;

--
-- Name: tbt_mcq_master_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_mcq_master_id_seq OWNED BY public.tbt_mcq_master.id;


--
-- Name: tbt_mcq_task1_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_mcq_task1_dtls (
    id integer NOT NULL,
    team_id integer,
    question_id integer,
    choosen_option integer,
    save_count integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.tbt_mcq_task1_dtls OWNER TO postgres;

--
-- Name: tbt_mcq_task1_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_mcq_task1_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_mcq_task1_dtls_id_seq OWNER TO postgres;

--
-- Name: tbt_mcq_task1_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_mcq_task1_dtls_id_seq OWNED BY public.tbt_mcq_task1_dtls.id;


--
-- Name: tbt_mcq_task2_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_mcq_task2_dtls (
    id integer NOT NULL,
    team_id integer,
    question_id integer,
    choosen_option integer,
    save_count integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.tbt_mcq_task2_dtls OWNER TO postgres;

--
-- Name: tbt_mcq_task2_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_mcq_task2_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_mcq_task2_dtls_id_seq OWNER TO postgres;

--
-- Name: tbt_mcq_task2_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_mcq_task2_dtls_id_seq OWNED BY public.tbt_mcq_task2_dtls.id;


--
-- Name: tbt_mcq_task3_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_mcq_task3_dtls (
    id integer NOT NULL,
    team_id integer,
    question_id integer,
    choosen_option integer,
    save_count integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.tbt_mcq_task3_dtls OWNER TO postgres;

--
-- Name: tbt_mcq_task3_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_mcq_task3_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_mcq_task3_dtls_id_seq OWNER TO postgres;

--
-- Name: tbt_mcq_task3_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_mcq_task3_dtls_id_seq OWNED BY public.tbt_mcq_task3_dtls.id;


--
-- Name: tbt_mcq_task4_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_mcq_task4_dtls (
    id integer NOT NULL,
    team_id integer,
    question_id integer,
    choosen_option integer,
    save_count integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.tbt_mcq_task4_dtls OWNER TO postgres;

--
-- Name: tbt_mcq_task4_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_mcq_task4_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_mcq_task4_dtls_id_seq OWNER TO postgres;

--
-- Name: tbt_mcq_task4_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_mcq_task4_dtls_id_seq OWNED BY public.tbt_mcq_task4_dtls.id;


--
-- Name: tbt_mcq_task5_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_mcq_task5_dtls (
    id integer NOT NULL,
    team_id integer,
    question_id integer,
    choosen_option integer,
    save_count integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.tbt_mcq_task5_dtls OWNER TO postgres;

--
-- Name: tbt_mcq_task5_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_mcq_task5_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_mcq_task5_dtls_id_seq OWNER TO postgres;

--
-- Name: tbt_mcq_task5_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_mcq_task5_dtls_id_seq OWNED BY public.tbt_mcq_task5_dtls.id;


--
-- Name: tbt_mcq_task6_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_mcq_task6_dtls (
    id integer NOT NULL,
    team_id integer,
    question_id integer,
    choosen_option character varying(1024) DEFAULT NULL::character varying,
    save_count integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.tbt_mcq_task6_dtls OWNER TO postgres;

--
-- Name: tbt_mcq_task6_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_mcq_task6_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_mcq_task6_dtls_id_seq OWNER TO postgres;

--
-- Name: tbt_mcq_task6_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_mcq_task6_dtls_id_seq OWNED BY public.tbt_mcq_task6_dtls.id;


--
-- Name: tbt_mcq_task_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_mcq_task_dtls (
    id integer NOT NULL,
    task integer NOT NULL,
    team_id integer,
    question_id integer,
    chosen_option integer,
    save_count integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.tbt_mcq_task_dtls OWNER TO postgres;

--
-- Name: tbt_mcq_task_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_mcq_task_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_mcq_task_dtls_id_seq OWNER TO postgres;

--
-- Name: tbt_mcq_task_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_mcq_task_dtls_id_seq OWNED BY public.tbt_mcq_task_dtls.id;


--
-- Name: tbt_schedule; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_schedule (
    id integer NOT NULL,
    task_number integer DEFAULT 0 NOT NULL,
    tasks character varying(2048) DEFAULT NULL::character varying,
    launch_date timestamp without time zone,
    task_deadline timestamp without time zone,
    absolute_deadline timestamp without time zone,
    tbt_phase integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_schedule OWNER TO postgres;

--
-- Name: tbt_schedule_challenge; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_schedule_challenge (
    id integer NOT NULL,
    task_number integer DEFAULT 0 NOT NULL,
    tasks character varying(2048) DEFAULT NULL::character varying,
    launch_date timestamp without time zone,
    task_deadline timestamp without time zone,
    tbt_phase integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_schedule_challenge OWNER TO postgres;

--
-- Name: tbt_schedule_challenge_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_schedule_challenge_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_schedule_challenge_id_seq OWNER TO postgres;

--
-- Name: tbt_schedule_challenge_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_schedule_challenge_id_seq OWNED BY public.tbt_schedule_challenge.id;


--
-- Name: tbt_schedule_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_schedule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_schedule_id_seq OWNER TO postgres;

--
-- Name: tbt_schedule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_schedule_id_seq OWNED BY public.tbt_schedule.id;


--
-- Name: tbt_status_challenge; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_status_challenge (
    id integer NOT NULL,
    team_id integer NOT NULL,
    i_agree_challenge integer DEFAULT 0 NOT NULL,
    task1_arena_uploaded integer DEFAULT 0 NOT NULL,
    task1_arena_upload_time timestamp without time zone,
    task1_file_name character varying(64) DEFAULT NULL::character varying,
    task1_arena_marks real,
    task1_arena_remark character varying(1024) DEFAULT NULL::character varying,
    task2_video_uploaded integer DEFAULT 0 NOT NULL,
    task2_video_link character varying(256) DEFAULT NULL::character varying,
    task2_video_upload_time timestamp without time zone,
    task2_code_uploaded integer DEFAULT 0 NOT NULL,
    task2_code_upload_time timestamp without time zone,
    challenge_task2_total_marks real,
    task2_total_remark character varying(1024) DEFAULT NULL::character varying,
    challenge_result character varying(256) DEFAULT NULL::character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_status_challenge OWNER TO postgres;

--
-- Name: tbt_status_challenge_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_status_challenge_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_status_challenge_id_seq OWNER TO postgres;

--
-- Name: tbt_status_challenge_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_status_challenge_id_seq OWNED BY public.tbt_status_challenge.id;


--
-- Name: tbt_status_complete; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_status_complete (
    id integer NOT NULL,
    team_id integer NOT NULL,
    task0_noc integer DEFAULT 0 NOT NULL,
    task1_status integer DEFAULT 0 NOT NULL,
    task1_bonus_marks integer,
    task1_total_marks real,
    task1_graded integer DEFAULT 0 NOT NULL,
    task2_status integer DEFAULT 0 NOT NULL,
    task2_bonus_marks integer,
    task2_total_marks real,
    task2_graded integer DEFAULT 0 NOT NULL,
    task3_status integer DEFAULT 0 NOT NULL,
    task3_bonus_marks integer,
    task3_total_marks real,
    task3_graded integer DEFAULT 0 NOT NULL,
    task4_status integer DEFAULT 0 NOT NULL,
    task4_bonus_marks integer,
    task4_total_marks real,
    task4_graded integer DEFAULT 0 NOT NULL,
    task5_status integer DEFAULT 0 NOT NULL,
    task5_bonus_marks integer,
    task5_total_marks real,
    task5_graded integer DEFAULT 0 NOT NULL,
    task6_status integer DEFAULT 0 NOT NULL,
    task6_bonus_marks integer,
    task6_total_marks real,
    task6_graded integer DEFAULT 0 NOT NULL,
    tbt_completed integer DEFAULT 0 NOT NULL,
    award_grade character varying(64) DEFAULT NULL::character varying,
    names_ok integer DEFAULT 0 NOT NULL,
    bonus_task_downloaded integer,
    profile_photo_request integer DEFAULT 0 NOT NULL,
    completed_in_days integer,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_status_complete OWNER TO postgres;

--
-- Name: tbt_status_complete_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_status_complete_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_status_complete_id_seq OWNER TO postgres;

--
-- Name: tbt_status_complete_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_status_complete_id_seq OWNED BY public.tbt_status_complete.id;


--
-- Name: tbt_status_experiment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_status_experiment (
    id integer NOT NULL,
    team_id integer NOT NULL,
    task1_version integer DEFAULT 1 NOT NULL,
    task2_version integer DEFAULT 1 NOT NULL,
    task3_version integer DEFAULT 1 NOT NULL,
    task4_version integer DEFAULT 1 NOT NULL,
    task5_version integer DEFAULT 1 NOT NULL,
    task6_version integer DEFAULT 1 NOT NULL,
    task1_uploaded integer DEFAULT 0 NOT NULL,
    task1_upload_time timestamp without time zone,
    task1_marks real,
    task1_remark character varying(1024) DEFAULT NULL::character varying,
    task2_uploaded integer DEFAULT 0 NOT NULL,
    task2_upload_time timestamp without time zone,
    task2_marks real,
    task2_remark character varying(1024) DEFAULT NULL::character varying,
    task3_uploaded integer DEFAULT 0 NOT NULL,
    task3_upload_time timestamp without time zone,
    task3_marks real,
    task3_remark character varying(1024) DEFAULT NULL::character varying,
    task4_uploaded integer DEFAULT 0 NOT NULL,
    task4_upload_time timestamp without time zone,
    task4_marks real,
    task4_remark character varying(1024) DEFAULT NULL::character varying,
    task5_uploaded integer DEFAULT 0 NOT NULL,
    task5_upload_time timestamp without time zone,
    task5_marks real,
    task5_remark character varying(1024) DEFAULT NULL::character varying,
    task6_uploaded integer DEFAULT 0 NOT NULL,
    task6_upload_time timestamp without time zone,
    task6_marks real,
    task6_remark character varying(1024) DEFAULT NULL::character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_status_experiment OWNER TO postgres;

--
-- Name: COLUMN tbt_status_experiment.task1_uploaded; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.tbt_status_experiment.task1_uploaded IS '0=not submitted,1=saved,2=submitted,4=incomplete';


--
-- Name: tbt_status_experiment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_status_experiment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_status_experiment_id_seq OWNER TO postgres;

--
-- Name: tbt_status_experiment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_status_experiment_id_seq OWNED BY public.tbt_status_experiment.id;


--
-- Name: tbt_status_mcq; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_status_mcq (
    id integer NOT NULL,
    team_id integer NOT NULL,
    task1_mcq_status integer DEFAULT 0 NOT NULL,
    task1_mcq_time timestamp without time zone,
    task1_mcq_version integer DEFAULT 1 NOT NULL,
    task1_mcq_marks real,
    task2_mcq_status integer DEFAULT 0 NOT NULL,
    task2_mcq_time timestamp without time zone,
    task2_mcq_version integer DEFAULT 1 NOT NULL,
    task2_mcq_marks real,
    task3_mcq_status integer DEFAULT 0 NOT NULL,
    task3_mcq_time timestamp without time zone,
    task3_mcq_version integer DEFAULT 1 NOT NULL,
    task3_mcq_marks real,
    task4_mcq_status integer DEFAULT 0 NOT NULL,
    task4_mcq_time timestamp without time zone,
    task4_mcq_version integer DEFAULT 1 NOT NULL,
    task4_mcq_marks real,
    task5_mcq_status integer DEFAULT 0 NOT NULL,
    task5_mcq_time timestamp without time zone,
    task5_mcq_version integer DEFAULT 1 NOT NULL,
    task5_mcq_marks real,
    task6_mcq_status integer DEFAULT 0 NOT NULL,
    task6_mcq_time timestamp without time zone,
    task6_mcq_version integer DEFAULT 1 NOT NULL,
    task6_mcq_marks real,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_status_mcq OWNER TO postgres;

--
-- Name: tbt_status_mcq_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_status_mcq_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_status_mcq_id_seq OWNER TO postgres;

--
-- Name: tbt_status_mcq_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_status_mcq_id_seq OWNED BY public.tbt_status_mcq.id;


--
-- Name: tbt_teachers_dtls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_teachers_dtls (
    id integer NOT NULL,
    user_id integer,
    tbt_clg_id integer NOT NULL,
    team_id integer DEFAULT 0 NOT NULL,
    elsi_tch_id integer,
    name character varying(512) DEFAULT NULL::character varying,
    name_on_cheque character varying(1024) DEFAULT NULL::character varying,
    cheque_issued character varying(255) DEFAULT NULL::character varying,
    account_number character varying(512) DEFAULT NULL::character varying,
    account_holders_name character varying(512) DEFAULT NULL::character varying,
    bank_name character varying(512) DEFAULT NULL::character varying,
    bank_address character varying(512) DEFAULT NULL::character varying,
    account_type character varying(512) DEFAULT NULL::character varying,
    "IFSC_code" character varying(512) DEFAULT NULL::character varying,
    bankdtl_added_date timestamp without time zone,
    emailid character varying(256) DEFAULT NULL::character varying,
    alt_email1 character varying(256) DEFAULT NULL::character varying,
    alt_email2 character varying(256) DEFAULT NULL::character varying,
    contact_num character varying(25) DEFAULT NULL::character varying,
    alt_contact1 character varying(50) DEFAULT NULL::character varying,
    alt_contact2 character varying(50) DEFAULT NULL::character varying,
    department character varying(128) DEFAULT NULL::character varying,
    designation character varying(30) DEFAULT NULL::character varying,
    gender character varying(15) DEFAULT NULL::character varying,
    coor_flag integer DEFAULT 0 NOT NULL,
    tbt_flag integer DEFAULT 0 NOT NULL,
    submitted_to_office integer DEFAULT 0,
    submitted_to_cert_team integer DEFAULT 0,
    "Remark" character varying(516) DEFAULT NULL::character varying,
    login_created integer DEFAULT 0 NOT NULL,
    profile_photo character varying(50) DEFAULT NULL::character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_teachers_dtls OWNER TO postgres;

--
-- Name: tbt_teachers_dtls_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_teachers_dtls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_teachers_dtls_id_seq OWNER TO postgres;

--
-- Name: tbt_teachers_dtls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_teachers_dtls_id_seq OWNED BY public.tbt_teachers_dtls.id;


--
-- Name: tbt_teams; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_teams (
    team_id integer NOT NULL,
    tbt_clg_id integer NOT NULL,
    tbt_phase integer NOT NULL,
    tl_id integer DEFAULT 0 NOT NULL,
    tm1_id integer DEFAULT 0,
    tm2_id integer DEFAULT 0,
    tm3_id integer DEFAULT 0,
    year character varying(16) DEFAULT NULL::character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_teams OWNER TO postgres;

--
-- Name: tbt_teams_schedule; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_teams_schedule (
    id integer NOT NULL,
    team_id integer,
    launch_date timestamp without time zone NOT NULL,
    task0_deadline timestamp without time zone,
    task1_deadline timestamp without time zone,
    task2_deadline timestamp without time zone NOT NULL,
    task3_deadline timestamp without time zone NOT NULL,
    task4_deadline timestamp without time zone NOT NULL,
    task5_deadline timestamp without time zone NOT NULL,
    task6_deadline timestamp without time zone NOT NULL,
    absolute_deadline timestamp without time zone NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.tbt_teams_schedule OWNER TO postgres;

--
-- Name: tbt_teams_schedule_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_teams_schedule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_teams_schedule_id_seq OWNER TO postgres;

--
-- Name: tbt_teams_schedule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_teams_schedule_id_seq OWNED BY public.tbt_teams_schedule.id;


--
-- Name: tbt_teams_team_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_teams_team_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_teams_team_id_seq OWNER TO postgres;

--
-- Name: tbt_teams_team_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_teams_team_id_seq OWNED BY public.tbt_teams.team_id;


--
-- Name: tbt_tutorials; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbt_tutorials (
    id integer NOT NULL,
    task_id integer,
    tutorial_heading character varying(2048) DEFAULT NULL::character varying,
    tutorial_video_link character varying(2048) DEFAULT NULL::character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tbt_tutorials OWNER TO postgres;

--
-- Name: tbt_tutorials_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbt_tutorials_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbt_tutorials_id_seq OWNER TO postgres;

--
-- Name: tbt_tutorials_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbt_tutorials_id_seq OWNED BY public.tbt_tutorials.id;


--
-- Name: users_login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_login (
    id integer NOT NULL,
    team_id integer,
    username character varying(512) DEFAULT NULL::character varying NOT NULL,
    password character varying(1024) DEFAULT NULL::character varying,
    tbt integer DEFAULT 0 NOT NULL,
    active integer NOT NULL,
    agree integer DEFAULT 0 NOT NULL,
    token character varying(1024) DEFAULT NULL::character varying,
    last_login timestamp without time zone,
    login_count integer,
    change_count integer DEFAULT 0 NOT NULL,
    forgot_count integer DEFAULT 0 NOT NULL,
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
-- Name: departments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.departments ALTER COLUMN id SET DEFAULT nextval('public.departments_id_seq'::regclass);


--
-- Name: designations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.designations ALTER COLUMN id SET DEFAULT nextval('public.designations_id_seq'::regclass);


--
-- Name: elsi_region id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_region ALTER COLUMN id SET DEFAULT nextval('public.elsi_region_id_seq'::regclass);


--
-- Name: region id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.region ALTER COLUMN id SET DEFAULT nextval('public.region_id_seq'::regclass);


--
-- Name: state id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.state ALTER COLUMN id SET DEFAULT nextval('public.state_id_seq'::regclass);


--
-- Name: tbt_challenge_master id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_challenge_master ALTER COLUMN id SET DEFAULT nextval('public.tbt_challenge_master_id_seq'::regclass);


--
-- Name: tbt_challenge_team_schedule id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_challenge_team_schedule ALTER COLUMN id SET DEFAULT nextval('public.tbt_challenge_team_schedule_id_seq'::regclass);


--
-- Name: tbt_clg_contact_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_clg_contact_dtls ALTER COLUMN id SET DEFAULT nextval('public.tbt_clg_contact_dtls_id_seq'::regclass);


--
-- Name: tbt_college_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_college_dtls ALTER COLUMN id SET DEFAULT nextval('public.tbt_college_dtls_id_seq'::regclass);


--
-- Name: tbt_experiment_master id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_experiment_master ALTER COLUMN id SET DEFAULT nextval('public.tbt_experiment_master_id_seq'::regclass);


--
-- Name: tbt_feedback id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_feedback ALTER COLUMN id SET DEFAULT nextval('public.tbt_feedback_id_seq'::regclass);


--
-- Name: tbt_mcq_master id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_master ALTER COLUMN id SET DEFAULT nextval('public.tbt_mcq_master_id_seq'::regclass);


--
-- Name: tbt_mcq_task1_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task1_dtls ALTER COLUMN id SET DEFAULT nextval('public.tbt_mcq_task1_dtls_id_seq'::regclass);


--
-- Name: tbt_mcq_task2_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task2_dtls ALTER COLUMN id SET DEFAULT nextval('public.tbt_mcq_task2_dtls_id_seq'::regclass);


--
-- Name: tbt_mcq_task3_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task3_dtls ALTER COLUMN id SET DEFAULT nextval('public.tbt_mcq_task3_dtls_id_seq'::regclass);


--
-- Name: tbt_mcq_task4_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task4_dtls ALTER COLUMN id SET DEFAULT nextval('public.tbt_mcq_task4_dtls_id_seq'::regclass);


--
-- Name: tbt_mcq_task5_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task5_dtls ALTER COLUMN id SET DEFAULT nextval('public.tbt_mcq_task5_dtls_id_seq'::regclass);


--
-- Name: tbt_mcq_task6_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task6_dtls ALTER COLUMN id SET DEFAULT nextval('public.tbt_mcq_task6_dtls_id_seq'::regclass);


--
-- Name: tbt_mcq_task_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task_dtls ALTER COLUMN id SET DEFAULT nextval('public.tbt_mcq_task_dtls_id_seq'::regclass);


--
-- Name: tbt_schedule id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_schedule ALTER COLUMN id SET DEFAULT nextval('public.tbt_schedule_id_seq'::regclass);


--
-- Name: tbt_schedule_challenge id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_schedule_challenge ALTER COLUMN id SET DEFAULT nextval('public.tbt_schedule_challenge_id_seq'::regclass);


--
-- Name: tbt_status_challenge id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_status_challenge ALTER COLUMN id SET DEFAULT nextval('public.tbt_status_challenge_id_seq'::regclass);


--
-- Name: tbt_status_complete id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_status_complete ALTER COLUMN id SET DEFAULT nextval('public.tbt_status_complete_id_seq'::regclass);


--
-- Name: tbt_status_experiment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_status_experiment ALTER COLUMN id SET DEFAULT nextval('public.tbt_status_experiment_id_seq'::regclass);


--
-- Name: tbt_status_mcq id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_status_mcq ALTER COLUMN id SET DEFAULT nextval('public.tbt_status_mcq_id_seq'::regclass);


--
-- Name: tbt_teachers_dtls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_teachers_dtls ALTER COLUMN id SET DEFAULT nextval('public.tbt_teachers_dtls_id_seq'::regclass);


--
-- Name: tbt_teams team_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_teams ALTER COLUMN team_id SET DEFAULT nextval('public.tbt_teams_team_id_seq'::regclass);


--
-- Name: tbt_teams_schedule id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_teams_schedule ALTER COLUMN id SET DEFAULT nextval('public.tbt_teams_schedule_id_seq'::regclass);


--
-- Name: tbt_tutorials id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_tutorials ALTER COLUMN id SET DEFAULT nextval('public.tbt_tutorials_id_seq'::regclass);


--
-- Name: users_login id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_login ALTER COLUMN id SET DEFAULT nextval('public.users_login_id_seq'::regclass);


--
-- Data for Name: departments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.departments (id, name, main_branch) FROM stdin;
\.


--
-- Data for Name: designations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.designations (id, name, type) FROM stdin;
\.


--
-- Data for Name: elsi_region; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.elsi_region (id, region_name, type, active, clg_id, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: region; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.region (id, region_name, type, active, clg_id, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: state; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.state (id, state) FROM stdin;
\.


--
-- Data for Name: tbt_challenge_master; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_challenge_master (id, theme, description, create_at, update_at) FROM stdin;
\.


--
-- Data for Name: tbt_challenge_team_schedule; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_challenge_team_schedule (id, team_id, theme_id, launch_date, task1_deadline, task2_deadline, tbt_phase, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_clg_contact_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_clg_contact_dtls (id, tbt_clg_id, name, emailid, gender, branch, alt_email1, alt_email2, alt_email3, contact_num, alt_contact1, alt_contact2, alt_contact3, designation, type, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_college_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_college_dtls (id, elsi_clg_id, region_id, college_name, abbreviation, district, address, state, pincode, college_type, principal_meet, robots_given, tbt_allowed, tbt_count, completed, legal_docs, legal_docs_remarks, loi_status, po_status, po_remark, wo_reg, wo_invite, wo_confirm, wo_attend, phase, lab_inaugrated, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_competition; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_competition (id, year, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_experiment_master; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_experiment_master (id, task_id, ex_version_id, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_feedback; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_feedback (id, team_id, usr_id, teacher_name, email_id, question1, question2, question3, question4, question5, question6, question7, question8, question9, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_mcq_master; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_mcq_master (id, question_id, mcq_version_id, question_text, option_1, option_2, option_3, option_4, option_5, correct_option, answer_explanation, task, tbt_phase, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_mcq_task1_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_mcq_task1_dtls (id, team_id, question_id, choosen_option, save_count, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_mcq_task2_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_mcq_task2_dtls (id, team_id, question_id, choosen_option, save_count, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_mcq_task3_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_mcq_task3_dtls (id, team_id, question_id, choosen_option, save_count, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_mcq_task4_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_mcq_task4_dtls (id, team_id, question_id, choosen_option, save_count, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_mcq_task5_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_mcq_task5_dtls (id, team_id, question_id, choosen_option, save_count, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_mcq_task6_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_mcq_task6_dtls (id, team_id, question_id, choosen_option, save_count, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_mcq_task_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_mcq_task_dtls (id, task, team_id, question_id, chosen_option, save_count, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_schedule; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_schedule (id, task_number, tasks, launch_date, task_deadline, absolute_deadline, tbt_phase, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_schedule_challenge; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_schedule_challenge (id, task_number, tasks, launch_date, task_deadline, tbt_phase, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_status_challenge; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_status_challenge (id, team_id, i_agree_challenge, task1_arena_uploaded, task1_arena_upload_time, task1_file_name, task1_arena_marks, task1_arena_remark, task2_video_uploaded, task2_video_link, task2_video_upload_time, task2_code_uploaded, task2_code_upload_time, challenge_task2_total_marks, task2_total_remark, challenge_result, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_status_complete; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_status_complete (id, team_id, task0_noc, task1_status, task1_bonus_marks, task1_total_marks, task1_graded, task2_status, task2_bonus_marks, task2_total_marks, task2_graded, task3_status, task3_bonus_marks, task3_total_marks, task3_graded, task4_status, task4_bonus_marks, task4_total_marks, task4_graded, task5_status, task5_bonus_marks, task5_total_marks, task5_graded, task6_status, task6_bonus_marks, task6_total_marks, task6_graded, tbt_completed, award_grade, names_ok, bonus_task_downloaded, profile_photo_request, completed_in_days, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_status_experiment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_status_experiment (id, team_id, task1_version, task2_version, task3_version, task4_version, task5_version, task6_version, task1_uploaded, task1_upload_time, task1_marks, task1_remark, task2_uploaded, task2_upload_time, task2_marks, task2_remark, task3_uploaded, task3_upload_time, task3_marks, task3_remark, task4_uploaded, task4_upload_time, task4_marks, task4_remark, task5_uploaded, task5_upload_time, task5_marks, task5_remark, task6_uploaded, task6_upload_time, task6_marks, task6_remark, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_status_mcq; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_status_mcq (id, team_id, task1_mcq_status, task1_mcq_time, task1_mcq_version, task1_mcq_marks, task2_mcq_status, task2_mcq_time, task2_mcq_version, task2_mcq_marks, task3_mcq_status, task3_mcq_time, task3_mcq_version, task3_mcq_marks, task4_mcq_status, task4_mcq_time, task4_mcq_version, task4_mcq_marks, task5_mcq_status, task5_mcq_time, task5_mcq_version, task5_mcq_marks, task6_mcq_status, task6_mcq_time, task6_mcq_version, task6_mcq_marks, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_teachers_dtls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_teachers_dtls (id, user_id, tbt_clg_id, team_id, elsi_tch_id, name, name_on_cheque, cheque_issued, account_number, account_holders_name, bank_name, bank_address, account_type, "IFSC_code", bankdtl_added_date, emailid, alt_email1, alt_email2, contact_num, alt_contact1, alt_contact2, department, designation, gender, coor_flag, tbt_flag, submitted_to_office, submitted_to_cert_team, "Remark", login_created, profile_photo, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_teams; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_teams (team_id, tbt_clg_id, tbt_phase, tl_id, tm1_id, tm2_id, tm3_id, year, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_teams_schedule; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_teams_schedule (id, team_id, launch_date, task0_deadline, task1_deadline, task2_deadline, task3_deadline, task4_deadline, task5_deadline, task6_deadline, absolute_deadline, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: tbt_tutorials; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbt_tutorials (id, task_id, tutorial_heading, tutorial_video_link, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: users_login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_login (id, team_id, username, password, tbt, active, agree, token, last_login, login_count, change_count, forgot_count, remember_token, created_at, updated_at) FROM stdin;
\.


--
-- Name: departments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.departments_id_seq', 1, false);


--
-- Name: designations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.designations_id_seq', 1, false);


--
-- Name: elsi_region_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.elsi_region_id_seq', 1, false);


--
-- Name: region_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.region_id_seq', 1, false);


--
-- Name: state_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.state_id_seq', 1, false);


--
-- Name: tbt_challenge_master_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_challenge_master_id_seq', 1, false);


--
-- Name: tbt_challenge_team_schedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_challenge_team_schedule_id_seq', 1, false);


--
-- Name: tbt_clg_contact_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_clg_contact_dtls_id_seq', 1, false);


--
-- Name: tbt_college_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_college_dtls_id_seq', 1, false);


--
-- Name: tbt_experiment_master_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_experiment_master_id_seq', 1, false);


--
-- Name: tbt_feedback_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_feedback_id_seq', 1, false);


--
-- Name: tbt_mcq_master_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_mcq_master_id_seq', 1, false);


--
-- Name: tbt_mcq_task1_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_mcq_task1_dtls_id_seq', 1, false);


--
-- Name: tbt_mcq_task2_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_mcq_task2_dtls_id_seq', 1, false);


--
-- Name: tbt_mcq_task3_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_mcq_task3_dtls_id_seq', 1, false);


--
-- Name: tbt_mcq_task4_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_mcq_task4_dtls_id_seq', 1, false);


--
-- Name: tbt_mcq_task5_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_mcq_task5_dtls_id_seq', 1, false);


--
-- Name: tbt_mcq_task6_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_mcq_task6_dtls_id_seq', 1, false);


--
-- Name: tbt_mcq_task_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_mcq_task_dtls_id_seq', 1, false);


--
-- Name: tbt_schedule_challenge_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_schedule_challenge_id_seq', 1, false);


--
-- Name: tbt_schedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_schedule_id_seq', 1, false);


--
-- Name: tbt_status_challenge_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_status_challenge_id_seq', 1, false);


--
-- Name: tbt_status_complete_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_status_complete_id_seq', 1, false);


--
-- Name: tbt_status_experiment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_status_experiment_id_seq', 1, false);


--
-- Name: tbt_status_mcq_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_status_mcq_id_seq', 1, false);


--
-- Name: tbt_teachers_dtls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_teachers_dtls_id_seq', 1, false);


--
-- Name: tbt_teams_schedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_teams_schedule_id_seq', 1, false);


--
-- Name: tbt_teams_team_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_teams_team_id_seq', 1, false);


--
-- Name: tbt_tutorials_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbt_tutorials_id_seq', 1, false);


--
-- Name: users_login_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_login_id_seq', 1, false);


--
-- Name: departments departments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_pkey PRIMARY KEY (id);


--
-- Name: designations designations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.designations
    ADD CONSTRAINT designations_pkey PRIMARY KEY (id);


--
-- Name: elsi_region elsi_region_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.elsi_region
    ADD CONSTRAINT elsi_region_pkey PRIMARY KEY (id);


--
-- Name: region region_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.region
    ADD CONSTRAINT region_pkey PRIMARY KEY (id);


--
-- Name: state state_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.state
    ADD CONSTRAINT state_pkey PRIMARY KEY (id);


--
-- Name: tbt_challenge_master tbt_challenge_master_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_challenge_master
    ADD CONSTRAINT tbt_challenge_master_pkey PRIMARY KEY (id);


--
-- Name: tbt_challenge_team_schedule tbt_challenge_team_schedule_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_challenge_team_schedule
    ADD CONSTRAINT tbt_challenge_team_schedule_pkey PRIMARY KEY (id);


--
-- Name: tbt_clg_contact_dtls tbt_clg_contact_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_clg_contact_dtls
    ADD CONSTRAINT tbt_clg_contact_dtls_pkey PRIMARY KEY (id);


--
-- Name: tbt_college_dtls tbt_college_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_college_dtls
    ADD CONSTRAINT tbt_college_dtls_pkey PRIMARY KEY (id);


--
-- Name: tbt_competition tbt_competition_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_competition
    ADD CONSTRAINT tbt_competition_pkey PRIMARY KEY (id);


--
-- Name: tbt_experiment_master tbt_experiment_master_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_experiment_master
    ADD CONSTRAINT tbt_experiment_master_pkey PRIMARY KEY (id);


--
-- Name: tbt_feedback tbt_feedback_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_feedback
    ADD CONSTRAINT tbt_feedback_pkey PRIMARY KEY (id);


--
-- Name: tbt_mcq_master tbt_mcq_master_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_master
    ADD CONSTRAINT tbt_mcq_master_pkey PRIMARY KEY (id);


--
-- Name: tbt_mcq_task1_dtls tbt_mcq_task1_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task1_dtls
    ADD CONSTRAINT tbt_mcq_task1_dtls_pkey PRIMARY KEY (id);


--
-- Name: tbt_mcq_task2_dtls tbt_mcq_task2_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task2_dtls
    ADD CONSTRAINT tbt_mcq_task2_dtls_pkey PRIMARY KEY (id);


--
-- Name: tbt_mcq_task3_dtls tbt_mcq_task3_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task3_dtls
    ADD CONSTRAINT tbt_mcq_task3_dtls_pkey PRIMARY KEY (id);


--
-- Name: tbt_mcq_task4_dtls tbt_mcq_task4_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task4_dtls
    ADD CONSTRAINT tbt_mcq_task4_dtls_pkey PRIMARY KEY (id);


--
-- Name: tbt_mcq_task5_dtls tbt_mcq_task5_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task5_dtls
    ADD CONSTRAINT tbt_mcq_task5_dtls_pkey PRIMARY KEY (id);


--
-- Name: tbt_mcq_task6_dtls tbt_mcq_task6_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task6_dtls
    ADD CONSTRAINT tbt_mcq_task6_dtls_pkey PRIMARY KEY (id);


--
-- Name: tbt_mcq_task_dtls tbt_mcq_task_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_mcq_task_dtls
    ADD CONSTRAINT tbt_mcq_task_dtls_pkey PRIMARY KEY (id);


--
-- Name: tbt_schedule_challenge tbt_schedule_challenge_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_schedule_challenge
    ADD CONSTRAINT tbt_schedule_challenge_pkey PRIMARY KEY (id);


--
-- Name: tbt_schedule tbt_schedule_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_schedule
    ADD CONSTRAINT tbt_schedule_pkey PRIMARY KEY (id);


--
-- Name: tbt_status_challenge tbt_status_challenge_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_status_challenge
    ADD CONSTRAINT tbt_status_challenge_pkey PRIMARY KEY (id);


--
-- Name: tbt_status_complete tbt_status_complete_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_status_complete
    ADD CONSTRAINT tbt_status_complete_pkey PRIMARY KEY (id);


--
-- Name: tbt_status_experiment tbt_status_experiment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_status_experiment
    ADD CONSTRAINT tbt_status_experiment_pkey PRIMARY KEY (id);


--
-- Name: tbt_status_mcq tbt_status_mcq_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_status_mcq
    ADD CONSTRAINT tbt_status_mcq_pkey PRIMARY KEY (id);


--
-- Name: tbt_teachers_dtls tbt_teachers_dtls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_teachers_dtls
    ADD CONSTRAINT tbt_teachers_dtls_pkey PRIMARY KEY (id);


--
-- Name: tbt_teams tbt_teams_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_teams
    ADD CONSTRAINT tbt_teams_pkey PRIMARY KEY (team_id);


--
-- Name: tbt_teams_schedule tbt_teams_schedule_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_teams_schedule
    ADD CONSTRAINT tbt_teams_schedule_pkey PRIMARY KEY (id);


--
-- Name: tbt_tutorials tbt_tutorials_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbt_tutorials
    ADD CONSTRAINT tbt_tutorials_pkey PRIMARY KEY (id);


--
-- Name: users_login users_login_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_login
    ADD CONSTRAINT users_login_pkey PRIMARY KEY (id);


--
-- Name: public_tbt_competition_id0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_tbt_competition_id0_idx ON public.tbt_competition USING btree (id);


--
-- Name: public_tbt_feedback_id0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_tbt_feedback_id0_idx ON public.tbt_feedback USING btree (id);


--
-- Name: public_users_login_username0_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX public_users_login_username0_idx ON public.users_login USING btree (username);


--
-- PostgreSQL database dump complete
--

