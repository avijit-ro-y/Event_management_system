from django import forms
from event.models import Participant,Event,Category

class CategoryModelForm(forms.ModelForm):
    """Model form create korar jonno alada kore fild create korte hoyna.
    modeles (database) e jsob filed use kora hoyeche setai abar reuse
    kora jay."""
    class Meta:
        model=Category
        fields=['name','description']
        
class EventModelForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=['name','description','date','time','location','category']
class ParticipantModelForm(forms.ModelForm):
    class Meta:
        model=Participant
        fields=['name','email','events']
    