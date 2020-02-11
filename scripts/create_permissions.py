import os

accs = ['administrator','client','analyst']
endpoints = ['all','view','add','edit','delete']
dirs = os.listdir('/home/lucas/dev/overhead/middleware/app/controllers')
aux  = []
for dir in dirs:
    if dir.__contains__('Controller'):
        aux.append(dir)

dirs = aux
print("""
---
--  Controllers
---
\n""")
i = 1
for dir in dirs:
    print("insert into controllers (id, name) values ({}, \'{}\');".format(i,dir[:-13]))
    i += 1

print("""
---
--  Actions
---

insert into actions (id, name) values (1, 'all');
insert into actions (id, name) values (2, 'view');
insert into actions (id, name) values (3, 'add');
insert into actions (id, name) values (4, 'edit');
insert into actions (id, name) values (5, 'delete');
\n""")
print('---\n--Resources\n---\n\n')
i = 1
for dir in dirs:
    for endpoint in endpoints:
        print("insert into resources (id, controller_id, action_id) values (  {}, {}, {}); -- {}/{}".format(i,dirs.index(dir)+1,endpoints.index(endpoint)+1,dir[:-13],endpoint))
        i += 1
    print('\n')

for acc in accs:
    print("\n--{}\n\n".format(acc))
    i = 1
    for dir in dirs:
        dir1 = dir[:-13]
        for endpoint in endpoints:
            print(str("""insert into privileges (role_id, resource_id, allow) values ({}, {}, true); -- {}/{}\n""").format(accs.index(acc)+1,i,dir1,endpoint),end='')
            i += 1
        print(' ')
