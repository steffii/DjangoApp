from django.db import models

# Create your models here.

class Questions(models.Model):
    questions_text=models.CharField(max_length=100)
    pub_date=models.DateTimeField("date published")

    def __str__(self):
        return self.questions_text

class Choice(models.Model):
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text