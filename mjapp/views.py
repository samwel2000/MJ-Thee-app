from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.db.models import Sum

from mjapp.forms import PurchaseForm, ServiceForm, BookingForm, ServiceOfferedForm
from mjapp.models import Purchases, Services, Bookings, ServiceOffered

@login_required
def dashboard(request):
    get_purchase_sum = Purchases.objects.all().aggregate(Sum('amount'))
    get_offered_sum = ServiceOffered.objects.all().aggregate(Sum('amount'))
    profit = None
    loss = None
    if get_purchase_sum and get_offered_sum:
        if get_purchase_sum['amount__sum'] <= get_offered_sum['amount__sum']:
            profit = get_offered_sum['amount__sum'] - get_purchase_sum['amount__sum']
        else:
            loss = get_purchase_sum['amount__sum'] - get_offered_sum['amount__sum']
    elif get_purchase_sum:
        loss = get_purchase_sum['amount__sum']
    elif get_offered_sum:
        profit = get_offered_sum['amount__sum']
    else:
        profit = 0
        loss = None
    template_name = 'mjapp/dashboard.html'
    context = {
        'purchase_total':get_purchase_sum,
        'offered_total':get_offered_sum,
        'profit':profit,
        'loss':loss,
    }
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
def editService(request, id):
    get_service = Services.objects.get(pk=id)
    form = ServiceForm(instance=get_service)
    if request.method=='POST':
        form = ServiceForm(request.POST, instance=get_service)
        if form.is_valid():
            form.save()
            messages.success( request, f'Query ok beautiful, service updated succesifully')
            return redirect('service')
    get_services = Services.objects.all().order_by('-date')
    template_name = 'mjapp/service.html'
    context = {
        'form':form,
        'update':'update',
        'services':get_services,
    }
    return render(request, template_name, context)

@login_required
def deleteService(request, id):
    get_service = Services.objects.get(pk=id)
    try:
        get_service.delete()
        messages.info(request, f'Service deleted succesifully girl')
    except:
        messages.error(request, f'You can not delete this service girl !! there are customers you served with this service')
    return redirect('service')

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
def editBooking(request, id):
    get_booking = Bookings.objects.get(pk=id)
    form = BookingForm(instance=get_booking)
    if request.method=='POST':
        form = BookingForm(request.POST, instance=get_booking)
        if form.is_valid():
            form.save()
            messages.success( request, f'Query ok beautiful, booking updated succesifully')
            return redirect('booking')
    get_bookings = Bookings.objects.all().order_by('-date')
    template_name = 'mjapp/booking.html'
    context = {
        'form':form,
        'update':'update',
        'bookings':get_bookings,
    }
    return render(request, template_name, context)

@login_required
def cancelBooking(request, id):
    get_booking = Bookings.objects.get(pk=id)
    get_booking.delete()
    messages.info(request, f'Service booking deleted succesifully')
    return redirect('booking')

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
