# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

#     ### katta harfdagi stringlar ####
# cars = ['Bmw','mercedes benz', 'Volvo', 'gm', 'tesla', 'audi']
# cars.sort()
# print(cars)

#     ### ro'yxatni teskari tartiblash  ###
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)
#
#    ### listni boshqa o'zgaruvchiga tartiblab saqlash ###
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# a=sorted(cars)
# print(cars)
# print(a)


#     ## royxatni teskariga aylantirish ###
# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)

#    ### royxatni tartiblash ####
# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
# print(f"juft sonlar: {juft_sonlar}")
# print(f"toq sonlar: {toq_sonlar}")


# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

#
#     ## ro'yxatni kesish ###
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
# print(my_cars)

   ### nusxa olish ###
# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])


# ismlar=['salom']
# nnusxa=ismlar
mashinalar=["damas","neksiya","malibu"]
uzb=input("masinangizni kiriting")
if uzb in mashinalar: 
    print("bor")
else:
  print("yo'q")