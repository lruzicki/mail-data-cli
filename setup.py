import argparse

directory = "emails"

parser = argparse.ArgumentParser("Do some crazy stuff with emails data")
parser.add_argument('-ic',  '--incorrect-emails', help = 'Show incorrect emails from mails directory', action='store_true')
parser.add_argument('-s',  '--search', type = str, help = 'Search mails by text')
parser.add_argument('-gbd',  '--group-by-domain', help = 'Group emails by domain name', action='store_true')
parser.add_argument('-feil',  '--find-emails-not-in-logs', type = str, help = 'Height of sth')
args = parser.parse_args()

def waitMenu():
    input("Press Enter to continue...")


