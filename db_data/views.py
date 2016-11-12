from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from models import Officer, Politburo, Sponsor

# Create your views here.
def officers(request):
    template = loader.get_template("officers.html")
    officers_all = Officer.objects.order_by('last_name')
    officer_list = []
    count = 0
    for officer in officers_all:
        if count % 4 == 0:
            officer_list.append([])
        officer_list[count / 4].append(officer)
        count += 1
    context = RequestContext(request, {'officers' : officer_list})
    return HttpResponse(template.render(context))

def politburo(request):
    template = loader.get_template("politburo.html")
    pb = Politburo.objects.all()
    for member in pb:
        member.contact = member.contact.replace('[name]', member.officer.first_name)
    context = RequestContext(request, {'pb' : pb})
    return HttpResponse(template.render(context))

def sponsors(request):
    template = loader.get_template("sponsors.html")
    sponsors_all = Sponsor.objects.order_by('name')

    sponsors_current = []
    sponsors_old = []
    count_current = 0
    count_old = 0
    for sponsor in sponsors_all:
        if sponsor.current:
            if count_current % 4 == 0:
                sponsors_current.append([])
            sponsors_current[count_current / 4].append(sponsor)
            count_current += 1
        else:
            if count_old % 4 == 0:
                sponsors_old.append([])
            sponsors_old[count_old / 4].append(sponsor)
            count_old += 1

    context = RequestContext(request, {'sponsors_current': sponsors_current,
                                       'sponsors_old': sponsors_old})
    return HttpResponse(template.render(context))