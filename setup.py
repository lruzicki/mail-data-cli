import argparse

directory = "emails"

parser = argparse.ArgumentParser("Fetch data from emails")
parser.add_argument('-ic',  '--incorrect-emails', help = 'Show incorrect emails from mails directory', action = 'store_true')
parser.add_argument('-s',  '--search', type = str, help = 'Search mails by text')
parser.add_argument('-gbd',  '--group-by-domain', help = 'Group emails by domain name', action = 'store_true')
parser.add_argument('-feil',  '--find-emails-not-in-logs', type = str, help = 'Search for emails not saved in the logs')
parser.formatter_class = lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position = 30)

try:
    args = parser.parse_args()
except SystemExit:
    print( "Incorrect input, try again! Maybe you need help? \n" )
    parser.print_help()
    exit (-1)

def waitMenu():
    input("Press Enter to continue...")