import os
import time
import subprocess

print("Welcome to IPmaster/NMAP ")
print("Select profile")
print("1: Intense scan")
print("2: Intense scan plus UDP")
print("3: Intense scan, all TCP ports")
print("4: Intense scan, no ping")
print("5: Ping scan")
print("6: Quick scan")
print("7: Quick scan plus")
print("8: Quick traceroute")
print("9: Regular scan")
ScanType = input("Enter your election here: ")
ip = input("Introduce the ip here: ")

def RunningOverlay():    
 print("Loading")
 print("11%")
 time.sleep(0.2)
 print("24%")
 time.sleep(0.2)
 print("41%")
 time.sleep(0.2)
 print("64%")
 time.sleep(0.1)
 print("89%")
 time.sleep(0.1)
 print("100%")


def Program1():
    RunningOverlay()
    newT1 = subprocess.run(["start", "cmd", "/k", f"nmap -T4 -A -v {ip}"], shell = True)
def Program2():
    RunningOverlay()
    newT2 = subprocess.run(["start", "cmd", "/k", f"nmap -sS -sU -T4 -A -v {ip}"], shell = True)
def Program3():
    RunningOverlay()
    newT3 = subprocess.run(["start", "cmd", "/k", f"nmap -p 1-65535 -T4 -A -v {ip}"], shell = True)
def Program4():
   RunningOverlay()
   newT4 = subprocess.run(["start", "cmd", "/k", f"nmap -T4 -A -v -Pn {ip}"], shell = True)
def Program5():
   RunningOverlay()
   newT5 = subprocess.run(["start", "cmd", "/k", f"nmap -sn {ip}"], shell = True)
def Program6():
   RunningOverlay()
   newT6 = subprocess.run(["start", "cmd", "/k", f"nmap -T4 -F {ip}"], shell = True)
def Program7():
   RunningOverlay()
   newT7 = subprocess.run(["start", "cmd", "/k", f"nmap -sV -T4 -O -F --version-light {ip}"], shell = True)
def Program8():
   RunningOverlay()
   newT8 = subprocess.run(["start", "cmd", "/k", f"nmap -sn --traceroute {ip}"], shell = True)
def Program9():
   RunningOverlay()
   newT9 = subprocess.run(["start", "cmd", "/k", f"nmap {ip}"], shell = True)
   

if ScanType == "1":
    Program1()
if ScanType == "2":
   Program2()
if ScanType == "3":
   Program3()
if ScanType == "4":
   Program4()
if ScanType == "5":
   Program5()
if ScanType == "6":
   Program6()
if ScanType == "7":
   Program7()
if ScanType == "8":
   Program8()
if ScanType == "9":
   Program9()