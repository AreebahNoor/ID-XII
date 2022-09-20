from requests import get as gt
from os import system as cmd
from urllib.request import urlopen as uo
from urllib.request import HTTPError as he
from urllib.request import URLError as ue

logo = """.___________            ____  _______ ____ \n|   \______ \           \   \/  /_   /_   |\n|   ||    |  \   ______  \     / |   ||   |\n|   ||    `   \ /_____/  /     \ |   ||   |\n|___/_______  /         /___/\  \|___||___|\n            \/                \_/     \n                           Version : 0.0.1\n"""

def bilal_id():
    cmd("clear")
    print(logo)
    url = input("[*] Enter Web URL : ")
    try:
        print("-"*47)
        bilal = gt(url)
        for key, value in bilal.headers.items():
            print(f"{key}:{value}")
    except Exception as e:
        print(e)
    try:
        print("-"*47)
        tg = uo(url)
        bilal_haider_id = tg.info()
        print(bilal_haider_id)
        print("-"*47)
    except Exception as e:
        print(e)
def get_headers(s):
    cmd("clear")
    print(logo)
    d = dict()
    sep=":"
    for kv in s.split('\n'):
        kv = kv.strip()
        if sep in kv:
            k = kv.split(sep)[0].strip()
            if k == 'user-agent':
                v = kv.split(sep)[1]
            else:
                v = ":".join(kv.split(sep)[:]).split()[1]
            if k.lower() == 'cookie':
                continue 
            d[k] = v
    return d
def main():
    cmd("clear")
    print(logo)
    print("[{}] Copy Website HTTPS Header".format("01"))
    print("[{}] Convert Header In Json Form".format("02"))
    print("[{}] Exit ".format("00"))
    x1 = input("\n[->] Select an Option : ")
    if x1 in ["1","01"]:bilal_id()
    elif x1 in ["2","02"]:
        print(logo)
        file = input("[->] Enter Header Text File : ")
        try:
            data = open(file,'r').read()
        except FileNotFoundError:
            exit("[*] Text File Not Found")
        print("-"*47)
        print(get_headers(data))
        print("-"*47)
    elif x1 in ["0","00"]:exit()
    else:main()
if __name__=="__main__":
    main()
