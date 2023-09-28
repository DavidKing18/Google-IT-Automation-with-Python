#!/usr/bin/env python3

import re
import operator
import csv

errors = {}
per_user = {}

with open("syslog.log") as file:
	logs = [log.strip() for log in file.readlines()]

for log in logs:
	result = re.search(r"ticky: (ERROR|INFO) ([\w'#\[\] ]*) \(([\w. ]*)\)", log)
	if result:
		user = result[3]
		error_message = result[2]
		message = result[1]
		per_user[user] = per_user.get(user, {"INFO": 0, "ERROR": 0})
		per_user[user][message] += 1
		if message == "ERROR":
			errors[error_message]  = errors.get(error_message, 0) + 1

errors_s = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
per_user_s = sorted(per_user.items(), key=operator.itemgetter(0))
per_user_s = [(user[0], user[1]["INFO"], user[1]["ERROR"]) for user in per_user_s]

errors_s.insert(0, ("Error", "Count"))
per_user_s.insert(0, ("Username", "INFO", "ERROR"))

with open("error_message.csv", "w") as file:
	writer = csv.writer(file)
	writer.writerows(errors_s)

with open("user_statistics.csv", "w") as file:
	writer = csv.writer(file)
	writer.writerows(per_user_s)
