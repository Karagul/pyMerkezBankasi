from xml.etree import ElementTree
from urllib.request import urlopen
from urllib.error import HTTPError
from datetime import date as _date, timedelta


class Currency:
    def __init__(self, currency: ElementTree):
        self.code = currency.get('Kod')

        temp = currency.find('Unit').text
        self.unit = int(temp) if temp else None

        self.name = currency.find('Isim').text

        self.currency_name = currency.find('CurrencyName').text

        temp = currency.find('ForexBuying').text
        self.forex_buying = float(temp) if temp else None

        temp = currency.find('ForexSelling').text
        self.forex_selling = float(temp) if temp else None

        temp = currency.find('BanknoteBuying').text
        self.banknote_buying = float(temp) if temp else None

        temp = currency.find('BanknoteSelling').text
        self.banknote_selling = float(temp) if temp else None

        cross_rate_usd = currency.find('CrossRateUSD').text
        self.cross_rate_usd = float(cross_rate_usd) if cross_rate_usd else None

    def __repr__(self):
        return f'--------\nCode: {self.code}\nUnit: {self.unit}\nName: {self.name}\nCurrency Name: {self.currency_name}\n' \
               f'Forex Buying: {self.forex_buying}\nForex Selling: {self.forex_selling}\nBanknote Buying:' \
               f' {self.banknote_buying}\nBanknote Selling: {self.banknote_selling}\nCross Rate USD: ' \
               f'{self.cross_rate_usd}\n--------'


class Exchange:
    _base_url = "https://www.tcmb.gov.tr/kurlar/"

    def _get_xml(self, date: _date = _date.today()):
        if not isinstance(date, _date):
            raise TypeError

        if date == _date.today():
            url = f'{self._base_url}today.xml'
        else:
            url = f'{self._base_url}{date.year}{date.month:02d}/{date.day:02d}{date.month:02d}{date.year}.xml'

        try:
            xml = urlopen(url)
        except HTTPError:
            return None

        return ElementTree.parse(xml).getroot()

    @staticmethod
    def _parse_xml(xml: ElementTree, code='USD'):
        if not xml:
            return None
        for currency in xml.findall('Currency'):
            if currency.get('Kod') == code:
                return Currency(currency)

    def get_today(self, code='USD'):
        xml = self._get_xml()
        return self._parse_xml(xml, code)

    def get_yesterday(self, code='USD'):
        xml = self._get_xml(_date.today() - timedelta(days=1))
        return self._parse_xml(xml, code)

    def get(self, date, code='USD'):
        xml = self._get_xml(date)
        return self._parse_xml(xml, code)


