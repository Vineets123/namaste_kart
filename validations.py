from datetime import date, datetime
import csv

current_date_formatted = date.today()
current_date = str(current_date_formatted).replace('-', '')

file_path = f'incoming_files/{current_date}'
error_file = 'error_file.csv'



#extracting product_master information
product_id = []
price_dic = {}
with open('product_master.csv', 'r') as product_master:
    datas = product_master.readlines()[1:]
    for product in datas:
        rows = str(product).split(',')
        product_id.append(str(product)[0:3])
        price_dic[rows[0]] = rows[2]
    product_master.close()


def get_header(file):
    with open(f'{file_path}/{file}', 'r') as orders:
        header = orders.readlines()[0:1]
    return header



def get_error_file(file):
    data_lines = []
    errors = []
    with open(f'{file_path}/{file}', 'r') as orders:
        data = orders.readlines()[1:]

        for id in data:
            row = str(id).replace('\n','').split(',')


            if row[2] not in product_id:
                errors.append("invalid product_id")

            if row[5].strip() not in ('Mumbai', 'Bangalore',''):
                errors.append("invalid city")

            if datetime.strptime(row[1], "%Y-%m-%d").date() >= current_date_formatted:
                errors.append("invalid date")


            if row[0] == '':
                errors.append("order_id is empty")

            if row[1] == '':
                errors.append("order_date is empty")

            if row[2] == '':
                errors.append("product_id is empty")

            if row[3] == '':
                errors.append("quantity is empty")

            if row[4] == '':
                errors.append("sales is empty")

            if row[5] == '' or row[5] == '\n':
                errors.append("city is empty")

            if row[2] not in product_id:
               errors.append("no product_id in master hence invalid sales calculation")
            elif float(row[4]) != float(price_dic[row[2]]) * float(row[3]):
               errors.append("invalid sales calculation")

            if errors != []:
                row.append(errors)
            if len(row) == 7:
                data_lines.append(row)
                errors = []



    return data_lines





