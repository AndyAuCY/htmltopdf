import subprocess
import datetime
import pdfkit
url = input("输入网址：")
cur_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '.pdf'
print(cur_time)
subprocess.call('wkhtmltopdf ' + url + ' ' + cur_time)