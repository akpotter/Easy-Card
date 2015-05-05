# 2015.05.05 18:39:54 CST
# Embedded file name: easycard.py
import sys
import datetime
import hashlib
import urllib
import urllib2
import json
from Crypto.Cipher import DES3
import pytz
version = '0.3'
copyright = 'Copyright (C) 2015 Zhi-Wei Cai.'
key = 'EasyCardToKingay23456789'
iv = '01234567'
salt = 'L0CalKing'
const = 8544

def getID(data, isEncrypt, key, iv, encode):
    size = len(data)
    if size % 16 != 0:
        data += '\x06' * (16 - size % 16)
    des3 = DES3.new(key, DES3.MODE_CBC, iv)
    if isEncrypt:
        result = des3.encrypt(data).encode(encode).rstrip()
    else:
        result = des3.decrypt(data.decode(encode))
    return result


def getVerify(const, seed, salt):
    hash = hashlib.md5()
    hash.update(str(seed * const) + salt)
    return hash.hexdigest().upper()


def proc(data):
    e = getID(data, 1, key, iv, 'base64')
    cardID = urllib.quote_plus(e)
    date = datetime.datetime.now(pytz.timezone('Asia/Taipei'))
    seed = date.month + date.day + date.hour
    begin = '{:%Y-%m-%d}'.format(date - datetime.timedelta(days=30))
    end = '{:%Y-%m-%d}'.format(date)
    verify = getVerify(const, seed, salt)
    url = 'https://wallet.easycard.com.tw/EasyWallet/QueryManager/V3/GetTXNThinDataInfo?verify={}&cardID={}&begin={}&end={}&ev=1'.format(verify, cardID, begin, end)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    content = response.read()
    dict = json.loads(content)
    try:
        if dict[-1]['B'] != '--':
            print '{: ^90}'.format('\xe5\x8d\xa1\xe8\x99\x9f "{} {} {}"\xef\xbc\x8c\xe9\xa4\x98\xe9\xa1\x8d\xef\xbc\x9a{} \xe5\x85\x83'.format(data[0:3], data[3:9], data[-1], dict[-1]['B']))
            if len(dict) > 1:
                if dict[0]['T'].encode('utf-8') != '\xe6\x9f\xa5\xe7\x84\xa1\xe4\xba\xa4\xe6\x98\x93\xe8\xb3\x87\xe6\x96\x99':
                    print '\n{:=^90}\n'.format('[ \xe4\xba\xa4\xe6\x98\x93\xe6\x98\x8e\xe7\xb4\xb0 ]')
                i = 1
                for item in dict:
                    try:
                        if item['T']:
                            if item['T'] == 'D':
                                action = '\xe6\x89\xa3\xe6\xac\xbe'
                            else:
                                action = '\xe5\x84\xb2\xe5\x80\xbc'
                            print '#{:>4} [{}] {} {:>5} \xe5\x85\x83\xef\xbc\x8c\xe9\xa4\x98\xe9\xa1\x8d {:>5} \xe5\x85\x83\xef\xbc\x8c\xe5\x9c\xb0\xe9\xbb\x9e\xef\xbc\x9a{}'.format(i, item['D'], action, item['Q'], item['A'], item['L'].encode('utf-8').replace('<BR>', '-'))
                            i += 1
                    except KeyError as err:
                        pass

    except KeyError as err:
        print '\xe5\x8d\xa1\xe8\x99\x9f "{}" \xe4\xb8\x8d\xe5\xad\x98\xe5\x9c\xa8\xef\xbc\x81'.format(data)
    except ValueError as err:
        print '\xe5\x8d\xa1\xe8\x99\x9f "{}" \xe4\xb8\x8d\xe5\xad\x98\xe5\x9c\xa8\xef\xbc\x81'.format(data)

    print '\n{:=^90}\n\n'.format('[ \xe6\x9f\xa5\xe8\xa9\xa2\xe7\xb5\x90\xe6\x9d\x9f ]')


if __name__ == '__main__':
    print '\n\xe6\x82\xa0\xe9\x81\x8a\xe5\x8d\xa1\xe9\xa4\x98\xe9\xa1\x8d\xe6\x98\x8e\xe7\xb4\xb0\xe6\x9f\xa5\xe8\xa9\xa2 v{}'.format(version)
    print '{}\n'.format(copyright)
    if len(sys.argv) > 1:
        try:
            print '\n{:=^90}\n'.format('[ \xe6\x9f\xa5\xe8\xa9\xa2\xe9\x96\x8b\xe5\xa7\x8b ]')
            proc(str(sys.argv[1]))
        except ValueError as err:
            pass

    else:
        while 1:
            try:
                data = raw_input('\xe8\xab\x8b\xe8\xbc\xb8\xe5\x85\xa5\xe5\x8d\xa1\xe7\x89\x87\xe8\x99\x9f\xe7\xa2\xbc\xef\xbc\x9a').replace(' ', '')
                if len(data):
                    print '\n{:=^90}\n'.format('[ \xe6\x9f\xa5\xe8\xa9\xa2\xe9\x96\x8b\xe5\xa7\x8b ]')
                    proc(data)
                else:
                    break
            except ValueError as err:
                pass
# okay decompyling easycard.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.05.05 18:39:54 CST
