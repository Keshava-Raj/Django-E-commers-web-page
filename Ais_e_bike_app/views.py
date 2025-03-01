from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import Register_form ,Addvaickal,vaik_taking_user,Provider_register
from django.contrib import messages
from .login import customusercreationform

from django.contrib.auth import authenticate , login,logout
from django.contrib.auth.decorators import login_required





 

def basefile(request):
    return render(request, "sbasefile.html")    


def home(request):
    return render(request, "home.html") 

def Aboutus(request):
    
    return render(request, "About us.html")

def contact1(request):
    
    return render(request, "contact Us.html")

def users_register(request):

        return render(request,'test file.html')
    
def dashboard(request):
    # Logic for dashboard view
    return render(request, 'user dashbord.html')

def users_register(request):
    if request.method == 'GET':
        return render(request,"test file.html") 
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['mobile']
        age = request.POST['age']
        password = request.POST['paswd']
        confirm_password = request.POST['paswd1']
        
        if Register_form.objects.filter(email=email):
            messages.error(request ,"This email id is already exist try anather email id")
            return redirect("register")
        if Register_form.objects.filter(mobile=phone):
            messages.error(request ,"This Phone number is already exist try anather Phone number")
            return redirect("register")
            
        if password != confirm_password:
            messages.error(request ,"Password doe'nt match")
            return redirect("register")
        
        myuser = Register_form.objects.create(
                name=name,
                email=email,
                mobile=phone,
                age=age,
                passewrd=password,
                passewrd1 = confirm_password
        ).save()
        
        messages.success(request,'your Account is succssefully Created')
    
    return redirect( "userlogin" )


#from django.contrib.auth.hashers import make_password, check_password

def user_login(request):
    if request.method == 'GET':
        
        return render(request, 'loginpage.html' )

    if request.method == 'POST': 
        email_id = request.POST['email']
        password = request.POST['paswd']
        
        
        if Register_form.objects.filter(email=email_id) and Register_form.objects.filter(passewrd=password):

            rie = Register_form.objects.all()
            messages.success( request, "your succssessfully Login in Your Account")
            
            return redirect("dashboard")
        else:
            messages.error( request, "you enterd bad credentials")
            return redirect("userlogin")
    return render(request, 'user dashbord.html', {'fname':rie})

def provider_Login(request): 

    if request.method == 'POST': 
        email_id = request.POST['Email_id']
        password_p = request.POST['PPassword']
        user = authenticate(request, email=email_id, password=password_p)
        if user is not None:
        #if Provider_register.objects.filter(email=email_id) and Provider_register.objects.filter(password=password_p ):
            login(request, user)
            book = Provider_register.objects.get(email=email_id)
            messages.success(request,"You have successfully logged in Your Account")
            return redirect("sucssessfulllogin")
            
        else:
            messages.error( request, "Invalid Username Or Password")
            return redirect("ProviderLogin")
    context = {
        'hidde': True,  # Navigation will be hidden
    }
    return render(request, 'providerLogin.html',context )


def provider_register(request):
    if request.method == 'POST':
        form = customusercreationform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'your Vaickel Provider Account as been succssefully Created')
            return redirect("sucssessfulllogin") # Redirect to the login page after registration")
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = customusercreationform()
    return render(request, 'provider register.html', {'form': form})


@login_required
def provider_dashboard(request):

    current_user = request.user

    return render(request, "provider dashaboard.html", {'provider':current_user})
    

def logout_view(request):
    logout(request)
    return redirect('home')


def providtexter_addvaickal(request):    
    
    if request.method == 'GET':
        return render(request,"Add vaivkal.html")
    
    if request.method == 'POST':
        valname = request.POST['valname']
        valnumb = request.POST['vaickelnumb']
        val_cost_per_day = request.POST['costperday']
        val_cost_per_hr = request.POST['costperhr']
        valrc = request.FILES['vaiRC']
        valimage = request.FILES['VaImage']
 
        myuser = Addvaickal.objects.create(
            Vai_name  = valname,
            RC = valrc,
            cost =  val_cost_per_day,
            vai_number =valnumb,
            cost_per_hr = val_cost_per_hr,
            image = valimage
        ).save()
        return redirect("textfile")


@login_required
def providtexter_Login(request):
    rows = Addvaickal.objects.all()
    return render(request, "textfilesdcddd.html", {'names':rows})

def bookvaickel(request):
    
    if request.method == 'GET':
        return render(request,"bookvacel.html") 
    if request.method == 'POST':
        bookname = request.POST['bname']
        bphone = request.POST['bphone']
        license = request.POST["blicence"]
        bookimage = request.POST["BImage"]            #here have one Error fixed

        fromtime = request.POST['fromtime']
        totime = request.POST['totime']


        
        vackeltaker = vaik_taking_user.objects.create(
        name = bookname,
        Phone_valid = bphone,
        licence = license, 
        taker_img = bookimage ,
        time_to_take_days = fromtime,  
        time_in_hr = totime ,
        ).save()
        return redirect("orderbooked")


def ridersuccess(request):
    return render(request, 'order sucssess.html')


'''
def User_Register(request):
    if request.method == 'GET':
        return render(request,"provider register.html") 
    if request.method == 'POST':
        namep = request.POST['name2']
        username = request.POST['username']
        email = request.POST['email2'] 
        passsword  = request.POST['password']

        user = User.objects.create_user(
            first_name = namep,
            username = username,
            email = email,
            password = passsword,
        ).save()
        messages.success(request,'your Account is succssefully Created')
        return redirect("providerdashboard")
    
    '''
