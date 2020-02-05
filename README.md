# pyMerkezBankasi
Merkez Bankası Currencies

f-strings support python3.6+

Returns Python object Currency

Example Usage:

from currency import Exchange
from datetime import date

exchange = Exchange()

currency_today = exchange.get_today()  # Default code USD
print(currency_today)
print(currency_today.banknote_selling)

currency_yesterday = exchange.get_yesterday(code='EUR')  # Get Euro Currency of yesterday
print(currency_yesterday)
print(currency_yesterday.forex_selling)

specific_date = date(2019, 1, 2)
specific_currency = exchange.get(date=specific_date, code='GBP')
print(specific_currency)


output:

--------
Date: 2020-02-05
Code: USD
Unit: 1
Name: ABD DOLARI
Currency Name: US DOLLAR
Forex Buying: 5.976
Forex Selling: 5.9867
Banknote Buying: 5.9718
Banknote Selling: 5.9957
Cross Rate USD: None
--------
5.9957
--------
Date: 2020-02-04
Code: EUR
Unit: 1
Name: EURO
Currency Name: EURO
Forex Buying: 6.6017
Forex Selling: 6.6136
Banknote Buying: 6.5971
Banknote Selling: 6.6235
Cross Rate USD: None
--------
6.6136
--------
Date: 2019-01-02
Code: GBP
Unit: 1
Name: İNGİLİZ STERLİNİ
Currency Name: POUND STERLING
Forex Buying: 6.7643
Forex Selling: 6.7996
Banknote Buying: 6.7596
Banknote Selling: 6.8098
Cross Rate USD: None
--------
--------
Date: 2020-02-05
Code: USD
Unit: 1
Name: ABD DOLARI
Currency Name: US DOLLAR
Forex Buying: 5.976
Forex Selling: 5.9867
Banknote Buying: 5.9718
Banknote Selling: 5.9957
Cross Rate USD: None
--------


