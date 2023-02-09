from django.db import models

class Quote(models.Model):
    """
    The scrapped data will be saved in this model
    """
    text = models.TextField(max_length=1000,null=True, blank=True)
    related_link = models.TextField(max_length=1512,null=True, blank=True)


    def __str__(self):
        return self.text
    


class FreePatent(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=2000,null=True, blank= True)

    def __str__(self):
        return self.title
    

class LogoModel(models.Model):
    title = models.CharField(max_length=500,null=True, blank=True)
    description = models.TextField(max_length=2000,null=True, blank=True)
    def __str__(self):
        return self.title
    

class ImageModel(models.Model):
    title = models.CharField(max_length=500,null=True, blank=True)
    description = models.TextField(max_length=2000,null=True, blank=True)
    def __str__(self):
        return self.title



class TrademarkModel(models.Model):
    title = models.CharField(max_length=500,null=True, blank=True)
    description = models.TextField(max_length=2000,null=True, blank=True)
    def __str__(self):
        return self.title
