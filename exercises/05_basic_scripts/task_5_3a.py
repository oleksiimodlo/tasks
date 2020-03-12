# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

access_str = '\n'.join(access_template)
trunk_str = '\n'.join(trunk_template)

vlan_dict = {'access':'Input VLAN number: ', 'trunk':'Input VLANs numbers: '}

mode = input('Input interface mode (access/trunk): ')
interface = input('Input interface type and number: ')
vlans = input(vlan_dict[mode])

s = {'access':access_str, 'trunk':trunk_str} #dict for 2 different outputs

output = '\ninterface {}\n' + s[mode]

print(output.format(interface, vlans))
