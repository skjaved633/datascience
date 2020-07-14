#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 2020

@author: hydra
"""
# Python code to demonstrate a dictionary 
# with multiple inputs in a key. 
import os.path
import pandas as pd
from sys import exit
import pyrebase #import firebase
from pathlib import Path
home=str(Path.home())
# creating an empty dictionary 
from collections import defaultdict
dict= defaultdict(list)
"""
firebaseConfig = {
 paste your firebase code here
} #this code from firebase app project
firebase = pyrebase.initialize_app(firebaseConfig) #initialise firebase
storage = firebase.storage() #init storage
path_to_cloud = "INT_EX/client's data.py"
storage.child(path_to_cloud).download(home+"/client data.csv") #download the file
"""

print("Welcome to Hydra \n This is the Client's Data Log")

while True:
    print ("Type:\n\t*show to see data base\n\t*enter to write to data base\n\t*edit to Change the client's Details \n\t*exit to exit")
    op = input("\n> ")
    if "enter" in op:
        print("Enter client name")
        dict["client's name"].append(input())
        print("Enter Address")
        dict["address"].append(input())
        print("Enter Type of service")
        dict["type of service"].append(input())
        print("Enter 10 digit contact number")
        dict["contact"].append(input())
        h=pd.DataFrame(dict)
        h.to_csv(home+"/client data.csv")
            
    elif "show" in op:
        h=pd.DataFrame(dict)
        print(h.head())
    elif "exit" in op:
        exit(0)
    elif "edit" in op:
        pd.read_csv(home+"/client data.csv")
        h=pd.DataFrame(dict)
        print(h.head())
        print("Type: \n\t*name to change the client name \n\t*address to change the Address \n\t*type to change the service type \n\t*contact to change the contact number \n\t*return to go back")
        nop=input("\n> ")
        if "name" in nop:
            print("Type the changed name press enter then Type serial number")
            dict["client's name"][int(input())]=(input())
            h=pd.DataFrame(dict)
            h.to_csv(home+"/client data.csv")
        elif "address" in nop:
            print("Type the changed address press enter then Type serial number")
            dict["address"][int(input())]=(input())
            h=pd.DataFrame(dict)
            h.to_csv(home+"/client data.csv")
        elif "type" in nop:
            print("Type the changed type of service press enter then Type serial number")
            dict["type of service"][int(input())]=(input())
            h=pd.DataFrame(dict)
            h.to_csv(home+"/client data.csv")
        elif "contact" in nop:
            print("Type the changed contact number press enter then Type serial number")
            dict["contact"][int(input())]=(input())
            h=pd.DataFrame(dict)
            h.to_csv(home+"/client data.csv")
        elif "return" in nop:
            exit(0)

#storage.child(path_to_cloud).put(home+"/client data.csv") #upload the file on firbase
