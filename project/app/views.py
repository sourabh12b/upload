from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
import razorpay
from django.contrib.auth.models import User
from auth1.forms import *
from .managers import Mymanager
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt

def home(req):
    cart=req.session.get('cart')
    if cart==None:
        req.session['cart']={}
    queryset=earbud.objects.all()
    if req.GET.get('search'):
        queryset=queryset.filter(name__icontains=req.GET.get('search'))
        context={'data':queryset}
        return render(req,'app/display.html',context)
    return render(req,"app/index.html")


def shop(req):
    if req.method=="POST" and req.POST.get('max') and req.POST.get('min'):
        mini=int(req.POST.get('min'))
        maxi=int(req.POST.get('max'))
        data=earbud.products.get_product(mini,maxi)
        return render(req,"app/shop.html",{'data':data})
    data = earbud.objects.all()
    paginator=Paginator(data,3)
    page_number=req.GET.get('page')
    data=paginator.get_page(page_number)
    if req.method=="POST":
        stock=int(req.POST.get('instock'))
        required=int(req.POST.get('req_quan'))
        id=int(req.POST.get('idproduct'))
        # print(type(stock))
        # print(required)
        if required > stock:
            return render(req,"app/shop.html",{'data':data,'msg':'inappropriate choice','id':id})
        cat_id="airdopes"+str(id)
        cart=req.session.get('cart') #local variable
        old=cart.get(cat_id)
        if old:
            cart[cat_id]=required+old
        else:
            cart[cat_id]=required
        req.session['cart']=cart #ssign new value
        cart=req.session.get('cart')
        # print(cart)
    
    return render(req,"app/shop.html",{'data':data})




def cart(request):
    global GT           
    data = request.session.get('cart')
    list_final = []
    GT = 0
    for i, j in data.items():
        if "airdopes" in i:
            id = int(i[8:])
            d1 = earbud.objects.get(pk=id)
            price = d1.price
            total = j * price
            lis = [d1, j, total]
            list_final.append(lis)
            GT += total
    return render(request, 'app/mycart.html', {'list_final': list_final, 'GT': GT})



def contact1(request):
    context={}
    if request.method=="POST":
        nm=request.POST.get('my-name')
        em=request.POST.get('my-email')
        ms=request.POST.get('my-message')
        data=contact(name=nm, email=em, message=ms)
        msg='thank you for contacting us you will recieve a reply soon'
        context={'msg':msg}
        data.save()
    return render(request,"app/contact.html",context)


def display(req):
    if req.method=="POST":
        stock=int(req.POST.get('instock'))
        required=int(req.POST.get('req_quan'))
        id=int(req.POST.get('idproduct'))
        # print(type(stock))
        # print(required)
        if required > stock:
            data = earbud.objects.all()
            return render(req,"app/display.html",{'data':data,'msg':'inappropriate choice','id':id})
        cat_id="airdopes"+str(id)
        cart=req.session.get('cart') #local variable
        old=cart.get(cat_id)
        if old:
            cart[cat_id]=required+old
        else:
            cart[cat_id]=required
        req.session['cart']=cart #ssign new value
        cart=req.session.get('cart')
        # print(cart) 
        data = earbud.objects.all() 
    return render(req,"app/display.html",{'data':data})


@csrf_exempt       
def make_payment(request):
        if request.method=="POST":
            print(GT)
            name = request.user
            print(name) 
            amount = GT * 100
            client = razorpay.Client(auth=("rzp_test_gUestVh0McVPA7" , "cUTNYj336yZ5aGgKdUpOsPUu" ))
            response_payment = client.order.create({'amount':amount, 'currency':'INR',
                                'payment_capture':'1' }) 
            print(response_payment)
            order_status = response_payment['status']
            order_id = response_payment['id']
            print(order_id)
            if order_status=='created':
                product = ItemModel(amount =amount , order_id = response_payment['id'],)
                product.save()
                return render(request,'app/mycart.html',{'payment':response_payment})
        if request.user.is_authenticated:
            user=request.user
            data=request.session.get('cart')
            print(data)
            for i,j in data.items():
                if 'airdopes' in i:
                    cat='airdopes'
                    id=int(i[8:])
                    quan=j
                    ins=transaction(user=user,cat=cat,cat_id=id,purchased_quan=quan)
                    ins.save()  
                                   
                request.session['cart']={}
                return redirect('mycart')
            
            else:
                return redirect('log')
            



@csrf_exempt
def payment_status(request):
    # print(request.POST)
    if request.method=='POST':
        response = request.POST
        # print(response)
        params_dict = {
            'razorpay_order_id': response['razorpay_order_id'],
            'razorpay_payment_id': response['razorpay_payment_id'],
            'razorpay_signature': response['razorpay_signature']
        }

        # client instance
        client = razorpay.Client(auth=("rzp_test_gUestVh0McVPA7" , "cUTNYj336yZ5aGgKdUpOsPUu" ))

        try:
            status = client.utility.verify_payment_signature(params_dict)
            item = ItemModel.objects.get(order_id=response['razorpay_order_id'])
            item.razorpay_payment_id = response['razorpay_payment_id']
            item.paid = True
            item.save()
            return render(request, 'app/payment_status.html', {'status': True})
        except:
            return render(request, 'app/payment_status.html', {'status': False})
    return render(request, 'app/payment_status.html')

    
# # admin







# Create your views here.
