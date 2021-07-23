from bs4 import BeautifulSoup
import requests
word = input("word: ")

try:
    req = requests.get(f"https://www.dictionary.com/browse/{word}#")
    soup = BeautifulSoup(req.content,"html.parser")
    definition = soup.find(class_="one-click-content css-nnyc96 e1q3nk1v1").text
    print("\n"* 10)
    print(definition) 
    print("\n" * 2)
except:
    print("word not found")
