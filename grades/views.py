from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory

from .models import Student, Subject, StudentGrade
from .forms import StudentForm, StudentGradeForm



def student_list(request):
    query = request.GET.get('q', '')
    if query:
        students = Student.objects.filter(student_name__icontains=query)
    else:
        students = Student.objects.all()

    return render(request, 'grades/student_list.html', {'students': students})


def enter_marks(request, student_id):
    student = get_object_or_404(Student, student_key=student_id)

    GradeFormSet = modelformset_factory(
        StudentGrade,
        form=StudentGradeForm,
        extra=0
    )

    for subject in Subject.objects.all():
        StudentGrade.objects.get_or_create(
            student=student,
            subject=subject,
            defaults={'grade': 0}
        )

    queryset = StudentGrade.objects.filter(student=student)

    if request.method == "POST":
        formset = GradeFormSet(request.POST, queryset=queryset)
        if formset.is_valid():
            formset.save()
            return redirect('grades:view_marks', student_id=student.student_key)
    else:
        formset = GradeFormSet(queryset=queryset)

    return render(request, 'grades/enter_marks.html', {
        'student': student,
        'formset': formset
    })


def view_marks(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    marks = StudentGrade.objects.filter(student=student)

    return render(request, 'grades/view_marks.html', {
        'student': student,
        'marks': marks
    })


def delete_student(request, student_id):
    student = get_object_or_404(Student, student_key=student_id)
    student.delete()
    return redirect('grades:student_list')

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades:student_list')
    else:
        form = StudentForm()

    return render(request, 'grades/add_student.html', {'form': form})
