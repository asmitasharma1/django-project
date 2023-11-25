from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm 
from .models import PoliceOfficer, Profile, Complaint
from django.contrib.auth import get_user_model
from myApp.models import Complaint

from django.contrib.auth.hashers import make_password

password = make_password('user_password')

from django.http import Http404
from django.template import TemplateDoesNotExist


def html_page(request, page):
    try:
        return render(request, f'myApp/{page}.html')
    except TemplateDoesNotExist:
        raise Http404

def about(request):
    return render(request, 'myApp/about.html')

def adminlogin(request):
    return render(request, 'myApp/adminlogin.html')
User = get_user_model()
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        age = request.POST['age']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']

    
        if User.objects.filter(username=username).exists():
            return render(request, 'myApp/signup.html', {'error_message': 'Username already exists. Please choose a different one.'})

      
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

       
        profile = Profile(user=user, age=age, address=address, phone=phone)
        profile.save()
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if login(request, user):
                print("User is successfully authenticated and logged in.")
               
                return redirect('home')
            else:
                print("Login failed.")
        else:
            print("Authentication failed.")
        
        return redirect('home')  
    return render(request, 'myApp/signup.html')



def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email').lower() 
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'myApp/userlogin.html', {'error_message': 'User does not exist.'})

        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            
            return render(request, 'myApp/userlogin.html', {'error_message': 'Invalid credentials. Please try again.'})
    return render(request, 'myApp/userlogin.html')

def policelogin(request):
    if request.method == 'POST':
        email = request.POST.get('email').lower() 
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            policeofficer = PoliceOfficer.objects.get(user=user)
        except User.DoesNotExist:
            print("User with email {} does not exist.".format(email))
            user = None
            policeofficer = None
        except PoliceOfficer.DoesNotExist:
            print("PoliceOfficer for user {} does not exist.".format(email))
            user = None
            policeofficer = None

        if user is not None and user.check_password(password) and policeofficer is not None:
            login(request, user)
            return redirect('policedashboard')  
        else:
            error_message = "Invalid email or password for police login. Please try again."
            return render(request, 'myApp/policelogin.html', {'error_message': error_message})

    return render(request, 'myApp/policelogin.html')


   
@login_required
def home(request):
    try:
        user_profile = request.user.profile 
    except Profile.DoesNotExist:
        user_profile = None
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'myApp/home.html', context)

def report(request):
    return render(request, 'myApp/report.html')

def complaintsuccess(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            
            form.save()
           
            return redirect('complaintsuccess')  
    else:
        form = ComplaintForm()  

    return render(request, 'myApp/complaintsuccess.html', {'form': form})

def mycomplaints(request):
    email = request.user.email
    complaints = Complaint.objects.filter(email=email)
    
    return render(request, 'myApp/mycomplaints.html', {'complaints': complaints})

@login_required
def policedashboard(request):
    total_complaints = Complaint.objects.count()
    solved_complaints = Complaint.objects.filter(is_solved=True).count()
    active_complaints = Complaint.objects.filter(is_solved=False).count()

    active_complaint_data = Complaint.objects.filter(is_solved=False)  

    return render(request, 'myApp/policedashboard.html', {
        'total_complaints': total_complaints,
        'solved_complaints': solved_complaints,
        'active_complaints': active_complaints,
        'active_complaint_data': active_complaint_data,
    })

def userlogout(request):
    logout(request)
    return render(request, 'myApp/logout.html')


def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, 'myApp/complaint_list.html', {'complaints': complaints})    

def policereport(request):
    complaints = Complaint.objects.all() 
    return render(request, 'myApp/policereport.html', {'complaints': complaints})

def mark_complaint_as_solved(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    complaint.is_solved = True
    complaint.save()
    return redirect('policereport')

from django.contrib.auth import logout
from django.shortcuts import redirect

def policelogout(request):
    logout(request)
    return render(request, 'myApp/policelogout.html')






