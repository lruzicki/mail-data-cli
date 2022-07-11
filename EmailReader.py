import glob, os
import pandas as pd
import os

from pyparsing import dict_of

class EmailReader:

    def __init__(self):
        self.list_of_correct_emails = []
        self.list_of_incorrect_emails = []       

    def incorrect_emails(self, directory):
        self.read_all_emails_from_directory(directory)
        print(len(self.list_of_incorrect_emails))
        for single_mail in self.list_of_incorrect_emails:
            print(single_mail)

    def search_emails_by_text(self, text):
        for email in self.list_of_correct_emails:
            if text in email:
                print(email)

    def group_emails_by_domain(self):
        dict_of_mails = {}

        for mail in self.list_of_correct_emails:
            domain = mail.split("@", 1)[1]
            domain = domain.split(".", 1)[0]
            if domain in dict_of_mails.keys(): dict_of_mails[domain].append(mail)
            else: dict_of_mails[domain] = [mail]

        for key, val in dict_of_mails.items(): val.sort()
        dict_of_mails = dict(sorted(dict_of_mails.items()))
        for key, val in dict_of_mails.items():
            print(key, val)
        
        del dict_of_mails

    def emails_not_in_log_file(self, directory):
        found_emails_in_logs = []
        not_found_emails_in_logs = []
        file = open(directory, 'r')
        all_lines = file.readlines()
        for line in all_lines:
            mail = line.split("Email has been sent to '", 1)[1]
            mail = mail[:-3]
            if mail not in found_emails_in_logs:
                found_emails_in_logs.append(mail)

        for mail in self.list_of_correct_emails:
            if mail not in found_emails_in_logs:
                not_found_emails_in_logs.append(mail)

        print(len(not_found_emails_in_logs))
        for mail in sorted(not_found_emails_in_logs):
            print(mail)

        del found_emails_in_logs
        del not_found_emails_in_logs
        file.close()

    def is_valid_email(self, line):
        if line.count('@') == 1 and\
                    line.find('@') >= 1 and\
                    line.rfind('.') - line.find('@') >= 1 and\
                    len(line) - line.rfind('.') - 1 >= 1 and len(line) - line.rfind('.') - 1 <= 4:# and line[-line.rfind('.'):].isalnum()
                    if line not in self.list_of_correct_emails:
                        self.list_of_correct_emails.append(line)
        else:
                    if line not in self.list_of_incorrect_emails:
                        self.list_of_incorrect_emails.append(line)

    def read_all_emails_from_directory(self, directory):
        owd = os.getcwd()
        os.chdir(directory)
        for file_name in glob.glob("*.txt"):
            file = open(file_name, 'r')
            all_lines = file.readlines()

            for line in all_lines:
                line = line[:-1]
                self.is_valid_email(line)
            file.close()

        for file_name in glob.glob("*.csv"):
            data= pd.read_csv(file_name, delimiter=';')
            for single_mail in data.email:
                self.is_valid_email(single_mail)  
        os.chdir(owd) # return to the previous directory          

    def read_all_csv(self):
        pass

