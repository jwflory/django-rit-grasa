from django import forms
from haystack.forms import SearchForm


class grasaSearchForm(SearchForm):
    q = forms.CharField(required=False, label=('Search'),
                        widget=forms.TextInput(attrs={'type': 'search', 'name': 'q', 'id': 'id_q', 'class': 'form-control', 'placeholder': 'Search...', 'aria-label': 'Search for a Program by name', 'aria-describedby': 'button-addon2'}))

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(grasaSearchForm, self).search()

        if not self.is_valid():
            print("Here")
            return self.no_query_found()
        print("Search Valid")
        return sqs