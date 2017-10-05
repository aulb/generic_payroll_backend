from api.models import Report, TimeReport, JobGroup
from api.serializers import ReportSerializer, TimeReportSerializer, JobGroupSerializer
from api.utils import TimeReportCSVParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


"""
Basic API Layout
GET /reports/ - Retrieve a list of available reports
GET /timereports/ - Get all time report information
POST /timereport/{csv_file} - Post new 
GET /jobgroups/ - Retrieve all
"""
class ReportList(APIView):
	def get(self, request, format=None):
		reports = Report.objects.all()
		serializer = ReportSerializer(reports, many=True)
		return Response(serializer.data)


class TimeReportList(APIView):
	def does_report_exist(self, report_id):
		try:
			if Report.objects.get(report_id=report_id):
				return True
		except Report.DoesNotExist:
			return False

	def save_new_report(self, report_id):
		serializer = ReportSerializer(data={'report_id': report_id})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, format=None):
		time_reports = TimeReport.objects.all()
		serializer = TimeReportSerializer(time_reports, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		print(request.FILES.keys())
		csv_string = request.FILES['file'].read().decode('utf-8') 
		# Get data and report id
		parsed_data = TimeReportCSVParser(csv_string)
		report_id = parsed_data.report_id
		data = parsed_data.data

		serializer = TimeReportSerializer(data=data, many=True)
		# If the report id already exist do not store, TODO: error separation
		if not self.does_report_exist(report_id) and serializer.is_valid():
			serializer.save()
			self.save_new_report(report_id)
			return Response({'result': 'success'}, status.HTTP_201_CREATED)
		else:
			return Response({'result': 'error'}, status=status.HTTP_400_BAD_REQUEST)


class JobGroupList(APIView):
	def get(self, request, format=None):
		job_groups = JobGroup.objects.all()
		serializer = JobGroupSerializer(job_groups, many=True)
		return Response(serializer.data)

