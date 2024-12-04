from django import forms
from .models import Topic
 
class NewTopicFrom(forms.ModelForm):
    
    message = forms.CharField(widget=forms.Textarea,max_length=40000)
    class Meta:
        model = Topic
        fields = ['subject', 'message']