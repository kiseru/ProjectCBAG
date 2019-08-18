from django import forms

from academic_groups.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'academic_group', 'educational_form')
