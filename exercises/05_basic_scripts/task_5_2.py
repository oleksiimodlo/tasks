# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
net = input('Input subnet address (x.x.x.x/x): ')
subnet = net[:(net.find('/'))].split('.')
#print(subnet)
mask = net[(net.find('/')):]
mask_bin = int(mask[1:])*'1' + (32-int(mask[1:]))*'0'
#print(mask)
output = '''
Network:
{:<8}  {:<8}  {:<8}  {:<8}
{:08b}  {:08b}  {:08b}  {:08b}

Mask:
{}
{:<8}  {:<8}  {:<8}  {:<8}
{}  {}  {}  {}
'''
print(output.format(int(subnet[0]),int(subnet[1]),int(subnet[2]),int(subnet[3]),\
                    int(subnet[0]),int(subnet[1]),int(subnet[2]),int(subnet[3]),mask,\
                    int(mask_bin[:8],2),int(mask_bin[8:16],2),int(mask_bin[16:24],2),int(mask_bin[24:],2),\
                    mask_bin[:8],mask_bin[8:16],mask_bin[16:24],mask_bin[24:]))
