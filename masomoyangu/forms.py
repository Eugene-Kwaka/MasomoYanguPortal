from dataclasses import fields
from django import forms
from .models import *
from django.forms import widgets

# Authentication & Authorization
from django.contrib.auth.forms import UserCreationForm


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

# This is a class of DateInput to show a widget of a calender when adding dates in a form
class DateInput(forms.DateInput):
    input_type = 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_finished']


class YoutubeSearchForm(forms.Form):
    text = forms.CharField(max_length=255, label="Search youtube video")


class BookSearchForm(forms.Form):
    text = forms.CharField(max_length=255, label="Search for books")

class DictionarySearchForm(forms.Form):
    text = forms.CharField(max_length=255, label="Search for words")

class WikiSearchForm(forms.Form):
    text = forms.CharField(max_length=255, label="Search in Wikipedia")

# This form makes a user choose two choices (Length or Mass)
class ConversionForm(forms.Form):
    CHOICES = [
        ('length', 'Length'),
        ('mass', 'Mass')
    ]
    measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

# This form makes a user choose between length conversion rates i.e (yard or foot)
class ConversionLengthForm(forms.Form):
    CHOICES = [
        ('yard', 'Yard'),
        ('foot', 'Foot')
    ]   
    # A user enters a number they want to be converted 
    input = forms.CharField(required=False,label=False, widget=forms.TextInput(
        attrs={
            'type':'number',
            'placeholder':'Enter a Number'
        }
    )) 
    # Specifies type of length
    measure1 = forms.CharField(label='', widget=forms.Select(choices=CHOICES))
    # Specifies type of length
    measure2 = forms.CharField(label='', widget=forms.Select(choices=CHOICES))

# Here the form is for a user to choose between Mass conversion rates(Pounds & Kilograms)
class ConversionMassForm(forms.Form):
    CHOICES = [
        ('pound', 'Pound'),
        ('kilogram', 'Kilogram')
    ]   
    # User enters a number to be converted 
    input = forms.CharField(required=False,label=False, widget=forms.TextInput(
        attrs={
            'type':'number',
            'placeholder':'Enter a Number'
        }
    )) 
    measure1 = forms.CharField(label='', widget=forms.Select(choices=CHOICES))
    measure2 = forms.CharField(label='', widget=forms.Select(choices=CHOICES))



class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1', 'password2' ]