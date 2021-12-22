from django.shortcuts import render, redirect
from base_app.models import ModelFormRegistration
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator


def is_manager(user):
    return  user.groups.filter(name='manager').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservations_list(request):
    registrations = ModelFormRegistration.objects.filter(is_processed=False).order_by('date')

    paginator = Paginator(registrations, 5)
    page = request.GET.get('page')
    registrations = paginator.get_page(page)

    return render(request, 'reservations_list.html', context={'reg_list': registrations})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    ModelFormRegistration.objects.filter(pk=pk).update(is_processed=True)
    return redirect('reservations_list')

