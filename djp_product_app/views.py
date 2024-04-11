from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .form import MovieForm
# Create your views here.
def home(request):
    movie = Movie.objects.all()
    context = {
        'movie_list':movie
    }
    return render(request,"index.html",context)

def movie_detail(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':movie})


def movie_add(request):
    if request.method=='POST':
        name= request.POST['name']
        desc = request.POST['desc']
        img= request.FILES['img']
        year=request.POST['year']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect("/")

    return render(request,"add.html")

def movie_update(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect("/")
    else:
        return render(request,"update.html",{'form':form,'movie':movie})


def movie_delete(request,movie_id):
    if request.method=="POST":
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect("/")
    return render(request,"delete.html")