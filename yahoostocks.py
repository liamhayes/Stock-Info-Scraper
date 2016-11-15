import yahoo_finance as yahoo

def stocks():
    try:
        
        stock = raw_input('Enter Stock Symbol: ')
        Sample = raw_input('What data do you want? ')
        finance = yahoo.Share(stock)

        if Sample.lower() == 'stock price':
            print finance.get_price()

        elif Sample.lower() == 'open':
            print finance.get_open()

        elif Sample.lower() == 'historical':
            dates1 = raw_input('From what date(i.e 2014-04-25)? ')
            dates2 = raw_input('To what date(i.e 2014-04-25)? ')
            filetxt = stock+'.txt'
            historical = str(finance.get_historical(dates1,dates2))
            saveFile = open(filetxt,'a')
            saveFile.write(historical)
            print ('Look for file', filetxt)

    except Exception,e:
        print 'RESTART PROGRAM'

stocks()
