from django.urls import path
from . import views

app_name = 'grades'

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add-student/', views.add_student, name='add_student'),
    path('enter-marks/<int:student_id>/', views.enter_marks, name='enter_marks'),
    path('view-marks/<int:student_id>/', views.view_marks, name='view_marks'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
]
