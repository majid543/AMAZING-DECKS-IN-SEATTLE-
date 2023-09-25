from django.shortcuts import render
from .models import Project
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Customers,Picture,Project,ScheduleAppointment
from .forms import CustomersForm,ScheduleForm
from django.shortcuts import get_object_or_404

class CustomerCreateView(CreateView):
    form_class = CustomersForm
    template_name = 'app/quote.html'  # Replace with the actual template name
    def get_success_url(self):
        return self.request.path 

class CustomersCreateView(CreateView):
    form_class = CustomersForm
    template_name = 'app/schedule.html'  # Replace with the actual template name
    def get_success_url(self):
        return self.request.path 

def policy_view(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            # Create an instance of ScheduleAppointment model and save it to the database
            schedule_appointment = ScheduleAppointment(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            schedule_appointment.save()

            # Display a "Thank You" message
            return render(request, 'app/thank_you.html')
    else:
        form = ScheduleForm()

    return render(request, 'app/policy.html', {'form': form})

def homeview(request):
    projects = Project.objects.all()
    return render(request, 'app/home.html',{'projects':projects})

def gallery_view(request):
    projects = Project.objects.all()
    return render(request, 'app/gallery.html', {'projects': projects})
    


def area_view(request):
    return render(request, 'app/area.html')

def fetch_project_photos(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    pictures = Picture.objects.filter(project=project)
    
    # Collect image URLs from related Image objects
    photos = []

    for picture in pictures:
        for image in picture.image.all():
            photos.append({'url': image.image.url})

    return JsonResponse({'photos': photos})