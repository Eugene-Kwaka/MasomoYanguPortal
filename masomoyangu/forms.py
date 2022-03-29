from dataclasses import fields
from django import forms
from .models import *
from django.forms import widgets


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

class ConversionForm(forms.Form):
    CHOICES = [
        ('length', 'Length'),
        ('mass', 'Mass')
    ]
    measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

class ConversionLengthForm(forms.Form):
    CHOICES = [
        ('yard', 'Yard'),
        ('foot', 'Foot')
    ]    
    input = forms.CharField(required=False,label=False, widget=forms.TextInput(
        attrs={
            'type':'number',
            'placeholder':'Enter a Number'
        }
    )) 
    measure1 = forms.CharField(label='', widget=forms.Select(choices=CHOICES))
    measure2 = forms.CharField(label='', widget=forms.Select(choices=CHOICES))

class ConversionMassForm(forms.Form):
    CHOICES = [
        ('pound', 'Pound'),
        ('kilogram', 'Kilogram')
    ]    
    input = forms.CharField(required=False,label=False, widget=forms.TextInput(
        attrs={
            'type':'number',
            'placeholder':'Enter a Number'
        }
    )) 
    measure1 = forms.CharField(label='', widget=forms.Select(choices=CHOICES))
    measure2 = forms.CharField(label='', widget=forms.Select(choices=CHOICES))



class YoutubeSearchForm(forms.Form):
    text = forms.CharField(max_length=255, label="Search youtube video")


class BookSearchForm(forms.Form):
    text = forms.CharField(max_length=255, label="Search for books")

class DictionarySearchForm(forms.Form):
    text = forms.CharField(max_length=255, label="Search for words")

class WikiSearchForm(forms.Form):
    text = forms.CharField(max_length=255, label="Search in Wikipedia")


