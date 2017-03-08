from django.shortcuts import render
from django.shortcuts import redirect
from exam_1 import models



def get_students(request):
    stu_list = models.Students.objects.all()

    return render(request,"get_students.html",{"stu_list":stu_list})

def add_students(request):
    if request.method == "GET":
        cs_obj = models.Classes.objects.all()
        return render(request,"add_students.html",{ "cs_obj":cs_obj })
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        cs = request.POST.get("cs")
        models.Students.objects.create(name=name,age =age,gender= gender,cs_id=cs)
        return redirect("students.html")

def del_students(request):
    nid = request.GET.get("nid")
    models.Students.objects.filter(id=nid).delete()
    return redirect("students.html")
def edit_students(request):
    if  request.method=="GET":
        nid = request.GET.get("nid")
        stu_obj = models.Students.objects.filter(id = nid).first()
        cs_list = models.Classes.objects.all()
        return render(request,"edit_students.html",{"stu_obj":stu_obj,"cs_list":cs_list})
    if  request.method=="POST":
        nid = request.GET.get("nid")
        name = request.POST.get("name",None)
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        cs = request.POST.get("cs")
        models.Students.objects.filter(id=nid).update(name=name,age=age,gender=gender,cs_id=cs)
        return redirect("students.html")