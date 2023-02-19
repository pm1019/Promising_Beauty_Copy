from django.shortcuts import render

# Create your views here.
def payment(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        country=request.POST['country']
        addressline1=request.POST['addressLine1']
        addressLine2=request.POST['addressLine2']
        city=request.POST['city']
        satate=request.POST['state']
        zipcode=request.POST['zipcode']
        phone=request.POST['phone']
        email=request.POST['email']
        typeupi=request.POST['typeupi']
        upiID=request.POST['upiid']
        typeCreditCard=request.POST['typeCreditCard']
        cc_name=request.POST['cc_name']
        cc_num=request.POST['cc_num']
        cc_Exdate=request.POST['cc_Exdate']
        typeDebitCard=request.POST['typeDebitCard']
        dc_name=request.POST['dc_name']
        dc_num=request.POST['dc_num']
        dc_Exdate=request.POST['dc_Exdate']

        payment=Pay_details()