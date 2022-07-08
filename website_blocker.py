import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["facebook.com", "www.facebook.com", "instagram.com", "www.instagram.com", "youtube.com", "www.youtube.com", "twitter.com", "www.twitter.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        print("working time")
        with open (hosts_path, "r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect +" "+website+"\n")

    else:
        with open(hosts_path, "r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("fun hours")
    time.sleep(5)
