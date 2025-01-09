import os
import time
import subprocess

line1 = "                   .^~!7??JJJJYYYYYJJJ??7~^.                          "
line2 = "                 :7JJYYYYYYYYYYYYYYYYYYY55YJ!.                        "
line3 = "                :JYJ?~::~?YYYYYYYYYYYYYYYYY55J:                       "
line4 = "                !YJY^    :YYYYYYYYYYYYYYY55555J                       "
line5 = "                !YJY?^..^7YYYYYYYYYYYYYY555555Y.                      "
line6 = "                7YYYYYYYYYYYYYYYYYYYYY55555555Y.                      "
line7 = "                ~777777????????JYYYY5555555555Y.                      "
line8 = "      ..:^^^^^^^^^^^^^^^^^^^^^^!5YY55555555555Y. ........             "
line9 = "   .^7?JJJYYYYYYYYYYYYYYYYY55555YY555555555555Y. ::::::::::.          "
line10 = "  ^?JJJJJJJJJYYYYYYYYYYYYYYYYYY555555555555555Y. ::::::::::::         "
line11 = " ^JJJJJJJJYYYYYYYYYYYYYYYYYYY55555555555555555Y. :::::::::::::        "
line12 = ".JJJJJJJYYYYYYYYYYYYYYYYYYY555555555555555555PJ .:::::::::::::.       "
line13 = "~YJJJJYYYYYYYYYYYYYYYYYYYY555555555555555555PY: :::::::::::::^:       "
line14 = "?JJJYYYYYYYYYYYYYYYY55555555555555PPPPPPPP5Y!..::::::::::::::^:.      "
line15 = "JJJJYYYYYYYYYYYYY55YJ7!!!!!!!!!!!!!!!!!!!~:..::::::::::::^^^^^^.      "
line16 = "JYYYYYYYYYYYYYYYY?~:......................:::::::::::::::^^^^^^.      "
line17 = "?YYYYYYYYYYYYYYJ^ ..::::::::::::::::::::::::::::::^^^^^^^^^^^^^.      "
line18 = "~YYYYYYYYYYYYYY: .::::::::::::::::::::::::::::::^^^^^^^^^^^^^^^       "
line19 = ".JYYYYYYYYYYY5! .:::::::::::::::::::::::::::::^^^^^^^^^^^^^^^^.       "
line20 = " ^YYYYYYYYYY55! .::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^:        "
line21 = "  ^J5YYYYYY555! .:::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^:         "
line22 = "   .!?YY555555! .:::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^:.          "
line23 = "      .:^^^^^^: .:::::::::::::^:.........................              "
line24 = "                .:::::::::::::^::::::::::::::::                        "
line25 = "                ::::::::::::^^^^^^^^^^^^^^^^^^^                        "
line26 = "                :::::::^^:^^^^^^^^^^^:.. .:^^^^                        "
line27 = "                .^::::^^^^^^^^^^^^^^^:     ^^^:                        "
line28 = "                 :^^^^^^^^^^^^^^^^^^^^:...^^^^.                        "
line29 = "                  .::^^^^^^^^^^^^^^^^^^^^^^:.                          "
line30 = "                     ...:::^^^^^^^^^^:::..                             "
line31 = "                            ......                                     "
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)
print(line8)
print(line9)
print(line10)
print(line11)
print(line12)
print(line13)
print(line14)
print(line15)
print(line16)
print(line17)
print(line18)
print(line19)
print(line20)
print(line21)
print(line22)
print(line23)
print(line24)
print(line25)
print(line26)
print(line27)
print(line28)
print(line29)
print(line30)
print(line31)
print("Coded by Marcomsa_YT")
print("Welcome to IPMASTER")

time.sleep(0.5)
print("Select an option:")
print("1: NMAP")
print("2: WHOIS")
print("3: Vulnerability Scan")
LoginVar = input("Type down your option here: ")
dir = os.system("chdir")
if LoginVar == "1":
    newT1 = subprocess.run(["start", "cmd", "/k", "python Nmap.py"], shell = True)
if LoginVar =="2":
    newT2 = subprocess.run(["start", "cmd", "/k", "python Whois.py"], shell = True)
if LoginVar == "3":
    newT3 = subprocess.run(["start", "cmd", "/k", "python VulnerabilitySCN.py"], shell = True)