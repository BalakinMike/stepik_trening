import json, pprint
with open("manager_sales.json", 'r') as file:
    data = json.load(file)
# for i in range(10):
#     print(data[i]['manager']['first_name'], data[i]['cars'][0]['price'])

priz = {}

for j in range(len(data)):
    sum_0 = 0
    for i in range(len(data[j]['cars'])):
        sum_0 += int(data[j]['cars'][i]['price'])
    priz[j] = sum_0
print(max(priz.values()))
print(priz)
print(data[4]['manager']['first_name'])