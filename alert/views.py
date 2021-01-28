from django.shortcuts import render
from django.views import generic
from .models import Alert_user
from .forms import Create_alert 
from django.core.mail import send_mail
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import Alert_user_filter
# Create your views here.

# @login_required(login_url='login')

def contact(request):
    return render(request, 'alert/contact.html')


# Folder alert -----------------------------------------------------------
# def alert_user(request):
#     alert = Alert_user.objects.all()
#     alert_user = {'alert_user': alert,}
#     return render(request, 'alert/alert_user.html', alert_user)



def alert_lost_view(request):
    alert_user = Alert_user.objects.filter(type_alert="1").order_by('-date')
    my_filter = Alert_user_filter(request.GET, queryset=alert_user)
    alert_user = my_filter.qs
    paginator = Paginator(alert_user, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'my_filter':my_filter, 'page_obj': page_obj}
    return render(request, 'alert/alert_lost.html', context)

def alert_find_view(request):
    alert_user = Alert_user.objects.all().exclude(type_alert="1").order_by('-date')
    my_filter = Alert_user_filter(request.GET, queryset=alert_user)
    alert_user = my_filter.qs
    paginator = Paginator(alert_user, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'my_filter':my_filter, 'page_obj': page_obj}
    return render(request, 'alert/alert_find.html', context)

class Alert_detail(generic.DetailView):

    model = Alert_user 
    template_name = "alert/alert_detail.html"

@login_required(login_url='{% url "login" %}')
def alert(request):
    form = Create_alert(initial={'user': request.user.id})
    if request.method == 'POST':
        form = Create_alert(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'alert/create_alert.html', context)


def choice_alert(request):
    return render(request, 'alert/choice_alert.html')

def contact(request, pk):
    alert_detail = Alert_user.objects.get(id=pk)

    if request.method == 'POST':
        object_mail = request.POST['subject']
        message = request.POST['message']
        email_user = request.user.email
        email_alert = alert_detail.user.email
        send_mail(object_mail, message, email_user, [email_alert])
    context = {'alert_detail': alert_detail}
    return render(request, 'alert/contact.html', context)

