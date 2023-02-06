from bscscan.accounts import Account
from bscscan.tokens import Tokens
import pandas as pd
import json
import re 
import slack_sdk
import os
import schedule
import datetime
import time

key = 'HTU63DF6739HRD1RV7W4Y6B99JR5X7BSUW'
MY_ADDR = '0xe07B3b1fA77078191033168ADAd506dA1288D24f'

SLACK_TOKEN = 'xoxb-868419702244-4723842834359-urDC5KfB4U8yutxWxJDsA6bL'  #본인의 Slack Bot Token 입력
SLACK_CHANNEL = '#test' #메시지를 보낼 Channel명 입력

api = Account(address=MY_ADDR, api_key=key)
transactions = api.get_transaction_page(page=1, offset=100, sort='desc', erc20=True)
my_addr = MY_ADDR.lower()
#print("--------------------------------------")
#print("   from        to    symbol     amount")
#print("--------------------------------------")
pre_txid = ''
from_list = [] #배열
for each in transactions :
    if each['from'] ==  '0x0000000000000000000000000000000000000000':
        continue
    qty = int(each['value'])/(10**18)
    from_list.append(each['from']) #배열 다 가지고 올 수 있도록, 결과['','',...,'']
    s = "%8s %8s  %7s %8.3f"%(each['from'], each['to'], each['tokenSymbol'], qty)

#api = Tokens(contract_address='0xa5DeC77c4d1B4eba2807C9926b182812A0cBf9Eb',
#             api_key=key)
#balance = api.get_token_balance(address=MY_ADDR)

for i in from_list: #가지고 오는
    api = Tokens(contract_address='0xa5DeC77c4d1B4eba2807C9926b182812A0cBf9Eb',
                api_key=key)
    balance = api.get_token_balance(address=i)  # i = from_list
    # result = re.sub("0", "", balance) #0 빼기
    
    # print(result)
    # print(balance)

def Bscscanbot(slack_messege):  #slack bot massage
    slack_token = SLACK_TOKEN   #slack bot token
    channel = SLACK_CHANNEL     #chnnel for sending massege from slack bot
    message = slack_messege     #message from slack bot 
    client = slack_sdk.WebClient(token=slack_token)
    client.chat_postMessage(channel=channel, text=message)
    

# list_scheduled_messages("1551991429", "2661991427")
    
#def start() :
#    now = datetime.datetime.now() # 현재 시간
#    Bscscanbot.message("시간 : " + str(now) + "PepperFi 현재 사용자 건수 : " + str(balance))
#    openTime = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1) # 자정


chat = "PepperFi 현재 사용자 건수:" + str(len(i)) # 보낼 메시지 입력

def message():
    print("Bscscanbot(chat)")

schedule.every().monday.at("10:55").do(Bscscanbot(chat))

# Bscscanbot(chat)
