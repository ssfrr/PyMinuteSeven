import csv

def TogglEntryListFromCSV(filename):
	entryList = []
	csvFile = open(filename, 'r')
	reader = csv.reader(csvFile, delimiter=',')

	#skip the first line
	reader.next()
	for row in reader:
		entry = togglTimeEntry()
		entry.User = row[0]
		entry.Client = row[1]
		entry.Project = row[2]
		entry.Description = row[3]
		if row[4] == 1:
			entry.Billable = True
		else:
			entry.Billable = False
		if row[5] == 1:
			entry.Closed = True
		else:
			entry.Closed = False
		entry.StartedAt = row[6]
		entry.LastChanged = row[7]
		entry.Duration = row[8]
		entry.Tags = row[9].split(' ')
		entryList.append(entry)

	return entryList


class togglTimeEntry:
	def __init__(self):
		self.User = ''
		self.Client = ''
		self.Project = ''
		self.Description = ''
		self.Billable = True
		self.Closed = True
		self.StartedAt = ''
		self.LastChanged = ''
		self.Duration = ''
		self.Tags = []
