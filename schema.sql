drop table if exists entries;
create table entries (
  id serial primary key not null,
  date timestamp with time zone not null default now(),
  title varchar(80) not null,
  content text not null
);

insert into entries values
(1, default, 'FlaskData', 'This is flask app was written by Andriienko Illia'),
(2, default, 'What?', 'This is flask app was written by what'),
(3, default, 'Who?', 'This is flask app was written by who'),
(4, default, 'Why', 'This is flask app was written by why');