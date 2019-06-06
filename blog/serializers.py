from rest_framework import serializers
from blog.models import NewReporter, NewArticle, ContactMe


class ReporterSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewReporter
		fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewArticle
		fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContactMe
		fields = '__all__'
