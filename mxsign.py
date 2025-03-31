#!/usr/bin/env python
# cron:40 7,21 * * *
# new Env("MX签到")
# coding=utf-8
import requests
import os
from sendNotify import send
import re
import random
import time

def mx(cookie):
    url = "https://mox.moxing.app/api/forum/check-in/sign"
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://mox.moxing.app',
    'priority': 'u=1, i',
    'referer': 'https://mox.moxing.app/forum/sign',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'eyJpdiI6IlFjNlcraTVJbUNnLzVzUTdTTWQ0VkE9PSIsInZhbHVlIjoiMStRMWN0clAyQ1FxQ1NFVEZ1QzhraDFQb21XQkg2RGVCRlhHa2xwYWVuS25CWTNjbXJIQmJyNHRlODlPUzQ3SWI1YTFiK3pFdFVlTWY2eGlyRkxsKzAxL0ZRQXNoblpRZXpZeENtVHdHQU5OYlRSa0RMN0VZellRdnVmUTJiaCsiLCJtYWMiOiI5YjljNzU2ZDIyNzZhMDkxYjdmN2RlNGFkYTgyOWNlNWQwYmE4OWQ3MDJjZTZlNmE4ZTgxOGJkYzZkYjExYmZhIiwidGFnIjoiIn0=',# Requests sorts cookies= alphabetically
    'cookie': cookie,
    }
    json_data = {}
    response = requests.get(url,headers=headers, json=json_data)
    if response.status_code == 200:
        print("成功访问")
    return response.json()
    
if __name__ == "__main__":
    content = "==========================\n"
    cookie = os.environ.get('MXCOOKIE')
    interval = random.uniform(0, 60)
    msg =  mx(cookie)
    print(msg)
    time.sleep(interval)
   #  content += "今日MX签到: \n" + msg['msg'] + "\n"
   #  code = msg['code']
    content += "=========================="
    print(content)
    send("MX签到", content)
