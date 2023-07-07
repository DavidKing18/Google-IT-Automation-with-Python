import pandas 
import requests
import arrow

visitors = [354, 634, 534, 677, 434]
errors = [12, 15, 21, 6, 22]
df = pandas.DataFrame({"Visitors": visitors, "Errors": errors}, index = ["Mon", "Tue", "Wed", "Thu", "Fri"])
print(df)

print()

response1 = requests.get("http://www.google.com")
print(len(response1.text))

print()

response2 = requests.get("http://www.python.org")
print(response2.status_code)

date = arrow.get("2022-11-22", "YYYY-MM-DD")
date.shift(weeks=+6).format("MMM DD YYYY")
print(date)