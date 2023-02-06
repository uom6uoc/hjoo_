#Protocon transactions 코드
from bscscan.accounts import Account

key = 'HTU63DF6739HRD1RV7W4Y6B99JR5X7BSUW'

address = '0xa5DeC77c4d1B4eba2807C9926b182812A0cBf9Eb'

api = Account(address=address, api_key=key)
transactions = api.get_all_transactions(offset=100, sort='asc', internal=False)

print(transactions[0])

#결과: page 73 added로 보여준다