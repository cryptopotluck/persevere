from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from tinymce.widgets import TinyMCE
from django.core.files.storage import FileSystemStorage
from .forms import ProfilePictureUpdateForm, ProfileFrom, ProfilePage
from .models import Profile
from django.shortcuts import get_object_or_404
from django.views import View
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome back!')
            return redirect('welcome')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'users/login.html')

class ProfileUpdate(View):
    template_name = 'users/profile_form.html'

    def get(self, request):
        post = get_object_or_404(Profile, user_id=request.user)
        form = ProfileFrom(initial={'about': post.about, 'first_name': post.first_name, 'last_name': post.last_name,
                                    'address': post.address, 'profile_image': post.profile_image, 'city': post.city,
                                    'country': post.country, 'postal_code': post.postal_code})

        form.fields['about'].widget = TinyMCE()
        about = Profile.objects.get(user=request.user).about
        username = User.objects.get(username=request.user).username
        email = User.objects.get(username=request.user).email
        firstname = Profile.objects.get(user=request.user).first_name
        lastname = Profile.objects.get(user=request.user).last_name
        address = Profile.objects.get(user=request.user).address
        city = Profile.objects.get(user=request.user).city
        country = Profile.objects.get(user=request.user).country
        postalcode = Profile.objects.get(user=request.user).postal_code
        profile_pic = Profile.objects.get(user=request.user).profile_image
        context = {
            'post': post,
            'form': form,
            'about': about,
            'username': username,
            'first_name': firstname,
            'email': email,
            'last_name': lastname,
            'profile_pic': profile_pic,
            'address': address,
            'city': city,
            'country': country,
            'postalcode': postalcode

        }
        return render(request, self.template_name, context)

    def post(self, request):
        if request.method == 'POST':
            profile_form = ProfileFrom(request.POST, request.FILES,  instance=request.user.profile)
            profile_page =  ProfilePage(request.POST, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save(Profile.profile_image)
                profile_page.save(Profile.first_name)
                profile_page.save(Profile.last_name)
                profile_page.save(Profile.address)
                profile_page.save(Profile.about)
                profile_page.save(Profile.city)
                profile_page.save(Profile.country)
                profile_page.save(Profile.postal_code)

        return redirect('profile')


# def profile(request):
#     if request.method == 'POST':
#         # uploaded_pic = request.FILES['profile_image2']
#         profile_form = ProfileFrom(request.POST, instance=request.user.profile)
#         # profile_picture_form = ProfilePictureUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         profile_page = ProfileFrom(request.POST, instance=request.user.profile)
#         if profile_form.is_valid():
#             profile_form.save(Profile.about)
#             profile_page.save(Profile.first_name)
#             profile_page.save(Profile.last_name)
#             profile_page.save(Profile.address)
#             profile_page.save(Profile.city)
#             profile_page.save(Profile.country)
#             profile_page.save(Profile.postal_code)
#             # profile_picture_form.save(Profile.profile_image)
#             fs = FileSystemStorage()
#             # fs.save(uploaded_pic)
#         return redirect('profile')
#     else:
#         post = get_object_or_404(Profile, user_id=request.user)
#         form = ProfileFrom(initial={'about': post.about, 'first_name': post.first_name, 'last_name': post.last_name,
#                                     'address': post.address, 'profile_image': post.profile_image, 'city': post.city,
#                                     'country': post.country, 'postal_code': post.postal_code})
#
#         form.fields['about'].widget = TinyMCE()
#         about = Profile.objects.get(user=request.user).about
#         username = User.objects.get(username=request.user).username
#         email = User.objects.get(username=request.user).email
#         firstname = Profile.objects.get(user=request.user).first_name
#         lastname = Profile.objects.get(user=request.user).last_name
#         address = Profile.objects.get(user=request.user).address
#         city = Profile.objects.get(user=request.user).city
#         country = Profile.objects.get(user=request.user).country
#         postalcode = Profile.objects.get(user=request.user).postal_code
#         profile_pic = Profile.objects.get(user=request.user).profile_image
#         context = {
#             'post': post,
#             'form': form,
#             'about': about,
#             'username': username,
#             'first_name': firstname,
#             'email': email,
#             'last_name': lastname,
#             'profile_pic': profile_pic,
#             'address': address,
#             'city': city,
#             'country': country,
#             'postalcode': postalcode
#
#
#         }
#
#     return render(request, 'users/profile_form.html', context)


def register(request):
    if request.method == 'POST':
        # Get form values
        email = request.POST['email']
        username = request.POST['userName']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Check if passwords match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'We have a copycat, username has been taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already in use try recovering password.')
                    return redirect('register')
                else:
                    # looks good
                    user = User.objects.create_user(email=email, username=username, password=password)
                    auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    user.save()
                    messages.success(request, 'You are now logged in please enhance your profile.')
                    return redirect('welcome')

        else:
            messages.error(request, 'We have a Bad Typer... Passwords do not match')
            return render(request, 'users/register.html')
    else:
        return render(request, 'users/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You logged out, see you next time!')
        return redirect('login')