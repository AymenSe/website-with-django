from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from blog.models import NewReporter, NewArticle, ContactMe


class AddReporterForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddReporterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Submit', 'Enter'))

    class Meta:
        model = NewReporter
        fields = '__all__'
        labels = {
            'full_name': 'Full Name',
        }


class AddArticleForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddArticleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Submit', 'Enter'))

    class Meta:
        model = NewArticle
        fields = '__all__'
        labels = {
            'pub_date': 'Date',
            'headline': 'Title',
            'content': 'Content',
            'reporter': 'Reporter',
            'image': 'Upload Image',
        }


class AddContactForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Submit', 'Send'))

    class Meta:
        model = ContactMe
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'second_name': 'Second Name',
            'email': 'Email',
            'msg': 'Message',
            'rate': 'Rate',
        }
