from django.forms import ModelForm
from consumer.models import Consumer
class ConsumerRegForm(ModelForm):
    class Meta:
        model=Consumer
        fields="__all__"
    def clean(self):
        print("clean reg")
class ConsumerLoginForm(ModelForm):
    class Meta:
        model=Consumer
        fields=["username","password"]

        def clean(self):
            print("clean login")
