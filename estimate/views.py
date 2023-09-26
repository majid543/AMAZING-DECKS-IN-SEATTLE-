from django.shortcuts import render,redirect
from .forms import UserInputForm
from django.views.generic.edit import CreateView

from .forms import ScheduleForm


def customers_create_view(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            # Process the form data here
            form.save()
            # Redirect to the same page (self.request.path)
            return redirect("/calculate-charges")
    else:
        form = ScheduleForm()
    
    template_name = 'estimate/input_form.html'  # Replace with the actual template name
    context = {'form': form}
    return render(request, template_name, context)

def calculate_service_charges(age,distance, deck_height):
    # Calculate service charges based on user input
    base_charge = 0  # Set a default base charge
    if deck_height < 5:
        base_charge = 50
    else:
        base_charge = 100

    # You can add more calculations here based on age, distance, and other factors
    # For example, you can add charges based on age or distance

    # Total service charges calculation
    total_charges = base_charge  # Add more charges here as needed

    return total_charges

def calculate_charges(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            distance = form.cleaned_data['distance']
            deck_height = form.cleaned_data['deck_height']

            # Calculate service charges
            service_charges = calculate_service_charges(age, distance, deck_height)

            return render(request, 'result.html')
    else:
        form = UserInputForm()
    return render(request, 'input_forms.html', {'form': form})