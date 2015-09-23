from django.shortcuts import *
from django.template import *
from mardi.models import *

def home(request):
    menu=[]
    dropStyle=""
    active=''
    mList = menuList.objects.all()
    title=r"/"
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
    pageTitle="The MARDI GRAS"
    cont = Context({'menuList':menu,'pageTitle':pageTitle,
                    'sample': menu,'details': pageObj.details,
                    'dropStyle':dropStyle})
    html = render_to_response('home.html',cont)
    return html
