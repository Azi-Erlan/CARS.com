from django.views import generic
from django.urls import reverse_lazy
from drivers.models import Driver
from drivers.forms import DriverForm


class DriverCreateView(generic.CreateView):
    template_name = 'create_driver.html'
    form_class = DriverForm
    success_url = reverse_lazy('drivers_list')


class DriverListView(generic.ListView):
    template_name = 'drivers_list.html'
    model = Driver
    context_object_name = 'drivers'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class DriverUpdateView(generic.UpdateView):
    template_name = 'create_driver.html'
    form_class = DriverForm
    model = Driver
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('drivers_list')


class DriverDeleteView(generic.DeleteView):
    model = Driver
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('drivers_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)