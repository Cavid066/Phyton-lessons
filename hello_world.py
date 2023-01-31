# # # animal = input('Ferma admin paneline xos geldiniz. Axtardiginiz heyvani daxil edin: ')
# # # farm = ('inek', 'keci', 'at', 'at', 'at', 'keci', 'at', 'qoyun', 'at', 'keci', 'at', 'toyuq', 'inek', 'keci', 'at', 'toyuq', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'qoyun', 'keci', 'keci', 'qoyun', 'at', 'qoyun', 'inek', 'at', 'keci', 'qoyun', 'inek', 'keci', 'qoyun', 'inek', 'toyuq', 'at', 'toyuq', 'keci', 'inek', 'toyuq', 'at', 'toyuq', 'at', 'keci', 'qoyun', 'keci', 'keci', 'inek')
# # # qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}
# # # text = """
# # # Axtarilan Heyvan: {}
# # # {}
# # # Fermadaki {} sayi:  {}
# # # Diger heyvanlara olan faizi: {}
# # # {} umumi qiymeti: {} AZN
# # # """.format(
# # #     animal,
# # #    '-'*20,
# # #    animal,
# # #    farm.count(animal),
# # #    str((farm.count(animal))/len(farm)*100),
# # #    animal,
# # #    str(qiymetler[animal]* farm.count(animal))
# # # )
# # # print(text)


# # users = [
# #     {'name': 'ucal', 'username': 'ucl', 'password': '1234', 'blocked': False},
# #     {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
# #     {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
# # ]


# # # 1. istifadəçi username səhv girərsə belə bir istifadəçi yoxdur deyin
# # # 2. şifrəni səhv girərsə şifrəniz yanlışdır deyin
# # # 3. əgər blok olunubsa siz daxil ola bilməzsiniz deyin
# # # 4. əgər hər şey qaydasındadırsa “filankes giriş etdiniz” deyin



# # # username = input('username daxil edin :  ').strip()
# # # current_user = None

# # # for info in users :
# # #     if username == info['username']:
# # #         current_user = info

# # # if current_user == None:
# # #     print('bele isdifadeci yoxdur')  
# # #     exit()

# # # password = input('sifreni daxil edin: ')

# # # if current_user.get('password') != password:
# # #     print('sifreniz duzgun deyil')
# # #     exit()

# # # if current_user.get('blocked'):
# # #     print('siz daxil ola bilmezsiniz') 
# # #     exit()


# # # print('hormetli {} xosh gelmisiniz!'.format(current_user.get('name')))

# # # shop = {
# # #     "t-shirt" : 59.00,
# # #     "jeans" : 75.00,
# # #     "sweatshirt" : 60.00, 
# # #     "shoe" : 124.99, 
# # #     "jacket" : 154.90
# # # }

# # # # brand = input('mehsulu daxil edin:  ')

# # # # print(shop.get(brand))

# # # new_products = {'papaq': 5, 'kurtqa': 158 }
# # # # result=shop.update(new_products)
# # # # print(result)
# # # print(shop.update(new_products))
# # # # print(shop) 


# # # # print(len(shop))
  
  
# # # for k in shop:
# # #     shop[k] *= 1.3
    
# # # print(shop)

# # # info = ["Resul", 35]

# # # info[0] = 'Resul Serifov'
# # # info[-1] -= 10

# # # ['Resul Serifov', 25]

# # # print(info)

# # # dil = 'Python'
# # # versiya = 3

# # # message = '{} her gun {} {} oyrenirem'

# # # print(message.format('men'.capitalize(), dil.upper(), versiya))

# # eded = 6

# # # if eded % 2:
# # #     nov = 'tek'
# # # else:
# # #     nov = 'cut'

# # # nov = 'tek' if eded % 2 else 'cut'

# # # print(nov)

# # # ededler = [1, 53, 22, 5, 6, 1, 3, 4, 75]
# # # ['tek', 'tek', 'cut', 'tek', 'cut', 'tek', 'tek', 'cut', 'tek']

