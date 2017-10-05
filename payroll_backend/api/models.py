from django.db import models


class Report(models.Model):
	"""Report model stores simply stores the report_id and created_date. 
	Along with a primary key, I believe its good practice to have primary keys on most tables.
	"""
	id = models.AutoField(primary_key=True)
	report_id = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)

class TimeReport(models.Model):
	"""TimeReport model connects the report_id from the Report model. A one to many relationship.
	"""
	id = models.AutoField(primary_key=True)
	report_id = models.IntegerField()
	employee_id = models.IntegerField()
	job_group = models.CharField(max_length=64)
	hours_worked = models.FloatField()
	date = models.DateField()

class JobGroup(models.Model):
	"""JobGroup model stores the job_group name and hourly rate.
	Rates are used to calculate the amount owed.
	"""
	id = models.AutoField(primary_key=True)
	job_group = models.CharField(max_length=64)
	rate = models.FloatField()
