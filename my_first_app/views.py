from django.shortcuts import render

# Create your views here.

def my_view(request):
    cars = [
        'Audi',
        'BMW',
        'Mercedes',
        'Toyota',
        'Honda',
        'Ford',
        'Chevrolet',
        'Nissan',
        'Hyundai',
        'Kia',
        'Volkswagen',
        'Volvo',
        'Mazda',
        'Subaru',
        'Jeep',
        'Dodge',
        'Chrysler',
        'Buick',
        'Cadillac',
        'GMC',
        'Ram',
        'Acura',
        'Infiniti',
        'Lexus',
        'Lincoln',
        'Land Rover',
        'Jaguar',
        'Porsche',
        'Ferrari',
        'Lamborghini',
        'Maserati',
        'McLaren',
        'Bugatti',
        'Koenigsegg',
        'Pagani',
        'Aston Martin',
        'Bentley',
        'Rolls-Royce',
        'Lotus',
        'Alfa Romeo',
        'Fiat',
        'Mini',
        'Smart',
        'Tesla',
        'Rivian',
        'Lucid',
    ]

    context = {
        'cars': cars
    }

    return render(request, 'my_first_app/car_list.html', context)
