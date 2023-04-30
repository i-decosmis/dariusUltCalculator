# This is a sample Python script.
import sys
import json
import time
import threading
import requests as requests
import PySimpleGUI as sg

lock_button_image = b'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'
ult_dmgs = []
base_dmg_lvl = [0, 64, 67.6, 71.38, 75.33, 79.45, 83.75, 88.23, 92.88, 97.7, 102.7, 107.88, 113.23, 118.75, 124.45,
                130.32, 136.38, 142.6, 149]
sg.Window._move_all_windows = True


def get_data():
    global ult_dmgs
    global base_dmg
    url_abilities = "https://127.0.0.1:2999/liveclientdata/activeplayerabilities"
    url_stats = "https://127.0.0.1:2999/liveclientdata/activeplayer"
    data_abilities = 0
    data_stats = 0
    try:
        response_abilities = requests.get(url_abilities, verify=False)
        response_stats = requests.get(url_stats, verify=False)
        data_abilities = json.loads(response_abilities.content)
        data_stats = json.loads(response_stats.content)
    except requests.exceptions.ConnectionError as e:  # This is the correct syntax
        ult_dmgs = []
        # print(e)
        r = "No response"

    return data_abilities, data_stats


def ult_dmg():
    global ult_dmgs
    global base_dmg_lvl
    data_abilities, data_stats = get_data()
    if data_abilities != 0 and data_stats != 0:
        try:
            attack_dmg = data_stats["championStats"]["attackDamage"]
            bonus_ad = attack_dmg - base_dmg_lvl[data_stats["level"]]
            lvl = data_abilities["R"]["abilityLevel"]
            if lvl == 1:
                base_dmg = 125
            elif lvl == 2:
                base_dmg = 250
            elif lvl == 3:
                base_dmg = 375
            else:
                base_dmg = 125
            ult_dmgs = [base_dmg + (bonus_ad / 100) * 75, base_dmg + ((base_dmg / 100) * 20) + (bonus_ad / 100) * 90,
                        base_dmg + ((base_dmg / 100) * 40) + (bonus_ad / 100) * 105,
                        base_dmg + ((base_dmg / 100) * 60) + (bonus_ad / 100) * 120,
                        base_dmg + ((base_dmg / 100) * 80) + (bonus_ad / 100) * 135,
                        base_dmg + base_dmg + (bonus_ad / 100) * 150]
        except KeyError as e:
            # print(e)
            r = "No response"


def update_dmg():
    while True:
        ult_dmg()
        time.sleep(0.2)


def update_text(window, i, text):
    window[str(i)].update(text)


def update_window(window, i, alert, alert_msg, update_code):
    while 5 >= i >= 0:
        if update_code == 0:
            if i == 0:
                update_text(window, i, "No stack: " + str("%.0f" % ult_dmgs[i]))
            elif i == 1:
                update_text(window, i, str(i) + " Stack: " + str("%.0f" % ult_dmgs[i]))
            else:
                update_text(window, i, str(i) + " Stacks: " + str("%.0f" % ult_dmgs[i]))
        elif update_code == 1:
            if i == 0:
                update_text(window, i, "No stack: ")
            elif i == 1:
                update_text(window, i, str(i) + " Stack: ")
            else:
                update_text(window, i, str(i) + " Stacks: ")
        i -= 1
        update_text(window, alert, alert_msg)


def windows_start():
    font = ("Arial", 15)
    sg.theme_background_color("#042028")
    layout = [[sg.Button("", image_data=lock_button_image, auto_size_button=True,
                         button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0,
                         key='Close')],
              [sg.Text("0 Stack:", font=font, key='0', background_color="#042028")],
              [sg.Text("1 Stack:", font=font, key='1', background_color="#042028")],
              [sg.Text("2 Stack:", font=font, key='2', background_color="#042028")],
              [sg.Text("3 Stack:", font=font, key='3', background_color="#042028")],
              [sg.Text("4 Stack:", font=font, key='4', background_color="#042028")],
              [sg.Text("5 Stack:", font=font, key='5', background_color="#042028")],
              [sg.Text("Waiting for game...", font=font, key='A', background_color="#042028")]]
    window = sg.Window("Demo", layout, keep_on_top=True, no_titlebar=True,
                       grab_anywhere_using_control=True,
                       background_color="#042028", element_padding=4, margins=(10, 10))
    while True:
        event, values = window.read(timeout=250)
        if event == 'Close':
            sys.exit()
        if len(ult_dmgs) != 0:
            update_window(window, 5, 'A', "Ok", 0)
            window.refresh()
        else:
            update_window(window, 5, 'A', "Waiting for game...", 1)
            window.refresh()


if __name__ == '__main__':
    x = threading.Thread(target=update_dmg)
    x.daemon = True
    y = threading.Thread(target=windows_start)
    x.start()
    y.start()
