#! python3
# main.py - Downloads and saves functions from the modules' pages from the Official Python Documentation website.

import requests, bs4, time

url = "https://docs.python.org/3/library/"
mods = ["os", "shutil", "sys"]

def wait():
 for _ in range(3):
  print(".")
  time.sleep(1)	

for x in mods:
  print("Downloading", url+x+".html")

 res = requests.get(url+x+".html")
 wait()

 res.raise_for_status()
 soup = bs4.BeautifulSoup(res.text, "html.parser")

 print("Selecting functions...")
	
 func = soup.select('dt code')
 params = soup.select('dt')
 exp = soup.select('dd')
 code = []
 wait()

 for i in range(0, len(func)-1, 2):
  t1 = func[i].getText()
  t2 = func[i+1].getText()
  code.append(t1+t2)	

 print("Functions selected!")
	
 time.sleep(1.5)

 print("Writing data...")

 for i in range(len(exp)):
  fileName = "data" + x + ".txt"
  file = open(fileName, "a")
  try:
    file.write("\n"+code[i]+"\n"+exp[i].getText() + "\n*************************************\n")
  except Exception:
    print("Weird Character")
  print("Function no.", i, "done!")

  file.close()

 print("Functions for", x, "are done. Moving on to next one.")
 wait()
	
print("All done!")
