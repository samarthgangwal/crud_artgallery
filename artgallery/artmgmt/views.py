from django.shortcuts import render, redirect 
from artmgmt.forms import SellerForm  
from artmgmt.models import Seller 

# Create your views here.
  
def emp(request):  
    if request.method == "POST":  
        form = SellerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = SellerForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    sellers = Seller.objects.all()  
    return render(request,"show.html",{'sellers':sellers})  
def edit(request, id):  
    seller = Seller.objects.get(id=id)  
    return render(request,'edit.html', {'seller':seller})  
def update(request, id):  
    seller = Seller.objects.get(id=id)  
    form = SellerForm(request.POST, instance = seller)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'seller': seller})  
def destroy(request, id):  
    seller = Seller.objects.get(id=id)  
    seller.delete()  
    return redirect("/show")  



