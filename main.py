import os
from datetime import date,datetime
import validations as val
import shutil
import csv
import mail
import sys

current_date = date.today()
current_date = str(current_date).replace('-', '')
file_path = f'incoming_files/{current_date}'
success_path = 'success_files'
rejection_path = 'rejected_files'
incoming_files = os.listdir(file_path)

if not incoming_files:
    mail.send_mail(0, 0, 0)
    sys.exit()


for file in incoming_files:
    header = val.get_header(file)


    if len(val.get_error_file(file)) == 0:

        if os.path.exists(success_path):
            if os.path.exists(f'{success_path}/{current_date}'):
                shutil.copy( f'incoming_files/{current_date}/{file}',f'{success_path}/{current_date}')
            else:
                os.makedirs(f'{success_path}/{current_date}', exist_ok=True)
                shutil.copy( f'incoming_files/{current_date}/{file}',f'{success_path}/{current_date}')
        else:
            os.makedirs(success_path, exist_ok=True)
            os.makedirs(f'{success_path}/{current_date}')
            shutil.copy( f'incoming_files/{current_date}/{file}',f'{success_path}/{current_date}')
    else:

        if os.path.exists(rejection_path):
            if os.path.exists(f'{rejection_path}/{current_date}'):
                shutil.copy(f'incoming_files/{current_date}/{file}',f'{rejection_path}/{current_date}')
                with open(f'error_{file}','w') as error:
                    writer = csv.writer(error)
                    writer.writerow(['order_id', 'order_date', 'product_id', 'quantity', 'sales', 'city','rejection_reason'])
                    for i in val.get_error_file(file):

                        writer.writerow(i)
                shutil.copy(f'error_{file}',f'{rejection_path}/{current_date}')
                os.remove(f'error_{file}')

            else:
                os.makedirs(f'{rejection_path}/{current_date}', exist_ok=True)
                shutil.copy(f'incoming_files/{current_date}/{file}',f'{rejection_path}/{current_date}')
                with open(f'error_{file}','w') as error:
                    writer = csv.writer(error)
                    writer.writerow(['order_id', 'order_date', 'product_id', 'quantity', 'sales', 'city''rejection_reason'])
                    for i in val.get_error_file(file):
                        writer.writerow(i)
                shutil.copy(f'error_{file}', f'{rejection_path}/{current_date}')
                os.remove(f'error_{file}')
        else:
            os.makedirs(rejection_path, exist_ok=True)
            os.makedirs(f'{rejection_path}/{current_date}')
            shutil.copy(f'incoming_files/{current_date}/{file}',f'{rejection_path}/{current_date}')
            with open(f'error_{file}', 'w') as error:
                writer = csv.writer(error)
                writer.writerow(['order_id', 'order_date', 'product_id', 'quantity', 'sales', 'city''rejection_reason'])
                for i in val.get_error_file(file):
                    writer.writerow(i)
            shutil.copy(f'error_{file}', f'{rejection_path}/{current_date}')
            os.remove(f'error_{file}')

#Count of files
total_files = 0
success_files = os.listdir(f'{success_path}/{current_date}')
success_files_count = 0
rejected_files_count = 0
for count in incoming_files:
    total_files += 1
for count in success_files:
    success_files_count += 1

rejected_files_count = total_files - success_files_count

mail.send_mail(total_files,success_files_count,rejected_files_count)





