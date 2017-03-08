from django.shortcuts import render
from django.shortcuts import redirect
# from exam_1 import  models
from exam_1.models import *

def get_teachers(request):
    te_list = Teachers.objects.all()

    return render( request,"get_teachers.html",{ "te_list":te_list})

def add_teachers(request):
    if request.method == "GET":
        cla_list = Classes.objects.all()
        return render(request,"add_teachers.html",{ "cla_list":cla_list })
    if request.method == "POST":
        name = request.POST.get("name")
        cla_list = request.POST.getlist("cla_list")
        # print("+++++++++++",cla_list,type(cla_list))
        Teachers.objects.create(name=name)
        te_obj = Teachers.objects.filter(name = name).first()
        te_obj.classes_set.set(cla_list)
        #
        # cla_obj = Classes.objects.filter(teachers__name = name)
        # print(cla_obj)
        # # cla_obj.m.add(cla_list)
        return redirect("/teachers.html")

def del_teachers(request):
     nid =request.GET.get("nid")
     te_obj = Teachers.objects.get(id = nid)
     te_obj.classes_set.remove()
     te_obj.delete()
     return redirect("/teachers.html")



def edit_teachers(request):
    if request.method=="GET":
        nid =request.GET.get("nid")
        te_obj = Teachers.objects.filter(id = nid).first()
        l = []
        for i in te_obj.classes_set.all():
            l.append(i.id)
        cla_list = Classes.objects.all()
        return render(request,"edit_teachers.html",{"te_obj":te_obj,"cla_list":cla_list,"l":l })
    if request.method=="POST":
        nid = request.GET.get("nid")
        name = request.POST.get("name")
        cla_id = request.POST.getlist("cla_id")
        Teachers.objects.filter(id=nid).update(name =name)
        te_obj = Teachers.objects.filter(id=nid).first()
        te_obj.classes_set.set(cla_id)
        return redirect("/teachers.html")