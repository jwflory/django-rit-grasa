from .forms import *
from django import forms
from haystack import connections
from haystack.constants import DEFAULT_ALIAS
from haystack.forms import SearchForm
from haystack.query import EmptySearchQuerySet, SearchQuerySet
from haystack.utils import get_model_ct
from haystack.utils.app_loading import haystack_get_model

activityList = [
    ("Academic Support", "Academic Support"),
    ("Arts and Culture", "Arts and Culture"),
    ("Career or College Readiness", "Career or College Readiness"),
    ("Civic Engagement", "Civic Engagement"),
    ("Community Service / Service Learning", "Community Service / Service Learning"),
    ("Entrepreneurship / Leadership", "Entrepreneurship / Leadership"),
    ("Financial Literacy", "Financial Literacy"),
    ("Health and Wellness", "Health and Wellness"),
    ("Media Technology", "Media Technology"),
    ("Mentoring", "Mentoring"),
    ("Nature / Environment", "Nature / Environment"),
    ("Play", "Play"),
    ("Public Speaking", "Public Speaking"),
    ("Social and Emotional Learning (SEL)", "Social and Emotional Learning (SEL)"),
    ("Sports and Recreation", "Sports and Recreation"),
    (
        "Science, Tech, Engineering, Math (STEM)",
        "Science, Tech, Engineering, Math (STEM)",
    ),
    ("Tutoring", "Tutoring"),
    ("Other", "Other"),
]
transportationList = [("Provided", "Provided")]
gradesList = [
    ("K-3rd", "K-3rd"),
    ("K-5th", "K-5th"),
    ("3rd-5th", "3rd-5th"),
    ("6th-8th", "6th-8th"),
    ("9th-12th", "9th-12th"),
]
genderList = [
    ("Male-Only", "Male-Only"),
    ("Female-Only", "Female-Only"),
]
feesList = [
    ("Free", "Free"),
    ("$1-$25", "$1-$25"),
    ("$26-$50", "$26-$50"),
    ("$51-$75", "$51-$75"),
    ("$75+", "$75+"),
]
timingList = [
    ("Before-School", "Before-School"),
    ("After-School", "After-School"),
    ("Evenings", "Evenings"),
    ("Weekends", "Weekends"),
    ("Summer", "Summer"),
    # Refactored to "Other Time" to avoid conflicts with activities "Other"
    ("Other-Time", "Other-Time"),
]


class grasaSearchForm(SearchForm):
    q = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "type": "search",
                "name": "q",
                "id": "id_q",
                "class": "form-control",
                "placeholder": "Search...",
                "aria-label": "Search for a Program by name",
                "aria-describedby": "button-addon2",
            }
        ),
    )

    activities = forms.MultipleChoiceField(
        choices=activityList,
        required=False,
        label="",
        widget=forms.CheckboxSelectMultiple,
    )

    transportations = forms.MultipleChoiceField(
        choices=transportationList,
        required=False,
        label="",
        widget=forms.CheckboxSelectMultiple,
    )

    grades = forms.MultipleChoiceField(
        choices=gradesList,
        required=False,
        label="",
        widget=forms.CheckboxSelectMultiple,
    )

    genders = forms.MultipleChoiceField(
        choices=genderList,
        required=False,
        label="",
        widget=forms.CheckboxSelectMultiple,
    )

    fees = forms.MultipleChoiceField(
        choices=feesList, required=False, label="", widget=forms.CheckboxSelectMultiple
    )

    timings = forms.MultipleChoiceField(
        choices=timingList,
        required=False,
        label="",
        widget=forms.CheckboxSelectMultiple,
    )

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        if not self.is_valid():
            print("Here")
            return self.no_query_found()
        print("Search Valid")

        if self.cleaned_data["q"] == "":
            # sqs = SearchQuerySet().exclude(no_such_field="x")
            # sqs = SearchQuerySet().filter(content="soccer")
            sqs = SearchQuerySet()
            print(sqs.count())
            # sqs = sqs.filter(content="soccer")
            print("q = ''")
        else:
            print("q = something")
            sqs = super(grasaSearchForm, self).search()
            print(sqs.count())

        sqs = sqs.order_by("title")
        selectedActivities = self.cleaned_data["activities"]
        for activity in activityList:
            for selectedActivity in selectedActivities:
                print(selectedActivity)
                if activity[0] == selectedActivity:
                    sqs = sqs.filter(content=activity[0])

        selectedTransportations = self.cleaned_data["transportations"]
        for transportation in transportationList:
            for selectedTransportation in selectedTransportations:
                if transportation[0] == selectedTransportation:
                    print("inside transport filter")
                    print(transportation[0])
                    print(selectedTransportation)
                    sqs = sqs.filter(content=transportation[0])

        selectedGrades = self.cleaned_data["grades"]
        for grade in gradesList:
            for selectedGrade in selectedGrades:
                if grade[0] == selectedGrade:
                    sqs = sqs.filter(content=grade[0])

        selectedGenders = self.cleaned_data["genders"]
        for gender in genderList:
            for selectedGender in selectedGenders:
                if gender[0] == selectedGender:
                    sqs = sqs.filter(content=gender[0])

        selectedFees = self.cleaned_data["fees"]
        for selectedFee in selectedFees:
            # These need to be specially written since they aren't stored as a range in the DB
            if "Free" == selectedFee:
                print("Free selected")
                sqs = sqs.filter(fees=0.00)
            if "$1-$25" == selectedFee:
                print("$1-$25 selected")
                sqs = sqs.filter(fees__gte=0.01)
                sqs = sqs.filter(fees__lte=25.99)
            if "$26-$50" == selectedFee:
                print("$26-$50 selected")
                print(sqs.count())
                sqs = sqs.filter(fees__gte=26.00)
                sqs = sqs.filter(fees__lte=50.99)
                print(sqs.count())
            if "$51-$75" == selectedFee:
                print("$51-$75 selected")
                sqs = sqs.filter(fees__gte=51.00)
                sqs = sqs.filter(fees__lte=75.99)
            if "$75+" == selectedFee:
                sqs = sqs.filter(fees__gte=75.00)

        selectedTimings = self.cleaned_data["timings"]
        for timing in timingList:
            for selectedTiming in selectedTimings:
                if timing[0] == selectedTiming:
                    sqs = sqs.filter(content=timing[0])
        print(sqs.count())
        return sqs
