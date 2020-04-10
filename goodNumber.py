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

