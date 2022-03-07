#! /usr/bin/python

import argparse
import os


parser = argparse.ArgumentParser(description='This script is used to gather information about systems network, '
                                             'ports and web services')
# Argument to run the script with
parser.add_argument("-ip", "--ip-address", help="Supplies an IP Address, defaults to network: 10.10.10.10",
                    default="10.10.10.10")
parser.add_argument("-o", "--output", help="Sets file name for the output stream. \n"
                                           "Defaults to Scan", default="Scan")
# Parsing the argument
args = parser.parse_args()

print('Doing scan for IP Address: ' + args.ip_address)
print('Outputing the files to infogetresults/')

ipa = args.ip_address
outstream = args.output

# Commands executed by the script
cmd = 'mkdir infogetresults'
cmd1 = 'nmap -T4 -n -Pn -p* -o infogetresults/' + outstream + '_nmap_allports.txt ' + ipa
cmd2 = 'nmap -A -T4 -n -Pn -p* -o infogetresults/' + outstream + '_nmap_deepscan.txt ' + ipa
cmd3 = 'nikto -o infogetresults/' + outstream + '_nikto.txt -p 80,443,8080 -host ' + ipa
cmd4 = 'gobuster dir -v -e -u http://' + ipa + ' -w /usr/share/wordlists/dirb/common.txt -o infogetresults/' + outstream + '_gobuster.txt'
cmd5 = 'whatweb ' + ipa + ' > infogetresults/' + outstream + '_whatweb_scan.txt'
# Executing the commands
os.system(cmd)
print("Results directory created")
os.system(cmd1)
print("Nmap scan for all ports...")
print("DONE")
os.system(cmd2)
print("Nmap deep scan...")
print("DONE")
os.system(cmd4)
print("GoBuster scan...")
print("DONE")
os.system(cmd5)
print("WhatWeb scan...")
print("DONE")
os.system(cmd3)
print("Nikto scan...")
print("DONE")
