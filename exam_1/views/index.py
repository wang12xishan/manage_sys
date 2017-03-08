from django.shortcuts import redirect,render



def index(request):
    if request.method =="GET":
        return render(request,"index.html")
    if request.method == "POST":
        return redirect("index.html")