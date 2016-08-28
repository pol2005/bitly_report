import bitly_api.bitly_api
import csv
import datetime


csv_file=csv.writer(open('my_file.csv','wb'),delimiter =';')
c = bitly_api.Connection(access_token='<your_access_token>')
headers = ["bitlink","long url","created","clicks"]
csv_file.writerow(headers)

for field in c.user_link_history():
    csv_file.writerow([field['link'],field['long_url'],datetime.datetime.fromtimestamp(field['created_at']).strftime('%Y-%m-%d %H:%M:%S'),c.link_clicks(field['link'])])


