from django.db.models.signals import post_save
from django.dispatch import receiver
from labs.models import Progress

@receiver(post_save, sender=Progress)
def update_task_status(sender, instance, **kwargs):
    # Update task completion status or any other related logic
    if instance.completed:
        instance.task.flag = 'Completed'
        instance.task.save()
