from django.shortcuts import render
from django.shortcuts import render, redirect 
from .models import Post, CV
from .forms import send_cv

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
def gallery(request):
    return render(request, 'gallery.html')

def news(request): 
    posts = Post.objects.all()
    return render(request, 'news.html', {'posts':posts})

def cv(request):
    return render(request, 'cv.html',)


def add_cv(request):

    if request.method == "POST":
        form = send_cv(request.POST, request.FILES)

        if form.is_valid():
            cv = form.save(commit=False)
            cv.name = form.cleaned_data['name']
            cv.email = form.cleaned_data['email']
            cv.image = form.cleaned_data['image']
            

            cv.save()

            form.save_m2m()
           
            return redirect('home')

    else:
        form = send_cv()
   
    return render(request, 'cv.html', {'form':form})
