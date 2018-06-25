import csv
input1 = open('dowtod.csv', 'rU')

output1 = open('lotdata/universityst.csv', 'wb')
output2 = open('lotdata/lot16A.csv', 'wb')
output3 = open('lotdata/15th.csv', 'wb')
output4 = open('lotdata/13th.csv', 'wb')
output5 = open('lotdata/lot29.csv', 'wb')
output6 = open('lotdata/lot17.csv', 'wb')
output7 = open('lotdata/lot12A.csv', 'wb')
output8 = open('lotdata/lot15.csv', 'wb')
output9 = open('lotdata/lot42.csv', 'wb')
output10 = open('lotdata/lot56.csv', 'wb')

writer1 = csv.writer(output1)
writer2 = csv.writer(output2)
writer3 = csv.writer(output3)
writer4 = csv.writer(output4)
writer5 = csv.writer(output5)
writer6 = csv.writer(output6)
writer7 = csv.writer(output7)
writer8 = csv.writer(output8)
writer9 = csv.writer(output9)
writer10 = csv.writer(output10)

writer1.writerow(['ISSUE_DATE', 'ISSUE_TIME', 'FINE_AMOUNT', 'TICKET_LOCATION_STREET', 'VIOLATION DESCRIPTION', 'TIME', 'DOW'])
writer2.writerow(['ISSUE_DATE', 'ISSUE_TIME', 'FINE_AMOUNT', 'TICKET_LOCATION_STREET', 'VIOLATION DESCRIPTION', 'TIME', 'DOW'])
writer3.writerow(['ISSUE_DATE', 'ISSUE_TIME', 'FINE_AMOUNT', 'TICKET_LOCATION_STREET', 'VIOLATION DESCRIPTION', 'TIME', 'DOW'])
writer4.writerow(['ISSUE_DATE', 'ISSUE_TIME', 'FINE_AMOUNT', 'TICKET_LOCATION_STREET', 'VIOLATION DESCRIPTION', 'TIME', 'DOW'])
writer5.writerow(['ISSUE_DATE', 'ISSUE_TIME', 'FINE_AMOUNT', 'TICKET_LOCATION_STREET', 'VIOLATION DESCRIPTION', 'TIME', 'DOW'])
writer6.writerow(['ISSUE_DATE', 'ISSUE_TIME', 'FINE_AMOUNT', 'TICKET_LOCATION_STREET', 'VIOLATION DESCRIPTION', 'TIME', 'DOW'])
writer7.writerow(['ISSUE_DATE', 'ISSUE_TIME', 'FINE_AMOUNT', 'TICKET_LOCATION_STREET', 'VIOLATION DESCRIPTION', 'TIME', 'DOW'])
writer8.writerow(['ISSUE_DATE', 'ISSUE_TIME', 'FINE_AMOUNT', 'TICKET_LOCATION_STREET', 'VIOLATION DESCRIPTION', 'TIME', 'DOW'])
writer9.writerow(['ISSUE_DATE', 'ISSUE_TIME', 'FINE_AMOUNT', 'TICKET_LOCATION_STREET', 'VIOLATION DESCRIPTION', 'TIME', 'DOW'])
writer10.writerow(['ISSUE_DATE', 'ISSUE_TIME', 'FINE_AMOUNT', 'TICKET_LOCATION_STREET', 'VIOLATION DESCRIPTION', 'TIME', 'DOW'])

for row in csv.reader(input1):
    if (row[3] == "UNIVERSITY ST"):
        writer1.writerow(row)
    if (row[3] == "LOT 16A - FAC/STAFF LOT"):
    	writer2.writerow(row)
    if (row[3] == "15TH AVE"):
    	writer3.writerow(row)
    if (row[3] == "13TH AVE"):
    	writer4.writerow(row)
    if (row[3] == "LOT 29A - EMU VIS LOT"):
    	writer5.writerow(row)
    if (row[3] == "LOT 17 - HEDCO"):
    	writer6.writerow(row)
    if (row[3] == "LOT 12A - ONYX-LAWRENCE"):
    	writer7.writerow(row)
    if (row[3] == "LOT 15 - JAQUA"):
    	writer8.writerow(row)
    if (row[3] == "LOT 42 - 12TH W OF KIN"):
    	writer9.writerow(row)
    if (row[3] == "LOT 56 - MILLRACE"):
    	writer10.writerow(row)

input1.close()
output1.close()
output2.close()
output3.close()
output4.close()
output5.close()
output6.close()
output7.close()
output8.close()
output9.close()
output10.close()
