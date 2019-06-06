from django.db import models

# Create your models here.


class NewReporter(models.Model):
    f_name = models.CharField(max_length=64)
    s_name = models.CharField(max_length=64)
    email = models.CharField(max_length=256)
    data_birth = models.DateField()
    domain = models.CharField(max_length=128)

    def __str__(self):
        return '{} {}'.format(self.f_name, self.s_name)


class NewArticle(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=256)
    content = models.TextField()
    reporter = models.ForeignKey(NewReporter, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.headline


class ContactMe(models.Model):
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    email = models.CharField(max_length=256)
    msg = models.TextField()
    rate = models.CharField(max_length=10, choices=(('1', 'Bad'), ('2', 'Normal'), ('3', 'Good')))

