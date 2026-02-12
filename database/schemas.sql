-- user table

create table users(
    uid serial primary key,
    username varchar(30) unique not null,
    passwd_hash text not null,
    role varchar(20)
);