# # # novler = [ 'tek' if eded % 2 else 'cut' for eded in ededler if eded < 10]
# # # novler = { eded: ('tek' if eded % 2 else 'cut') for eded in ededler if eded < 10}

# # # print(novler)

# # print('alma', 'armud', 'heyva', 'nar', sep=' ve ', end=' yemek isteyirem\n')
# # # print('bitdi!')

# # # ededler.sort(reverse=True)

# # # m1, m2, m3 = ['alma', 'armud', 'heyva']
# # # print(m1, m2, m3)

# # # meyveler = ['alma', 'armud', 'heyva', 'nar']

# # # features = {
# # #     'sep': ' ve ', 
# # #     'end': ' yemek isteyirem\n'
# # # }

# # # print(*meyveler, **features)

# # # s = ['sehve', 'sehife']

# # # cumle = 'sehvelereden en xosuma gelen sehve bu sehvedir'

# # # result = cumle.replace('sehve', 'sehife')
# # # result = cumle.replace(*s)
# # # print(result)




# # l = [10, -21, 46, 73, -35, -31, 71, 36, -92, -53, -34, -18, -78, 54, -49, 2, 62, 25, 14, 8, 63, 84, -83, 40, 90, 57, -15, -7, 35, 78] 
# # bu listdən yeni bir dictionary hazırlayın. Həmin dictionarynin keyləri ədədlər, valueləri isə mübət və ya mənfi yazılı stringlər olacaq.
# # Ornək: {10: 'musbet', -21: 'menfi', ...:...}



# # result= {eded: ('musbet'if eded >0  else 'menfi' ) for eded in l }

# # print(result)

# # cumle = "sehifelerden en yaxsi sehife bu sehifedir"
# # l = ["sehife", "sehve"]
# # result = cumle.replace(*l)
# # print(result)
# # num = 74
# # binnum = bin(num)
# # octnum = oct(num)
# # hexnum = hex(num)
# # print(hexnum)

# # b = '1001010'
# # print(int(b, 2))
# # print(int('112', 8))
# # print(int('4a', 16))


# # print(chr(78))
# # print(ord('N'))
# # print(bin(ord('N')))

# # num = 74
# # binnum = bin(num)
# # octnum = oct(num)
# # hexnum = hex(num)
# # print(hexnum)

# # b = '1001010'
# # print(int(b, 2))
# # print(int('112', 8))
# # print(int('4a', 16))


# # print(chr(78))
# # print(ord('N'))
# # print(bin(ord('N')))

# #  num = 74
# # # binnum = bin(num)
# # # octnum = oct(num)
# # # hexnum = hex(num)
# # # print(hexnum)

# # # b = '1001010'
# # # print(int(b, 2))
# # # print(int('112', 8))
# # # print(int('4a', 16))


# # # print(chr(78))
# # # print(ord('N'))
# # # print(bin(ord('N')))
# # letter = 'G'

# # print(chr(ord(letter) + 32))



# # ('79052479075', "+# ### ### ## ##") => "+7 905 247 90 75"
# # ('79052479075', "+# (###) ### ##-##") => "+7 (905) 247 90-75"
# # ('79052479075', "+# ### ### ## ##") => "+7 905 247 90 75"

# # phone_number = input()
# # print ('{}{}{} {}{} {}{}{} {}{} {}{}'.format(*phone_number))



# # 3. Birinci argument ilk qiyməti, ikinci argument isə yeni qiyməti göstərir. Yeni qiymətin ilkindən neçə faiz fərqləndiyini print edən funksiya düzəldin.
# # `find_percent(200, 60) # output: qiymet 70% azalmisdir` 
# # `find_percent(100, 150) # output: qiymet 50% artmisdir`

# # def find_percent(firs,second):
# #     diff = first - second
# #     percent = (abs(diff) / first) * 100
# #     if first  > second:
# #         print(f'qiymet {percent} azalmisdir ')
# #     elif first < second:
# #         print(f'qiymet {percent}% artmisdir') 
# #     else: first = second:
# #           print('qiymet deyismemisdir')       




