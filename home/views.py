from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.


def welcome_page(request):

    if request.method == 'POST':
        messages.success(request, 'We have received the email & will be in contact soon!')
        message = request.POST['message']
        email = request.POST['email']
        first_name = request.POST['first']
        last_name = request.POST['last']
        # student = request.POST['student']
        # donate = request.POST['donate']
        # volunteer = request.POST['volunteer']
        message = "From " + first_name.title() + ' ' + last_name.title() + "," + "\n" + email + " \n \n" + message +\
                  "\n \n" + "We will respond back to the above email shortly, thanks for contacting us." + "\n" +\
                  "Persevere" + "\n" + "P: 877-260-7299" + "\n" + "info@perseverenow.org"
        send_mail(
                  # first_name,
                  # last_name,
                  "Automated Email From Persevere",

                  # student,
                  # donate,
                  # volunteer,
                  message,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=['cryptopotluck@gmail.com', email]
                  )
    return render(request, 'home/welcome_page.html')


def mail(request):
    if request.method == 'POST':
        messages.success(request, 'We have received the email & will be in contact soon!')
        message = request.POST['message']
        email = request.POST['email']
        first_name = request.POST['first']
        last_name = request.POST['last']
        message = "From " + first_name.title() + ' ' + last_name.title() + "," + "\n" + email + " \n \n" + message + \
                    "\n \n" + "We will respond back to the above email shortly, thanks for contacting us." + "\n" + \
                    "Persevere" + "\n" + "P: 877-260-7299" + "\n" + "info@perseverenow.org"
        send_mail(
            "Automated Email From Persevere",
            message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['cryptopotluck@gmail.com', email]
            )
        return redirect(request, 'welcome')
    if request.method == 'GET':
        return redirect('welcome')