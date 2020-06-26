import pyautogui as py
import time


py.FAILSAFE = True

list = {
'https://www.youtube.com/watch?v=ZCu2gwLj9ok',
'https://www.youtube.com/watch?v=yNeo-VUmHJI',
'https://www.youtube.com/watch?v=XnOIRWJ10qU',
'https://www.youtube.com/watch?v=XY28M0dIx6o',
'https://www.youtube.com/watch?v=dnNlnF2Wr_g',
'https://www.youtube.com/watch?v=g80hMksipbI',
'https://www.youtube.com/watch?v=rWVjht-MIto',
'https://www.youtube.com/watch?v=qz7tCZE_3wA',
'https://www.youtube.com/watch?v=iH0PEJxoxiM',
'https://www.youtube.com/watch?v=VtKbiyyVZks',
'https://www.youtube.com/watch?v=3L4Dm-wV5BY',
'https://www.youtube.com/watch?v=DXrfdy2VKa8',
'https://www.youtube.com/watch?v=yV9NTcmWXsE',
'https://www.youtube.com/watch?v=aV5lWd6F6K8',
'https://www.youtube.com/watch?v=u4x9YyRnFDE',
'https://www.youtube.com/watch?v=l9UXpWmedfQ',
'https://www.youtube.com/watch?v=qvbfs6efedQ',
'https://www.youtube.com/watch?v=zzQZ1n1Qgk0',
'https://www.youtube.com/watch?v=KuNUepg9oSQ',
'https://www.youtube.com/watch?v=28GpKacWLWI',
'https://www.youtube.com/watch?v=6UE2WNQDDvY',
'https://www.youtube.com/watch?v=YRLw55eGMn8',
'https://www.youtube.com/watch?v=ZkPY_Ul8gZY',
'https://www.youtube.com/watch?v=xk-BEBSq5AU',
'https://www.youtube.com/watch?v=BubwLnPcQjc',
'https://www.youtube.com/watch?v=ly8EhVV4szY',
'https://www.youtube.com/watch?v=Ppbpxel1A3c',
'https://www.youtube.com/watch?v=S2Ps44EG5hc',
# 'https://m.youtube.com/watch?v=bU0tKzy5-uE',
'https://www.youtube.com/watch?v=8rYMMFT_iXo',
'https://www.youtube.com/watch?v=5u81A0r4V6s',
# 'https://www.youtube.com/watch?v=35fBK7kCTgU&list=RD0TC1Yxh4_O0&index=27',
# 'https://www.youtube.com/watch?v=gxE4ngu78Ro&list=RD0TC1Yxh4_O0&index=27',
# 'https://www.youtube.com/watch?v=HbeCzCw1tT4&list=RD0TC1Yxh4_O0&index=27',
'https://m.youtube.com/watch?v=4eaXoebXKfY',
# 'https://www.youtube.com/watch?v=M83aYoVANOA&list=RDMMaIHF7u9Wwiw&index=27',
# 'https://www.youtube.com/watch?v=UyHk9yRQV7E&list=RDMMaIHF7u9Wwiw&index=27',
# 'https://www.youtube.com/watch?v=vRjh8NxEz30&list=RDMMaIHF7u9Wwiw&index=23',
# 'https://www.youtube.com/watch?v=blYo4WheVgA&list=RDMMaIHF7u9Wwiw&index=22',
'https://www.youtube.com/watch?v=agRVIIdIVIk',
'https://www.youtube.com/watch?v=r6X5obk7ccQ'

}

def add_songs():
    time.sleep(3)

    for song in list:
        py.typewrite('!play ' + song)
        py.press('enter')
        time.sleep(2)

    py.sleep(5)
    py.typewrite('!shuffle')
    py.press('enter')

add_songs()
