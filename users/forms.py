from .models import Profile
from django import forms
from tinymce.widgets import TinyMCE


class ProfileFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileFrom, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ['about', 'profile_image', 'email', 'first_name', 'last_name', 'address', 'city', 'country', 'postal_code']
        widgets = {
            'about': TinyMCE(),
        }



class ProfilePictureUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        # profile_image = forms.FileInput()
        fields = ['profile_image']


class ProfilePage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'address', 'city', 'country', 'postal_code')


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


form = ProfileFrom()