import mechanize
import sys

def ConnectToMinute7():
	EmailAddress = 'srussell@bulogics.com'
	Password = raw_input('Password for ' + EmailAddress + ': ')

	br = mechanize.Browser()
	br.open('http://www.minute7.com')
	br.select_form(predicate=lambda form:form.attrs.get('id',0)=='loginModuleForm')

	br['data[AccountUser][email]'] = EmailAddress
	br['data[AccountUser][password]'] = Password
	br.submit()
	return br

def SubmitTimeEntry(br, entry):
	inventoryIDContents = entry.WorkType
	customerIDContents = entry.Project

	br.select_form(predicate=lambda form:form.attrs.get('id',0)=='timeEntryForm')
	WorkTypeList = br.form.find_control('data[TimeEntry][inventory_item_id]').items
	WorkTypeList = filter(lambda item:item.attrs['contents'] == inventoryIDContents, WorkTypeList)
	if len(WorkTypeList) == 0:
		print("WorkType '" + inventoryIDContents + "' not found")
		sys.exit(1)
	WorkTypeValue = WorkTypeList[0].attrs['value']

	ProjectList = br.form.find_control('data[TimeEntry][customer_id]').items
	ProjectList = filter(lambda item:item.attrs['contents'] == customerIDContents, ProjectList)
	if len(ProjectList) == 0:
		print("Project '" + customerIDContents + "' not found")
		sys.exit(1)
	ProjectValue = ProjectList[0].attrs['value']

	br.form['data[TimeEntry][inventory_item_id]'] = [WorkTypeValue]
	br.form['data[TimeEntry][customer_id]'] = [ProjectValue]
	br.form['data[TimeEntry][description]'] = entry.Description
	br.form['data[TimeEntry][duration]'] = entry.Duration
	br.form['data[TimeEntry][date]'] = entry.Date
	br.submit()

class Minute7TimeEntry:
	WorkType = ''
	Project = ''
	Description = ''
	Duration = ''
	Date = ''

