import yfinance as yf
import statistics as stats



class stocks:
    def getOpenPriceList(ticker, peroid = '2y'):
        return list(yf.Ticker(ticker).history(peroid).Open)

    def getChange(data1, data2):
        output = []
        for i in range(len(data1)):
            output.append(data2[i]-data1[i])
        return output
    def getStockChange(ticker, peroid = '2y'):
        Open = list(yf.Ticker(ticker).history(peroid).Open)
        Close = list(yf.Ticker(ticker).history(peroid).Close)
        return stocks.getChange(Open, Close)        

    def cov(data1, data2):
        avg1 = stats.mean(data1)
        avg2 = stats.mean(data2)
        acum = 0 
        for i in range(len(data1)):
            acum+= ((data1[i]-avg1)*(data2[i]-avg2))/len(data1)
        return acum

    def correlation(data1, data2):
        devproduct = (stats.stdev(data1)*stats.stdev(data2))
        return stocks.cov(data1, data2)/devproduct

    def offsetCorrelation(data1, data2, points=1):
        for i in range(points):
            data1.pop(0)
            data2.pop()
        return stocks.correlation(data1, data2)
        

    def tickerCorrelation(ticker1, ticker2, peroid='2y'):
        data1 = stocks.getStockChange(ticker1, '2y')
        data2 = stocks.getStockChange(ticker2, '2y')
        return stocks.correlation(data1, data2)
    def tickerOffsetCorrelation(ticker1, ticker2, points=1):
        data1 = stocks.getStockChange(ticker1)
        data2 = stocks.getStockChange(ticker2)
        return stocks.offsetCorrelation(data1,data2, points)
        

    
if __name__ == '__main__':
    while(True):
        t1 = input("stock1: ")
        t2 = input("stock2: ")
        percent = (stocks.tickerCorrelation(t1, t2)*100)
        offsetpercent = (stocks.tickerOffsetCorrelation(t1,t2, 1)*100)
        print(f"{t1} and {t2} are {percent:0.2f}% correlated")
        print(f"{t1} and {t2} the next day are {offsetpercent:0.2f}% correlated")


