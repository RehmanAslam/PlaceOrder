





"""
import requests
url = 'https://...'
payload = {'key1': 'value1', 'key2': 'value2'}

# GET
r = requests.get(url)

# GET with params in URL
r = requests.get(url, params=payload)

# POST with form-encoded data
r = requests.post(url, data=payload)

# POST with JSON 
import json
r = requests.post(url, data=json.dumps(payload))

# Response, status etc
from threading import _newname
r.text
r.status_code """

"""
get_response = requests.get(url='http://google.com')
post_data = {'username':'joeb', 'password':'foobar'}
# POST some form-encoded data:
post_response = requests.post(url='http://httpbin.org/post', data=post_data)
#To send data that is not form-encoded, send it serialised as a string (example taken from the documentation):
"""
      
        
import json
import requests
import facebook



"""url = "http://localhost:8080"
data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
"""
"""




#phone = newPhone.json();



print("data is  posting")
print(postResponse.json())"""







urlbk = 'https://api.skylinedynamics.com/bk/v1.6/orders'
menu_api = 'https://api.skylinedynamics.com/bk/v1.6/menus'
guestLogin = 'https://api.skylinedynamics.com/bk/v1.6/guest-login'





json_data = requests.get(menu_api).json()

customer_id = 1818636
address_id = 2135116
store_id = 2
weight = 1
quantity = 1
orderMode = 1
orderType = 0
serviceCharge = 7
Source = 10
subtotal = 0
grossTotal = 0
discount = 0
total = 0
note = 'Please bring a change for 100'
name = input('Which Meal = ').upper()

price = 0
itemId = 0
phone = "+966538280597"
"""headers = {'Content-type':'application/json','Accept':'text/plain'}
postData = {'phoneNumber':phone}
postResponse = requests.post(guestLogin, data=json.dumps(postData),headers=headers)
"""

headers = {'Content-type':'application/json','Accept':'text/plain',"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXN0b21DbGFpbXMiOnsiaWQiOiIxODE4NjM2IiwidXNlcm5hbWUiOiJndWVzdC03Y2I3YWY4NTFlODczNDg5MWY2NGQ1OThlYTI4MWNlNEBlbWFpbC5jb20iLCJlbWFpbCI6Imd1ZXN0LTdjYjdhZjg1MWU4NzM0ODkxZjY0ZDU5OGVhMjgxY2U0QGVtYWlsLmNvbSIsImZpcnN0bmFtZSI6IiIsImxhc3RuYW1lIjoiIiwicGhvbmVOdW1iZXIiOiIrOTY2NTM4MjgwNTk3IiwidmVyaWZpZWQiOnRydWUsImF1dGhUeXBlIjoiZ3Vlc3QiLCJiaXJ0aGRheSI6IjkwMDAtMDEtMDEifSwiaXNzIjoiaHR0cDovLzU0LjE1NC43LjExOjgwODQvZ3Vlc3QtbG9naW4iLCJpYXQiOjE1MTMxNTI1NTMsImV4cCI6MTcwMjM2ODU1MywibmJmIjoxNTEzMTUyNTUzLCJqdGkiOiJYMTJSbWNOWnR1ZU4yVThMIn0.wj5Gj7zEYOR5DdN64lzC4i4hHSIJTnczcK39JavK12A"}

for sandwich in json_data['subMenu'][2]['items']:
        
        if name in sandwich['name']:
            
           # token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXN0b21DbGFpbXMiOnsiaWQiOiIxODE4NjM2IiwidXNlcm5hbWUiOiJndWVzdC03Y2I3YWY4NTFlODczNDg5MWY2NGQ1OThlYTI4MWNlNEBlbWFpbC5jb20iLCJlbWFpbCI6Imd1ZXN0LTdjYjdhZjg1MWU4NzM0ODkxZjY0ZDU5OGVhMjgxY2U0QGVtYWlsLmNvbSIsImZpcnN0bmFtZSI6IiIsImxhc3RuYW1lIjoiIiwicGhvbmVOdW1iZXIiOiIrOTY2NTM4MjgwNTk3IiwidmVyaWZpZWQiOnRydWUsImF1dGhUeXBlIjoiZ3Vlc3QiLCJiaXJ0aGRheSI6IjkwMDAtMDEtMDEifSwiaXNzIjoiaHR0cDovLzU0LjE1NC43LjExOjgwODQvZ3Vlc3QtbG9naW4iLCJpYXQiOjE1MTMxNTI1NTMsImV4cCI6MTcwMjM2ODU1MywibmJmIjoxNTEzMTUyNTUzLCJqdGkiOiJYMTJSbWNOWnR1ZU4yVThMIn0.wj5Gj7zEYOR5DdN64lzC4i4hHSIJTnczcK39JavK12A'
            newName = name
            price = sandwich['price']
            itemId = sandwich['itemId']
            subTotal = price - discount
            Total = subTotal +serviceCharge
            
           # post_data = {'phoneNumber':phone,'itemName':newName,'itemId':itemId ,'grossTotal':price,'storeId':store_id,'customerId':customer_id,'weight': weight,'discount':discount,'quantity':quantity,'source': Source,'orderType':orderType,'serviceCharges':serviceCharge,'orderMode':orderMode,'subTotal':subTotal,'Total':Total,'note':note}
            #postResponse = requests.post(guestLogin, data=json.dumps(post_data),headers=headers)
            post_data = {
  "orderMode": 1,
  "orderType": 0,
  "customerId": "1818636",
  "addressId": "1887881",
  "storeId": "2",
  "subTotal": 37,
  "discountTotal": 0,
  "grossTotal": 37,
  "total": 44,
  "serviceCharge": 7,
  "entries": [
    {
      "itemId": 40008,
      "name": "BIG KING™ XL MEAL",
      "price": 26,
      "modifiers": [
         {
            "modItemId": 100038,
            "name": "Coke",
            "price": 0,
            "weight": 1,
            "quantity": 1,
            "modGroupId": 11002
          },
          {
            "modItemId": 100143,
            "name": "Coke",
            "price": 0,
            "weight": 1,
            "quantity": 1,
            "modGroupId": 11014
          }
      ]
    },
    {
      "itemId": 0,
      "name": "ONION RINGS",
      "price": 0,
      "modifiers": [
          {
                "modItemId": 80019,
                "name": "ONION RINGS LARGE (15 PC)",
                "price": 11,
                "weight": 1,
                "quantity": 1,
                "modGroupId": 0
              }
      ]
    }
  ],
  "notes1": "THIS IS JUST A TEST PLEASE CANCEL",
  "notes2": "",
  "creditCardIsPayment": False,
  "source": 11
}
            
            #post_data = {'phoneNumber':phone,'itemName':newName,'price':price}
            post_response = requests.post(url=urlbk, data=post_data,headers=headers)
            
            #print(newData)
            #print(post_data)
            print(post_response.json())
                       
                       
                    
