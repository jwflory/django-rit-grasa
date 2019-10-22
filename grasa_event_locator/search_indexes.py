import datetime
from haystack import indexes
from grasa_event_locator.models import Program


class ProgramIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #Added this line so that filtering by fees didn't always return empty set
    fees = indexes.FloatField(model_attr='fees')

    def get_model(self):
        return Program

    def index_queryset(self, using=None):
        #"""Used when the entire index for model is updated."""
        return self.get_model().objects.filter(isPending=False)