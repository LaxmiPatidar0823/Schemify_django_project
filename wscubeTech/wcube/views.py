from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from wscubeTech.form import userform
from wcube.models import service
from news.models import News

# Create your views here.
def homepage(request):    
    data = {
        "title" : "Home New",
        "text" : "Hii this is my index.html page",
        'mylist' : ["c++", "python","Java"],
        "number" : [10,20,30,40,68],
        "student_details" : [
            {"name" : "laxmi", 
             "phone_number": 7987965078},
            
            {"name" : "seema", 
             "phone_number": 8224041632}
            
        ]          
    }
    return render(request, "index.html", data)

def about(request):
    return HttpResponse("Heeloo")

def course(request):
    return HttpResponse("<h1>my course</h1>")

'''Dynamic url, int str and slug(- @)   jo value upr url me dalenge vhi value page pr print hogi'''

def courseDetails(request,courseID):
    return HttpResponse(courseID)

def courseDetailstr(request,courseID):
    return HttpResponse(courseID)

def coursewithoutType(request,courseID):
    return HttpResponse(courseID)

def aboutAs(request):
    return render(request, "about.html")

def contactAs(request):
    newsData = News.objects.all()
    data = {
        'newsData' : newsData
    }
    return render(request, "contact.html", data)


def newsDetails(request, newsId):
    newsDetail = News.objects.get(id = newsId)  #get use for single object data ya specific according to id  this is dynamic url
    data = {
        'newsDetails' : newsDetail
    }
    return render(request,'newsDetails.html', data)  #http://127.0.0.1:8000/news/1

def serviceAs(request):
    # serviceData = service.objects.all().order_by('service_title')
    serviceData = service.objects.all().order_by('-service_title') [:3]   ## use - for descending order, [:3]for limit
    # serviceData = service.objects.all()
  
    return render(request, "service.html", {'serviceData':serviceData})

def userformFun(request):
    sum = 0
    data = {}
    try:
        # n = int(request.GET['user'])
        # n1 = int(request.GET['userName'])
        n = int(request.GET.get('user'))
        n1 = int(request.GET.get('userName'))     
        sum = n+n1
        data={
            'n' : n,
            'n1' : n1,
            'output': sum
        }
        # return HttpResponseRedirect('/thankyou')   ...thanku page pr redirect hoga sidhe output value print ni hogi
        url = '/thankyou?output={}'.format(sum)
        # return HttpResponseRedirect(url)
        return redirect(url)     # both redirect and HttpResponseredirect we use to redirect pade
        
    except:
        pass
    # return render(request, "userform.html",{'output' : sum})
    return render(request, "userform.html",data)

def UserDetails(request):
    details = {}
    if request.method == "POST":
     data = request.POST
   
     firstName = data.get('First_Name')
     lastName = data.get('Last_Name')
     output = firstName +" " + lastName
     print(firstName)
     print(lastName)
     details={
        'first' : firstName,
        'last' : lastName,
        'output' : output
     }
    return render(request, "userDetails.html",{'details':details})


def thank(request):
    if request.method == 'GET':
        output = request.GET.get('output')  # uyl me jo key name h voh aayega single quotos ke under
        
    return render(request, 'thankyou.html',{'out' : output })


# action url in form means form ka data us page pr nhi rehke kisi or page pr jata or vha ki url pr submit hota h default me toh parent url  pr submit hota h

# action or userform same h userform redirect hoke thankyou page pr jara but action form pr action me submitform url dali h esliye voh redirect nhi hua or form submit krne pr submitform url pr chl gya  

def action(request):
    sum = 0
    data = {}
    if request.method == "POST":
     
      try:
       
        n = int(request.POST.get('user'))
        n1 = int(request.POST.get('userName'))     
        sum = n+n1
        data={
            'n' : n,
            'n1' : n1,
            'output': sum
        }
        
        url = '/thankyou?output={}'.format(sum)
        return redirect(url)     
        
      except:
        pass
    return render(request, 'actionform.html',data)

def submit(request):
    
     try:
        if request.method == "POST":
            
         n = int(request.POST.get('user'))
         n1 = int(request.POST.get('userName'))     
         sum = n+n1
         data={
            'n' : n,
            'n1' : n1,
            'output': sum
         }
        return HttpResponse(sum)
     except:
        pass


def form_py(request):
    fn = userform
    
    return render(request, 'formpy.html', {'form':fn})

def calculator(request):
    c = ' '
    data = {}
    try:
        if request.method == 'POST':
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            op = request.POST.get('opr')
            
            if op == '+':
                c = n1 + n2
            elif op == '-':
                c = n1 - n2
            elif op == '*':
                c = n1 * n2
            elif op == '/':
                c = n1/ n2
            
            data ={
                "n1" : n1,
                "n2":n2,
                "c" : c
            }
            
    except:
         c = "invalid operator"
    print(c)
   
    return render(request, "calculator.html", data)


def EvenOdd(request):
    c = ' '
#   try: 
    if request.method == 'POST':
        if request.POST.get('num') == '':
            return render(request, 'evenOdd.html',{'error': True})
        
        num = eval(request.POST.get('num'))
        
        if num%2 == 0:
            c = "Num is Even"
            
        else:
            c = "Num is Odd"
            
        print(c)
#   except:
#       c = "invalid"   
    return render(request, "evenOdd.html", {'c' : c})   


def marksheet(request):
    total = 0
    percentage = 0
    Division = ''
    data = {}
    if request.method == 'POST':
        s1 = int(request.POST.get('subject1'))
        s2 = int(request.POST.get('subject2'))
        s3 = int(request.POST.get('subject3'))
        s4 = int(request.POST.get('subject4'))
        s5 = int(request.POST.get('subject5'))
        
        total = s1 + s2 + s3 + s4 + s5
        percentage = total / 5
        
        if percentage >= 90 and percentage < 100:
            Division = 'A+'
        elif percentage < 90 and percentage >= 80:
            Division = 'A'
        elif percentage < 80 and percentage >= 70:
            Division = 'B+'
        elif percentage < 70 and percentage >= 60:
            Division = 'B'
        elif percentage < 60 and percentage >= 50:
            Division = 'c'
        elif percentage < 50 and percentage >= 40:
            Division = 'D'
        else:
            Division = 'E'
            
        data = {
            'total' :  total,
            'percentage' : percentage,
            'Division' : Division
        }    
        
    return render(request, 'marksheet.html', data)



# admin username = laxmi, password = l12345678
# python manage.py changepassword laxmi