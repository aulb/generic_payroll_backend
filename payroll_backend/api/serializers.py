from rest_framework import serializers
from api.models import Report, TimeReport, JobGroup


class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Report
		fields = '__all__'

	id = serializers.IntegerField(read_only=True)
	report_id = serializers.IntegerField()

	def create(self, validated_data):
		return Report.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.report_id = validated_data.get('report_id', instance.report_id)
		instance.save()
		return instance


class TimeReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = TimeReport
		fields = '__all__'

	id = serializers.IntegerField(read_only=True)
	report_id = serializers.IntegerField()
	employee_id = serializers.IntegerField()
	job_group = serializers.CharField(max_length=64)
	hours_worked = serializers.FloatField()

	def create(self, validated_data):
		return TimeReport.objects.create(**validated_data)


class JobGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = JobGroup
		fields = '__all__'

	id = serializers.IntegerField(read_only=True)
	job_group = serializers.CharField(max_length=64)
	rate = serializers.FloatField()

	def create(self, validated_data):
		return JobGroup.objects.create(**validated_data)
