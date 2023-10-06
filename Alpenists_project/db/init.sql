CREATE DATABASE IF NOT EXISTS alpenists;
USE alpenists;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> a9bb40cf8a34

CREATE TABLE climbers (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    fio VARCHAR(100) NOT NULL, 
    address VARCHAR(100) NOT NULL, 
    CONSTRAINT pk_climbers PRIMARY KEY (id)
);

CREATE TABLE `groups` (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    name VARCHAR(100) NOT NULL, 
    CONSTRAINT pk_groups PRIMARY KEY (id)
);

CREATE TABLE mountains (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    name VARCHAR(100) NOT NULL, 
    height INTEGER NOT NULL, 
    coutry VARCHAR(100) NOT NULL, 
    district VARCHAR(100), 
    CONSTRAINT pk_mountains PRIMARY KEY (id)
);

CREATE TABLE users (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    login VARCHAR(100) NOT NULL, 
    password_hash VARCHAR(200) NOT NULL, 
    CONSTRAINT pk_users PRIMARY KEY (id), 
    CONSTRAINT uq_users_login UNIQUE (login)
);

CREATE TABLE climbers_groups (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    climbers_id INTEGER NOT NULL, 
    group_id INTEGER NOT NULL, 
    CONSTRAINT pk_climbers_groups PRIMARY KEY (id), 
    CONSTRAINT fk_climbers_groups_climbers_id_climbers FOREIGN KEY(climbers_id) REFERENCES climbers (id), 
    CONSTRAINT fk_climbers_groups_group_id_groups FOREIGN KEY(group_id) REFERENCES `groups` (id)
);

CREATE TABLE climbings (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    date_start DATETIME NOT NULL, 
    date_end DATETIME NOT NULL, 
    mountains_id INTEGER NOT NULL, 
    group_id INTEGER NOT NULL, 
    CONSTRAINT pk_climbings PRIMARY KEY (id), 
    CONSTRAINT fk_climbings_group_id_groups FOREIGN KEY(group_id) REFERENCES `groups` (id), 
    CONSTRAINT fk_climbings_mountains_id_mountains FOREIGN KEY(mountains_id) REFERENCES mountains (id)
);

INSERT INTO alembic_version (version_num) VALUES ('a9bb40cf8a34');

