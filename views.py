from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .models import Register






class Registerusers(CreateView):
    model = Register

    def get(self, request):
        return render(request, 'testproject/demofile.html')

    def post(self, request):
        name = request.POST['uname']
        mobilenumber = request.POST['phonenumber']
        postalcode = request.POST['postalcode']
        email = request.POST['email']
        register = Register(name=name, email=email, mobilenumber=mobilenumber, postalcode=postalcode)
        register.save()
        return redirect('register')





class Viewusers(CreateView):
    model = Register

    def get(self, request):
        return render(request, 'testproject/demofileview.html')

class Updateusers(CreateView):
    model = Register

    def get(self, request):
        return render(request, 'testproject/demofileupdate.html')

    def post(self,request):
        id = request.POST['userid']
        name = request.POST['uname']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        postalcode = request.POST['postalcode']
        Register.objects.filter(id=id).update(name=name, email=email, mobilenumber=phonenumber, postalcode=postalcode)
        return redirect('viewusers')



def deleteuser(request):
    print('entered')
    id = request.GET['id']
    print('id',id)

    Register.objects.filter(id=id).delete()
    return JsonResponse('success',safe=False)















