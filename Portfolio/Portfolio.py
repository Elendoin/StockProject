import currencies as curr
import currencies.exceptions
import DataRetrieval as dataRetrieval

class Portfolio:
    actions = {}

    def __init__(self, name, mainCurrency):
        self.name = name
        self.mainCurrency = mainCurrency

    def add_stock(self, ticker, value, currency, conversionRate):
        ticker = ticker.upper()
        tickerData = dataRetrieval.find_company(ticker)
        history = tickerData.history(period="1mo")

        if history.empty:
            raise Exception('Incorrect ticker!')

        if tickerData is None:
            raise Exception('TickerData is None!')

        try:
            value = float(value)
        except:
            raise Exception('Invalid value!')

        try:
            currency = curr.Currency(currency)
        except currencies.exceptions.CurrencyDoesNotExist as e:
            raise Exception('This currency does not exist!')

        if currency.money_currency == self.mainCurrency.money_currency:
            self.actions[name] = self.actions.get(ticker, 0) + value
            return 0
        else:
            try:
                conversionRate = float(conversionRate)
                value *= conversionRate
            except:
                raise Exception('Invalid conversion rate!')
            self.actions[ticker] = self.actions.get(ticker, 0) + value
            return 0

