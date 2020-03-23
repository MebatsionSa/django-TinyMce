from django.db import models

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    tutorial_content = models.TextField()

    def __str__(self):
        return self.tutorial_title