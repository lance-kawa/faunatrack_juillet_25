from django import forms

from faunatrack.models import Observation



class BaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'border rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full p-2.5'

class ObservationForm(BaseForm):
    class Meta:
        model = Observation
        fields = ['species', 'notes', 'quantity', 'project', 'location']


# class ProjetForm(forms.ModelForm):
#     class Meta:
#         model = Observation
#         fields = ['title', 'description', 'is_public']



# class SpeciesForm(forms.ModelForm):
#     class Meta:
#         model = Observation
#         fields = ['name', 'at_risk']