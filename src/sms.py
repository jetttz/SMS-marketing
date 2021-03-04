import pandas as pd
from datetime import date
import time
import random
from twilio.rest import Client
import requests
import urllib.request
from lxml import html
from twilio.base.exceptions import TwilioRestException

class send:
	def __init__(self,amount):
		self.numberofSMS = amount
		self.filename = str(date.today())+"_"+str(amount)+".txt"
		self.message = "we are open today Hey Restaurant"
 
	def processing(self):
		finalnumber = []
		data = open("final.txt","r")
		process = data.read().splitlines()
		
		for i in range(self.numberofSMS):
			finalnumber.append(random.choice(process))
		return finalnumber

	def sendsms(self,listnumber):
		account_sid = "ACCOUNTID"
		auth_token  = "APIKEY"
		client = Client(account_sid, auth_token)
		f = open(self.filename,"a")

		count = 0
		for number in listnumber:
			try:
				f.write(number+"\n")
				message = client.messages.create(to=number, from_="phonenumber",body=self.message)
				count+=1
				print(count)
				
				print(message.sid)
			except:
				print("error")
			
	def compare():
		compare = open("final.txt","r")
		p = compare.read().splitlines()
		data = open("2020-12-29_500.txt","r")
		process = data.read().splitlines()
		data1 = open("send.txt","r")
		process1 = data1.read().splitlines()
		test = open("send1.txt","w")
		count =500
		while count !=0:
			c = random.choice(p) 
			if  c not in process and c not in process1:
				test.write(c+"\n")
				count -=1
				
		test.close()		

		a = open("send1.txt","r")
		s = a.read().splitlines()
		print(len(s))

	def checkareacode(self,number):
		return number[0:3] in open("datacheck/areacode.txt","r").read().splitlines()	

	def read_pagesource(self):
		final=[]
		listnumber = []
		for count in range(1,12):
			url = str(count)+"_500.html"
			readnumber, = pd.read_html(url, header=0, parse_dates=["Phone"])
			readnumber = readnumber[["Phone"]]
			listnumber.extend(readnumber.values.tolist())
		
		
		
		for number in range(len(listnumber)):
			tempnumber = str(listnumber[number])
			removespeical = tempnumber[1:-1]
			if len(removespeical) == 10 and removespeical not in final:
				final.append(removespeical)
		test = []
		history = open("history/2020-12-31_2000.txt","r").read().splitlines()
		history1 = open("history/2021-01-01_2000.txt","r").read().splitlines()
		block = open("datacheck/block.txt","r").read().splitlines()
		f = open("test/final.txt","w")
		
		for i in range(5026):
			if final[i] not in history and final[i] not in history1 and self.checkareacode(final[i]) == True and final[i] not in block:  
				f.writelines(final[i]+"\n")
		f.close()




Phone = open("final.txt","r").read().splitlines()
obj = send(5000)
obj.sendsms(Phone)

