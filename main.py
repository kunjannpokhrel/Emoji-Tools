import demoji
import json
import requests

url='https://www.emoji.family/api/emojis'
request= requests.get(url)
if request.status_code == 200:
 print("DATA RETRIVED FROM API")
 data= request.json()
else:
 print("EMOJI NOT FOUND")

def text():
  text= input("Enter The Emoji: ")
  if text=="":
    print("EMPTY INPUT (ARE U DUMB OR WHAT?)")
    return None
  emoji=demoji.findall(text)
  for i,j in emoji.items():
   print(f"{i} ---> {j}")

def emoji():
 text = input("Enter The Text: ").strip().lower()
 if not text:
   print("EMPTY INPUT (0 BRAIN CELLS)")
   return None
 found = False
 for item in data:
   tags = item.get('tags') or []
   group = item.get('group', '')
   subgroup = item.get('subgroup', '')
   annotation = item.get('annotation', '')
   for t in tags:
    if text in [t.lower()] or text in [group.lower(), subgroup.lower(), annotation.lower()]:
     print(" ".join(item.get('emoji', [])))
     found = True
 if found==False:
    print("No matching emoji found!! TRY AGAIN BOZO")

def load_data():
  with open("emojiData.json","r") as f:
    data=json.load(f)
  return data

def unicode(emoji):
  if not emoji:
   print("INVALID EMOJI BOZO")
   return None
  return "-".join(f"{ord(c):x}" for c in emoji)

def extract_date(first, second, data):
  unicode1 = unicode(first)
  unicode2 = unicode(second)
  if unicode1 is None or unicode2 is None:
    return None
  if unicode2 not in data:
    print("Emoji not found lol")
    return None
  combinations = data[unicode2]
  for i in combinations:
    if i["leftEmoji"] == unicode1:
     return unicode1, unicode2, i["date"]
  print("Emoji combination not found lol")
  return None

def get_image(date,unicode1,unicode2):
 url=f'https://www.gstatic.com/android/keyboard/emojikitchen/{date}/u{unicode1}/u{unicode1}_u{unicode2}.png'
 response = requests.get(url)
 with open("combined.png", "wb") as f:
  f.write(response.content)
 print("THE FACTORY IS DONE COMBINING !!!")

def combine():
  first=input("First emoji: ").strip()
  if first=="":
    print("EMPTY FIRST EMOJI :)")
    return
  second=input("Second emoji: ").strip()
  if second=="":
    print("EMPTY SECOND EMOJI :)")
    return
  data=load_data()
  result = extract_date(first, second, data)
  if result is None:
    return
  unicode1, unicode2, date = result
  get_image(date, unicode1, unicode2)

def main():
  try:
   choose=int(input("[1] Emoji --> Text \n[2] Text ---> Emoji \n[3] Combine Two Emojis \nCHOOSE ONE: "))
  except ValueError:
   print("PLEASE ENTER A NUMBER (BASIC KNOWLEDGE)")
   return
  if choose== 1:
   text()
  elif choose== 2:
    emoji()
  elif choose== 3:
   combine()
  else:
   print("INVALID CHOICE (BRO RANGE IS 1 to 3)")
main()