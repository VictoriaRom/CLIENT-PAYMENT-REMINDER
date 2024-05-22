# Payment Reminder for Clients

The automation project we are going to see is a payment reminder for clients. It is very common for businesses to have an accountant or someone in charge of billing who needs to keep track of payments. It may also be that the business owner themselves needs to know whether clients have paid or not. With this project, we will automate this process by sending reminders both via email and mobile phone.

![2024-05-21_22h08_44](https://github.com/VictoriaRom/CLIENT-PAYMENT-REMINDER/assets/97700058/a9aea5ab-86e6-43a9-84b9-0e3214084d80)



## Objective

The main objective of this project is to streamline the tracking of client payments and send automatic reminders if a client is pending payment.

## Functionality

The workflow of the project is as follows:

1. **Daily Execution:** The system runs daily to check the payment status of clients.
2. **Payment Verification:** An Excel file containing client information is read, and it is checked whether they are up to date with payments.
3. **Sending Reminders:** If a client is due to make a payment but has not yet done so, a reminder will be sent to them via email and SMS.

## Usage

To use this project, follow these steps:

1. Configure the `clients_information.csv` file with client information.
2. Run the main script `app.py` to initiate the verification and reminder sending process.
3. Check payment records in the log file or user interface.

## Dependencies

This project uses Python and some external libraries. To install all dependencies, make sure your environment is set up and run:

pip install -r requirements.txt
