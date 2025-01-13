from django import forms


class FechasForm(forms.Form):
    producto = [
        ('zapatos','Zapatos'),
        ('camiseta','Camiseta'),
        ('pantalones','Pantalones'),
        ('gorra','Gorra'),
        ('pulsera','Pulsera'),
        ('gafas de sol','Gafas de sol'),
        ('corbata','Corbata'),
        ('maleta','Maleta'),
        ('calcetines','Calcetines'),
        ('chaqueta','Chaqueta'),
        ('vestido','Vestido'),
        ('falda','Falda'),
    ]
    producto = forms.ChoiceField(choices=producto)
    comienzo = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    termino = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    