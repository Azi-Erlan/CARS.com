from django.shortcuts import render, redirect
from drivers.forms import DriverForm
from drivers.models import Driver


def create_driver_view(request):

    if request.method == "POST":

        form = DriverForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/drivers_list/')

    else:
        form = DriverForm()

    return render(
        request,
        'create_driver.html',
        {'form': form}
    )

def drivers_list_view(request):

    if request.method == "GET":

        drivers = Driver.objects.all().order_by('-id')

    return render(request, 'drivers_list.html', {'drivers': drivers})

def update_driver_view(request, id):

    driver = Driver.objects.get(id=id)

    if request.method == "POST":

        form = DriverForm(request.POST, request.FILES, instance=driver)

        if form.is_valid():
            form.save()
            return redirect('/drivers_list/')

    else:
        form = DriverForm(instance=driver)

    return render(request, 'create_driver.html', {'form': form})


def delete_driver_view(request, id):

    driver = Driver.objects.get(id=id)

    driver.delete()

    return redirect('/drivers_list/')