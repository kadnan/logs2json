import sys
from AccessLog import *

def main():
    if len(sys.argv) < 3:
        print "Incorrect Syntax. Usage: python main.py -f <filename>"
        sys.exit(2)
    elif sys.argv[1] != "-f":
        print "Invalid switch '"+sys.argv[1]+"'"
        sys.exit(2)
    elif os.path.isfile(sys.argv[2]) == False:
        print "File does not exist"
        sys.exit(2)

    print toJson(sys.argv[2])


if __name__ == "__main__":
    main()
    