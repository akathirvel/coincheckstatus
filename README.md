# coincheckstatus
Python version 3.8


Download the code
step 1:
pip install -r requirements.txt

step 2:
add the entry in input.json

    sender email id  and password
    receiver_email id 
    url
    
    {

          "sentmail": "test4anglesk@gmail.com",
          "password": "xxxxxxx",
          "receiver_email": "xxxxxx@gmail.com",
          "url": "https://api.coingecko.com/api/v3/status_updates?project_type=coin"
        }


step 3:
    python WSInvoke.py
