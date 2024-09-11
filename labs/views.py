# from django.shortcuts import render, get_object_or_404, redirect
# from labs.models import LabTask, Progress, Comment, LabCategory
# from labs.forms import CommentForm, LabTaskForm
# from django.db.models import Sum  # Import Sum for aggregation
# from django.contrib.auth.decorators import login_required

# def home(request):
#     categories = LabCategory.objects.all()
#     tasks = LabTask.objects.all().select_related('category')
#     context = {
#         'categories': categories,
#         'tasks': tasks,
#     }
#     return render(request, 'labs/home.html', context)



# def task_detail(request, pk):
#     task = get_object_or_404(LabTask, pk=pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.task = task
#             comment.save()
#             return redirect('task_detail', pk=task.pk)
#     else:
#         form = CommentForm()
#     comments = Comment.objects.filter(task=task)
#     return render(request, 'labs/task_detail.html', {'task': task, 'form': form, 'comments': comments})


# @login_required
# def leaderboard(request):
#     scores = Progress.objects.values('user').annotate(total_score=Sum('score')).order_by('-total_score')
#     context = {
#         'scores': scores,
#     }
#     return render(request, 'labs/leaderboard.html', context)


# @login_required
# def user_progress(request):
#     progress = Progress.objects.filter(user=request.user).select_related('task')
#     context = {
#         'progress': progress,
#     }
#     return render(request, 'labs/user_progress.html', context)


# @login_required
# def create_task(request):
#     if request.method == 'POST':
#         form = LabTaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lab_category_list')
#     else:
#         form = LabTaskForm()
#     return render(request, 'labs/create_task.html', {'form': form})



# @login_required
# def submit_task(request, pk):
#     task = get_object_or_404(LabTask, pk=pk)
#     if request.method == 'POST':
#         form = TaskCompletionForm(request.POST)
#         if form.is_valid():
#             progress = form.save(commit=False)
#             progress.user = request.user
#             progress.save()
#             return redirect('user_progress')
#     else:
#         form = TaskCompletionForm(initial={'task': task})
#     return render(request, 'labs/submit_task.html', {'form': form, 'task': task})


# @login_required
# def add_comment(request, pk):
#     task = get_object_or_404(LabTask, pk=pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.task = task
#             comment.save()
#             return redirect('task_detail', pk=pk)
#     else:
#         form = CommentForm()
#     return render(request, 'labs/add_comment.html', {'form': form, 'task': task})


from rest_framework import viewsets
from labs.models import LabCategory, LabTask, Progress, Comment
from labs.serializers import LabCategorySerializer, LabTaskSerializer, ProgressSerializer, CommentSerializer

class LabCategoryViewSet(viewsets.ModelViewSet):
    queryset = LabCategory.objects.all()
    serializer_class = LabCategorySerializer

class LabTaskViewSet(viewsets.ModelViewSet):
    queryset = LabTask.objects.all()
    serializer_class = LabTaskSerializer

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
