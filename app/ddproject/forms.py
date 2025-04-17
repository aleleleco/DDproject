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
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'classe': forms.Select(attrs={'class': 'form-control'}),
            'raca': forms.Select(attrs={'class': 'form-control'}),
            'nivel': forms.NumberInput(attrs={'class': 'form-control'}),
            'forca': forms.NumberInput(attrs={'class': 'form-control'}),
            'destreza': forms.NumberInput(attrs={'class': 'form-control'}),
            'inteligencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'sabedoria': forms.NumberInput(attrs={'class': 'form-control'}),
            'carisma': forms.NumberInput(attrs={'class': 'form-control'}),
            'pontos_vida_maxima': forms.NumberInput(attrs={'class': 'form-control'}),
            'pontos_vida_atual': forms.NumberInput(attrs={'class': 'form-control'}),
            'idiomas': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'historia': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalize os QuerySets se necessário
        self.fields['classe'].queryset = Classe.objects.all()
        self.fields['raca'].queryset = Raca.objects.all()
        self.fields['idiomas'].queryset = Idioma.objects.all()