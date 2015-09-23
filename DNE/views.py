from django.shortcuts import *
from django.template import *
from mardi.models import *
from django.core.mail import send_mail
from mardi.forms import *
from django.core import mail

def not_found(request):
    menu=[]
    dropStyle=""
    active=''
    mList = menuList.objects.all()
    pageTitle="NOT FOUND"
    for menuitem in mList:
        subList=[]
        sub= subMenu.objects.filter(subParent=menuitem.displayName)
        subList=list(sub)
        if subList:
            dropStyle='has-dropdown'
        menu.append((menuitem.displayName,menuitem.menuUrl,subList,dropStyle))
    menu.sort()
    cont = Context({'menuList':menu,'pageTitle':pageTitle,
                    'dropStyle':dropStyle})
    html = render_to_response('404.html',cont)
    return html
