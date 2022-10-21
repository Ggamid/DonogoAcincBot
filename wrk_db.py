import psycopg2
from config import host, user, password, db_name


def create_table():
    try:
        table = """
        CREATE TABLE IF NOT EXISTS users(
            tg_id BIGINT, 
            num_of_que SMALLINT DEFAULT(0),
            count_right SMALLINT DEFAULT(0),
            count_wrong SMALLINT DEFAULT(0),
            name TEXT DEFAULT('не получено'),
            phone_number TEXT DEFAULT('не получено')
        );
        """
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            with con.cursor() as cur:
                cur.execute(table)

    except Exception as e:
        print("[INFO] Error while working with PostgreSQL", e)


def drop_data_in_table():
    try:

        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute("TRUNCATE TABLE users")

    except Exception as e:
        print("[INFO] Error while working with PostgreSQL", e)


def drop_table():
    try:

        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute("DROP TABLE users")

    except Exception as e:
        print("[INFO] Error while working with PostgreSQL", e)


def add_user(tg_id):
    try:
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as connect:
            connect.autocommit = True
            with connect.cursor() as cursor1:
                cursor1.execute(f"select tg_id from users where tg_id = %s", [tg_id])
                if cursor1.fetchone() is not None:
                    print("такой пользователь уже в БД")
                else:
                    cursor1.execute(f"insert into users(tg_id) values(%s)",
                                    [tg_id])
    except psycopg2.Error as e:
        print("Error", e)


def check_num_of_que(tg_id):
    try:
        print(tg_id)
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as connect:
            connect.autocommit = True
            with connect.cursor() as cursor1:
                cursor1.execute(f"select num_of_que from users where tg_id=%s", [tg_id])
                num = cursor1.fetchone()[0]
        return num
    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def add_phone_number(tg_id, phone_number):
    try:
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute(f"update users set phone_number = %s where id = %s", [phone_number, tg_id])
    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def add_name(tg_id, name):
    try:
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute(f"update users set name = %s where id = %s", [name, tg_id])
    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def update_que(tg_id):
    try:
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute(f"select num_of_que from users where tg_id = %s", [tg_id])
                num_of_que = cur.fetchone()[0]
                if num_of_que <= 18:
                    num_of_que += 1
                    cur.execute(f"update users set num_of_que = %s where tg_id = %s", [num_of_que, tg_id])
                else:
                    num_of_que = 1
                    cur.execute(f"update users set num_of_que = %s where tg_id = %s", [num_of_que, tg_id])
    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def update_right(tg_id, zero=True):
    try:
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute(f"select count_right from users where tg_id = %s", [tg_id])
                num_of_que = cur.fetchone()[0]
                if zero:
                    print(num_of_que, "до +1")
                    num_of_que += 1
                    print(num_of_que, "после +1")
                    cur.execute(f"update users set count_right = %s where tg_id = %s", [num_of_que, tg_id])
                else:
                    num_of_que = 0
                    cur.execute(f"update users set count_right = %s where tg_id = %s", [num_of_que, tg_id])
    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def update_wrong(tg_id, zero=True):
    try:
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            with con.cursor() as cur:
                cur.execute(f"select count_wrong from users where tg_id = %s", [tg_id])
                num_of_que = cur.fetchone()[0]
                if zero:
                    cur.execute(f"update users set count_wrong = %s where tg_id = %s", [num_of_que, tg_id])
                else:
                    num_of_que = 0
                    cur.execute(f"update users set count_wrong = %s where tg_id = %s", [num_of_que, tg_id])
    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


# 635915647
