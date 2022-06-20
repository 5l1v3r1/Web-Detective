# -*- coding: utf-8 -*-
import os
os.system('title 👁️‍🗨️ Web Detective 🔍')
from assets.newidentity import *

try:
     from colorama import Fore, init, Back, Style
except: os.system('pip install colorama')
try:
     import requests
except: os.system('pip install requests')

try:
     from pystyle import *
except: os.system('pip install pystyle')
import time

init()

os.system('mode 85,24')
#----------------------------------
fsuc = Fore.LIGHTGREEN_EX
ferr = Fore.RED
wh = Fore.LIGHTWHITE_EX
mag = Fore.GREEN
bmag = Back.LIGHTGREEN_EX
res = Style.RESET_ALL
suc = f'{wh}[{Fore.GREEN}+{wh}]'
err = f'{wh}[{Fore.RED}-{wh}]'
findall = 0
findsuc = 0
niz = '\n'*2

loop = True
while loop:
 os.system('title 👁️‍🗨️ Web Detective 🔍')    
 os.system('cls')   
 print(wh)
 print(niz)
 print("""                         
                  ,_           ____       _            _   _           
                ,'  '\,_      |  _ \  ___| |_ ___  ___| |_(_)_   _____ 
                |_,-'_)       | | | |/ _ \ __/ _ \/ __| __| \ \ / / _ \\
                /##c '\  (    | |_| |  __/ ||  __/ (__| |_| |\ V /  __/
               ' |'  -{.  )   |____/ \___|\__\___|\___|\__|_| \_/ \___|
                 /\__-' \[]   
                /'-_'\        
                '     \  
                
                                 """)
 methods = f"""
 {wh}[{mag}1{wh}] Проверить на наличие Соц.Сетей
 {wh}[{mag}2{wh}] Поиск по нику/почте/имени/телефону 
 {wh}[{mag}3{wh}] Поиск по вашей базе данных
 {wh}[{mag}4{wh}] Новая личность
 """
 detectivevar = input(f'{bmag}Detective{bmag}{res}{wh} >{res}{wh} ')
 if detectivevar == '4':


     lang = input('Язык [Ru/En]: ')
     gend = input('Пол [М/Ж]: ')

     if lang == 'ru' or lang == 'Ru':
          if gend == 'м' or gend == 'М':
           rusucmale()
          if gend == 'ж' or gend == 'Ж':
               rusucfem() 
          jobru()
          address()
          dr()
          input()
     if lang == 'en' or lang == 'En':
          if gend == 'м' or gend == 'М':
           ensucmale()
          if gend == 'ж' or gend == 'Ж':
               ensucfem()
          joben()
          addressen()
          dr()
          input()     

 if detectivevar == 'help' or detectivevar == 'Help':
     print(methods)
     input()
 if detectivevar == '1':
     name = input('Имя: ')
     saveres = input('Сохранять результаты в ТХТ файл? [y/n]: ')
     if saveres == 'y' or saveres == 'Y':
      fn = input('Имя файла: ')
     #вк
     vk = requests.get(f'https://vk.com/{name}')
     if vk.status_code == 200:
          print(f'{suc}{fsuc} VK: {wh}https://vk.com/{name}')   
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'VK: {vk.url}' + "\n")
          else: pass    
     if vk.status_code != 200:
          print(f'{err}{ferr} VK: {wh}https://vk.com/{name}')
     #гитхаб
     gith = requests.get(f'https://github.com/{name}')
     if gith.status_code == 200:
          print(f'{suc}{fsuc} Github: {wh}https://github.com/{name}')   
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'Github: {gith.url}' + "\n")
          else: pass              
     if gith.status_code != 200:
          print(f'{err}{ferr} Github: {wh}https://github.com/{name}')
      #реплит    
     replit = requests.get(f'https://www.replit.com/@{name}')
     if replit.status_code == 200:
          print(f'{suc}{fsuc} Replit: {wh}https://www.replit.com/@{name}')  
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'Replit: {replit.url}' + "\n")
          else: pass               
     if replit.status_code != 200:
          print(f'{err}{ferr} Replit: {wh}https://www.replit.com/@{name}')
     #биолинк     
     biolink = requests.get(f'https://bio.link/{name}')    
     if biolink.status_code == 200:
          print(f'{suc}{fsuc} Biolink: {wh}https://bio.link/{name}')   
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'Biolink: {biolink.url}' + "\n")
          else: pass              
     if biolink.status_code != 200:
          print(f'{err}{ferr} Biolink: {wh}https://bio.link/{name}') 

     #девиан    
     devian = requests.get(f'https://www.deviantart.com/{name}')    
     if devian.status_code == 200:
          print(f'{suc}{fsuc} DevianArt: {wh}https://www.deviantart.com/{name}')   
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'DevianArt: {devian.url}' + "\n")
          else: pass              
     if devian.status_code != 200:
          print(f'{err}{ferr} DevianArt: {wh}https://www.deviantart.com/{name}')        
     #пинтерест   
     pinterest = requests.get(f'https://www.pinterest.ru/{name}')    
     if pinterest.status_code == 200:
          print(f'{suc}{fsuc} Pinterest: {wh}https://www.pinterest.ru/{name}')  
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'Pinterest: {pinterest.url}' + "\n")
          else: pass              
     if pinterest.status_code != 200:
          print(f'{err}{ferr} Pinterest: {wh}https://www.pinterest.ru/{name}')    


     #твич       
     twitch = requests.get(f'https://www.twitch.tv/{name}')    
     if twitch.status_code == 200:
          print(f'{suc}{fsuc} Twitch: {wh}https://www.twitch.tv/{name}')
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'Twitch: {twitch.url}' + "\n")
          else: pass                
     if twitch.status_code != 200:
          print(f'{err}{ferr} Twitch: {wh}https://www.twitch.tv/{name}')      

     #реддит
     redd = requests.get(f'https://www.reddit.com/user/{name}')
     if redd.status_code == 200:
          print(f'{suc}{fsuc} Reddit: {wh}https://www.reddit.com/user/{name}')  
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'Reddit: {redd.url}' + "\n")
          else: pass              
     if redd.status_code != 200:
          print(f'{err}{ferr} Reddit: {wh}https://www.reddit.com/user/{name}')     

     #саундклауд
     sound = requests.get(f'https://soundcloud.com/{name}')
     if sound.status_code == 200:
          print(f'{suc}{fsuc} Soundcloud: {wh}https://soundcloud.com/{name}')  
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'Soundcloud: {sound.url}' + "\n")
          else: pass              
     if sound.status_code != 200:
          print(f'{err}{ferr} Soundcloud: {wh}https://soundcloud.com/{name}')     

     #пастбин
     pastebin = requests.get(f'https://pastebin.com/u/{name}')
     if pastebin.status_code == 200:
          print(f'{suc} {fsuc}Pastebin: {wh}https://pastebin.com/u/{name}')  
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'Pastebin: {pastebin.url}' + "\n")
          else: pass              
     if pastebin.status_code != 200:
          print(f'{err}{ferr} Pastebin: {wh}https://pastebin.com/u/{name}')    
     #одноклассники
     odn = requests.get(f'https://ok.ru/{name}')
     if odn.status_code == 200:
          print(f'{suc} {fsuc}OK: {wh}https://ok.ru/{name}')  
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'OK: {odn.url}' + "\n")
          else: pass              
     if odn.status_code != 200:
          print(f'{err}{ferr} OK: {wh}https://ok.ru/{name}')    

     #скретч
     scr = requests.get(f'https://scratch.mit.edu/users/{name}')
     if scr.status_code == 200:
          print(f'{suc} {fsuc}Scratch: {wh}https://scratch.mit.edu/users/{name}')  
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'Scratch: {scr.url}' + "\n")
          else: pass              
     if scr.status_code != 200:
          print(f'{err}{ferr} Scratch: {wh}https://scratch.mit.edu/users/{name}')    

     #фрилансер
     fre = requests.get(f'https://www.freelancer.com/u/{name}')
     if fre.status_code == 200:
          print(f'{suc} {fsuc}Freelancer: {wh}https://www.freelancer.com/u/{name}')  
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'Freelancer: {fre.url}' + "\n")
          else: pass              
     if fre.status_code != 200:
          print(f'{err}{ferr} Freelancer: {wh}https://www.freelancer.com/u/{name}')    


     #хабр
     habr = requests.get(f'https://habr.com/ru/users/{name}')
     if habr.status_code == 200:
          print(f'{suc}{fsuc} Habr: {wh}https://habr.com/ru/users/{name}')  
          if saveres == 'y' or saveres == 'Y':
               with open(f'{fn}.txt', 'a', -1, 'UTF-8') as f:
                f.write(f'Habr: {habr.url}' + "\n")
          else: pass              
     if habr.status_code != 200:
          print(f'{err}{ferr} Habr: {wh}https://habr.com/ru/users/{name}')     

     input()     

 if detectivevar == '2':
     mail = input('Ник/Почта/Имя/Номер: ')
     save = input('Сохранить в TXT файл?[y/n]: ')
     if save == 'y' or save == 'Y': 
          filename = input('Имя файла: ')
     else: pass          
   
     os.system(f'title Просмотрено: {findall}/7 │ Найдено: {findsuc}')  
     with open('datebase/db1.txt', 'r', encoding="utf8") as f:
           findall += 1
           for text in f.read().split('\n'):
                  if f'{mail}' in text:
                       findsuc += 1 
                       print(f'{text}')
                       if save == 'y' or save == 'Y':
                         with open(f'{filename}.txt', 'a', -1, 'UTF-8') as f:
                          f.write(f'{text}' + "\n")
                       else: pass   

     os.system(f'title Просмотрено: {findall}/7 │ Найдено: {findsuc}')  
     with open('datebase/db2.txt', 'r', encoding="utf8") as f:
           findall += 1
           for text in f.read().split('\n'):
                  if f'{mail}' in text:
                       findsuc += 1 
                       print(f'{text}')
                       if save == 'y' or save == 'Y':
                         with open(f'{filename}.txt', 'a', -1, 'UTF-8') as f:
                          f.write(f'{text}' + "\n")
                       else: pass   
   

     os.system(f'title Просмотрено: {findall}/7 │ Найдено: {findsuc}')   
     with open('datebase/db3.txt', 'r', encoding="utf8") as f:
           findall += 1
           for text in f.read().split('\n'):
                  if f'{mail}' in text:
                       findsuc += 1 
                       print(f'{text}')
                       if save == 'y' or save == 'Y':
                         with open(f'{filename}.txt', 'a', -1, 'UTF-8') as f:
                          f.write(f'{text}' + "\n")
                       else: pass   


     os.system(f'title Просмотрено: {findall}/7 │ Найдено: {findsuc}')     
     with open('datebase/db4.txt', 'r', encoding="utf8") as f:
           findall += 1
           for text in f.read().split('\n'):
                  if f'{mail}' in text:
                       findsuc += 1 
                       print(f'{text}')
                       if save == 'y' or save == 'Y':
                         with open(f'{filename}.txt', 'a', -1, 'UTF-8') as f:
                          f.write(f'{text}' + "\n")
                       else: pass   



     os.system(f'title Просмотрено: {findall}/7 │ Найдено: {findsuc}')       
     with open('datebase/db5.txt', 'r', encoding="utf8") as f:
           findall += 1
           for text in f.read().split('\n'):
                  if f'{mail}' in text:
                       findsuc += 1 
                       print(f'{text}')
                       if save == 'y' or save == 'Y':
                         with open(f'{filename}.txt', 'a', -1, 'UTF-8') as f:
                          f.write(f'{text}' + "\n")
                       else: pass   
 

     os.system(f'title Просмотрено: {findall}/7 │ Найдено: {findsuc}')  
     with open('datebase/db6.txt', 'r', encoding="utf8") as f:
           findall += 1
           for text in f.read().split('\n'):
                  if f'{mail}' in text:
                       findsuc += 1 
                       print(f'{text}')
                       if save == 'y' or save == 'Y':
                         with open(f'{filename}.txt', 'a', -1, 'UTF-8') as f:
                          f.write(f'{text}' + "\n")
                       else: pass   
   
     os.system(f'title Просмотрено: {findall}/7 │ Найдено: {findsuc}')  

     with open('datebase/db7.txt', 'r', encoding="utf8") as f:
           findall += 1
           for text in f.read().split('\n'):
                  if f'{mail}' in text:
                       findsuc += 1 
                       print(f'{text}')
                       if save == 'y' or save == 'Y':
                         with open(f'{filename}.txt', 'a', -1, 'UTF-8') as f:
                          f.write(f'{text}' + "\n")
                       else: pass   


     os.system(f'title Просмотрено: {findall}/7 │ Найдено: {findsuc}')  
     input()



 if detectivevar == '3':
     filename = input('Имя файла: ')
     mail = input('Информация для поиска: ')
     save = input('Записать в TXT файл?[y/n]: ')
     if save == 'y' or save == 'Y':
          filee = input('Имя файла для записи: ')
 
     try:
          with open(f'{filename}.txt', 'r', encoding='utf8') as f:
            for text in f.read().split('\n'):
                  if f'{mail}' in text:
                       print(f'{text}') 
                       if save == 'y' or save == 'Y':
                         with open(f'{filee}.txt', 'a', -1, 'UTF-8') as f:
                          f.write(f'{text}' + "\n")
                       else: pass     
     except: print(f'{err} Ошибка')         
     time.sleep(1)

