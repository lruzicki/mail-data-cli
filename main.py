from EmailReader import *
from setup import *
import sys
emailReader = EmailReader(directory)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if args.incorrect_emails:
            emailReader.incorrect_emails()
        if args.search:
            emailReader.search_emails_by_text(args.search)
        if args.group_by_domain:
            emailReader.group_emails_by_domain()
        if args.find_emails_not_in_logs:
            emailReader.emails_not_in_log_file(args.find_emails_not_in_logs)
    # no arguments passed, open menu
    else:
        while True:
            try:
                option = int(input('''Input number to select option: \n
                1. Print incorrect emails\n
                2. Search emails by text\n
                3. Group emails by domain\n
                4. Print emails not in log file\n
                5. Exit\n
                your option: '''))
            except:
                print("\nInput only 1, 2, 3, 4 or 5!")
            else:
                if option == 1:
                    emailReader.incorrect_emails()
                    waitMenu()
                elif option == 2:
                    while True:
                        try:
                            text_to_look_for = str(input('Text to look for: '))
                        except:
                            print("\nInvalid input, try again.")
                        else:
                            emailReader.search_emails_by_text(text_to_look_for)
                            waitMenu()
                            break
                elif option == 3:
                    emailReader.group_emails_by_domain()
                    waitMenu()
                elif option == 4:
                    while True:
                        try:
                            logfile_name = str(input('Input name of log file: '))
                        except:
                            print("\nInvalid input, try again.")
                        else:
                            emailReader.emails_not_in_log_file(logfile_name)
                            waitMenu()
                            break
                elif option == 5:
                    break