delete from privileges;
delete from resources;
delete from actions;
delete from controllers;
delete from users;
delete from roles;

---
--  Roles
---


insert into roles (id, name) values (1, 'administrador');
insert into roles (id, name) values (2, 'usuário');


insert into users (username, password, role_id, email) values ('admin', 'sha256$l2ygbSdF$2d03f994b4d99fdf6ca30832852826564189f3438a9f6abc7249bc74c08b7843', 1, 'lucasssousa10@gmail.com');
insert into users (username, password, role_id, email) values ('user', 'sha256$l2ygbSdF$2d03f994b4d99fdf6ca30832852826564189f3438a9f6abc7249bc74c08b7843', 2, 'lucasssousa10@gmail.com');

---
--  Controllers
---


insert into controllers (id, name) values (1, 'users');
insert into controllers (id, name) values (2, 'servidor');

---
--  Actions
---

insert into actions (id, name) values (1, 'all');
insert into actions (id, name) values (2, 'view');
insert into actions (id, name) values (3, 'add');
insert into actions (id, name) values (4, 'edit');
insert into actions (id, name) values (5, 'delete');


---
--Resources
---


insert into resources (id, controller_id, action_id) values (  1, 1, 1); -- users/all
insert into resources (id, controller_id, action_id) values (  2, 1, 2); -- users/view
insert into resources (id, controller_id, action_id) values (  3, 1, 3); -- users/add
insert into resources (id, controller_id, action_id) values (  4, 1, 4); -- users/edit
insert into resources (id, controller_id, action_id) values (  5, 1, 5); -- users/delete

insert into resources (id, controller_id, action_id) values (  6, 2, 1); -- servidor/all
insert into resources (id, controller_id, action_id) values (  7, 2, 2); -- servidor/view
insert into resources (id, controller_id, action_id) values (  8, 2, 3); -- servidor/add
insert into resources (id, controller_id, action_id) values (  9, 2, 4); -- servidor/edit
insert into resources (id, controller_id, action_id) values ( 10, 2, 5); -- servidor/delete


--administrator


insert into privileges (role_id, resource_id, allow) values (1, 1, true); -- users/all
insert into privileges (role_id, resource_id, allow) values (1, 2, true); -- users/view
insert into privileges (role_id, resource_id, allow) values (1, 3, true); -- users/add
insert into privileges (role_id, resource_id, allow) values (1, 4, true); -- users/edit
insert into privileges (role_id, resource_id, allow) values (1, 5, true); -- users/delete
 
insert into privileges (role_id, resource_id, allow) values (1, 1, true); -- servidor/all
insert into privileges (role_id, resource_id, allow) values (1, 2, true); -- servidor/view
insert into privileges (role_id, resource_id, allow) values (1, 3, true); -- servidor/add
insert into privileges (role_id, resource_id, allow) values (1, 4, true); -- servidor/edit
insert into privileges (role_id, resource_id, allow) values (1, 5, true); -- servidor/delete


--client


insert into privileges (role_id, resource_id, allow) values (2, 1, true); -- users/all
insert into privileges (role_id, resource_id, allow) values (2, 2, true); -- users/view
insert into privileges (role_id, resource_id, allow) values (2, 3, true); -- users/add
insert into privileges (role_id, resource_id, allow) values (2, 4, true); -- users/edit
insert into privileges (role_id, resource_id, allow) values (2, 5, true); -- users/delete

insert into privileges (role_id, resource_id, allow) values (2, 1, true); -- servidor/all
insert into privileges (role_id, resource_id, allow) values (2, 2, true); -- servidor/view
insert into privileges (role_id, resource_id, allow) values (2, 3, true); -- servidor/add
insert into privileges (role_id, resource_id, allow) values (2, 4, true); -- servidor/edit
insert into privileges (role_id, resource_id, allow) values (2, 5, true); -- servidor/delete