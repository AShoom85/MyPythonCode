import os
import sqlite3
import sys
'''
print(sqlite3.threadsafety)
print(sqlite3.paramstyle)
print(sqlite3.version)
print(sqlite3.sqlite_version)
print(sqlite3.sqlite_version_info)

print('Открываем базу данных')
con = sqlite3.connect("testdb.db")
if con:
    print('Работаем с базой данных')
print('Закрьmаем базу данных')
con.close()

con = sqlite3.connect("testdb.db")
con.close()

con = sqlite3.connect("testdb.db")
con.close()

con = sqlite3.connect( "testdb.db ")
con.close()

connection = sqlite3.connect('testdb.db')
print('Создается курсор из соединения с БД')
cursor = connection.cursor()
connection.close()

db_filename = 'todo.db'
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)
if db_is_new:
    print('Need to create schema')
else:
    print('Database exists, assume schema does, too.')
conn.close()




db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Schema Created Successfully')

    else:
        print('Database exists, assume schema does, too.')'''




db_filename = 'todo.db'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        
        print('Creating schema')
        conn.executescript("""
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
                               );""")  
               
            
        print('Schema Created Successfully')
        
        print('Inserting initial data')

        conn.executescript("""
            insert into project (name, description, deadline)
            values ('pycat', 'Python Cat of the Week','2019-11-28');
            
            insert into task (details, status, deadline, project)
            values ('write about select cat', 'done', '2019-12-25','pycat');
            
            insert into task (details, status, deadline, project)
            values ('write about random cat', 'waiting', '2019-12-22','pycat');
            
            insert into task (details, status, deadline, project)
            values ('write about black cat', 'active', '2019-12-31','pycat');
            """)

    else:
        print('Database exists, assume schema does, too.')


db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select id, priority, details, status, deadline from task
    where project = 'pycat'
    """)

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))


with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select name, description, deadline from project
    where name = 'pycat'
    """)
    name, description, deadline = cursor.fetchone()

    print('Project details for {} ({})\n  due {}'.format(
        description, name, deadline))

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    
    print(cursor.arraysize)

    cursor.execute("""
    select id, priority, details, status, deadline from task
    where project = 'pycat' order by deadline
    """)

    print('\nNext 5 tasks:')
    for row in cursor.fetchmany(5):
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select * from task where project = 'pycat'
    """)

    print('Task table has these columns:')
    for colinfo in cursor.description:
        print(colinfo)


with sqlite3.connect(db_filename) as conn:
    # Change the row factory to use Row
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
    select name, description, deadline from project
    where name = 'pycat'
    """)
    name, description, deadline = cursor.fetchone()

    print('Project details for {} ({})\n  due {}'.format(
        description, name, deadline))

    cursor.execute("""
    select id, priority, status, deadline, details from task
    where project = 'pycat' order by deadline
    """)

    print('\nNext 5 tasks:')
    for row in cursor.fetchmany(5):
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            row['id'], row['priority'], row['details'],
            row['status'], row['deadline'],
        ))




print(sys.argv)

print(len(sys.argv))

project_name = sys.argv[0]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = """
    select id, priority, details, status, deadline from task
    where project = ?
    """

    cursor.execute(query, (project_name,))

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))





project_name = sys.argv[0]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = """
    select id, priority, details, status, deadline from task
    where project = :project_name
    order by deadline, priority
    """

    cursor.execute(query, {'project_name': project_name})

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))


db_filename = 'todo.db'
id = int(sys.argv[1])
status = sys.argv[2]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    query = "update task set status = :status where id = :id"
    cursor.execute(query, {'status': status, 'id': id})

db_filename = 'todo.db'
id = int(sys.argv[1])

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    query = "DELETE FROM task WHERE id = :id"
    cursor.execute(query, {'id': id})

    

        
