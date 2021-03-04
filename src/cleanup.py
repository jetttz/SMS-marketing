import pandas as pd


class clean:
	
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


	def checkfirstcolum(self,rawdata):
		return any(list(map(lambda check: True if check in str(rawdata) else False, ["PHONE","Phone","phone","Phone#","PHONE#","Phonenumber","PHONENUMBER"])))

	def findfirstcolum(self,rawdata):
		phone  = ["PHONE","Phone","phone","Phone#","PHONE#","Phonenumber","PHONENUMBER"]
		index = 0
		for a,b in enumerate(list(map(lambda check: True if check in str(rawdata) else False, ["PHONE","Phone","phone","Phone#","PHONE#","Phonenumber","PHONENUMBER"]))):
			if b:
				index = a

		return phone[index]

	def checkonecolumn(self,data):
		
	    	return len(data.columns) < 2 

	def checkcsv(self,rawdata):
		#check if the remvoe square bracket and check phone is in correct format and correct areacode only in us  then Filter out None in the list and put it in list again
		try:
			if self.checkonecolumn(pd.read_csv(rawdata)):
				return list(filter(None,list(map(lambda phone: str(phone)[1:-1] if self.checkformat(str(phone)[1:-1]) == True and self.checkareacode(str(phone)[1:-1]) == True else None  , 
				pd.read_csv(rawdata).to_numpy().tolist()))))
			elif self.checkfirstcolum(pd.read_csv(rawdata)):
				return list(filter(None,list(map(lambda phone: str(phone)[1:-1] if self.checkformat(str(phone)[1:-1]) == True and self.checkareacode(str(phone)[1:-1]) == True else None  , 
				pd.read_csv(rawdata,usecols=[self.findfirstcolum(pd.read_csv(rawdata))] ).to_numpy().tolist()))))		
		except :
			print("DataError")


	def checkareacode(self,number):
		return number[0:3] in open("datacheck/areacode.txt","r").read().splitlines()

	def checkformat(self,number):
		return len(number) == 10 or len(number) == 11

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





