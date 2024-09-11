from django.db import models
from django.contrib.auth.models import User

class LabCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ActiveLabTaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(flag__isnull=True)

class LabTask(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(LabCategory, related_name='tasks', on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    flag = models.CharField(max_length=100, blank=True, null=True)
    hint = models.TextField(blank=True, null=True)

    objects = models.Manager()  # Default manager
    active_tasks = ActiveLabTaskManager()  # Custom manager for active tasks

    def __str__(self):
        return self.name

    def get_total_score(self):
        return self.progress_set.filter(completed=True).aggregate(total_score=models.Sum('score'))['total_score'] or 0

    def clean(self):
        if not self.flag and not self.hint:
            raise ValidationError('At least one of flag or hint must be provided.')

    def save(self, *args, **kwargs):
        self.clean()  # Call the clean method before saving
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Lab Task'
        verbose_name_plural = 'Lab Tasks'

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(LabTask, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.task.name}"

    def save(self, *args, **kwargs):
        # Optionally update the task completion status
        if self.completed:
            self.task.flag = 'Completed'
            self.task.save()
        super().save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(LabTask, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.name}"
