from django.shortcuts import render
from . import models
from core import urls
from .models import signup,login,login3,signup2,payment2,payment3


# Create your views here.
def signup1(request):
    return render(request,'page1/signup.html')

def pay1(request):
    return render(request,'page1/pay1.html')

def success(request):
    return render(request,'page1/success.html')

def save1(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        email= request.POST.get('email')
        password=request.POST.get('password')
        total = signup(username=username,email=email,password=password)
        total.save()
    return render(request,'page1/signup.html')

def login1(request):
    return render(request,'page1/signup.html')

def save2(request):
    if request.method == 'POST':
        email = request.POST.get('email1')
        password = request.POST.get('password1')
        total1 = login(email=email,password=password)
        total1.save()
    return render(request,'page1/signup.html')

def login_save3(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        total2 = login3(username = username,password=password)
        total2.save()
    return render(request,'page3/new3.html')

def signin2(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confpassword')
        total = signup2(username=username,email = email,password =password,confirm_password =confirm_password)
        total.save()
    return render(request,'page2/new2.html')

def pay2(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        date = request.POST.get('date')
        cvv = request.POST.get('cvv')
        total2 = payment2(cardholder_name=name,card_number=number,Expiry_date=date, cvv = cvv)
        total2.save()
    return render(request,'page2/pay2.html')

def pay3(request):
    if request.method == "POST":
        print("inj a py3 post------------------------")
        name = request.POST.get('name1')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipcode')
        cardnumber = request.POST.get('cardnumber')
        month = request.POST.get('month')
        cvv = request.POST.get('cvv')
        total3 = payment3(full_name=name,email=email,Address=address,city=city,zip_code=zipcode,cardnumber=cardnumber,Expiry_month=month,cvv=cvv)
        total3.save()
    return render(request,'page3/payment.html')
        


