import io
import csv
import datetime

# TODO: Rename this to utils.py
class TimeReportCSVParser:
	"""Small utility class used to parse the incoming report csv file.
	
	Attributes:
		report_id: An integer representing the report id of this file.
		data: An list containing simple objects extracted from the csv rows.
	"""
	incoming_format = '%d/%m/%Y'
	outgoing_format = '%Y-%m-%d'

	def __init__(self, csv_string):
		self.report_id, self.data = self.parse_report(csv_string)

	def parse_report(self, csv_string):
		data = []
		report_id = None

		rows = list(csv.DictReader(io.StringIO(csv_string)))
		row_length = len(rows)
		for index, row in enumerate(rows):
			if index < row_length - 1:
				data.append(self.parse_row(row))

		# Get the report id here, report id is always the last row
		report_id = int(row['hours worked'])

		# Update all data with report_id
		for row in data:
			row['report_id'] = report_id

		return report_id, data

	def parse_row(self, row):
		data = {
			'date': self.parse_raw_date(row['date']),
			'hours_worked': float(row['hours worked']),
			'employee_id': int(row['employee id']),
			'job_group': row['job group']
		}
		return data

	def parse_raw_date(self, report_date):
		date_string = datetime.datetime.strptime(report_date, self.incoming_format)
		return date_string.strftime(self.outgoing_format)
