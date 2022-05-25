from django import forms

from industries.models import Industry, Franchise, Game


class AddIndustry(forms.ModelForm):
    class Meta:
        model = Industry
        fields = "__all__"


class AddFranchise(forms.ModelForm):
    class Meta:
        model = Franchise
        fields = "__all__"


class AddGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"
