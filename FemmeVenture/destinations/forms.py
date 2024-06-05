from django.forms import ModelForm, widgets, Textarea 
from django import forms
from django.core.exceptions import ValidationError
from .models import Review
from .models import Feedback


class ReviewForm(ModelForm):
    class Meta: 
        model = Review 
        fields = ['value', 'body']  # Ensure 'value' is an IntegerField in the model.

        labels = {
            'value': '',  # You can remove this if you're not using it.
            'body': ''    
        }
        widgets = {
            'body': Textarea(attrs={
                'class': 'form-control custom-field',
                'name': 'body',
                'id': 'id_body',
                'rows': 5,
                'placeholder': 'Write a Review'
            }),
        }
        



        
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        # Update the class for 'body' field only, as 'value' will be handled in the template
        if 'body' in self.fields:
            self.fields['body'].widget.attrs.update({'class': 'form-control custom-field'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control custom-field'})



class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['body']
        labels = {
            'body': ''  # Keeps the label empty if that is your intention
        }
        widgets = {
            'body': Textarea(attrs={
                'class': 'form-control custom-field',
                'name': 'body',
                'id': 'id_body',
                'rows': 4,
                'placeholder': 'Write your feedback here...'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)

        # Apply a general class to all fields first, though you only have 'body' defined
        for name, field in self.fields.items():
            # This will apply or override the classes and attributes uniformly across all fields
            field.widget.attrs['class'] = 'form-control custom-field'

            # If there are specific attributes for a field, you can update them here
            if name == 'body':
                field.widget.attrs.update({
                    'rows': 2,  # Ensuring the rows are set as needed
                    'placeholder': 'Write your feedback here...'  # Ensuring the placeholder is set as needed
                })

# Note: If you plan to add more fields to the form in the future, consider adding more specific handling in the if statement.
