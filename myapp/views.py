from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from myapp.models import *
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request, 'index.html')

def registerPage(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "Username  Already Taken")
            return redirect('/register')
        
        user = User.objects.create(
         first_name = firstname,
         last_name = lastname,
         username = username
         )
        user.set_password(password)  #password - incript
        user.save()
        messages.info(request, "Account Created Successfully")
        return redirect('/register')
    return render(request, 'register.html')

    
def loginPage(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/login')
        
        user = authenticate(username = username , password = password)
      
        if user is None:
           messages.error(request, "Invalid password")
           return redirect('/login')
      
        else:
           login(request , user)
           return redirect('/form')
        
    return render(request, 'login.html')

def formPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        age = request.POST.get('age')
        caste = request.POST.get('caste')
        state = request.POST.get('state')
        annualIncome = request.POST.get('annual-income')
        profession = request.POST.get('proffession')
        gender = request.POST.get('gender')
        
        user = Userdata.objects.create(
            user_name = username,
            user_age = age,
            user_category = caste,
            user_state = state,
            user_annualincome = annualIncome,
            user_profession = profession,
            user_gender = gender
        )
        
        eligible_schemes = SchemeData.objects.filter(Q(Q(scheme_caste__icontains=user.user_category) | Q(scheme_caste='All')) &
                                                     Q(scheme_annualIncome__gte = user.user_annualincome) & 
                                                     Q(Q(scheme_gender=user.user_gender) | Q(scheme_gender = 'All')) & 
                                                     Q(Q(scheme_age__gte=user.user_age) & Q(scheme_Minage__lte=user.user_age)) &
                                                     Q(Q(scheme_education_level=user.user_profession) | Q(scheme_education_level = 'All')))
        
        print(eligible_schemes) 
        return render(request,'eligibleSchemes.html' ,{'eligible_schemes' : eligible_schemes,'userdata':user})
        
    return render(request, 'form.html')


def viewSchemes(request):
    
    schemes =  SchemeData.objects.all()
    
    if request.POST.get('search'):
        schemes = schemes.filter(scheme_name__icontains = request.POST.get('search'))
        
    context = {
        'schemes':schemes
    }
    return render(request, 'view_schemes.html',context)


def SchemeDetails(request, schemeID):
    scheme = SchemeData.objects.get(id = schemeID)
    data = {
        'schemeDetails' : scheme
    }
    return render(request, 'SchemeDetails.html', data)

