from django import forms

from catalog.models import Product

STOP_WORD = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for word in STOP_WORD:
            if word in cleaned_data:
                raise forms.ValidationError(
                    'Это слово использовать недопустимо')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in STOP_WORD:
            if word in cleaned_data:
                raise forms.ValidationError(
                    'Это слово использовать недопустимо')

        return cleaned_data
