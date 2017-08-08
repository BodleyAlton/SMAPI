drop database if exists smapi;

create database smapi with owner= admin;

\c smapi;

create table client (
cid serial,
contact varchar,
first_name varchar,
last_name varchar,
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

INSERT INTO product (pid, title, descr, status, weight, leng, width, height) VALUES (1, 'dewalt power tools . 38inch heavy-duty vsr pistol grip drill with keyless chuck dwd', 'Scelerisque pulvinar metus orci dictumst dolor placerat viverra vitae. Mattis.', 'arrived', 43.16, 86.26, 33.43, 93.30);
INSERT INTO product (pid, title, descr, status, weight, leng, width, height) VALUES (2, 'hitachi 18 v ni-cad cordless driver drill', 'Mi laoreet duis placerat ipsum urna vel tristique cras posuere.', 'delivered', 44.21, 41.75, 20.32, 54.99);
INSERT INTO product (pid, title, descr, status, weight, leng, width, height) VALUES (3, 'numax 21-degree 3-1/2" framing nailer', 'Sociosqu molestie risus interdum in imperdiet pellentesque at dictumst. Urna.', 'arrived', 80.29, 24.62, 56.24, 53.59);
INSERT INTO product (pid, title, descr, status, weight, leng, width, height) VALUES (4, 'premiere pads premiere pads 50 "400" series stainless steel scrubbers large pad50', 'Consequat feugiat inceptos elementum etiam libero sollicitudin cubilia nisl sit.', 'arrived', 35.71, 21.20, 67.16, 97.57);
INSERT INTO product (pid, title, descr, status, weight, leng, width, height) VALUES (5, 'chicago power tools power drill accessory set, 75-piece', 'Sapien et ut elementum et pharetra hac consectetur litora varius?', 'intransit', 49.76, 12.91, 53.21, 90.13);
INSERT INTO product (pid, title, descr, status, weight, leng, width, height) VALUES (6, 'hitachi 3 1/2" full-head plastic collated framing strip nailer', 'Donec aliquam platea gravida, gravida eu nam? Massa varius convallis.', 'delivered', 57.47, 45.79, 36.06, 85.44);
INSERT INTO product (pid, title, descr, status, weight, leng, width, height) VALUES (7, 'bostitch air regulator & gauge kit, 1/4 npt, btfp72326', 'Sociis dapibus risus odio donec netus tristique enim imperdiet. Aenean.', 'intransit', 56.28, 1.06, 79.21, 89.34);
INSERT INTO product (pid, title, descr, status, weight, leng, width, height) VALUES (8, 'hitachi 3.25 framing nailers nr83a2', 'Quis cras cursus malesuada rhoncus tincidunt lectus etiam elementum urna.', 'delivered', 39.23, 37.83, 19.11, 70.00);
INSERT INTO product (pid, title, descr, status, weight, leng, width, height) VALUES (9, 'stanley bostitch gr25-2 glueshot dual melt high/low temperature glue gun', 'Odio semper consectetur per tempus fusce nullam litora vivamus facilisi.', 'delivered', 55.92, 38.99, 32.99, 99.39);
INSERT INTO product (pid, title, descr, status, weight, leng, width, height) VALUES (10, 'black & decker 16" 3.4 amp powered handsaw with storage bag, phs550b', 'Donec gravida imperdiet auctor pulvinar natoque! Mus sapien in elit.', 'intransit', 34.97, 41.75, 34.69, 2.53);
INSERT INTO client (cid, contact, first_name, last_name, address_1, address_2, city, parish, country, date_created) VALUES (1, '(551) 380-4640', 'Imani', 'Stephenson', '6318 Museum Campus', 'Museum Campus', 'Raleigh', 'North Carolina', 'United States', to_date('2016-08-30', 'yyyy-mm-dd'));
INSERT INTO client (cid, contact, first_name, last_name, address_1, address_2, city, parish, country, date_created) VALUES (3, '(224) 262-1441', 'Diamond', 'Lamb', '604 Elaine', 'Elaine', 'Nashville', 'Tennessee', 'United States', to_date('2010-07-28', 'yyyy-mm-dd'));
INSERT INTO client (cid, contact, first_name, last_name, address_1, address_2, city, parish, country, date_created) VALUES (4, '(805) 721-1194', 'Charles', 'Whitney', '5913 Howard', 'Howard', 'San Francisco', 'California', 'United States', to_date('2011-05-17', 'yyyy-mm-dd'));
INSERT INTO client (cid, contact, first_name, last_name, address_1, address_2, city, parish, country, date_created) VALUES (5, '(540) 381-8061', 'Lia', 'Patterson', '5099 Parnell', 'Parnell', 'Lakewood', 'Colorado', 'United States', to_date('2010-12-28', 'yyyy-mm-dd'));
INSERT INTO client (cid, contact, first_name, last_name, address_1, address_2, city, parish, country, date_created) VALUES (6, '(516) 433-6735', 'Carley', 'Barlow', '2465 Besly', 'Besly', 'Rockford', 'Illinois', 'United States', to_date('2011-10-01', 'yyyy-mm-dd'));
INSERT INTO client (cid, contact, first_name, last_name, address_1, address_2, city, parish, country, date_created) VALUES (7, '(661) 159-0001', 'Brayan', 'Nicholson', '6736 Academy', 'Academy', 'Chula Vista', 'California', 'United States', to_date('2010-10-28', 'yyyy-mm-dd'));
INSERT INTO own (cid, pid) VALUES (7, 1);
INSERT INTO own (cid, pid) VALUES (7, 2);
INSERT INTO own (cid, pid) VALUES (7, 3);
INSERT INTO client (cid, contact, first_name, last_name, address_1, address_2, city, parish, country, date_created) VALUES (2, '(951) 749-2384', 'Naomi', 'Jacobs', '9661 Rose', 'Rose', 'Toledo', 'Ohio', 'United States', to_date('2010-11-01', 'yyyy-mm-dd'));
INSERT INTO own (cid, pid) VALUES (2, 2);
INSERT INTO own (cid, pid) VALUES (2, 3);
INSERT INTO client (cid, contact, first_name, last_name, address_1, address_2, city, parish, country, date_created) VALUES (8, '(225) 857-0044', 'Kolby', 'Delaney', '4222 71st', '71st', 'Topeka', 'Kansas', 'United States', to_date('2013-07-31', 'yyyy-mm-dd'));
INSERT INTO own (cid, pid) VALUES (8, 4);
INSERT INTO own (cid, pid) VALUES (1, 1);
INSERT INTO own (cid, pid) VALUES (3, 4);
INSERT INTO own (cid, pid) VALUES (5, 7);
INSERT INTO own (cid, pid) VALUES (5, 8);
INSERT INTO own (cid, pid) VALUES (5, 9);
INSERT INTO own (cid, pid) VALUES (4, 5);
INSERT INTO own (cid, pid) VALUES (4, 6);
INSERT INTO own (cid, pid) VALUES (6, 9);
INSERT INTO auth (id, username, password, role) VALUES (8, 'devinvaughn2106', 'Malesuada.', 'client');
INSERT INTO files (fid, file_type, file_path, file_name) VALUES (1, 'DOC', 'C:\Windows\Fonts', 'cga40866.fon');
INSERT INTO files (fid, file_type, file_path, file_name) VALUES (2, 'JPG', 'C:\Windows\Help\Windows\en-US', 'playing.H1S');
INSERT INTO files (fid, file_type, file_path, file_name) VALUES (3, 'JPG', 'C:\Windows\Cursors', 'size4_im.cur');
INSERT INTO files (fid, file_type, file_path, file_name) VALUES (4, 'DOC', 'C:\Windows\Fonts', 'gishabd.ttf');
INSERT INTO files (fid, file_type, file_path, file_name) VALUES (5, 'JPG', 'C:\Windows\Fonts', 'georgiaz.ttf');
INSERT INTO files (fid, file_type, file_path, file_name) VALUES (6, 'PDF', 'C:\Windows\Fonts', 'corbelb.ttf');
INSERT INTO files (fid, file_type, file_path, file_name) VALUES (7, 'XCLC', 'C:\Windows\Cursors', 'size3_r.cur');
INSERT INTO files (fid, file_type, file_path, file_name) VALUES (8, 'PNG', 'C:\Windows\Help\nvcpl', 'nvcplesn.chm');
INSERT INTO files (fid, file_type, file_path, file_name) VALUES (9, 'XCLC', 'C:\Windows\Fonts', 'CREDITVI.TTF');
INSERT INTO files (fid, file_type, file_path, file_name) VALUES (10, 'JPG', 'C:\Windows\Fonts', 'hvgasys.fon');
INSERT INTO assoc (pid, fid) VALUES (1, 1);
INSERT INTO assoc (pid, fid) VALUES (2, 2);
INSERT INTO assoc (pid, fid) VALUES (3, 3);
INSERT INTO assoc (pid, fid) VALUES (4, 4);
INSERT INTO assoc (pid, fid) VALUES (5, 5);
INSERT INTO assoc (pid, fid) VALUES (6, 6);
INSERT INTO assoc (pid, fid) VALUES (7, 7);
INSERT INTO assoc (pid, fid) VALUES (8, 8);
INSERT INTO assoc (pid, fid) VALUES (9, 9);
INSERT INTO assoc (pid, fid) VALUES (9, 10);
INSERT INTO auth (id, username, password, role) VALUES (1, 'elliomoon5376', 'Tellus.', 'client');
INSERT INTO auth (id, username, password, role) VALUES (2, 'cristonorto3832', 'Tempor.', 'client');
INSERT INTO auth (id, username, password, role) VALUES (3, 'genesiheat8684', 'Tellus!', 'client');
INSERT INTO auth (id, username, password, role) VALUES (4, 'alonzclin9315', 'Nunc.', 'client');
INSERT INTO auth (id, username, password, role) VALUES (5, 'kolbbarnet8962', 'Laoreet.', 'client');
INSERT INTO auth (id, username, password, role) VALUES (6, 'jadsim4115', 'Cursus?', 'client');
INSERT INTO auth (id, username, password, role) VALUES (7, 'karlieconr6656', 'Mauris.', 'client');




