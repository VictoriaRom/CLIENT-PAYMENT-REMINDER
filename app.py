import csv
from datetime import datetime
from send_email import send_email
from send_sms import send_sms

csv_filename = 'clients_information.csv'
sender = 'Company Name'

with open(csv_filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            current_date = datetime.now().strftime('%Y-%m-%d')
            next_payment_date = row['Next Payment']
            last_payment_date = row['Last Payment']

            if next_payment_date < current_date:
                
                client_name = row['Name']
                client_email = row['Email']
                client_phone_number = row['Phone Number']
                payment_period = row['Payment Period']

                sms_message = f"Hello {client_name},  your payment has expired. Please access the platform and make your payment {payment_period} as soon as possible."
                
                # Send SMS
                send_sms(sms_message,client_phone_number)
                # Send Email
                send_email(sender,client_email,last_payment_date,next_payment_date,client_name)