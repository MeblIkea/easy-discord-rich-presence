import PySimpleGUI as sg
from pypresence import Presence
import platform
import random
import time

infos = 0
perso = 0
fakegame = 0
total = 0
online = ['1', '2']
combo1_rpc = ''
combo2_rpc = ''
fake_game_lnchd = ''
client_id = ''
fake_street = ''

sg.change_look_and_feel('DarkTanBlue')

try:
    file = open('default_client_id.txt', 'r')
    client_id = file.read()
    file.close()
    print('File "default_client_id.txt" started!')
except Exception:
    print('File "default_client_id.txt" failed!')

try:
    file = open('fake-street.txt', 'r')
    fake_street = file.read().splitlines()
    file.close()
    print('File "fake-street.txt" started!')
except Exception:
    print('File "fake-street.txt" failed!')

layout = [
    [sg.Text('Your client id :'), sg.Text(client_id, size=(14, 1), key='client_id_text')],
    [sg.Input(client_id, key='client_id', size=(67, 1))],
    [sg.Button('Set', size=(28, 1)), sg.Button('Exit', size=(28, 1))],
    [sg.Button('Personalized', size=(18, 5)), sg.Button('Computer Infos', size=(18, 5)),
     sg.Button('Fake Game', size=(18, 5))]
]
personalized = [
    [sg.Button('Set', size=(27, 1)), sg.Button('Back', size=(27, 1))],
    [sg.Text('Details:                 '), sg.Input(key='detail')],
    [sg.Text('State:                   '), sg.Input(key='state')],
    [sg.CBox('', key='l_check'), sg.Text('Large Image:'), sg.Input(key='l_image')],
    [sg.Text('Large Image Text:  '), sg.Input(key='l_image_text')],
    [sg.CBox('', key='s_check'), sg.Text('Small Image:'), sg.Input(key='s_image')],
    [sg.Text('Small Image Text:  '), sg.Input(key='s_image_text')]
]
pc_info = [
    [sg.Button('Set', size=(27, 1)), sg.Button('Back', size=(27, 1))],
    [sg.Text('Machine :'), sg.Text(platform.machine())],
    [sg.Text('OS :'), sg.Text(platform.system())],
    [sg.CBox('', key='l_check'), sg.Text('Large Image:'), sg.Input(key='l_image')],
    [sg.Text('Large Image Text:  '), sg.Input(key='l_image_text')],
    [sg.CBox('', key='s_check'), sg.Text('Small Image:'), sg.Input(key='s_image')],
    [sg.Text('Small Image Text:  '), sg.Input(key='s_image_text')]
]
fake_game = [
    [sg.Button('Set', size=(27, 1)), sg.Button('Back', size=(27, 1))],
    [sg.Text('Details :                '), sg.InputCombo(('Fake server', 'Fake street (check fake-street.txt)'),
                                                         size=(43, 1), key='combo1')],
    [sg.Text('Stats :                  '), sg.InputCombo(('Fake server', 'Fake street (check fake-street.txt)'),
                                                         size=(43, 1), key='combo2')],
    [sg.CBox('', key='l_check'), sg.Text('Large Image:'), sg.Input(key='l_image')],
    [sg.Text('Large Image Text:  '), sg.Input(key='l_image_text')],
    [sg.CBox('', key='s_check'), sg.Text('Small Image:'), sg.Input(key='s_image')],
    [sg.Text('Small Image Text:  '), sg.Input(key='s_image_text')]
]

window = sg.Window('Main Menu', layout)

print('GUI-Appared')

RPC = Presence(client_id, pipe=0)
RPC.connect()

print('Connected to discord')

