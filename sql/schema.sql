CREATE TABLE members(
    member_ID integer NOT NULL Primary key,
    email varchar(50) NOT NULL UNIQUE,
    pw varchar(50) NOT NULL
);

CREATE TABLE members_info(
    email varchar(50) NOT NULL Primary key,
    first_name varchar(50),
    last_name varchar(50),
    phone_number varchar(50),
    birthday date,
    gender char(1),
    membership_type_ID integer,
    duration_group_ID integer,
    role_ID integer,
    sport_ID integer
);


CREATE TABLE age_groups(
    age_group_ID integer NOT NULL Primary key,
    age_group_name varchar(50),
    discount integer NOT NULL
);


CREATE TABLE sports(
    sport_ID integer NOT NULL Primary key,
    sport_name varchar(50),
    sport_type varchar(50),
    professionalism boolean
);


CREATE TABLE professionalisms(
    professionalism_ID integer NOT NULL Primary key,
    prof_name varchar(50),
    discount integer
);


CREATE TABLE roles(
    role_ID integer NOT NULL Primary key,
    role_name varchar(50),
    all_rights boolean,
    most_rights boolean,
    some_rights boolean
);


CREATE TABLE duration_groups(
    duration_group_ID integer NOT NULL Primary key,
    duration_group_name varchar(50),
    discount integer
);


CREATE TABLE memberships(
    membership_ID integer NOT NULL Primary key,
    membership_name varchar(50),
    price integer
);


-- ALTER TABLE members ADD FOREIGN KEY (email) REFERENCES members_info(email) ON DELETE CASCADE ON UPDATE CASCADE;