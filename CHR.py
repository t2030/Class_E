import os, sys, time
import requests
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
os.system("clear")
os.system("figlet CHR")

print
print "A Tool for Capturing HTTP Response"
print
print "Create By : Albraa & abdul"
print "Create For : Class_E"
print
print "           [1]> HTTP RESPONSE Capture      "
print 
print "           [0]> Exit "
print
option = raw_input("your option ==>> ")
os.system("clear")
if      option == "1":
        os.system("clear")
        url=raw_input("enter the website ")
        print "      [1]> Show Header       "
        print
        print "      [2]> Show Body         "
        HorB = raw_input("your option ==>> ")
        if HorB == "1":
                url_http = "https://" + url
                r = requests.get(url_http)
                os.system("figlet Header")
                print(r.headers)
        
        elif HorB == "2":
                url_http = ("https://") +url
                r = requests.get(url_http)
                os.system("figlet Header")
                print(r.content)
        else:
                print "\nERROR: Wrong Input"
                timeout(3)
                restart_program()
                


        

elif    option == "0" or option == "exit":
        sys.exit()

else:
        print "\nERROR: Wrong Input"
        timeout(3)
        restart_program()
