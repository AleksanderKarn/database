import psycopg2
import csv

with psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password=input('Введите пароль: ')
) as conn:

    with conn.cursor() as cur:
        with open("customers_data.csv", newline='') as f:
            data = csv.reader(f, delimiter=',')
            for i in data:
                if i == ['"customer_id","company_name","contact_name"']:
                    continue
                else:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (i[0], i[1], i[2]))

        with open("employees_data.csv", newline='') as f:
            emp_data = csv.reader(f, delimiter=',')
            for i in emp_data:

                if i == ["first_name","last_name","title","birth_date","notes"]:
                    continue
                else:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)", (i[0], i[1], i[2], i[3], i[4]))

        with open("orders_data.csv", newline='') as f:
            ord_data = csv.reader(f, delimiter=',')
            for i in ord_data:
                if i == ["order_id","customer_id","employee_id","order_date","ship_city"]:
                    continue
                else:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (i[0], i[1], i[2], i[3], i[4]))

conn.close()