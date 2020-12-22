from datetime import date
import holidays
import json

holiday_dict = {}

for holiday in [
    holidays.Germany(years=2020),
    holidays.India(years=2020),
    holidays.Japan(years=2020),
    holidays.Mexico(years=2020),
    holidays.Russia(years=2020),
    holidays.Brazil(years=2020)
]:
    key = holiday.country
    holiday_dict[key] = {}

    for _, name in sorted(holiday.items()):
        holiday_dict[key][name] = {
            "translation": name,
            "genum": 'm'
        }

    print(key)
    print(', '.join(holiday_dict[key].keys()))

with open('translate.json', 'w+') as file:
    file.write(json.dumps(holiday_dict))