from rest_framework import serializers
from .models import UserVideoSummary, Summary

class UserVideoSummarySerializer(serializers.ModelSerializer):
    summary_obj_id = serializers.SerializerMethodField()
    summary_obj_title = serializers.SerializerMethodField()

    class Meta:
        model = UserVideoSummary
        fields = ['summary_obj_id', 'summary_obj_title']

    def get_summary_obj_id(self, obj):
        return obj.summary.video_id

    def get_summary_obj_title(self, obj):
        return obj.summary.video_title

class SummaryOnly(serializers.ModelSerializer):
    class Meta:
        models = Summary
        fields = ["video_summary"]

