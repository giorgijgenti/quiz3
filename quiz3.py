
import requests
import json
import  sqlite3
conn = sqlite3.connect('davaleba_db.sqlite3')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS davaleba
            (ID integer primary key autoincrement,
            name varchar(20),
            name_local varchar(20),
            language varchar(20),
            description varchar(20),
            country varchar (20),
            location varchar(20),
            type varchar(20),
            date integer,
            date_year integer,
            date_month integer,
            date_day integer,
            week_day varchar(20)
)''')



response = requests.get("https://holidays.abstractapi.com/v1/?"
                        "api_key=180e5291b1654ad9a90957d807fe4e8e&country=US&year=2020&month=12&day=25")

print(response.content)

result_json = response.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent=4)
all_row = []
for each in res['holidays']:
    name = each['name']
    name_local = each['name_local']
    language = each['language']
    description = each['description']
    country = each['country']
    location = each['location']
    type = each['type']
    date = each['date']
    date_year = each['date_year']
    date_month = each['date_month']
    date_day = each['date_day']
    week_day = each['week_day']
    row = (name, name_local, language, description, country, location, type, date, date_year, date_month, date_day, week_day)
    all_row.append(row)
c.executemany('insert into davaleba'
              '(name, name_local, language, description, '
              'country, location, type, date, date_year, '
              'date_month, date_day, week_day) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,)', all_row)
conn.commit()
print(res_structured)
print(response.status_code)
print(response.headers)
print(response.text)
print(response.content)