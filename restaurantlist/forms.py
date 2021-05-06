from django import forms

from games.models import gamesLocation

from .models import Item




class ItemForms(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'Gamegangler',
            'name',
            'contents',
            'excludes',
            'public'
         ]

    def __init__(self, user=None, *args, **kwargs):
            #print(kwargs.pop('user'))
            print(user)
            print(kwargs)
            super(ItemForms, self).__init__(*args, **kwargs)
            self.fields['Gamegangler'].queryset = gamesLocation.objects.filter(owner=user)

