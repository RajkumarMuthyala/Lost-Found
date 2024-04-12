from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import Customer_Details



from django.shortcuts import render, redirect


 # Render the form template
def home(request):
    return render(request,'helloapp/home.html')
def move_home(request):
    return render(request,'home.html')
def form(requst):
    return render(requst,'helloapp/form.html')
def create_customer(request):
    if request.method == 'POST':
    # Retrieve form data (using a dictionary for clarity)
        customer_data = {
            'name':request.POST.get('name'),
            'email': request.POST.get('email'),
            'mobilenumber': request.POST.get('mobilenumber',''),
            'branch': request.POST.get('branch', ''),  # Set a default empty string for optional branch
            'itemdetails': request.POST.get('itemdetails'),
            'select_type': request.POST.get('select_type'),
        }

    # Form validation (optional but highly recommended)
    # ... (implement form validation using Django forms or custom logic, if needed)

    # Create and save new customer object
        new_customer = Customer_Details(**customer_data)
        new_customer.save()

        return render(request, 'helloapp/success.html')   # Redirect to a success page (optional)
    else:
        return render(request, 'helloapp/form.html') 


def view_all_customers(request):
  customers = Customer_Details.objects.all()  # Get all customer objects
  context = {'customers': customers}
  return render(request, 'helloapp/list.html', context)
def list(requst):
    return render(requst,'helloapp/list.html')


