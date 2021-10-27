from django.forms import ModelForm
from .models import Visitors

class VisitorForm(ModelForm):
    class Meta :
        model = Visitors
        fields = "__all__"