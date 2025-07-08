from django import forms

from faunatrack.models import Observation



class BaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'border rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full p-2.5 bonjour'

class ObservationForm(BaseForm):
    class Meta:
        model = Observation
        fields = "__all__"
        widgets = {
            'date_observation': forms.widgets.DateInput( 
                attrs={
                    'type': 'date',
                }
            ),
        }

    class Media:
        css = {
            'all': ('assets/test.css',)
        }

    def clean_notes(self):
        notes = self.cleaned_data.get('notes', None)
        if "pas beau" in notes:
            raise forms.ValidationError("Votre observation doit être plus belle que ça voyons !")
        return notes




# class ProjetForm(forms.ModelForm):
#     class Meta:
#         model = Observation
#         fields = ['title', 'description', 'is_public']



# class SpeciesForm(forms.ModelForm):
#     class Meta:
#         model = Observation
#         fields = ['name', 'at_risk']