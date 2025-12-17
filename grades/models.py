from django.db import models

class Student(models.Model):
    student_key = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name


class Subject(models.Model):
    subject_key = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class StudentGrade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()

    class Meta:
        unique_together = ('student', 'subject')

    @property
    def remarks(self):
        return "PASS" if self.grade >= 75 else "FAIL"
