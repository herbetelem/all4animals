from django.shortcuts import render

# Create your views here.


def profil(request):
    return render(request, 'housing/profil.html')




def housing(request):
    return render(request, 'housing/housing.html')

def user_calendar(request):
    return render(request, 'housing/user_calendar.html')

def housing_search(request):
    return render(request, 'housing/housing_search.html')

def my_calendar(request):
    return render(request, 'housing/my_calendar.html')

    