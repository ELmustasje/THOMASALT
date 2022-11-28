from tkinter import TOP
from venv import create
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
import random


def start(url):
    worldlist = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    for each_text in soup.findAll('div'):
        content = each_text.text
        words = content.lower().split()
        for each_word in words:
            worldlist.append(each_word)
    clean_wordlist(worldlist)   

def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/.,1234567890 "
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word) > 0:
            clean_list.append(word)
    print(random.choice(clean_list))
    



   
    
    


url = "https://github.com/Xethron/Hangman/blob/master/words.txt"
start(url)

 
  

   
    

    
   