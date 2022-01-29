import sys
import clipboard
import json

print (sys.argv)

if len(sys.argv) ==2:
    command = sys.argv[1]
    print(command)

    if command == "save":
        print("save")
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("unknown command")

else:
    print("please pass exactly one command.")