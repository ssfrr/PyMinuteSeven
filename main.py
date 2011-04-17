#!/usr/bin/python
from MinuteSevenPost import *
from ParseTogglData import *
import sys
from datetime import datetime 

def main(argv):
	if len(argv) != 2:
		print("Usage: main.py <FILENAME>")
		sys.exit(2)


	togglEntryList = TogglEntryListFromCSV(argv[1])
	togglEntryList = filter(lambda entry:entry.Project != '', togglEntryList)
	togglEntryList = filter(lambda entry:entry.Description != '', togglEntryList)
	m7EntryList = map(Minute7EventFromTogglEvent, togglEntryList)

	br = ConnectToMinute7()
	if br.title() != 'Minute7 - Timesheet Week View - Online Timesheet for QuickBooks':
		print("Login Error!")
		return 1

	print("Login Successful")

	for entry in m7EntryList:
		print("Adding to Minute7...")
		print(entry.WorkType)
		print(entry.Project)
		print(entry.Description)
		print(entry.Duration)
		print(entry.Date)
		print("-----------")
		SubmitTimeEntry(br, entry)
	return 0

def Minute7EventFromTogglEvent(togglEvent):
	m7Event = Minute7TimeEntry()
	m7Event.WorkType = WorkTypeDict[togglEvent.Project]
	m7Event.Project = ProjectDict[togglEvent.Project]
	m7Event.Description = togglEvent.Description
	m7Event.Duration = togglEvent.Duration
	togglDateTime = datetime.strptime(togglEvent.StartedAt, "%m/%d/%Y %I:%M %p")
	m7Event.Date = togglDateTime.strftime("%m/%d/%Y")
	return m7Event


ProjectDict = {'Example Toggl Project 1' : 'Minute7 Project 1',
               'Example Toggl Project 2' : 'Minute7 Project 2'}

WorkTypeDict = {'Example Toggl Project 1' : 'Minute7 Worktype 1',
                'Example Toggl Project 2' : 'Minute7 Worktype 2'}

if __name__ == "__main__":
	sys.exit(main(sys.argv))
