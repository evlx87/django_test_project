from django import forms

from catalog.models import Product, Version

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


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        exclude = {'owner', 'is_published'}

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


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'


class ModeratorProductForm(ProductForm, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')
