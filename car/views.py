from django.shortcuts import redirect, render
from .models import  Car
# Create your views here.
def lists(request):
    lists = Car.objects.all()
    context = {
'lists':lists,
     }
    return render(request, 'car/list.html',context)


def add(request):
    if request.POST:
        car_name = request.POST['car']
        year_name = request.POST['year']
        Car.objects.create(brand=car_name,year=year_name)
        return redirect('lists')
    else:
      return render(request, 'car/add.html')


def delete(request):
    if request.POST:
        id = request.POST['pk']
        try:
            Car.objects.get(id=id).delete()
            return redirect('lists')
        except:
            return redirect('lists')
    else:   
      return render(request, 'car/delete.html')