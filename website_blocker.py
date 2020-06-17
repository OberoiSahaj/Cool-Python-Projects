from datetime import datetime as dt
import time

starting = dt( 2020, 6, 15, 10 )
ending = dt( 2020, 6, 15, 16 )
        
hosts_path = "C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.youtube.com"]

while True:
    
    if starting < dt.now() < ending:

        time.sleep(10)
        print("Working hours")
        
        with open(hosts_path, "r+") as f:
            f.seek(len(f.read()))
            for website in website_list:
                f.write( "\n" + redirect + " " + website)
        
    else:
        time.sleep(10)
        print("Rest hours")

        with open("hosts_original.txt", "r") as f:
            
            with open(hosts_path, "w") as f2:

                f2.write(f.read())
