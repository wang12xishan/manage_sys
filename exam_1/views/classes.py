from django.shortcuts import render
from django.shortcuts import redirect
from exam_1 import models

def get_classes(request):
    cla_list = models.Classes.objects.all()
    return render(request,"get_classes.html",{"cla_list":cla_list})


def add_classes(request):
    if request.method == "GET":
        return render(request,"add_classes.html")
    if request.method == "POST":
        name = request.POST.get("name")
        models.Classes.objects.create(name = name)
        return redirect("/classes.html")

def del_classes(request):
    nid = request.GET.get("nid")
    models.Classes.objects.filter(id = nid).delete()
    return redirect("/classes.html")
def edit_classes(request):
    if request.method == "GET":
        nid = request.GET.get("nid")
        cla_obj = models.Classes.objects.filter(id = nid).first()
        return render(request,"edit_classes.html",{"cla_obj":cla_obj})
    if request.method =="POST":
        nid = request.GET.get("nid")
        name = request.POST.get("name")
        models.Classes.objects.filter(id=nid).update(name = name)

    return redirect("/classes.html")