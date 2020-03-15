# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input('Input IP address: ')

check = False

while not check:
    ip_list = ip.split('.')
    if len(ip_list) != 4:
        print ('Invalid IP address')
        ip = input('Input IP address: ')
    else:
        for i in range(len(ip_list)):
            ip_list[i] = int(ip_list[i])
            if 0 <= ip_list[i] <= 255:
                check = True
            else:
                check = False
                print ('Invalid IP address')
                ip = input('Input IP address: ')

if 1 <= int(ip_list[0]) <= 223:
    print ('unicast')
elif 224 <= int(ip_list[0]) <= 239:
    print ('multicast')
elif ip == '255.255.255.255':
    print ('local broadcast')
elif ip == '0.0.0.0':
    print ('unassigned')
else:
    print ('unused')
