from django.shortcuts import render
from .models import Tutors
from django.utils import timezone
from django.shortcuts import redirect
# Create your views here.
from .forms import CreateSchedule
def tutor_list(request):
    tutors = Tutors.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
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
