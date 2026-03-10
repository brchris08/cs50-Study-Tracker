from django.shortcuts import render, redirect, get_object_or_404
from .models import StudySession
from .forms import SessionForm
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    sessions = StudySession.objects.all().order_by('-date')
    
    # Calculate stats for Claude's summary cards
    total_minutes = sessions.aggregate(Sum('duration_minutes'))['duration_minutes__sum'] or 0
    total_hours = round(total_minutes / 60, 1)
    last_session = sessions.first()
    current_week = sessions.order_by('-week_number').first().week_number if sessions.exists() else 0

    return render(request, 'logs/dashboard.html', {
        'sessions': sessions,
        'total_hours': total_hours,
        'last_session': last_session,
        'current_week': current_week,
    })

@login_required
def log_session(request):
    if request.method == "POST":
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SessionForm()
    return render(request, 'logs/log_session.html', {'form': form})

def edit_session(request, pk):
    session = get_object_or_404(StudySession, pk=pk)
    if request.method == "POST":
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SessionForm(instance=session)
    return render(request, 'logs/log_session.html', {'form': form, 'edit_mode': True})

def delete_session(request, pk):
    session = get_object_or_404(StudySession, pk=pk)
    if request.method == "POST":
        session.delete()
        return redirect('dashboard')
    return render(request, 'logs/delete_confirm.html', {'session': session})