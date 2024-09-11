from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from profiles.forms import ProfileUpdateForm
from profiles.models import Profile



@login_required
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'profiles/profile.html', )


@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'profiles/edit_profile.html', {'form': form})

@login_required
def view_profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'profiles/view_profile.html', {'profile': profile})


@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'profiles/notifications.html', {'notifications': user_notifications})
