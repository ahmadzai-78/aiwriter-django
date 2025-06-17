from django import forms

STYLE_CHOICES = [
    ("formel", "Formel"),
    ("commercial", "Commercial"),
    ("amical", "Amical"),
]

class DocumentForm(forms.Form):
    client_name = forms.CharField(label="Nom du client", max_length=100)
    service = forms.CharField(label="Service", max_length=200)
    amount = forms.DecimalField(label="Montant (€)", max_digits=10, decimal_places=2)
    style = forms.ChoiceField(label="Style de rédaction", choices=STYLE_CHOICES)