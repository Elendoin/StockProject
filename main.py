import csv
import currencies as curr
import currencies.exceptions
import time
import AnomalyDetection
import DataRetrieval
import Portfolio.Portfolio as portfolio
import DataRetrieval as dataRetrieval
import yfinance as yf




if __name__ == '__main__':
    '''tickers = ['ORCL', 'AMD', 'PYPL', 'AI', 'MDB']
    try:
        data = yf.download(tickers, period = '1mo')['Close']
    except Exception as e:
        print(f"Error fetching data: {e}")
        exit(1)
    returns = cal.calculate_returns(data)
    result = cal.markowitz_optimization(returns, 0)
    print(result)
    print(result.sum())
    choice = input('Load wallet or create a new one:\n1 - Load\n2 - Create\n3 - Exit\n')'''

    pf = portfolio.Portfolio("Nikodem", currencies.Currency("PLN"))
    list_NASDAQ = open("NASDAQ.txt", "r")
    list_NASDAQ = list_NASDAQ.readlines()
    list_GPW = open("GPW.txt", "r")
    list_GPW = list_GPW.readlines()

    while True:
        choice = input('1 - Add stocks\n2 - Optimization\n3 - View wallet\n4 - Anomaly analysis\n5 - Exit\n')

        if choice == str(1):
            ticker = input("Enter the company ticker:\n")
            value = input("Enter the value:\n")
            currency = input("Enter the currency:\n")
            conversionRate = input("Enter the conversionRate:\n")
            try:
                result = pf.add_stock(ticker, value, currency, conversionRate)
            except Exception as e:
                print(f'An error occurred - {e}')

            if result != 0:
                print('Unknown error!')
                continue
        elif choice == str(2):
            print('Choice 2')

        elif choice == str(3):
            print(pf.actions)

        elif choice == str(4):
            ticker_list = DataRetrieval.compile_ticker_list(list = list_NASDAQ)
            ticker_list_gpw = DataRetrieval.compile_ticker_list(list_GPW = list_GPW)
            data1 = yf.download(ticker_list, period = '1mo')['Close']
            data2 = yf.download(ticker_list_gpw, period='1mo')['Close']
            result1 = AnomalyDetection.determine_anomaly(data1, 1.15)
            result2 = AnomalyDetection.determine_anomaly(data2, 1.15)
            anomaly_detected = False


            anomaly_list = []
            for key in result1:
                if result1[key] == True:
                    anomaly_detected= True
                    anomaly_list.append(key)
            for key in result2:
                if result2[key] == True:
                    anomaly_detected = True
                    anomaly_list.append(key)

            if anomaly_detected:
                print('Anomalies detected!')
            else:
                print('No anomalies detected!')

            while True:
                choice = input('1 - Display anomalies\n2 - List all\n3 - Return\n')
                if choice == str(1):
                    print(anomaly_list)
                elif choice == str(2):
                    for element in result1, result2:
                        print(element)
                elif choice == str(3):
                    break



        elif choice == str(5):
            exit(0)


