
import requests, json, time, datetime



class stocks:

    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15",
        ]
    
        self.Sess = requests.Session()
        self.headers = {'User-Agent': self.user_agents[0]}

        self.Sess.get("https://finance.yahoo.com/")
        self.datacache = {
        "historical":{}
        }

    def history(self, ticker, interval="1d", days=365, startTimestamp=False, endTimestamp=False):

        secounds = days*86400
        period2 = round(time.time())
        period1 = period2-secounds

        if(startTimestamp):
            peroid1 = startTimestamp
                
        if(endTimestamp):
            peroid2 = endTimestamp
            
        
        
        baseurl = "https://query1.finance.yahoo.com/v7/finance/download/"
        


        url=baseurl+ticker+"?period1="+str(period1)+"&period2="+str(period2)+"&interval="+interval+"&events=history"

        #Date,Open,High,Low,Close,Adj Close,Volume
        data = self.Sess.get(url).text.split('\n')
        data.pop(0)
        output = {}
        for line in data:
            line = line.split(',')
            output[line[0]] = {"open":float(line[1]),
                               "high":float(line[2]),
                               "low":float(line[3]),
                               "close":float(line[4]),
                               "adj close":float(line[5]),
                               "change":float(line[4])-float(line[1]),
                               "volume":float(line[6]) }
            
        return output
        



if __name__ == '__main__':

    app = stocks()
    data = app.history('GOOG')
    print(data)
    
    
        

