from __future__ import print_function, unicode_literals
from PyInquirer import prompt

def choose_weapon():
    answers = prompt([
        {
            'type': 'list',
            'name': 'weapon',
            'message': 'What weapon do you choose?',
            'choices': ['Photon Canon', 'Laser', 'Rocket'],
        }
    ])
    
    weapon_name = answers['weapon']
    weapon_power(weapon_name)
    return(weapon_name)  # use the answers as input for your app

def weapon_power(weapon_name):
    if weapon_name == 'Photon Canon':
        weapon_power = 50
    elif weapon_name == 'Laser':
        weapon_power = 35
    else:
        weapon_power = 20
    return(weapon_power)  # use the answers as input for your app
