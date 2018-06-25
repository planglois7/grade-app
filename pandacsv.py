import pandas as pd
import dateutil as du
csv_input = pd.read_csv('info.csv')
# csv_input = csv_input[csv_input.ISSUE_TIME.notnull()]
# time = csv_input['ISSUE_TIME']
#newtime = pd.Series.copy(time)
count = 0
# csv_input['TIME'] = pd.Series(csv_input['TIME'])
# print type(csv_input['TIME'][0])
for row in csv_input['ISSUE_DATE']:
	if (type(row) != float):
		dow = du.parser.parse(row).strftime("%a")
		# csv_input['DOW'][count] = dow
		print dow
	count += 1
	print count

count = 0
for row in csv_input['ISSUE_TIME']:
	if (type(row) != float):
		time_str = row.split(':')[0]
		# csv_input['TIME'][count] = time_str
		print time_str
	count += 1
	print count

# csv_input['TIME'] = time
csv_input.to_csv('output.csv', index=False)