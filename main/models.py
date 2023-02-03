from django.db import models

class Quote(models.Model):
    """
    The scrapped data will be saved in this model
    """
    text = models.TextField(max_length=1000,null=True, blank=True)
    related_link = models.CharField(max_length=1512,null=True, blank=True)


    def __str__(self):
        return self.text