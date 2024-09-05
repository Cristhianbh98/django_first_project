from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import Car

# Create your views here.

def my_view(request):
    cars = Car.objects.all()

    context = {
        'cars': cars
    }

    return render(request, 'my_first_app/car_list.html', context)

def single_car(request, id):
    car = Car.objects.get(id=id)

    context = {
        'car': car
    }

    return render(request, 'my_first_app/single_car.html', context)

class CarListView(TemplateView):
    model = Car
    template_name = 'my_first_app/car_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context