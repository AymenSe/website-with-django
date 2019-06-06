from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from rest_framework.viewsets import ModelViewSet

from blog.forms import AddArticleForm, AddContactForm, AddReporterForm
from blog.models import ContactMe, NewArticle, NewReporter
from blog.serializers import (ArticleSerializer, ContactSerializer,
                              ReporterSerializer)


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)


'''--------------------------------------------------------------------'''


def index(request):
    return render(request, "index.html", context={})


def About(request):
    return render(request, 'about.html', context={})


@login_required
def article(request):
    a_list = NewArticle.objects.all()
    context = {
        'article_list': a_list,
    }
    return render(request, 'article.html', context)


@login_required
def ReporterList(request):
    r_list = NewReporter.objects.all()
    context = {
        'reporter_list': r_list,
    }
    return render(request, 'reporter.html', context)


class AddReporterView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddReporterForm()
        context = {
            'form': form
        }
        return render(request, 'add_reporter.html', context)

    def post(self, request):
        form = AddReporterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_reporter/')
        else:
            context = {
                'form': form,
            }
            return render(request, 'add_reporter.html', context)


class AddArticleView(LoginRequiredMixin, View):

    def get(self, request):
        form_article = AddArticleForm()
        context = {
            'form_article': form_article,
        }
        return render(request, 'add_article.html', context)

    def post(self, request):
        form_article = AddArticleForm(request.POST)
        if form_article.is_valid():
            form_article.save()
            return redirect('/add_article/')
        else:
            context = {
                'form_article': form_article,
            }
            return render(request, 'add_article.html', context)


class ArticleViewSet(ModelViewSet):
    queryset = NewArticle.objects.all()
    serializer_class = ArticleSerializer


class ReporterViewSet(ModelViewSet):
    queryset = NewReporter.objects.all()
    serializer_class = ReporterSerializer


class ContactViewSet(ModelViewSet):
    queryset = ContactMe.objects.all()
    serializer_class = ContactSerializer


class AddContactView(View):

    def get(self, request):
        form = AddContactForm()
        context = {
            'form': form,
        }
        return render(request, 'contact_me.html', context)

    def post(self, request):
        form = AddContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact_me/')
        else:
            context = {
                'form': form,
            }
            return render(request, 'contact_me.html', context)
