# forms.py
from django import forms
from .models import Personagens, Classe, Raca, Idioma

class PersonagemForm(forms.ModelForm):
    class Meta:
        model = Personagens
        fields = [
            'nome',
            'classe',
            'raca',
            'nivel',
            'forca',
            'destreza',
            'inteligencia',
            'sabedoria',
            'carisma',
            'pontos_vida_maxima',
            'pontos_vida_atual',
            'idiomas',
            'historia',
        ]
        widgets = {
            'historia': forms.Textarea(attrs={'rows': 4}),
            'idiomas': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalize os QuerySets se necessário
        self.fields['classe'].queryset = Classe.objects.all()
        self.fields['raca'].queryset = Raca.objects.all()
        self.fields['idiomas'].queryset = Idioma.objects.all()