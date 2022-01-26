from django.shortcuts import render
from .models import PaymentInfo
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# views are here.


@login_required(login_url='adminlogin/')
def index(request):
    if request.method == "POST":
        data = dict(request.POST)
    #     print(data)
        PaymentInfo(
            username=data['username'][0],
            mobile=data['mobile'][0],
            aadhar=data['aadhar'][0],
            payment=data['payment'][0],
            address=data['address'][0],
        ).save()
        messages.success(
            request, f"{ data['username'][0]}'s Payment Added Successfully .")
    return render(request, 'index.html')
