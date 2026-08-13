from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib
import requests
import os
load_dotenv()



my_email = os.environ.get("MY_EMAIL")
my_password = os.environ["MY_PASSWORD"]
to_email = os.environ["TO_EMAIL"]
the_url="https://www.jumia.com.ng/fashion-unlimited-baggy-joggers-350468256.html"
response=requests.get(the_url,headers={"Accept-Language":"en-US,en;q=0.5",
                                       "User-Agent":"CCBot/2.0 (https://commoncrawl.org/faq/)"})

soup = BeautifulSoup(response.text,"html.parser")
links = "https://www.jumia.com.ng/fashion-unlimited-baggy-joggers-350468256.html"


line=soup.find(name="span",class_="-b -ubpt -tal -fs24 -prxs").getText().split("₦")
num = int(line[1].replace(",",""))


if num < 90000:
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login("my_email","my_password")
        server.sendmail(
            from_addr="my_email",
            to_addrs="from_email",
            msg=f"UNLIMITED BAGGY JOGGERS on Jumia is now {num}\n{links}"
        )
