from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Event, AttendanceRecord
from .forms import EventForm

def maintEvent(request):
    """
    View and Edit Events
    """
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()    #TODO - probably should validate event is in future
    else:
        form = EventForm()

    rows = Event.objects.all()
    ctx = {'pageHeading': 'Maintain Events', 'rows':rows, 'formAdd': form}
    return render(request, 'attendance/events.html', ctx)
