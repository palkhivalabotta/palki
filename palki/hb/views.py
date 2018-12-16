from django.shortcuts import render
from .models import UserRegister
from .models import Contact
from .models import payment
from .models import Cancel
# Create your views here.
def openHomePage(request):
    type="Home"
    return render(request,'index.html',{"type":type})


def openServices(request):
    type=request.GET.get("type")
    return render(request,'index.html',{"type":type})


def openUser(request):
    type=request.GET.get("type")
    return render(request,'index.html',{"type":type})


def loginUser(request):
    username = request.POST.get("email")
    password = request.POST.get("pass")
    res = UserRegister.objects.filter(email_id=username, password=password)
    # print(res)
    if not res:
        return render(request, 'index.html', {"type": 'h_user', "message": "Invalid User"})
    else:
        for x in res:
            print(x)
        return render(request, 'index2.html', {"type": type, "name": x})

def openSignUpPage(request):
    type = request.GET.get("type")
    return render(request, 'index.html', {"type": type})


def registerUser(request):
    u_fname = request.POST.get('u_fname')
    u_lname = request.POST.get('u_lname')
    u_email = request.POST.get('u_email')
    u_pass = request.POST.get('u_pass')
    u_rpass = request.POST.get('u_rpass')
    u_cno = request.POST.get('u_cno')
    u_add = request.POST.get('u_add')
    # print(u_fname,u_lname,u_email,u_pass,u_cno,u_add)
    ur = UserRegister(fname=u_fname, lname=u_lname, email_id=u_email, password=u_pass, rpassword=u_rpass,
                      contact_no=u_cno, address=u_add)
    ur.save()
    return render(request, 'index.html', {"type": "h_user", "message": "User Register Successfully"})

def openContact(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})

def ContactPage(request):
    u_name=request.POST.get('u_name')
    u_email=request.POST.get('u_email')
    u_phone=request.POST.get('u_phone')
    u_mess=request.POST.get('u_mess')
    #print(u_name,u_email,u_phone,u_phone,u_mess)
    uc=Contact(name=u_name,Email_id=u_email,phone_no=u_phone,message=u_mess)
    uc.save()

    return render(request,'index.html',{"type":'contact',"message":'Successfully message sent'})
#====================================================================================================================

def openUserHomePage(request):
    type="home"
    return render(request, 'index2.html', {"type":type})


def openBookingPage(request):
    type=request.GET.get("type")
    return render(request,'index2.html',{"type":type})


def openPayment(request):
    type=request.GET.get("type")
    return render(request,'index2.html',{"type":type})


def opendisplay(request):
    type=request.GET.get("type")
    return render(request,'index2.html',{"type":type})
#=====================================================================================

def openCancelPage(request):
    type=request.GET.get("type")
    return render(request,'index2.html',{"type":type})


def CancelPage(request):
    u_name = request.POST.get('u_name')
    room_no=request.POST.get('room_no')
    cust_id=request.POST.get('cust_id')
    uc=Cancel(Uname=u_name,Room_no=room_no,Cust_id=cust_id)
    uc.save()
    return render(request,'index2.html',{"type":'u_cancel',"message":'Successfully Your Room Will Be Cancelled'})


def paymentpage(request):
    name=request.POST.get('name')
    room_type=request.POST.get('room_type')
    check_in=request.POST.get('check_in')
    check_out=request.POST.get('check_out')
    contact_no=request.POST.get('contact_no')
    address=request.POST.get('address')
    total_amount=request.POST.get('total_amount')
    card_no=request.POST.get('card_no')
    card_type=request.POST.get('card_type')
    p=payment(Fullname=name,Room_type=room_type,Check_in=check_in,Check_out=check_out,Contact_no=contact_no,Address=address,Total_amount=total_amount,Card_no=card_no,Card_type=card_type)
    p.save()
    return render(request,'index2.html',{"type":'payment',"message":'Your Payment is Success'})


def display(request):
    recs=payment.objects.all()
    return render(request,'index2.html',{"type":type,"records":recs})