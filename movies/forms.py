from django import forms
from .models import Movie

genre_choices = (
    ("Action", "Action"),
    ("Comedy", "Comedy"),
    ("Drama Comedy", "Drama/Comedy"),
    ("Drama", "Drama"),
    ("Drama Mystery", "Drama/Mystery"),
    ("Drama Romance", "Drama/Romance"),
    ("Feel Good", "Feel Good"),
    ("Horror", "Horror"),
    ("Sci-Fi Dystopia", "Sci-Fi/Dystopia"),
    ("Series", "Series"),
    ("Superhero", "Superhero"),
    ("Thriller", "Thriller"),

)

rating_choices = (
    (10, "10"),
    (9, "9"),
    (8, "8"),
    (7, "7"),
    (6, "6"),
    (5, "5"),
    (4, "4"),
    (3, "3"),
    (2, "2"),
    (1, "1"),
)

class MovieForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=500, widget=forms.TextInput(attrs={'class':'title-box'}), required=False)
    director = forms.CharField(label="Director", max_length=500, widget=forms.TextInput(attrs={'class':'title-box'}), required=False)
    genre = forms.ChoiceField(choices = genre_choices, label="Genre", widget=forms.RadioSelect(attrs={'class':'genre-box'}), required=False)
    year = forms.IntegerField(label="Year Released", widget=forms.NumberInput(attrs={'class':'yearpicker'}), required=False)
    star1 = forms.CharField(label="Star 1", max_length=500, widget=forms.TextInput(attrs={'class':'star-box'}), required=False)
    star2 = forms.CharField(label="Star 2", max_length=500, widget=forms.TextInput(attrs={'class':'star-box'}), required=False)
    rating = forms.ChoiceField(choices = rating_choices, label="Rating", widget=forms.RadioSelect(attrs={'class':'rating-box'}), required=False)
    timeswatched = forms.IntegerField(label="Times Watched", widget=forms.NumberInput(attrs={'class':'times-box', 'min':"1", 'max':"100", 'step':"1"}), required=False)
    movieimage = forms.ImageField(label="Movie Image", widget=forms.FileInput(attrs={'class':'image-box', 'id':'movieupload', 'hidden':'hidden', 'required':'required'}), required=False)
    directorimage = forms.ImageField(label="Director Image", widget=forms.FileInput(attrs={'class':'image-box', 'id':'directorupload', 'hidden':'hidden', 'required':'required'}), required=False)
    


    class Meta:
        model = Movie
        exclude = ("",)