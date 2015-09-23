from django.shortcuts import *
from django.template import *
from mardi.models import *
from django.core.mail import send_mail
from mardi.forms import *
from django.core import mail

def index(request,title):
    menu=[]
    dropStyle=""
    active=''
    mList = menuList.objects.all()
    title=r"/mardi/"+title+r"/"
    pageObj = menuList.objects.get(menuUrl=title)
    pageTitle=pageObj.displayName
    for menuitem in mList:
        subList=[]
        sub= subMenu.objects.filter(subParent=menuitem.displayName)
        subList=list(sub)
        if subList:
            dropStyle='has-dropdown'
        menu.append((menuitem.displayName,menuitem.menuUrl,subList,dropStyle))
    menu.sort()
    cont = Context({'menuList':menu,'pageTitle':pageTitle,
                    'details': pageObj.details,
                    'dropStyle':dropStyle})
    html = render_to_response('details.html',cont)
    return html


def contact(request):
    pageTitle="Contact"
    menu=[]
    dropStyle=""
    active=''
    mList = menuList.objects.all()
    title=r"/mardi/contact/"
    pageObj = menuList.objects.get(menuUrl=title)
    pageTitle=pageObj.displayName
    for menuitem in mList:
        subList=[]
        sub= subMenu.objects.filter(subParent=menuitem.displayName)
        subList=list(sub)
        if subList:
            dropStyle='has-dropdown'
        menu.append((menuitem.displayName,menuitem.menuUrl,subList,dropStyle))
    menu.sort()
    if request.method == 'POST':
        formContact=contactForm(request.POST)
        if 1 == 1:
            name = request.POST.get('name')
            subject = name + request.POST.get('subject')
            message = request.POST.get('message')
            sender = request.POST.get('sender')
            recipients = ['info@example.com']
#            send_mail(subject, message,sender, recipients)
            formContact = [name,sender,'Thank you',subject ]
            cont = Context({'menuList':menu,'pageTitle':pageTitle,
                    'details': "Thank You",
                    'dropStyle':dropStyle})
            html = render_to_response('details.html',cont)
            return html
    else:
        formContact=contactForm()
    cont = Context({'menuList':menu,'pageTitle':pageTitle,
                    'form': formContact,'details': pageObj.details,
                    'dropStyle':dropStyle})
    html = render_to_response('details.html',cont)
    return html
