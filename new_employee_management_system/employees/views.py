from django.http import HttpResponse
from django.template import loader
from .models import Employee

# This function retrieves all employees name and render all employees page
def employees(request):
  myemployees = Employee.objects.all().values()
  template = loader.get_template('all_employees.html')
  context = {
    'myemployees': myemployees,
  }
  return HttpResponse(template.render(context, request))

# This function retrieves each Employee by id and render employee details page
def details(request, slug):
  myemployee = Employee.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'myemployee': myemployee,
  }
  return HttpResponse(template.render(context, request))

# This functino render the main page
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())