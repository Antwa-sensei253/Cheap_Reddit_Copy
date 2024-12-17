from django import forms
from .models import Topic, Post
 
class NewTopicFrom(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea,max_length=40000)
    class Meta:
        model = Topic
        fields = ['subject', 'message']

class newReplyForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What are your thoughts?'}),
        }
