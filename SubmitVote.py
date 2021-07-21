import requests as requests
import csv

submitVoteUrl = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/vote"
fileName = "myfile.csv"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'http://coinmarketcap.com', 'Origin': 'https://coinmarketcap.com',
    'Accept': 'application/json, text/plain, */*','Connection':'close',"content-type":'application/json'
    }



with open(fileName,"r") as csvfile :
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        reqBody = {}
        reqBody['cryptoId'] = row[1]
        reqBody['voted'] = 1
        reqBody['votedId'] = row[0]
        try :
            res = requests.post(url = submitVoteUrl,headers=headers,data=reqBody)
            if res.status_code == 200:
                print("success"+res.text)
            else:
                print (res.text)
        except Exception as e:
            print (e)
        print(row[0]+","+row[1])