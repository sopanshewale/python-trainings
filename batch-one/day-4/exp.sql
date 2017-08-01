create table project (
    name        text primary key,
    description text,
    deadline    date
);

create table task (
    id           integer primary key autoincrement not null,
    priority     integer default 1,
    details      text,
    status       text,
    deadline     date,
    completed_on date,
    project      text not null references project(name)
);

insert into project (name, description, deadline) values ('assignments', 'Assignments - Python for Data Science', '2017-05-24');

insert into task (details, status, deadline, project) values ('assignment 1', 'done', '2017-01-29', 'assignments'); 
insert into task (details, status, deadline, project) values ('assignment 2', 'in progress', '2017-02-22', 'assignments'); 
insert into task (details, status, deadline, project) values ('assignment 3', 'active', '2017-03-31', 'assignments');


