from sys import exit

import nyanko.connection
import nyanko.parsing


hosts = None

# load hosts from a file
try:
    with open("host") as fp:
        hosts = tuple(line.strip() for line in fp)
except FileNotFoundError:
    print("Error: host file not found. Exiting.")
    exit(1)
