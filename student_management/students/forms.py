import logging
from django import forms
from .models import Student

# Create a logger instance
logger = logging.getLogger(__name__)

class StudentForm(forms.ModelForm):
    # Adding min_value and max_value constraints for grade field
    grade = forms.IntegerField(min_value=1, max_value=12)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'enrollment_date', 'grade']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("A student with this email already exists.")
        return email

    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        logger.debug(f"Validating grade: {grade}")  # Add this for logging
        print(f"Grade entered: {grade}")  # Debugging statement
        if grade < 1 or grade > 12:
            logger.warning(f"Invalid grade entered: {grade}")
            raise forms.ValidationError("Grade must be between 1 and 12.")
        return grade
