import requests

def message():
    #region delete message
    a = requests.post("http://127.0.0.1:5000/msgData/",{
        "process":"del",
        "uid":"aaa"
    })
    print(a.text.encode(encoding='utf-8'))
    #endregion
    #region change message
    a = requests.post("http://127.0.0.1:5000/msgData/",{
        "process":"change",
        "uid":"bbb",
        "msg":"vbn vbjhbvm",
        "tel":"31"
    })
    print(a.text.encode(encoding='utf-8').decode(encoding='utf-8'))
    #endregion
    #region add message
    a = requests.post("http://127.0.0.1:5000/msgData/",{
        "process":"add",
        "uid":"asdfgjkl",
        "msg":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "tel":"111111111111111111111111111111111111111111111"
    })
    print(a.text.encode(encoding='utf-8').decode(encoding='utf-8'))
    #endregion
def user():
    #region add 2 users
    a = requests.post("http://127.0.0.1:5000/userData/",{
        "process":"add",
        "uid":"asdfgjkl",
        "tc":111122223333444,
        "isim":"Cio",
        "soyisim":"Babba",
        "dogum":"31.12.1453",
        "il":"adana",
        "ilce":"seyhan",
        "ikametgah": "mevlana mahallesi",
        "tel":"+905555555555"
    })
    b = requests.post("http://127.0.0.1:5000/userData/",{
        "process":"add",
        "uid":"aaaaaaaasssssssssssddddddddddddd",
        "tc":111122223333444,
        "isim":"Popo",
        "soyisim":"Fotosu",
        "dogum":"31.12.1453",
        "il":"istanbul",
        "ilce":"bağcılar",
        "ikametgah": "ben suri bilmiyor nargile cafe",
        "tel":"+90555999955"
    })
    print(a.text.encode(encoding='utf-8').decode(encoding='utf-8'))
    print(b.text.encode(encoding='utf-8').decode(encoding='utf-8'))
    #endregion
    #region delete user
    a = requests.post("http://127.0.0.1:5000/userData/",{
        "process":"del",
        "uid":"aaaaaaaasssssssssssddddddddddddd"
    })
    print(a.text.encode(encoding='utf-8'))
    #endregion
    #region change user
    a = requests.post("http://127.0.0.1:5000/userData/",{
        "process":"change",
        "uid":"asdfgjkl",
        "tc":111122223333444,
        "isim":"Cio",
        "soyisim":"Babba",
        "dogum":"31.12.1453",
        "il":"adana",
        "ilce":"seyhan",
        "ikametgah": "ne bakıyon gevvvvvşşşşeeek",
        "tel":"+905555555555"
    })
    print(a.text.encode(encoding='utf-8').decode(encoding='utf-8'))
    #endregion
def location():
    #region add 2 locations
    a = requests.post("http://127.0.0.1:5000/locationData/",{
        "process":"add",
        "uid":"asdfgjkl",
        "kor_x":11.11,
        "kor_y":11.11,
        "tel":"+905555555555"
    })
    b = requests.post("http://127.0.0.1:5000/locationData/",{
        "process":"add",
        "uid":"aaaaaaaasssssssssssddddddddddddd",
        "kor_x":11.11,
        "kor_y":11.11,
        "tel":"+9031313131311331"
    })
    print(a.text.encode(encoding='utf-8').decode(encoding='utf-8'))
    print(b.text.encode(encoding='utf-8').decode(encoding='utf-8'))
    #endregion
    #region delete location
    c = requests.post("http://127.0.0.1:5000/locationData/",{
        "process":"del",
        "uid":"aaaaaaaasssssssssssddddddddddddd"
    })
    print(c.text.encode(encoding='utf-8'))
    #endregion
    #region change location
    a = requests.post("http://127.0.0.1:5000/locationData/",{
        "process":"change",
        "uid":"asdfgjkl",
        "kor_x":12.11,
        "kor_y":11.12,
        "tel":"+905555555555"
    })
    print(a.text.encode(encoding='utf-8').decode(encoding='utf-8'))
    #endregion
