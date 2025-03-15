import yfinance as yf


def find_company(name):
    try:
        ticker_data = yf.Ticker(name)
        info = ticker_data.info
        return ticker_data
    except Exception as e:
        print(f"Error - fetching data: {e}")
        return None


def compile_ticker_list(list = None, list_GPW = None):
    new_list = []
    if list is not None:
        for line in list:
            new_list.append(line[:-1])
    if list_GPW is None:
        if not new_list:
            return list
        else:
            return new_list
    for line in list_GPW:
        line = line[:-1] +'.WA'
        new_list.append(line)
    return new_list
