CREATE TABLE members(
    _ID integer NOT NULL Primary key,
    email varchar(50) NOT NULL UNIQUE,
    pw varchar(50) NOT NULL,
    first_name varchar(50),
    last_name varchar(50),
    phone_number varchar(50),
    birthday date,
    gender char(1),
    membership_type_id integer,
    duration_group_id integer,
    role_id integer
);


CREATE TABLE age_groups(
    _ID integer NOT NULL Primary key,
    discount integer NOT NULL
);


CREATE TABLE sports(
    _ID integer NOT NULL Primary key,
    sport_name varchar(50),
    sport_type varchar(50),
    professionalism boolean
);


CREATE TABLE professionalisms(
    _ID integer NOT NULL Primary key,
    prof_name varchar(50),
    discount integer
);


CREATE TABLE roles(
    _ID integer NOT NULL Primary key,
    role_name varchar(50),
    all_rights boolean,
    most_rights boolean
);


CREATE TABLE duration_groups(
    _ID integer NOT NULL Primary key,
    group_name varchar(50),
    discount integer
);


CREATE TABLE memberships(
    _ID integer NOT NULL Primary key,
    discount integer
);
