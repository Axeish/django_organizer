from django import forms


from .models import Entry

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['name','type', 'description']
   


class TodoForm(forms.Form):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'todo'}))   

class FinForm(forms.Form):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'todo'}))       