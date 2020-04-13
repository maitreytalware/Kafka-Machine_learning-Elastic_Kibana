from kafka import KafkaProducer
import json
import random
import datetime
import pycountry
import geopy
import geocoder
import uuid
import sys
import csv
import pandas as pd
import time

class DataGenerator:
    def __init__(self):
        self.merchant_list=["Wal-Mart Stores", "The Kroger Co.","Costco","The Home Depot","Walgreen","Target", "CVS Caremark", "Lowes Companies","Amazon.com","Safeway","Best Buy","McDonald","Publix Super Markets","Apple Store / iTunes","Macys","Rite Aid","Royal Ahold / Ahold USA", "Sears Holdings","TJX","H-E-B Grocery","YUM! Brands","Albertsons", "Kohls","Dollar General","Delhaize America","Meijer", "WakeFern / ShopRite","Ace Hardware","BJs Wholesale Club","Whole Foods Market","Doctors Assoc. / Subway","Nordstrom","Gap","AT&T Wireless", "J.C. Penney Co.", "Aldi", "Bed Bath & Beyond", "SUPERVALU", "7-Eleven", "Ross Stores", "Verizon Wireless", "Starbucks", "Family Dollar Stores", "Bi-Lo", "L Brands", "Menard", "Trader Joes", "Wendys","Burger King Worldwide","Dollar Tree","Hy-Vee","Army / Air Force Exchange","Dunkin Group", "Health Mart Systems","AutoZone","Toys R Us","Wegmans Food Market","OReilly Automotive","DineEquity","Giant Eagle","Sherwin-Williams","Dicks Sporting Goods","Staples","Office Depot","Dillards","Good Neighbor Pharmacy", "Darden Restaurants","GameStop","PetSmart","QVC","Chick-fil-A","WinCo Foods","Tractor Supply Co.","Barnes & Noble","A&P","AVB Brandsource", "Signet Jewelers", "Foot Locker", "Big Lots","Hudsons Bay", "Alimentation Couche-Tard", "Defense Commissary Agency", "Neiman Marcus", "Jack in the Box", "Ascena Retail Group", "Burlington Coat Factory", "Ikea North America Services", "Williams-Sonoma", "Save Mart Supermarkets", "Panera Bread Company", "Advance Auto Parts", "Michaels Stores", "True Value Co.", "Dominos Pizza", "Belk", "Chipotle Mexican Grill", "Sonic", "Stater Bros. Holdings", "Price Chopper Supermarkets","Dell"]
        self.userList=[]
        self.marital_status_list=["Single", "Married"]
        self.gender_list=["Male", "Female"]
        self.loan_list=["Yes","No"]
        self.getUserDetails()

    def getUserDetails(self):
        try:
            with open('user_info.csv', 'r',encoding="ISO-8859-1") as csvfile:
                reader=csv.reader(csvfile)
                for row in reader:
                    if row not in self.userList:
                        self.userList.append(row)
        except KeyboardInterrupt:
            exit()

    def generateRandomTransaction(self):
        cc_no=random.randint(1000000000000000,9999999999999999)
        cc_provider=random.randint(1000,9999)
        random_country=random.randint(0,248)
        country=(list(pycountry.countries)[random_country])
        country_code=country.alpha_2
        country_name=country.name.replace("'","")
        age=random.randint(20,70)
        marital_status=random.choice(self.marital_status_list)
        marital_status_index=self.marital_status_list.index(marital_status)
        gender=random.choice(self.gender_list)
        gender_index=self.gender_list.index(gender)
        loan=random.choice(self.loan_list)
        loan_index=self.loan_list.index(loan)
        country_index=random_country
        return [cc_no,cc_provider,country_name,country_code,country_index,age,marital_status,marital_status_index,gender,gender_index,loan,loan_index]

    def generateTransactions(self):
        choice_value=random.randint(1,100)
        # choice_value=9
        if (choice_value<70):
            #print (choice_value)
            current_txn=random.choice(self.userList)
            #print (current_txn)
        else:
            current_txn=self.generateRandomTransaction()

        base_amount = random.randint(100,1000)
        variance = random.randint(10,40)
        cc_no=current_txn[0]
        cc_provider=current_txn[1]
        country_name=current_txn[2]
        country_code=current_txn[3]
        country_index=current_txn[4]
        age=current_txn[5]
        marital_status=current_txn[6]
        marital_status_index = current_txn[7]
        gender=current_txn[8]
        gender_index=current_txn[9]
        loan=current_txn[10]
        loan_index=current_txn[11]
        #--------------------------------------Check once-------------------------------
        amount = base_amount +( random.uniform(5,50) *variance)
        #amount = base_amount +( random.uniform(-4,6) *variance)
        merchant=random.choice(self.merchant_list)
        merchant_index=self.merchant_list.index(merchant)
        txn_time=datetime.datetime.now()
        year=txn_time.year
        month=txn_time.month
        day=txn_time.day
        hour=txn_time.hour
        minute=txn_time.minute
        txn_id=uuid.uuid1()
        # print (type(merchant_index))
        # print (type(country_index))
        # print (type(marital_status_index))
        # print (type(gender_index))
        # print (type(loan_index))
        data_to_send={"txn_id":str(txn_id),"cc_no":cc_no,"txn_time":str(txn_time),"year":year,"month":month,"day":day,"hour":hour,"minute":minute,"amount":round(amount,2),"cc_provider":cc_provider,"merchant":merchant,"merchant_index":int(merchant_index),"country_name":country_name,"country_code":country_code,"country_index":int(country_index),"age":age,"marital_status":marital_status,"marital_status_index":int(marital_status_index),"gender":gender,"gender_index":int(gender_index),"loan":loan,"loan_index":int(loan_index),"status":"None","status_index":0}
################## Check if status and status_id needs to be send###########
        print (data_to_send)
        return data_to_send

class MyListener:
    def __init__(self):
        # self.producerObj = Producer()
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'],client_id="test-producer",acks=1,retries=5, key_serializer=lambda a:json.dumps(a).encode('utf-8'),value_serializer=lambda b:json.dumps(b).encode('utf-8'))
        # print (self.producer.partitions_for('fifth_topic'))
        # print (self.producerObj)

    def send_data(self,data):
        data=json.dumps(data)
        jsondata=json.loads(data)
        # print (jsondata)
        future=self.producer.send('fifth_topic', value=jsondata, key=jsondata['txn_id'])
        # print (future)

        self.producer.flush()
        # self.producer.close()
    # def __del__(self):
        # self.producer.close()

dataGenerator=DataGenerator()
myListener=MyListener()

try:
    while True:
        temp_data=dataGenerator.generateTransactions()
        ##########Uncomment to send data to consumber#########
        myListener.send_data(temp_data)
        #print (temp_data)
        time.sleep(0.5)
except KeyboardInterrupt:

    exit()