# factorial = lambda x: 1 if x == 0 else x * factorial(x-1)
# print(factorial(3))

# baliqlar = {
#     'qelseme teneffusu', '2 kamerali urek', 'uzgec', 'korteks yoxdur',
#     'yumurtlama', 'dis yoxdur', '4 ayaq'
# }

# cuculer = {
#     'toraks teneffusu', 'urek yoxdur', '6 ayaq',
#     'korteks vardir', 'beyin yoxdur', 'yumurtlama', 'metamorfoz', 
#     'dis yoxdur'
# }

# amfibialar = {
#     'qelseme teneffusu', 'agciyer teneffusu', 'uzgec', '4 ayaq', 
#     '2 kamerali urek', '3 kamerali urek', 'metamorfoz', 'kotex vardir',
#     'yumurtlama', 'dis yoxdur'
# }

# surunenler = {
#     'agciyer teneffusu', '3 kamerali urek', '4 ayaq', 'korteks vardir', 'yumurtlama',
#     'dis var'
# }

# quslar = {
#     'agciyer teneffusu', '4 kamerali urek', 'korteks vardir',
#     'yumurtlama', 'dis yoxdur'
# }

# memeliler = {
#     'agciyer teneffusu', '4 kamerali urek', '4 ayaq', 'korteks vardir',
#     'dogma', 'dis vardir'
# }

# sinifler = {
#     'baliqlar': baliqlar,
#     'cuculer': cuculer,
#     'amfibialar': amfibialar,
#     'surunenler': surunenler,
#     'quslar': quslar,
#     'memeliler': memeliler,
# }


# 1. Quşların xüsusiyyətlərinə `"2 ayaq"` əlavə edin.
# 2. Balıqların xüsusiyyətlərindən `"4 ayaq"` məlumatını çıxarın
# 3. Amfibialar ilə cücülərin ortaq cəhətlərini göstərən kod yazın
# 4. Balıqlar ilə amfibiaların fərqli cəhətlərini göstərən kod yazın
# 5. Balıqlar ilə heç bir ortaq cəhətə sahib olmayan sinifi tapan kod yazın
# 6. Quşlar ilə ən çox ortaq cəhətə sahib olan sinifi tapın
# 7. İstifadəçi input ilə sizə bəzi özəlliklər girəcək. Siz həmin özəlliklərə əsasən heyvanın hansı sinifə aid ola biləcəyini təxmin edən kod yazın. Örnək

# `input: dis yoxdur, agciyer teneffusu, korteks vardir` 
# `output: Bu heyvan quslar sinifine aid ola biler`

# quslar.add('2 ayaq')
# print(quslar)

# baliqlar.remove('4 ayaq')
# print(baliqlar)

# print(amfibialar.intersection(cuculer))

# print(baliqlar.difference(amfibialar))

# import math
# def permutasiya(n,r):
#  if n < r:
#   return 
#   'n boyuk olmalidir'
#  else:
#   a = math.factorial(n)
#   diff = math.factorial(n - r)
#   result = a/diff
#  return result
#  print(permutasiya(2,3))

# 3. Giveaway programi duzeldin. Adamlar bitənə qədər hər enter basanda bir ad göstərsin.
    
#     Input ⇒Adlari girin: Hesen, Arif, Elnur, Kamal
    
#     Output⇒Kamal
    
#     Output ⇒Arif
    
#     Output ⇒Hesen

# import random
# names = [ 'Hasan' , 'Husayn ','ali' ,'Elnur']
# print(random.choice(names))


# import time

# for i in range(7, -1, -1):
#     print(f'{i} saniye')
#     time.sleep(1)
# print('bitdi')

import os

# os.mkdir('new file')
# os.chdir('new file')
# os.mkdir('txt.1')
# os.mkdir('txt.2')
# os.rmdir('txt.1')
# os.rename('txt.2', 'Python Notlar')
os.makedirs('/Phyton/General Python')