while True:
    event, values = window.read()

    if event == 'Set':
        if fakegame == 0:
            if infos == 0:
                if perso == 0:
                    for i in range(len(values['client_id'])):
                        total = total + 1

                    if total == 18:
                        window['client_id_text'].update(values['client_id'])
                        print('ClientID Setted')
                    else:
                        window['client_id_text'].update('NOT A CLIENT ID!!! >:(')
                        print('Error')
                    total = 0
                    client_id = values['client_id']
                    RPC = Presence(client_id, pipe=0)
                    RPC.connect()
                    print('Reconnected to discord')
                else:
                    fake_game_lnchd = False
                    if values['l_check'] is True:
                        if values['s_check'] is True:
                            RPC.update(
                                details=values['detail'], state=values['state'], large_image=values['l_image'],
                                large_text=values['l_image_text'], small_image=values['s_image'],
                                small_text=values['s_image_text']
                            )
                            print(
                                'Rich Presence Set : Detail :', values['detail'], ', State :', values['state'],
                                ', Large image :', values['l_image'], ', Large image text :', values['l_image_text'],
                                ', Small image :', values['s_image'], ', Small image text :', values['s_image_text']
                            )
                        else:
                            RPC.update(
                                details=values['detail'], state=values['state'], large_image=values['l_image'],
                                large_text=values['l_image_text']
                            )
                            print(
                                'Rich Presence Set : Detail :', values['detail'], ', State :', values['state'],
                                ', Large image :', values['l_image'], ', Large image text :', values['l_image_text']
                            )
                    else:
                        RPC.update(details=values['detail'], state=values['state'])
                        print(
                            'Rich Presence Set : Detail :', values['detail'], ', State :', values['state']
                        )
            else:
                fake_game_lnchd = False
                if values['l_check'] is True:
                    if values['s_check'] is True:
                        RPC.update(
                            details=f'Machine : {platform.machine()}', state=f'Os : {platform.system()}',
                            large_image=values['l_image'], large_text=values['l_image_text'],
                            small_image=values['s_image'], small_text=values['s_image_text']
                        )
                        print(
                            'Rich Presence Set : Detail :', f'Machine : {platform.machine()}',
                            ', State :', f'Os : {platform.system()}',
                            ', Large image :', values['l_image'], ', Large image text :', values['l_image_text'],
                            ', Small image :', values['s_image'], ', Small image text :', values['s_image_text']
                        )
                    else:
                        RPC.update(details=f'Machine : {platform.machine()}', state=f'Os : {platform.system()}',
                                   large_image=values['l_image'], large_text=values['l_image_text'])
                        print(
                            'Rich Presence Set : Detail :', f'Machine : {platform.machine()}',
                            ', State :', f'Os : {platform.system()}', ', Large image :', values['l_image'],
                            ', Large image text :', values['l_image_text']
                        )
                else:
                    RPC.update(details=f'Machine : {platform.machine()}', state=f'Os : {platform.system()}')
                    print(
                        'Rich Presence Set : Detail :', f'Machine : {platform.machine()}',
                        ', State :', f'Os : {platform.system()}'
                    )
        else:
            fake_game_lnchd = True
            if values['combo1'] == 'Fake server':
                combo1_rpc = f'In-game : {random.choice(online)}/32'
            if values['combo1'] == 'Fake street (check fake-street.txt)':
                combo1_rpc = f'In the {random.choice(fake_street)}'
            print(combo1_rpc)
            if values['combo2'] == 'Fake server':
                combo2_rpc = f'In-game : {random.choice(online)}/32'
            if values['combo2'] == 'Fake street (check fake-street.txt)':
                combo2_rpc = f'In the {random.choice(fake_street)}'
            print(combo2_rpc)
            if values['l_check'] is True:
                if values['s_check'] is True:
                    RPC.update(
                        details=combo1_rpc, state=combo2_rpc,
                        large_image=values['l_image'], large_text=values['l_image_text'],
                        small_image=values['s_image'], small_text=values['s_image_text']
                    )
                    print(
                        'Rich Presence Set : Detail :', combo1_rpc, ', State :', combo2_rpc,
                        ', Large image :', values['l_image'], ', Large image text :', values['l_image_text'],
                        ', Small image :', values['s_image'], ', Small image text :', values['s_image_text']
                    )
                else:
                    RPC.update(
                        details=combo1_rpc, state=combo2_rpc,
                        large_image=values['l_image'], large_text=values['l_image_text']
                    )
                    print(
                        'Rich Presence Set : Detail :', combo1_rpc, ', State :', combo2_rpc,
                        ', Large image :', values['l_image'], ', Large image text :', values['l_image_text']
                    )
            else:
                RPC.update(details=combo1_rpc, state=combo2_rpc)
                print(
                    'Rich Presence Set : Detail :', combo1_rpc, ', State :', combo2_rpc
                )

    if event == 'Exit':
        break

    if event == 'Personalized':
        window.close()
        window = sg.Window('Personalized', personalized)
        layout = [
            [sg.Text('Your client id :'), sg.Text(client_id, size=(14, 1), key='client_id_text')],
            [sg.Input(client_id, key='client_id', size=(67, 1))],
            [sg.Button('Set', size=(28, 1)), sg.Button('Exit', size=(28, 1))],
            [sg.Button('Personalized', size=(18, 5)), sg.Button('Computer Infos', size=(18, 5)),
             sg.Button('Fake Game', size=(18, 5))]
        ]
        perso = 1
        print('Personalized')

    if event == 'Computer Infos':
        window.close()
        window = sg.Window('Computer Infos', pc_info)
        layout = [
            [sg.Text('Your client id :'), sg.Text(client_id, size=(14, 1), key='client_id_text')],
            [sg.Input(client_id, key='client_id', size=(67, 1))],
            [sg.Button('Set', size=(28, 1)), sg.Button('Exit', size=(28, 1))],
            [sg.Button('Personalized', size=(18, 5)), sg.Button('Computer Infos', size=(18, 5)),
             sg.Button('Fake Game', size=(18, 5))]
        ]
        infos = 1
        print('Computer Infos')

    if event == 'Fake Game':
        window.close()
        window = sg.Window('Fake Game', fake_game)
        layout = [
            [sg.Text('Your client id :'), sg.Text(client_id, size=(14, 1), key='client_id_text')],
            [sg.Input(client_id, key='client_id', size=(67, 1))],
            [sg.Button('Set', size=(28, 1)), sg.Button('Exit', size=(28, 1))],
            [sg.Button('Personalized', size=(18, 5)), sg.Button('Computer Infos', size=(18, 5)),
             sg.Button('Fake Game', size=(18, 5))]
        ]
        fakegame = 1
        print('Fake Game')

    if event == 'Back':
        window.close()
        window = sg.Window('Main Menu', layout)
        personalized = [
            [sg.Button('Set', size=(27, 1)), sg.Button('Back', size=(27, 1))],
            [sg.Text('Details:                 '), sg.Input(key='detail')],
            [sg.Text('State:                   '), sg.Input(key='state')],
            [sg.CBox('', key='l_check'), sg.Text('Large Image:'), sg.Input(key='l_image')],
            [sg.Text('Large Image Text:  '), sg.Input(key='l_image_text')],
            [sg.CBox('', key='s_check'), sg.Text('Small Image:'), sg.Input(key='s_image')],
            [sg.Text('Small Image Text:  '), sg.Input(key='s_image_text')]
        ]
        print('Window personalized reloaded')
        pc_info = [
            [sg.Button('Set', size=(27, 1)), sg.Button('Back', size=(27, 1))],
            [sg.Text('Machine :'), sg.Text(platform.machine())],
            [sg.Text('OS :'), sg.Text(platform.system())],
            [sg.CBox('', key='l_check'), sg.Text('Large Image:'), sg.Input(key='l_image')],
            [sg.Text('Large Image Text:  '), sg.Input(key='l_image_text')],
            [sg.CBox('', key='s_check'), sg.Text('Small Image:'), sg.Input(key='s_image')],
            [sg.Text('Small Image Text:  '), sg.Input(key='s_image_text')]
        ]
        print('Window infos PC reloaded')
        fake_game = [
            [sg.Button('Set', size=(27, 1)), sg.Button('Back', size=(27, 1))],
            [sg.Text('Details :                '), sg.InputCombo(('Fake server', 'Fake street (check fake-street.txt)'),
                                                                 size=(43, 1), key='combo1')],
            [sg.Text('Stats :                  '), sg.InputCombo(('Fake server', 'Fake street (check fake-street.txt)'),
                                                                 size=(43, 1), key='combo2')],
            [sg.CBox('', key='l_check'), sg.Text('Large Image:'), sg.Input(key='l_image')],
            [sg.Text('Large Image Text:  '), sg.Input(key='l_image_text')],
            [sg.CBox('', key='s_check'), sg.Text('Small Image:'), sg.Input(key='s_image')],
            [sg.Text('Small Image Text:  '), sg.Input(key='s_image_text')]
        ]
        print('Window fake game reloaded')

        perso = 0
        infos = 0
        fakegame = 0
