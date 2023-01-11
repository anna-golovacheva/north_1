import psycopg2
import csv


def create_request(table, values):
    """
    Функция создает запрос для заполнения нужной таблицы.
    :param table: str
    :param values: str
    :return: str
    """
    table_fields_dict = {
        'employees': 'first_name, last_name, title, birth_date, notes',
        'customers_data': 'customer_id, company_name, contact_name',
        'orders_data': 'order_id, customer_id, employee_id, order_date, ship_city'
    }

    request = f'INSERT INTO {table} ({table_fields_dict[table]}) VALUES {values}'

    return request


def insert_values(cursor, table, values):
    """
    Функция выполняет запрос с помощью курсора.
    :param cursor: obj
    :param table: str
    :param values:str
    :return: None
    """
    request = create_request(table, values)
    try:
        with cursor:
            cursor.execute(request)
            print('insertion done')
    except:
        print('insertion failed')


def get_data_from_file(file):
    """
    Функция получает данные из csv-файла для заполнения таблицы.
    :param file: str
    :return: str
    """
    row_list = []
    with open(file) as csvfile:
        data_reader = csv.reader(csvfile, encoding='utf-8')
        _ = next(data_reader)
        for row in data_reader:
            clean_row = [item.replace("'", "") for item in row]
            row_tuple = tuple(clean_row)
            row_list.append(row_tuple)
    row_str = ','.join(map(str, row_list))
    return row_str


def main():
    employee_data_list = get_data_from_file('../data/employees_data.csv')
    customers_data_list = get_data_from_file('../data/customers_data.csv')
    orders_data_list = get_data_from_file('../data/orders_data.csv')

    connection = psycopg2.connect(
            host='localhost',
            database='north',
            user='postgres',
            password='12345'
        )

    try:
        with connection:
            print('connection done')
            curs = connection.cursor()

            insert_values(curs, 'employees', employee_data_list)
            insert_values(curs, 'customers_data', customers_data_list)
            insert_values(curs, 'orders_data', orders_data_list)

    except:
        print('connection failed')
    finally:
        connection.close()


if __name__ == '__main__':
    main()
