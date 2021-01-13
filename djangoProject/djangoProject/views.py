from django.shortcuts import render, redirect
from djangoProject.forms import IssueForm
from django.core.mail import send_mail
from django.contrib import messages
from djangoProject.settings import ISSUE_MAIL


# hander functions for errors
def handler404(request, exception):
    context = {
        'error_no': 404,
        'error_detail': 'Page Not Found'
    }
    return render(request, 'users/404.html', context)


def handler500(request):
    context = {
        'error_no': 500,
        'error_detail': 'Server Error'
    }
    return render(request, 'users/404.html', context)


def handler400(request, exception):
    context = {
        'error_no': 400,
        'error_detail': 'Bad Request'
    }
    return render(request, 'users/404.html', context)


def handler403(request, exception):
    context = {
        'error_no': 403,
        'error_detail': 'Permission Denied'
    }
    return render(request, 'users/404.html', context)


# show the home page
def home_view(request):
    if request.method == 'GET':
        # get request simple display
        form = IssueForm()
        return render(request, 'users/home.html', {'form': form})
    elif request.method == 'POST':
        form = IssueForm(request.POST)
        # get the required data,filter and send the mail
        if form.is_valid():
            id = form.cleaned_data.get('id')
            email = form.cleaned_data.get('email')
            role = form.cleaned_data.get('role')
            if role == 'ADM':
                roleFull = 'ADMIN'
            elif role == 'THR':
                roleFull = 'TEACHER'
            else:
                roleFull = 'STUDENT'
            description = form.cleaned_data.get('description')
            send_mail('issue raised by ' + id,
                      'Issue has been raised by user ' + id + '\n having email address '
                      + email + '\nrole ' + roleFull + '\nthe details are as below \n'
                      + description, from_email=None, recipient_list=[ISSUE_MAIL], fail_silently=False)
            # show the acknowledgement message to user
            messages.success(request,
                             message="Your issue has been reported, you will contacted soon via mail")
        else:
            messages.add_message(request, messages.ERROR,
                                 message="Could not send mail Check the details again")
        return redirect('home')
