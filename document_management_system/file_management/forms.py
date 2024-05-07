from django import forms


class FileUploadForm(forms.Form):
    file = forms.FileField(label='Select a file')
    description = forms.CharField(label='Optional Description', required=False)
