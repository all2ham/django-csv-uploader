from django import forms

class UploadForm(forms.Form):
    csv_file = forms.FileField(label='Select CSV File',widget=forms.FileInput(attrs={
        'name': 'csv_file',
        'id': 'csv_file',
        'type':'file',
        'style':'display:none;'
    }))