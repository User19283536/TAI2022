from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from djangoProject.models import Movies, Repertuar, tickets, bookings
from django.contrib.auth.models import User
from datetime import datetime
from dateutil import parser
from django.core.mail import send_mail


from django.template import RequestContext

def home_page(request):
    return render(request, 'index.html')



def repertuar(request):
    queryset = Movies.objects.all()
    queryset2 = Repertuar.objects.all()
    context={
        'movies': queryset,
        'repertuar': queryset2
    }
    return render(request, 'repertuar.html', context)

def cennik(request):
    return render(request, 'cennik.html')

def about(request):
    return render(request, 'about.html')

def kontakt(request):
    return render(request, 'kontakt.html')

def logowanie(request):
    return render(request, 'registration/login.html')

def rejestracja(request):
    return render(request, 'registration/register.html')

def wylogowany(request):
    return render(request, 'registration/logged_out.html')

def zarejestrowany(request):
    konta = User.objects.all()
    first = request.POST.get("first")
    last = request.POST.get("last")
    e_mail = request.POST.get("email")
    uname = request.POST.get("username")
    password = request.POST.get("password")

    try:
        a = konta.get(email=e_mail).email

        return render(request, "error.html")
    except ObjectDoesNotExist:
        try:
            b = konta.get(username=uname).username
            return render(request, "error.html")
        except ObjectDoesNotExist:
            user = User.objects.create_user(uname, e_mail, password)
            user.first_name = first
            user.last_name = last
            user.save()
            return render(request, "finalRegistered.html")

def finalZarejestrowany(request):
    return render(request, "registration/registered.html")

def rezerwacja(request):
    bilety = tickets.objects.all()
    normalny = bilety.get(id=1).price
    ulgowy = bilety.get(id=2).price
    szkolny = bilety.get(id=3).price
    rodzinny = bilety.get(id=4).price

    context = {
        "repertuar": Repertuar,
        "normalny": normalny,
        "ulgowy": ulgowy,
        "szkolny": szkolny,
        "rodzinny": rodzinny,
    }
    try:
        data = request.GET.get("data")
        available = request.GET.get("available")
        nrSeansu = request.GET.get("nrSeansu")
        rp = request.GET.get("rp")
        print(rp)
        context = {
            "repertuar": Repertuar,
            "normalny": normalny,
            "ulgowy": ulgowy,
            "szkolny": szkolny,
            "rodzinny": rodzinny,
            "data": data,
            "rp": int(rp),
            "title": Repertuar.objects.all().get(id=rp).t_id.title,
            "path": Repertuar.objects.all().get(id=rp).t_id.path,
            "nrSeansu": int(nrSeansu),
            "available": available
        }
    except ObjectDoesNotExist:
        print("Błąd")

    return render(request, 'rezerwacja.html', context)

def zarezerwowano(request):
    normalnyIlosc = int( request.POST.get("normalny") )
    ulgowyIlosc = int( request.POST.get("ulgowy") )
    szkolnyIlosc = int( request.POST.get("szkolny") )
    rodzinnyIlosc = int( request.POST.get("rodzinny") )
    bilety = tickets.objects.all()
    normalnyCena = bilety.get(id=1).price
    ulgowyCena = bilety.get(id=2).price
    szkolnyCena = bilety.get(id=3).price
    rodzinnyCena = bilety.get(id=4).price
    laczna_cena = normalnyCena*normalnyIlosc + ulgowyCena*ulgowyIlosc + szkolnyCena*szkolnyIlosc + rodzinnyCena*rodzinnyIlosc
    amount = normalnyIlosc + ulgowyIlosc + szkolnyIlosc + rodzinnyIlosc

    data = parser.parse(request.POST.get("data"))
    nrSeansu = request.POST.get("nrSeansu")
    idRepertuar = int(request.POST.get("idRepertuar"))
    title1 = Repertuar.objects.all().get(id=idRepertuar).t_id.title

    repertuarDB = Repertuar.objects.all().get(id=idRepertuar)

    if int(nrSeansu) == 1:

        if repertuarDB.av_tickets1 - amount < 0:
            return render(request, "error.html")

        Repertuar.objects.filter(id=idRepertuar).update(av_tickets1=repertuarDB.av_tickets1  - amount)
    elif int(nrSeansu) == 2:

        if repertuarDB.av_tickets2 - amount < 0:
            return render(request, "error.html")

        Repertuar.objects.filter(id=idRepertuar).update(av_tickets2=repertuarDB.av_tickets2  - amount)
    elif int(nrSeansu) == 3:

        if repertuarDB.av_tickets3 - amount < 0:
            return render(request, "error.html")

        Repertuar.objects.filter(id=idRepertuar).update(av_tickets3=repertuarDB.av_tickets3  - amount)
    elif int(nrSeansu) == 4:

        if repertuarDB.av_tickets4 - amount < 0:
            return render(request, "error.html")

        Repertuar.objects.filter(id=idRepertuar).update(av_tickets4=repertuarDB.av_tickets4  - amount)

    b = bookings(normalny = float( normalnyIlosc ),
                ulgowy = float( ulgowyIlosc ),
                szkolny = float( szkolnyIlosc ),
                rodzinny = float( rodzinnyIlosc ),
                title = title1,
                date = data,
                data_rezerwacji = datetime.now(),
                email = request.user.email,
                naleznosc = laczna_cena)

    b.save()

    send_mail(
        'Rezerwacja na seans',
        'Dziękujemy za skorzystanie z naszych usług,\nw naszym systemie została złożona rezerwacja na film {} w dniu {} na łaczną kwotę {} PLN\nBilety: \nnormalny: {}\nulgowy: {}\nszkolny: {}\nrodzinny: {}'.format(
            title1, data, "{:.2f}".format(laczna_cena), normalnyIlosc, ulgowyIlosc, szkolnyIlosc, rodzinnyIlosc ),
        'taiprojekt2022@gmail.com',
        [request.user.email],
        fail_silently=False,
    )

    return render(request, "zarezerwowano.html")

def konto(request):
    if request.user.is_authenticated:
        uzytkownik = request.user
        context = {
            "user": uzytkownik
        }
        return render(request, "konto.html", context)
    else:
        return render(request, "index.html")

def zmien(request):
    uzytkownik = User.objects.all().get(id=request.user.id)
    uzytkownik.email = request.POST.get("email")
    uzytkownik.first_name = request.POST.get("first_name")
    uzytkownik.last_name = request.POST.get("last_name")
    uzytkownik.username = request.POST.get("username")
    uzytkownik.save()
    return render(request, "kontoPotwierdzenie.html")


def handler404(request):
    return render(request, "index.html")