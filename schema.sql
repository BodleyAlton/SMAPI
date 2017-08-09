drop database if exists smapi;

create database smapi with owner= admin;

\c smapi;

create table client (
cid serial,
username varchar UNIQUE,
contact varchar,
first_name varchar,
last_name varchar,
trn int not null,
address_1 varchar,
address_2 varchar,
city varchar,
parish varchar,
country varchar,
date_created date,
primary key(cid)

);

create table product (
pid serial,
billNo int,
title varchar,
descr varchar,
status varchar,
weight float,
leng float,
width float,
height float,
primary key(pid)
);

create table files (
fid serial,
file_type varchar,
file_path varchar,
file_name varchar,
primary key(fid)
);

create table invoice(
pid int,
cid int,
fid int,
orderNum int,
primary key (pid,cid,fid),
foreign key (pid) references product(pid) on delete cascade on update cascade,
foreign key (cid) references client(cid) on delete cascade on update cascade,
foreign key (fid) references files(fid) on delete cascade on update cascade
);

-- create table assoc(
-- pid int,
-- fid int,
-- cid int,
-- primary key(pid,fid),
-- foreign key (pid) references product(pid) on delete cascade on update cascade,
-- foreign key (fid) references files(fid) on delete cascade on update cascade
-- foreign key (cid) references client(cid) on delete cascade on update cascade
-- );

create table auth(
id serial,
username varchar(30),
password varchar(80),
role varchar(300),
primary key(id,username),
foreign key(username) references client(username) on delete cascade on update cascade
);