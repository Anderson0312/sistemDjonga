from django import forms

# from django.contrib.auth.models import User
# from .models import Profile


# class UpdateUserForm(forms.ModelForm):
#     username = forms.CharField(max_length=100,
#                                required=True,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(required=True,
#                              widget=forms.TextInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ['username', 'email']


# class UpdateProfileForm(forms.ModelForm):
#     name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     profissao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     pais = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = Profile
#         fields = ['name', 'profissao',"pais","city"]