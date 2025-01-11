from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product
from store.models import Customer
from store.models import Collection
from store.models import Order 
from store.models import OrderItem

# Create your views here.


def say_hello(request):
    #-------managers and Query_Set---------

    #all Method :
    # query_set= Product.objects.all()

    # for Product in query_set:
    #     print(Product)


    #----------Retriving Objects-------------

    #get method : to get Single Value
    # try:
    #     product=Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass

    #filter method : (it returns query_set if the query_set is empty it will return none)
    #product=Product.objects.filter(pk=0).first()

    #check the existance of object : ( Return Boolean )
    # exists=Product.objects.filter(pk=0).exists()


    #----------Filtering objects----------

    #unit_price__gt (the double underscore is used to specify the logical operator where gt=greater than) :
    #query_set=Product.objects.filter(unit_price__gt=20)

    #print the results Between Range(Change in the hello.html file) :
    #query_set=Product.objects.filter(unit_price__range=(20,30))

    #Find all products in collection 1 :
    #query_set=Product.objects.filter(collection__id__gt=1)

    #Retrive that have string or text :
    #the i before the contains to make it case insensitive also check differnt loockups
    #query_set=Product.objects.filter(title__icontains='coffee')

    #retrive base on date :
    #query_set=Product.objects.filter(last_update__year=2021)

    #finding products that don't have description that is null
    #query_set=Product.objects.filter(description__isnull=True)

    #-------------Filtering Exercises------------

    #Customers with .com accounts : 
    #query_set=Customer.objects.filter(email__icontains='.com')

    #Collections that don’t have a featured product :
    # query_set=Collection.objects.filter(featured_product__isnull=True)

    # Products with low inventory (less than 10) :
    # query_set=Product.objects.filter(inventory__lt=10)

    #Orders placed by customer with id = 1 :
    # query_set=Order.objects.filter(customer__id=1)

    #Order items for products in collection 3 :
    query_set=OrderItem.objects.filter(product__collection__id=3)











    # return render(request,'hello.html',{'name':'Sahil','products':list(query_set)})
    # return render(request,'hello.html',{'name':'Sahil','customers':list(query_set)})
    # return render(request,'hello.html',{'name':'Sahil','collections':list(query_set)})
    # return render(request,'hello.html',{'name':'Sahil','order':list(query_set)})
    return render(request,'hello.html',{'name':'Sahil','orderItem':list(query_set)})
    
    