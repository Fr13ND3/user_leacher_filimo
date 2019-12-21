from os import system,name
try:
    import requests
except ModuleNotFoundError:
    print("Module Requests is Not Found !!")
    print("Start Installing !!")
    if name =="nt":
        system('pip install requests --user')
    else:
        system('sudo pip install requests')
from time import sleep
import re
try:
    with open('user_leached_filimo.txt','x'):
        pass
except Exception:
    pass
try:
    with open('link_leached_filimo.txt','x'):
        pass
except Exception:
    pass
_count_ = 0
count = 0
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'
}
links = []
url = ['https://www.filimo.com/iranian','https://www.filimo.com/','https://www.filimo.com/serial']
print('[*] Leaching Link...')
for bingo in url:
    req = requests.get(bingo,headers=headers)
    _div_ = re.compile('<div class="item swiper-slide"  data-uid="(.*?)">',re.M)
    link = re.findall(_div_,str(req.content))
    for i in link:
        if i not in links:
            if i == "":
                continue
            _link_ = "https://www.filimo.com/m/" + i
            links.append(_link_)
            count += 1
            with open('link_leached_filimo.txt','a')as af:
                af.write(_link_)
                af.write('\n')
        else:
            continue
print(f"[+] Leached {count} Link !!!\n\n")
all_user = []
for ii in links:
    req = requests.get(ii,headers=headers)
    if req.status_code == 200:
        try:
            _span_ = re.compile('<span class="comment-name" title="(.*?)">',re.M)
            user = re.findall(_span_,str(req.content))

            for i in user:
                if i not in all_user:
                    _count_ += 1
                    if "\\" in i:
                        continue
                    sleep(0.03)
                    print(f"[{_count_}] {i}")
                    all_user.append(i)
                    with open('user_leached_filimo.txt','a')as af:
                        af.write(i)
                        af.write('\n')                    
                else:
                    continue
                
        except Exception as er:
            print(f"[*] Error : {er}")
            continue
    else:
        print("Error !")