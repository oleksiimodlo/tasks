# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = input('Input IP address: ')

check = False

ip_list = ip.split('.')
if len(ip_list) != 4:
    print ('Invalid IP address')
else:
    for i in range(len(ip_list)):
        ip_list[i] = int(ip_list[i])
        if 0 <= ip_list[i] <= 255:
            check = True
        else:
            check = False
            print ('Invalid IP address')

if check:
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
