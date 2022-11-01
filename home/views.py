from django.shortcuts import render, redirect
from home.models import course, faculty
from home.forms import courseForms

# Create your views here.
def home(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')

def faculty(request):
    try:
        data = faculty().objects.all()
        context = {"faculty": data}
    except Exception as e:
        context = {"faculty": "Data Not Found"}
    return render(request, 'faculty.html', context)

def course(request):
    try:
        data = course().objects.all()
        context = {"Courses":data}
    except Exception as e:
        context = {"Courses":"Data Not Found"}
    return render(request, 'course.html', context)

def course_details(request, hm):
    fetch_data = course().objects.get(course_specialisation=hm)
    context = {"fetch_data":fetch_data}
    return render(request, 'course_details.html', context)

def courseAdd(request):
    form = courseForms()
    if request.method == 'POST':
        myData = courseForms(request.POST)
        if myData.is_valid():
            myData.save()
            return redirect('course')
    context = {"form":form}
    return render(request, 'course_add.html', context)


def notice(request):
    return render(request, 'notice.html')