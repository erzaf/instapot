import csv
import argparse
from pyfiglet import Figlet
from engine.automate import Automate

banner = Figlet(font='larry3d')
print(banner.renderText('InstaPot'), "Made with love by M0bl3y. V 1.0.1\n")

parser = argparse.ArgumentParser(description='InstaPot, an Instagram mass reporter tool')
parser.add_argument('Target',
                        metavar='target_username',
                        type=str,
                        help='Add the username of the target')
args = parser.parse_args()
target = args.Target

with open('./creds.csv') as source:
    source = csv.reader(source, delimiter=';')

    for i in source:
        Automate(i[0],i[1], target)