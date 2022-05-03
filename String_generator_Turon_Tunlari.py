# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 13:32:19 2022

@author: Mehrol Bazarov Baxtiyorovich
"""


""" TIP 1 list orqali """
import random

ibora1 = "Maqsadning enasini aytg'oningiz ma'qul" 
ibora2 = "Ozroq e'tibor, ozroq qunt bo'lsa, go'radan holva pishadi"
ibora3 = "Qirq yil qirg'in bo'lsa, ajali yetgan o'lur"

#initializing list
ibora_list = [ibora1, ibora2, ibora3]

#printing original list

print("\n Iboralar ro'yxati : " + str(ibora_list))

#using random.choice() to
#get a random ibora

random_ibora = random.choice(ibora_list)

#printing random ibora
print("\n Tasodifiy tanlangan ibora : " + str(random_ibora))




""" TIP 2 dictionary orqali """
# Python3 code to demonstrate working of
# Get random dictionary pair in dictionary
# Using random.choice() + list() + items()
import random
 
# Initialize dictionary
#ibora maqol gap hikmat duo Nasihat
ibora_dict = {'bet19' : "Maqsadning enasini aytg'oningiz ma'qul" , 
              'bet20' : "Ozroq e'tibor, ozroq qunt bo'lsa, go'radan holva pishadi", 
              'bet22' : "Qirq yil qirg'in bo'lsa, ajali yetgan o'lur",
              'bet23_1' : "Sinalmagan otning sirtidan o'tmaydirlur",
              'bet23_2' : "Bul kurash maydoni, Balx bozori emas",
              'bet43' : "Bizg'a ishonib, tuya ustida it qopdimu",
              'bet46' : "Jahl chiqsa, aql ketar",
              'bet50' : "Mamatning sovuniga kir yuvmabsan hali",
              'bet61_1' : "Erni er qiladurg'on ham xotun, go'r qiladurg'on ham xotin",
              'bet61_2' : "Yarim niyat - yarim davlat",
              'bet71' : "Bo'ylaringga qoqindiq",
              'bet77' : "Pul bo'lsa, changalda sho'rva", 
              'bet79' : "Kim ham bunaqalarning mushigini pisht desin",
              'bet86' : "Burning'izning ustida allaqanday zoti past chivin uchub yuribdi",
              'bet93' : "Chillaliksiz, inim",
              'bet94' : "Sen moxov bo'lsa, paxta qo'yishdan boshqasiga yaramaysan",
              'bet95' : "O'zim bek, o'zim xon, ko'lankam - maydon",
              'bet102_1' : "Ikki qo'chqorning boshi bir qozonda qaynamaydi",
              'bet102_2' : "Ot eng yaxshi yo'ldosh",
              'bet106' : "Tavakkalning boshi kal",
              'bet107' : "Otarga o'qi, ko'rarga ko'zi bo'lmay qoldi",
              'bet112' : "Yashil boqqa o'rgangan qushning tikanzorda yashagisi kelmas",
              'bet113' : "O'ychi o'yini o'ylaguncha tavakkalchi ishini bitiribdi",
              'bet114_1' : "Burgaga achchiq qilib ko'rpani kuydirgan bilan foyda bormu", 
              'bet114_2' : "Tog'ni ursa talqon qiladi"}

 
# printing original dictionary
# print("\n Iboralar lug'ati' : " + str(ibora_dict))

print("\n Iboralarning soni " + str(len(ibora_dict))) 
i = len(ibora_dict)
while i < 31:
      # Get random dictionary pair in dictionary
      # Using random.choice() + list() + items()
      res = key, val = random.choice(list(ibora_dict.items()))
      # printing result
      print("\n Tasodifiy tanlangan ibora : " + str(val))
      i += 1
      


"""
References
https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
https://www.geeksforgeeks.org/python-get-random-dictionary-pair/

"""