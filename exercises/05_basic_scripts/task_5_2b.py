# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

net = argv[1]
subnet = net[:(net.find('/'))].split('.')
s = '{:08b}{:08b}{:08b}{:08b}'
subnet_bin_8 = s.format(int(subnet[0]),int(subnet[1]),int(subnet[2]),int(subnet[3]))
#print (subnet_bin_8)
mask = net[(net.find('/')):]
mask_bin = int(mask[1:])*'1' + (32-int(mask[1:]))*'0'
#print(mask)

new_subnet = []
new_subnet.append(str(int(subnet_bin_8[0])*int(mask_bin[0])))
new_subnet.append(str(int(subnet_bin_8[1])*int(mask_bin[1])))
new_subnet.append(str(int(subnet_bin_8[2])*int(mask_bin[2])))
new_subnet.append(str(int(subnet_bin_8[3])*int(mask_bin[3])))
new_subnet.append(str(int(subnet_bin_8[4])*int(mask_bin[4])))
new_subnet.append(str(int(subnet_bin_8[5])*int(mask_bin[5])))
new_subnet.append(str(int(subnet_bin_8[6])*int(mask_bin[6])))
new_subnet.append(str(int(subnet_bin_8[7])*int(mask_bin[7])))
new_subnet.append(str(int(subnet_bin_8[8])*int(mask_bin[8])))
new_subnet.append(str(int(subnet_bin_8[9])*int(mask_bin[9])))
new_subnet.append(str(int(subnet_bin_8[10])*int(mask_bin[10])))
new_subnet.append(str(int(subnet_bin_8[11])*int(mask_bin[11])))
new_subnet.append(str(int(subnet_bin_8[12])*int(mask_bin[12])))
new_subnet.append(str(int(subnet_bin_8[13])*int(mask_bin[13])))
new_subnet.append(str(int(subnet_bin_8[14])*int(mask_bin[14])))
new_subnet.append(str(int(subnet_bin_8[15])*int(mask_bin[15])))
new_subnet.append(str(int(subnet_bin_8[16])*int(mask_bin[16])))
new_subnet.append(str(int(subnet_bin_8[17])*int(mask_bin[17])))
new_subnet.append(str(int(subnet_bin_8[18])*int(mask_bin[18])))
new_subnet.append(str(int(subnet_bin_8[19])*int(mask_bin[19])))
new_subnet.append(str(int(subnet_bin_8[20])*int(mask_bin[20])))
new_subnet.append(str(int(subnet_bin_8[21])*int(mask_bin[21])))
new_subnet.append(str(int(subnet_bin_8[22])*int(mask_bin[22])))
new_subnet.append(str(int(subnet_bin_8[23])*int(mask_bin[23])))
new_subnet.append(str(int(subnet_bin_8[24])*int(mask_bin[24])))
new_subnet.append(str(int(subnet_bin_8[25])*int(mask_bin[25])))
new_subnet.append(str(int(subnet_bin_8[26])*int(mask_bin[26])))
new_subnet.append(str(int(subnet_bin_8[27])*int(mask_bin[27])))
new_subnet.append(str(int(subnet_bin_8[28])*int(mask_bin[28])))
new_subnet.append(str(int(subnet_bin_8[29])*int(mask_bin[29])))
new_subnet.append(str(int(subnet_bin_8[30])*int(mask_bin[30])))
new_subnet.append(str(int(subnet_bin_8[31])*int(mask_bin[31])))

new_subnet_str = ''.join(new_subnet)
#print(new_subnet_str)

output = '''
Network:
{:<8}  {:<8}  {:<8}  {:<8}
{}  {}  {}  {}

Mask:
{}
{:<8}  {:<8}  {:<8}  {:<8}
{}  {}  {}  {}
'''
print(output.format(int(new_subnet_str[:8],2),int(new_subnet_str[8:16],2),int(new_subnet_str[16:24],2),int(new_subnet_str[24:32],2),\
                    new_subnet_str[:8],new_subnet_str[8:16],new_subnet_str[16:24],new_subnet_str[24:],mask,\
                    int(mask_bin[:8],2),int(mask_bin[8:16],2),int(mask_bin[16:24],2),int(mask_bin[24:],2),\
                    mask_bin[:8],mask_bin[8:16],mask_bin[16:24],mask_bin[24:]))

