#!/usr/bin/python3
for num_check in range(0, 100):
    if num_check == 99:
        print("{}".format(num_check))
    else:
        print("{:02}".format(num_check), end=", ")
