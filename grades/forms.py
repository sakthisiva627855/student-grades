from django import forms
from .models import Student, StudentGrade


# ✅ Form to ADD a Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name']
        widgets = {
            'student_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter student name'
                }
            )
        }


# ✅ Form to ENTER MARKS
class StudentGradeForm(forms.ModelForm):
    class Meta:
        model = StudentGrade
        fields = ['subject', 'grade']  # remarks auto-calculated
        widgets = {
            'grade': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter marks'
                }
            ),
            'subject': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }
