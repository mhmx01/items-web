from django import forms


class ItemShareForm(forms.Form):
    name = forms.CharField(max_length=64, label="Your name")
    email = forms.EmailField(label="Your email")
    to = forms.EmailField()
    comments = forms.CharField(widget=forms.Textarea, required=False)


class ItemSearchForm(forms.Form):
    DATE_OPTIONS = (
        ("----", "----"),
        ("before", "before"),
        ("after", "after"),
        ("on", "on"),
    )

    keyword = forms.CharField(max_length=64)
    date_option = forms.ChoiceField(choices=DATE_OPTIONS, required=False, label="Date")
    date_value = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), required=False, label=""
    )

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if request.user.is_authenticated:
            self.fields["mine"] = forms.BooleanField(
                required=False, label="Only my items"
            )
