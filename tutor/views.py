from django.shortcuts import render
from .models import Tutors
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
# Create your views here.
from .forms import CreateSchedule
def tutor_list(request):
    tutors = Tutors.objects.filter(published_date__lt=timezone.now()).order_by('-published_date')
    return render(request, 'tutors.html', {'tutors': tutors})

def tutor_new(request):
    if request.method == "POST":
        form = CreateSchedule(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.user = request.user
            schedule.published_date = timezone.now()
            schedule.save()
            return redirect('tutor_list')
    else:
        form = CreateSchedule()
    return render(request, 'postTutor.html', {'form': form})

def tutor_edit(request, pk):
    tutor = get_object_or_404(Tutors, pk=pk)
    if request.method == "POST":
        form = CreateSchedule(request.POST, instance=tutor)
        if form.is_valid():
            tutor = form.save(commit=False)
            tutor.author = request.user
            tutor.published_date = timezone.now()
            tutor.save()
            return redirect('tutor_list')
    else:
        form = CreateSchedule(instance=tutor)
    return render(request, 'postForm.html', {'form': form})

def tutor_delete(request, pk):
    tutor = get_object_or_404(Tutors, pk=pk)
    if request.user == tutor.user:
        tutor.delete()
        return redirect('tutor_list')
    else:
        return redirect('tutor_list')
