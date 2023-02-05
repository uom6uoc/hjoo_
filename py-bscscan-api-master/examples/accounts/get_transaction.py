from bscscan.accounts import Account

key = 'HTU63DF6739HRD1RV7W4Y6B99JR5X7BSUW'

MY_ADDR = '0xa5DeC77c4d1B4eba2807C9926b182812A0cBf9Eb'

api = Account(address=MY_ADDR, api_key=key)
transactions = api.get_transaction_page(page=1, offset=100, sort='desc', erc20=True)
my_addr = MY_ADDR.lower()
print("--------------------------------------")
print("   from        to    symbol     amount")
print("--------------------------------------")
for each in transactions :
    qty = int(each['value'])/(10**18)
    from_addr = ''
    to_addr = ''
    if each['from'] == my_addr :
        from_addr = 'my_addr'
    if each['to'] == my_addr :
        to_addr = 'my_addr'
    print("%8s %8s  %7s %8.3f"%(from_addr, to_addr, each['tokenSymbol'], qty))

print(transactions[0])

