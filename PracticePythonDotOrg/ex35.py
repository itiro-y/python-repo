# Birth Months
# load json file, extract month of all birthdays, count duplicates
import json

def main():
    countMonthDup()

def countMonthDup():
    with open('/PythonStuff/PracticePythonDotOrg/name_birth.json', 'r') as json_file:
        persons = json.loads(json_file.read())

    dates = []
    for i in range(len(persons)):
        dates.append(list(persons[i].values()))

    months = {
        "January": 0,
        "February": 0,
        "March": 0,
        "April": 0,
        "May": 0,
        "June": 0,
        "July": 0,
        "August": 0,
        "September": 0,
        "October": 0,
        "November": 0,
        "December": 0,
    }

    for i in range(len(dates)):
        month = dates[i][0][5:7]
        if month == '01':
            months['January'] += 1
        elif month == '02':
            months['February'] += 1
        elif month == '03':
            months['March'] += 1  
        elif month == '04':
            months['April'] += 1
        elif month == '05':
            months['May'] += 1
        elif month == '06':
            months['June'] += 1
        elif month == '07':
            months['July'] += 1
        elif month == '08':
            months['August'] += 1
        elif month == '09':
            months['September'] += 1
        elif month == '10':
            months['October'] += 1
        elif month == '11':
            months['November'] += 1
        elif month == '12':
            months['December'] += 1
        else:
            print("invalid month found")

    print(json.dumps(months, indent=4))
    return list(months.values())


if __name__ == '__main__':
    main()