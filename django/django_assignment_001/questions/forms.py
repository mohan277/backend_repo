from django.forms import ModelForm
from .models import Question
class ContentForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"