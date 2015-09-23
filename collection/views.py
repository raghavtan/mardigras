from django.shortcuts import *
from django.template import *
from collection.models import *
from mardi.models import *
from collection.models import *
import os,sys
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re

# Create your views here.
def products(request,id_product):
    menu=[]
    dropStyle=""
    active=''
    mList = menuList.objects.all()
    catalogue=[]
#-- pagination
    Base_dir = os.path.dirname(os.path.dirname(__file__))
    B_DIR=os.path.join(Base_dir, 'static\img\page',)
    p_dir=os.path.join(Base_dir, 'static\img\page',)
    image_list_names = os.listdir(B_DIR)
    image_list = os.listdir(p_dir)
    rex=re.compile(r"(?P<name>\S+)\.(\S+)",)
    for item in image_list:
        m=rex.match(item)
        if not m:
            image_list.remove(item)
    p_l=Paginator(image_list,6)
    p_r=p_l.num_pages
    pa = request.GET.get('page')
#    page_list=p_l.num_range
    try:
        products = p_l.page(pa)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = p_l.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = p_l.page(p_l.num_pages)
#--content        
    #product_obj= product_list.objects.get(product_id=id_product)
    #if product_obj:
        # render object details to context variables
    #else:
        # render 404 to context variables
    category_object=category_list.objects.all()
    category_tree_object = category_tree.objects.values()
    for categ in category_object:
        parent_categ=categ.category_id
        test = category_list.objects.all()
        children_list=[]
        children = category_tree.objects.filter(parent_category=parent_categ)
        for child in children:
            children_list.append(child.child_category)
        catalogue.append((categ.category_name,children_list))
        catalogue.sort()
    for menuitem in mList:
        subList=[]
        sub= subMenu.objects.filter(subParent=menuitem.displayName)
        subList=list(sub)
        if subList:
            dropStyle='has-dropdown'
        menu.append((menuitem.displayName,menuitem.menuUrl,subList,dropStyle))
    menu.sort()
    cont = Context({'menuList':menu,'pageTitle':id_product,
                    'products':products,
                    'details': id_product,'catalogue':catalogue,
                    'dropStyle':dropStyle})
    html = render_to_response('product.html',cont)
    return html

def collection(request):
    pageTitle="Collection"
    menu=[]
    dropStyle=""
    active=''
    mList = menuList.objects.all()
    title=r"/collection/"
    catalogue=[]
    categories=[]

    #-- pagination
    Base_dir = os.path.dirname(os.path.dirname(__file__))
    B_DIR=os.path.join(Base_dir, 'static\img\page',)
    p_dir=os.path.join(Base_dir, 'static\img\page',)
    image_list_names = os.listdir(B_DIR)
    image_list = os.listdir(p_dir)
    rex=re.compile(r"(?P<name>\S+)\.(\S+)",)
    for item in image_list:
        m=rex.match(item)
        if not m:
            image_list.remove(item)
    p_l=Paginator(image_list,6)
    p_r=p_l.num_pages
    pa = request.GET.get('page')
#    page_list=p_l.num_range
    try:
        products = p_l.page(pa)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = p_l.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = p_l.page(p_l.num_pages)
    
    pageObj = menuList.objects.get(menuUrl=title)
    pageTitle=pageObj.displayName
    category_object=category_list.objects.all()
    category_tree_object = category_tree.objects.values()
    for categ in category_object:
        categories.append((categ.category_id,
                           categ.category_name,categ.category_desc,
                           categ.icon_file_name))
        categories.sort()
        parent_categ=categ.category_id
        parent_categ=categ.category_id
        test = category_list.objects.all()
        children_list=[]
        children = category_tree.objects.filter(parent_category=parent_categ)
        for child in children:
            children_list.append(child.child_category)
        catalogue.append((categ.category_name,children_list))
        catalogue.sort()    
    for menuitem in mList:
        subList=[]
        sub= subMenu.objects.filter(subParent=menuitem.displayName)
        subList=list(sub)
        if subList:
            dropStyle='has-dropdown'
        menu.append((menuitem.displayName,menuitem.menuUrl,subList,dropStyle))
    menu.sort()
    cont = Context({'menuList':menu,'pageTitle':pageTitle,
                    'catalogue':catalogue,'products':products,
                    'categories': categories,'details': pageObj.details,
                    'dropStyle':dropStyle})
    html = render_to_response('category.html',cont)
    return html

def category(request,category):
    pageTitle=category+"Category"
    menu=[]
    dropStyle=""
    active=''
    mList = menuList.objects.all()
    title=r"/mardi/category/"
    catalogue=[]
    categories=[]
#-- pagination
    Base_dir = os.path.dirname(os.path.dirname(__file__))
    B_DIR=os.path.join(Base_dir, 'static\img\page',)
    p_dir=os.path.join(Base_dir, 'static\img\page',)
    image_list_names = os.listdir(B_DIR)
    image_list = os.listdir(p_dir)
    rex=re.compile(r"(?P<name>\S+)\.(\S+)",)
    for item in image_list:
        m=rex.match(item)
        if not m:
            image_list.remove(item)
    p_l=Paginator(image_list,6)
    p_r=p_l.num_pages
    pa = request.GET.get('page')
#    page_list=p_l.num_range
    try:
        products = p_l.page(pa)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = p_l.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = p_l.page(p_l.num_pages)
#-- content and catalogue tree    
    #pageObj = menuList.objects.get(menuUrl=title)
    #pageTitle=pageObj.displayName
    category_object=category_list.objects.all()
    category_tree_object = category_tree.objects.values()
    for categ in category_object:
        categories.append((categ.category_id,
                           categ.category_name,categ.category_desc,
                           categ.icon_file_name))
        categories.sort()
        parent_categ=categ.category_id
        test = category_list.objects.all()
        children_list=[]
        children = category_tree.objects.filter(parent_category=parent_categ)
        for child in children:
            children_list.append(child.child_category)
        catalogue.append((categ.category_name,children_list))
        catalogue.sort()
#-- menu
    for menuitem in mList:
        subList=[]
        sub= subMenu.objects.filter(subParent=menuitem.displayName)
        subList=list(sub)
        if subList:
            dropStyle='has-dropdown'
        menu.append((menuitem.displayName,menuitem.menuUrl,subList,dropStyle))
    menu.sort()
    cont = Context({'menuList':menu,'pageTitle':pageTitle,
                    'catalogue':catalogue,'products':products,
                    'categories': categories,'dropStyle':dropStyle})
    html = render_to_response('category.html',cont)
    return html
