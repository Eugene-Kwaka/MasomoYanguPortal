from django.urls import path
from .views import *

urlpatterns=[
    path('', home, name='home'),
    path('notes/', notes, name="notes"),
    # this path takes one to a specific note and delete's it
    path('delete_note/<int:pk>/', delete_note, name="delete_note"),
    # this path references a generic view hence '.as_view'
    path('notes_view/<int:pk>/', NotesDetailView.as_view(), name="notes_detail"),
    
    path('homework/', homework, name="homework"),
    path('update_homework/<int:pk>', update_homework, name="update_homework"),
    path('delete_homework/<int:pk>/', delete_homework, name="delete_homework"),

    path('youtube/', youtube, name="youtube"),

    path('todo/', todo, name="todo"),
    path('update_todo/<int:pk>', update_todo, name="update_todo"),
    path('delete_todo/<int:pk>/', delete_todo, name="delete_todo"),

    path('books/', books, name="books"),

    path('dictionary/', dictionary, name='dictionary'),

    path('wiki/', wiki, name='wiki'),

    path('conversion/', conversion, name="conversion"),
]   
