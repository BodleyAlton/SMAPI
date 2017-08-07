create table client (
cid serial,
contact int,
first_name varchar(40),
last_name varchar(40),
address_1 varchar(60),
address_2 varchar(60),
city varchar(60),
parish varchar(12),
date_created date,
primary key(cid)
);

create table product (
pid serial,
title varchar(50),
descr varchar(70),
status varchar(10),
weight float(4),
leng float(4),
weidth float(4),
height float(4),
primary key(pid)
);

create table files (
fid serial,
file_type varchar(5),
file_path varchar(40),
file_name varchar(30),
primary key(fid)
);

create table own(
pid int,
cid int,
primary key (pid,cid),
foreign key (pid) references product(pid) on delete cascade on update cascade,
foreign key (cid) references client(cid) on delete cascade on update cascade
);

create table assoc(
pid int,
fid int,
primary key(pid,fid),
foreign key (pid) references product(pid) on delete cascade on update cascade,
foreign key (fid) references files(fid) on delete cascade on update cascade
);

create table auth(
id int,
username varchar(30),
password varchar(80),
role varchar(300),
primary key(id,username),
foreign key(id) references client(cid) on delete cascade on update cascade
);