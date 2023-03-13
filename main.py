from sys import exit, argv
from os import path

from psycopg2 import connect, Error

from lib.config import ParseConfigFile

def main() -> None:
    if len(argv) < 1:
        exit(1)

    config = ParseConfigFile(argv[1])
#    for config_item_buff in config:
#       config_item = config_item_buff.split('=')
#       opt = config_item[0]
#       arg = config_item[1]
#
#       try:
#           cur.execute('''select name, vartype, min_val, max_val from pg_settings;''')
#       except Error as e:
#           print(e.pgerror)
    print(config)

if __name__ == '__main__':
    main()
