import csv
import cbpro
import os

# Clear Library
from Lib import clear

clear.clear()


public_client = cbpro.PublicClient()

days = public_client.get_product_24hr_stats('ETH-USD')

f = open('CoinBaseDays.csv', 'w', encoding='UTF8')

empty = []

empty.append(days)

writer = csv.writer(f)

row = empty[0:10]

writer.writerow(row)

print(days)

f.close()
