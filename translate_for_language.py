import json
import argparse

with open('translate.json', 'r') as file:
    translation_dict = json.loads(file.read())

key = 'IND'
names = 'Makar Sankranti / Pongal, Republic Day, Labour Day, Independence Day, Gandhi Jayanti, Christmas'.split(', ')
translations = "Makar Sankranti / Pongal, Tag der Republik, Tag der Arbeit, Unabhängigkeitstag, Gandhi Jayanti, Weihnachten".split(', ')

if len(names) != len(translations):
    print('ERROR: ' + key + ', ' + str(len(names)) + ', ' + str(len(translations)))
else:
    for i in range(len(names)):
        translation_dict[key][names[i]]['translation'] = translations[i]

key = 'JP'
names = "元日, 成人の日, 建国記念の日, 天皇誕生日, 振替休日, 春分の日, 昭和の日, 憲法記念日, みどりの日, こどもの日, 海の日, スポーツの日, 山の日, 敬老の日, 秋分の日, 文化の日, 勤労感謝の日".split(', ')
translations = 'Neujahrstag, Tag der Volljährigkeit, Tag der Staatsgründung, Geburtstag des Kaisers, Ersatzfeiertag, Tag der Frühlings-Tagundnachtgleiche, Showa-Tag, Tag der Verfassung, Tag des Grüns, Tag der Kinder, Tag der Marine, Tag des Sports, Tag der Berge, Tag des Respekts vor dem Alter, Tag der Herbst-Tagundnachtgleiche, Tag der Kultur, Tag des Dankes für die Arbeit'.split(', ')

if len(names) != len(translations):
    print('ERROR: ' + key + ', ' + str(len(names)) + ', ' + str(len(translations)))
else:
    for i in range(len(names)):
        translation_dict[key][names[i]]['translation'] = translations[i]

key = 'MX'
names = "Año Nuevo [New Year's Day], Día de la Constitución [Constitution Day] (Observed), Día de la Constitución [Constitution Day], Natalicio de Benito Juárez [Benito Juárez's birthday] (Observed), Natalicio de Benito Juárez [Benito Juárez's birthday], Día del Trabajo [Labour Day], Día de la Independencia [Independence Day], Día de la Revolución [Revolution Day] (Observed), Día de la Revolución [Revolution Day], Navidad [Christmas]".split(', ')
translations = "Neujahrstag, Tag der Verfassung (beobachtet), Tag der Verfassung, Geburtstag von Benito Juarez (beobachtet), Geburtstag von Benito Juarez, Tag der Arbeit, Unabhängigkeitstag, Tag der Revolution (beobachtet), Tag der Revolution, Weihnachten".split(', ')

if len(names) != len(translations):
    print('ERROR: ' + key + ', ' + str(len(names)) + ', ' + str(len(translations)))
else:
    for i in range(len(names)):
        translation_dict[key][names[i]]['translation'] = translations[i]

key = 'RU'
names = 'Новый год, Православное Рождество, День защитника отечества, День женщин, Праздник Весны и Труда, День Победы, День России, День народного единства'.split(', ')
translations = "Neujahr, orthodoxe Weihnachten, Tag der Vaterlandsverteidiger, Frauentag, Tag des Frühlings und der Arbeit, Tag des Sieges, Tag Russlands, Tag der nationalen Einheit".split(', ')

if len(names) != len(translations):
    print('ERROR: ' + key + ', ' + str(len(names)) + ', ' + str(len(translations)))
else:
    for i in range(len(names)):
        translation_dict[key][names[i]]['translation'] = translations[i]

key = 'BR'
names = 'Ano novo, Carnaval, Quarta-feira de cinzas (Início da Quaresma), Sexta-feira Santa, Páscoa, Tiradentes, Dia Mundial do Trabalho, Corpus Christi, Independência do Brasil, Nossa Senhora Aparecida, Finados, Proclamação da República, Natal'.split(', ')
translations = "Neujahr, Karneval, Aschermittwoch (Beginn der Fastenzeit), Karfreitag, Ostern, Tiradentes, Tag der Arbeit, Fronleichnam, Unabhängigkeit Brasiliens, Unsere Liebe Frau Aparecida, Die Toten, Proklamation der Republik, Weihnachten".split(', ')

if len(names) != len(translations):
    print('ERROR: ' + key + ', ' + str(len(names)) + ', ' + str(len(translations)))
else:
    for i in range(len(names)):
        translation_dict[key][names[i]]['translation'] = translations[i]

with open('translate.json', 'w') as file:
    file.write(json.dumps(translation_dict))