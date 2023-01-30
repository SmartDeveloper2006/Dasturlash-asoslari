# import random
# ismlar=['qodir','nodir','botir','sardor']
# print(random.choice(ismlar))

# import random
# print(random.randint(1,100))

# import random
# ball=0
# for i in range(5):
#     son1=random.randint(1,9)
#     son2=random.randint(1,9)
#     javob=int(input(f"{son1}*{son2}="))
#     if javob==son1*son2:
#         print('😊😊')
#         ball+=1
#     else:
#         print("😈😈")
# print(ball)


import time
vaqt=time.ctime()
print(vaqt)


# from time import gmtime, strftime
# s = strftime("%a, %d %b %Y %H:%M:%S",gmtime(1627987508.6496193))
# print(s)

# 45555255*5875858= 56546465664.split()
import time
vaqt=time.ctime()
hozir=vaqt.split()
yil=hozir[-1]
oy=hozir[1]
hafta_kun=hozir[0]
kun=hozir[2]
vaqt=hozir[-2]
print(f" yil: {yil} \n oy: {oy} \n kun: {kun} \n hafta kuni: {hafta_kun} \n vaqt: {vaqt}")








