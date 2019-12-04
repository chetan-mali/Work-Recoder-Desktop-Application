# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:05:15 2019

@author: Chetan Mali
"""

from datetime import datetime

def update_work(info:str):
    with open('Task Records.txt','a+') as f:
        f.write(f"\n> {info}")
def update_date(current_date:str,day=str):
    with open('Task Records.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    data[0] = f"Updated_Date ={current_date}\n"
    with open('Task Records.txt', 'w') as file:
        file.writelines( data )
    with open('Task Records.txt','a+') as f:
        f.write(f"\n\n----------------------------------\n[Date :{current_date}]    {day}\n----------------------------------")
        
        
if __name__ == "__main__":
    current_date = datetime.now().strftime('%Y-%m-%d')
    day = datetime.today().strftime('%A')
    with open('Task Records.txt') as f:
        Updated_Date = f.readline().split('=')[1]
    if current_date != Updated_Date[:-1]:
        update_date(current_date,day)
    print("@Minicoder",end="")
    while True:
        info = input("Task Done:")
        update_work(info)
        more = ""
        while more not in ["Y","y","n","N"]:
            more = input("Do you want to continue(Y/N):")
        if more == "n" or more == "N":
            break

