from django.forms import ModelForm
from .models import Track

class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields   = '__all__'

        