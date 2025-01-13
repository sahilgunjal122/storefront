from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models import Q,F
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
    # query_set=OrderItem.objects.filter(product__collection__id=3)


    #-------------Complex Lookups Using Q Objects------------

    #Products: inventroy < 10 AND unit_price < 20
    #Using two queries :
    # query_set=Product.objects.filter(inventory__lt=10,unit_price__gt=20)
    #Using Double Filter method :
    # query_set=Product.objects.filter(inventory__lt=10).filter(unit_price__gt=20)
    
    #Products : inventory < 10 OR unit_price < 20
    #Using Q Objects :
    #query_set=Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # query_set=Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))



    #-------------Referencing Fileds using F Objects----------
    #Products : inventory = unit_price
    # query_set=Product.objects.filter(inventory=F('collection_id'))




    #------------Sorting--------------
    #The Products are sorted by titile in Acending Order
    # query_set=Product.objects.order_by('title')

    #To define decending order minus(-) sign is used
    # query_set=Product.objects.order_by('unit_price','-title').reverse()

    #Using Filter method :
    # query_set=Product.objects.filter(collection__id=1).order_by('unit_price')


    #Use of Earliest Method :(does not return query set so give error have to change in the html)
    # query_set=Product.objects.order_by('unit_price')[0]
    # query_set=Product.objects.earliest('unit_price')
    # query_set=Product.objects.latest('unit_price')



    #-------------Limiting Results-------------
    #To Limit the Results the slicing will be done
    #So the Result will be 0, 1, 2, 3, 4
    # query_set=Product.objects.all()[0:5]


    #------------Selecting Fileds to Query------------
    #Values Method : ( It Gives the Values as mentioned )
    # query_set=Product.objects.values('id','title','collection__title')

    #values_list : ( The Values will be in the Tuple )
    # query_set=Product.objects.values_list('id','title','collection__title')


    # Question :Select products that have been ordered and sort them by title 
    query_set=Product.objects.filter(id__in=OrderItem.objects.values('product__id').distinct()).order_by('title')









    return render(request,'hello.html',{'name':'Sahil','products':list(query_set)})
    # return render(request,'hello.html',{'name':'Sahil','customers':list(query_set)})
    # return render(request,'hello.html',{'name':'Sahil','collections':list(query_set)})
    # return render(request,'hello.html',{'name':'Sahil','order':list(query_set)})
    # return render(request,'hello.html',{'name':'Sahil','orderItem':list(query_set)})
    
    