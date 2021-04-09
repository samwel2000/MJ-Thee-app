from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from mjapp.forms import PurchaseForm, ServiceForm, BookingForm, ServiceOfferedForm
from mjapp.models import Purchases, Services, Bookings, ServiceOffered

@login_required
def index(request):
    template_name = 'mjapp/home.html'
    context = {}
    return render(request, template_name, context)

@login_required
def dashboard(request):
    template_name = 'mjapp/dashboard.html'
    context = {}
    return render(request, template_name, context)

@login_required
def purchase(request):
    form = PurchaseForm()
    if request.method=='POST':
        form = PurchaseForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success( request, f'Query ok beautiful, purchase saved succesifully')
            return redirect('purchase')
    get_purchases = Purchases.objects.all().order_by('-date')
    template_name = 'mjapp/purchase.html'
    context = {
        'form':form,
        'purchases':get_purchases,
    }
    return render(request, template_name, context)

@login_required
def service(request):
    form = ServiceForm()
    if request.method=='POST':
        form = ServiceForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, f'Query ok beautiful, service saved succesifully')
            return redirect('service')
    get_services = Services.objects.all().order_by('-date')
    template_name = 'mjapp/service.html'
    context = {
        'form':form,
        'services':get_services,
    }
    return render(request, template_name, context)

@login_required
def booking(request):
    form = BookingForm()
    if request.method=='POST':
        form = BookingForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success( request, f'Query ok beautiful, booking added succesifully')
            return redirect('booking')
    get_bookings = Bookings.objects.all().order_by('-date')
    template_name = 'mjapp/booking.html'
    context = {
        'form':form,
        'bookings':get_bookings,
    }
    return render(request, template_name, context)

@login_required
def markComplete(request, id):
    Bookings.objects.filter(pk=id).update(
        status = True
    )
    messages.success(request, f'Service booking marked as complete succesifully')
    return redirect('booking')

@login_required
def serviceOffered(request):
    form = ServiceOfferedForm()
    if request.method=='POST':
        form = ServiceOfferedForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success( request, f'Query ok beautiful, service offered added succesifully')
            return redirect('serviceOffered')
    get_offered = ServiceOffered.objects.all().order_by('-date')
    template_name = 'mjapp/offered.html'
    context = {
        'form':form,
        'offered':get_offered,
    }
    return render(request, template_name, context)

@login_required
def markPayed(request, id):
    ServiceOffered.objects.filter(pk=id).update(
        payment = True
    )
    messages.success(request, f'Service offered marked as payed succesifully')
    return redirect('serviceOffered')
