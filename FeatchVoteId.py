import requests
import json
import time

import requests as requests

coinId = "1"
noOfIntr = 15
voteUniqueIdUrl = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/vote?id=" + coinId
submitVoteUrl = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/vote"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'http://coinmarketcap.com', 'Origin': 'https://coinmarketcap.com',
    'Accept': 'application/json, text/plain, */*','Connection':'close'
    }

### fetch vote unique id and submot the vote
try :
    file1 = open('myfile.csv', 'w')
    previousId = ""
    for i in range(0, noOfIntr):
        res = requests.get(voteUniqueIdUrl, headers=headers)
        if res.status_code == 200:
            data = res.json()
            ss = data['data']['unregisteredId']

            print(ss)
            if previousId != ss:
                previousId = ss
                file1.write(data['data']['unregisteredId']+","+coinId+"\n")
            else:
                print('Same')
                time.sleep(61)
            res.connection.close()


    file1.close()
except Exception as e:
    print(e)
finally:
    if not file1.closed:
        file1.close()