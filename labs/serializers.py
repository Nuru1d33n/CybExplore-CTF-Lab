from rest_framework import serializers
from labs.models import LabCategory, LabTask, Progress, Comment

class LabCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LabCategory
        fields = ['id', 'name', 'description']

class LabTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTask
        fields = ['id', 'name', 'description', 'category', 'difficulty', 'flag', 'hint']

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'user', 'task', 'completed', 'completed_at', 'score']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'task', 'content', 'created_at']
