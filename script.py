import csv, json

def splitAndStrip(string):
  return [s.strip() for s in string.split(',')]

responses = {}

with open('responses.csv') as csvfile:
  for rowIndex, row in enumerate(csv.reader(csvfile, delimiter=',', quotechar="\"")):
    if rowIndex == 0:
      continue # first row is header
    response = {}
    response['sunday'] = splitAndStrip(row[2])
    response['monday'] = splitAndStrip(row[3])
    response['tuesday'] = splitAndStrip(row[4])
    response['wednesday'] = splitAndStrip(row[5])
    response['thursday'] = splitAndStrip(row[6])
    response['friday'] = splitAndStrip(row[7])
    response['saturday'] = splitAndStrip(row[8])
    name = row[1]
    responses[name] = response

comrades = responses.keys()
daysOfWeek = responses[comrades[0]].keys()
timesOfDay = ['Mornings', 'Afternoons', 'PM Commute (5:30-7pm)', 'Evenings (after 7pm)']

print json.dumps(responses, indent=1)
print json.dumps(comrades, indent=1)
print len(comrades)
print json.dumps(daysOfWeek, indent=1)

# day -> time -> comrades
availabilities = {}

for day in daysOfWeek:
  availabilities[day] = {}
  for time in timesOfDay:
    availabilities[day][time] = [comrade for comrade in comrades if time in responses[comrade][day]]

print json.dumps(availabilities, indent=1)

