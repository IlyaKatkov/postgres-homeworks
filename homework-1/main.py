"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv

CSV_DATA_PATH = os.path.join('north_data')


def csv_postgres(csv_data_path, csv_file, table_name):
    try:
        with psycopg2.connect(database='home_work_1', user='postgres', password=os.getenv('BASE_PASSWORD')) as conn:
            with conn.cursor() as cur:
                with open(f"{csv_data_path}/{csv_file}", 'r') as file:
                    reader = csv.reader(file)
                    next(reader)

                    for row in reader:
                        query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(row))})"
                        cur.execute(query, row)


                cur.execute(f"SELECT * FROM {table_name}")
                rows = cur.fetchall()

                for row in rows:
                    print(row)
    finally:
        conn.close()


if __name__ == '__main__':
    csv_postgres(CSV_DATA_PATH, 'customers_data.csv', 'customers')
    csv_postgres(CSV_DATA_PATH, 'employees_data.csv', 'employees')
    csv_postgres(CSV_DATA_PATH, 'orders_data.csv', 'orders')