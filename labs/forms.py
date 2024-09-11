from django import forms
from labs.models import Comment, LabTask, Progress

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class TaskCompletionForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['task', 'completed', 'score']
        widgets = {
            'task': forms.HiddenInput(),
        }


class LabTaskForm(forms.ModelForm):
    class Meta:
        model = LabTask
        fields = "__all__"
        # fields = ['category', 'title', 'description', 'difficulty']

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['task', 'completed', 'score']

