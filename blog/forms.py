from django import forms
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                                widget=forms.Textarea)

# ModelForm because form is being built dynamically from Comment model
from .models import Comment
class CommentForm(forms.ModelForm):
    # need to indicate which model to use to build the form in the Meta class of the form
    class Meta:
        # introspects the model and builds the form dynamically
        model = Comment
        # explicitly tell the framework which fields to include in form
        fields = ('name', 'email', 'body')

class SearchForm(forms.Form):
    query = forms.CharField()