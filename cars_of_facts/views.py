from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Car

def bmw(req):
    return HttpResponse("""
        <h1>BMW</h1><p>BMW — это немецкий премиум-бренд, ставший символом драйва и инженерного совершенства 
        Слоган: «С удовольствием за рулем».</p>
        <img src=https://cdn.motor1.com/images/mgl/9mBAlv/s3/bmw-m4-csl-nurburgring.jpg>
    """)

def audi(req):
    return HttpResponse("""
        <h1>Audi</h1><p>Audi —это немецкий премиум-бренд,Золотая середина между агрессией BMW и пафосом Mercedes. Выбор тех, кто любит «тихую роскошь» и гаджеты. 
        Слоган: «Vorsprung durch Technik» (Превосходство высоких технологий).</p>
        <img src=https://dealerinspire-image-library-prod.s3.us-east-1.amazonaws.com/images/Aftc84C6CSvVZHmphjK623zTFrQtpX22sgab84L0.jpg>
    """)

def mercedes(req):
    return HttpResponse("""
        <h1>Mercedes</h1><p>Mercedes-Benz —это немецкий премиум-бренд,марка для тех, кто ценит роскошь и хочет подчеркнуть свой успех. 
        Слоган: «The Best or Nothing» (Лучшее или ничего).</p>
        <img src=https://img.championat.com/s/732x488/news/big/i/g/mercedes-amg-cle-53-4matic-coupe_1701859873820942894.jpg>
    """)


def cars_list_view(req):
    cars = Car.objects.all()
    return render(req, 'car_list.html', {'cars': cars})


def cars_detail_view(req, id):
    car = get_object_or_404(Car, id=id)
    return render(req, 'car_detail.html', {'car': car})