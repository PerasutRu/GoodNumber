import pandas as pd
import requests
from bs4 import BeautifulSoup

r = requests.get('https://somjade.com/ber/search.php?price=1000&show=20000#number_name') # โชว์ทุกเบอร์
r.encoding = 'utf-8' # กำหนด encoding กันปัญหาการถอดรหัสผิดแบบ
s = BeautifulSoup(r.text, 'lxml')
d = s.find('div',{'id':'number_list'})
p_tags = d.find_all('p')
type(p_tags)
Num_number = len(p_tags)
# พิมพ์ตัวอย่าง 1 tag และพิมพ์จำนวน tag ทั้งหมด
print(p_tags[0:1])
print(Num_number)

# =HYPERLINK("url","name")
# hyperlink for cvs file
import time

t0 = time.time()
rows = []
#url_prefix = 'https://somjade.com' # โชว์ 2000 เบอร์
url_prefix = 'https://somjade.com/ber' # โชว์ทุกเบอร์
#for e in p_tags:
for i, e in enumerate(p_tags[0:10]): # ทำ 10 ตัวแรก
  print('เบอร์ที่:', i, 'จาก', Num_number )
  N = e.get_text().split()[0].replace('-', '')
  Number = f"'{N}'"# change '062-961-9871' from '0629619871'
  Network = e.get_text().split()[1]
  Price = e.get_text().split()[2]
  Sex = e.get_text().split()[4]
  Type_paid = e.get_text().split()[5]
  Promotion = e.get_text().split()[6]
  if Type_paid == 'เบอร์เติมเงิน': #เติมเงิน
    Time = '0เดือน'
  else: #รายเดือน
    Time = e.get_text().split()[7]
  if e.get_text().split()[-1] == '[จองแล้ว]':
    Reserve = 'จองแล้ว'
  else:
    Reserve = 'ยังมีของ'
  link= url_prefix + e.find('a')['href'][2:]
  src = f'=HYPERLINK("{link}","{e.get_text().split()[0]}")'

  # ดึงข้อมูล
  r2 = requests.get(link)
  s2 = BeautifulSoup(r2.text, 'lxml')
  d2 = s2.find('span',{'id':'predict_point'})
  Score = d2.text

  rows.append((Number, Network, Price, Sex, Type_paid, Promotion, Time, Reserve, src, Score))
t1 = time.time()
print('เวลาในการคำนวณ: %f'%(t1-t0))

df = pd.DataFrame(rows, columns = ['Number', 'Network', 'Price', 'Sex', 'Type_paid', 'Promotion', 'Time', 'Reserve', 'Link', 'Score'])
df.to_csv('GoodNumber.csv', index= False, encoding="utf-8") # save file to csv

