import psycopg2
#
# tg_id = 1234124
from config import host, user, password, db_name

#
# try:
#     connect = psycopg2.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=db_name
#     )
#     cursor1 = connect.cursor()
#
#     print('*' * 30, 'Передача параметра в f-строке:', '', sep='\n')
#     cursor1.execute(f"select num_of_que from users where tg_id={tg_id}")
#     for row in cursor1.fetchall():
#         print('DB returned:', row, type(row), sep=' ')
#         print(f'Num of quie = {row[0]}')
#
#     print()
#
#     print('*' * 30, 'Передача параметра через переменную подстановки:', '', sep='\n')
#     cursor1.execute(f"select num_of_que from users where tg_id=%s", [tg_id])
#     for row in cursor1.fetchall():
#         print('DB returned:', row, type(row), sep=' ')
#         print(f'Num of quie = {row[0]}')
#     print('*' * 30)
#
#
# except psycopg2.Error as _ex:
#     print(_ex)

# from logging import basicConfig, INFO, getLogger
# from sqlalchemy import create_engine, text
#
#
# def logger_config(level=INFO):
#     basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s',
#                 datefmt='%d-%m-%Y %H:%M:%S',
#                 level=level)
#
#
# def main():
#     logger_config()
#     print_data_from_db(tg_id=12341234)
#
#
# def print_data_from_db(tg_id):
#     logger = getLogger('root')
#     pg_engine = create_engine('postgresql://avladavydov@localhost/telega')
#     sql = text('select num_of_que from telega.users where tg_id=:tg_id')
#     try:
#         sql = sql.bindparams(tg_id=tg_id)
#         with pg_engine.connect() as connection:
#             logger.info(f'Запрос данных для tg_id: {tg_id}')
#             cursor = connection.execution_options(stream_result=True).execute(sql)
#             logger.info(f'Получено записей: {cursor.rowcount}')
#
#             for row in cursor.fetchall():
#                 logger.info(f'Num of quie ={row[0]}')
#
#     except Exception as e:
#         logger.error(f'Ошибка при получении данных: {e}')
#
#
# if __name__ == '__main__':
#     main()

tg_id = 123
# with psycopg2.connect(host=host, user=user, password=password, database=db_name) as connect:
#     with connect.cursor() as cursor1:
#         cursor1.execute(f"select num_of_que from users where tg_id=%s", [tg_id])
#         for row in cursor1.fetchall():
#             num = row[0]
# with psycopg2.connect(host=host, user=user, password=password, database=db_name) as connect:
#     with connect.cursor() as cursor1:
#         cursor1.execute(f"select tg_id from users where tg_id = %s", [tg_id])
#         if cursor1.fetchone() is not None:
#             print("такой пользователь уже в БД")
#         else:
#             cursor1.execute(f"insert into users(tg_id, status_btn, num_of_que) values(%s, %s, %s)", [56555, True, 2])



