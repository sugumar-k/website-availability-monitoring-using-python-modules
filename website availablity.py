
def website_availablity():
    #importing the module 
    import logging 
    import os

    #now we will Create and configure logger 
    logging.basicConfig(filename="website availablity.log",
                        level=logging.INFO, 
					    format='%(name)s|%(asctime)s|%(levelname)s| %(message)s|',
					    filemode='w') 
                        
    logging.debug("website status results")

    #importing libraries to check whether the website is available or not

    import urllib
    from urllib import request
    import requests
    from requests.exceptions import HTTPError

#passing multiple urls as a input
    websites =tuple(input("enter websites").split())
    print (websites)
    for url in websites:
        try:
            response=requests.get(url)
            status=(response.status_code)
            dict={url:status}
            
        #if code returns any exceptions 
        except HTTPError as http_err:
            logging.error(f"HTTP error occured:{http_err}")
        except Exception as err:
            logging.error(f"other error occured:{err}")
        else:
            if status==200:
                logging.info(f"website is running successfully:{url}")
                logging.info(f"status is:{dict}")
            else:
                logging.warning(f"website having problem:{url}")
                logging.warning(f"status code is:{dict}")
website_availablity()


import schedule
import time
def email():
    #importing required libraries to send email
    import smtplib
    from email.message import EmailMessage
    msg = EmailMessage()
    msg["subject"]="website status"
    msg["from"]="message from "
    msg["to"]="Receiver email address"
    #attaching the log file to the mail
    with open ("website availablity.log","rb")as f:
        file_data=f.read()
        file_name=f.name
        print(file_name)
        msg.add_attachment(file_data,maintype="application",subtype=".log",filename=file_name)
 
    #setting the server
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    #login to the sender mail
    server.login("sender email address","password")
    server.send_message(msg)
    print ("mail sent")
    server.quit()


#for sending email every 1 hour

schedule.every(1).minutes.do(email)

while True:
    schedule.run_pending()
    time.sleep(1)

    

