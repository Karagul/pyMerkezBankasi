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


latest_currency = exchange.get_latest(code='USD')
print(latest_currency)