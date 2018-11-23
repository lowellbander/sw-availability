import csv, json

def splitAndStrip(string):
  return [s.strip() for s in string.split(',')]

responses = {}

with open('responses.csv') as csvfile:
  for rowIndex, row in enumerate(csv.reader(csvfile, delimiter=',', quotechar="\"")):
    if rowIndex == 0:
      continue # first row is header
    response = {}
    response['Sunday'] = splitAndStrip(row[2])
    response['Monday'] = splitAndStrip(row[3])
    response['Tuesday'] = splitAndStrip(row[4])
    response['Wednesday'] = splitAndStrip(row[5])
    response['Thursday'] = splitAndStrip(row[6])
    response['Friday'] = splitAndStrip(row[7])
    response['Saturday'] = splitAndStrip(row[8])
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
  for time in timesOfDay:
    availabilities[day + ' ' +time] = [comrade for comrade in comrades if time in responses[comrade][day]]

print json.dumps(availabilities, indent=1)

pairings = {}

for slot1 in availabilities:
  for slot2 in availabilities:
    pairings[slot1 + ' & ' + slot2] = list(set(availabilities[slot1]).union(availabilities[slot2]))
    # print len(comradesAvailable)

print json.dumps(pairings, indent=1)

