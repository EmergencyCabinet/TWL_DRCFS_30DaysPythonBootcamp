# web ma use garne ra 2 ta api lai interact garna use garxam 
#2 ta kura lai communicate aile internet ma bhako lai afno lai 
# application program interface 
#aba web api ko use garne 

import requests 

response = requests.get('https://my-json-server.typicode.com/typicode/demo/posts')
print(response.json())

new_response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(new_response.json())

# website ko HTML ma lekheko kura aayo 
# tei duita kura json format ma bhako le link garxa 
# get le chai lerauxa 
# kunai ne wesite ko bhitra ko content herne le chai request. get garne ho 
# dekhaune chai CHROME haru le ho 
# tara eta hamilai hernu xaina CODE hernu xa so WEBSITE  le bhitra o code pathauxa ra .get garxa eta hamle code matra pauxam 
