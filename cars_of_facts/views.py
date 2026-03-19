from django.views import generic
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import F
from .models import Car


class BmwView(generic.View):
    def get(self, request):
        return HttpResponse("""
            <h1>BMW</h1><p>BMW — это немецкий премиум-бренд...</p>
            <img src=https://cdn.motor1.com/images/mgl/9mBAlv/s3/bmw-m4-csl-nurburgring.jpg>
        """)


class AudiView(generic.View):
    def get(self, request):
        return HttpResponse("""
            <h1>Audi</h1><p>Audi — это немецкий премиум-бренд...</p>
            <img src=https://dealerinspire-image-library-prod.s3.us-east-1.amazonaws.com/images/Aftc84C6CSvVZHmphjK623zTFrQtpX22sgab84L0.jpg>
        """)


class MercedesView(generic.View):
    def get(self, request):
        return HttpResponse("""
            <h1>Mercedes</h1><p>Mercedes-Benz — это немецкий премиум-бренд...</p>
            <img src=https://img.championat.com/s/732x488/news/big/i/g/mercedes-amg-cle-53-4matic-coupe_1701859873820942894.jpg>
        """)


class CarListView(generic.ListView):
    template_name = 'car_list.html'
    model = Car
    context_object_name = 'cars'
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class CarDetailView(generic.DetailView):
    template_name = 'car_detail.html'
    model = Car
    context_object_name = 'car'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        request = self.request

        viewed = request.session.get('viewed_car', [])

        if obj.pk not in viewed:
            Car.objects.filter(pk=obj.pk).update(
                views=F("views") + 1
            )

            viewed.append(obj.pk)
            request.session['viewed_car'] = viewed

            obj.refresh_from_db()

        return obj


class SearchCarView(generic.ListView):
    template_name = 'car_list.html'
    context_object_name = 'cars'
    model = Car

    def get_queryset(self):
        query = self.request.GET.get('s')
        if query:
            return self.model.objects.filter(name__icontains=query)
        return self.model.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context