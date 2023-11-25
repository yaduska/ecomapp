from django import forms
from .models import ConversationMessages

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model=ConversationMessages
        fields=('content',)
        widgets={
            'content':forms.Textarea(attrs={'class':'w-full px-6 py-4 rounded-xl border'})
        }

