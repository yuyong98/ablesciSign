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
    url = "https://mox.moxing.app/forum/sign"
    headers = {
        'accept': 'text/html, application/xhtml+xml',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        'dnt': '1',
        'priority': 'u=1, i',
        'referer': 'https://mox.moxing.app/forum/sign',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
        'x-inertia': 'true',
        'x-inertia-version': 'e6f5ccfa8787fa1408a0ffa93a81c304',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'eyJpdiI6Ik1pVnhBZ1c3LzFUMTVWalpWeVIvb3c9PSIsInZhbHVlIjoiSFNXakgrNUh2M1krVkNXQ3N2ZFlQd1ZkMDZtUjhKQXg2U3dtbHRrdjZlRkZxb3VrM1dPL0I0T1VTckpqbEE5UlF1N1pCNVU1SjB6L1gyekg0VElFLzcrTXdoTEU4U3lDbktSK2h2SGJZUVBReEZsamZsbHVxU25yZXNmTXQ2QWoiLCJtYWMiOiJiZDE3YjBmYzM4ZDllMDg4Mjk1MmZjMDk1MDEyZGJmZmU5MjY2M2E2ZDJkY2E3MWQ3OGRmM2FlNTM3NGJhOGRkIiwidGFnIjoiIn0=',
        # Requests sorts cookies= alphabetically
        'cookie': cookie,
    }
    response = requests.get(url,headers=headers)
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
   # content += "今日MX签到: \n" + msg['msg'] + "\n"
    code = msg['code']
    content += "=========================="
    print(content)
    send("MX签到", content)
