import csv

def totalsGenerator(song_id):
  with open('DATA_MERGED.csv') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)
    totalPlays = 0
    totalRevenue = 0

    newCsv = open("MERGED_METRICS.csv", 'a')
    writer = csv.writer(newCsv)

    for line in csv_data:
      workId = line[0]
      plays = float(line[1])
      revenue = float(line[2])
      day = line[3]

      if workId == song_id:
        totalPlays += plays
        totalRevenue += revenue
    writer.writerow([song_id, totalPlays, totalRevenue])

def idPasser(month):

  newCsv = open("MERGED_METRICS.csv", 'w')
  writer = csv.writer(newCsv)
  writer.writerows([['WORK_ID','PLAYS','REVENUE','DAY']])
  newCsv.close()

  with open('DATA_MERGED.csv') as data_file:
    csv_data = csv.reader(data_file)
    idList = list()
    for line in csv_data:
      if line[0] not in idList and f'{month}' in line[3]:
        totalsGenerator(line[0])
        idList.append(line[0])

idPasser('Jul')