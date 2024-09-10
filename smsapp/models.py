from django.db import models

class SmsProvider (models.Model):
    TYPE_CHOICE=[('token', 'Token'),
        ('string', 'String'),]
    apikey=models.CharField(max_length=100,default='')
    ctype=models.CharField(max_length=10,choices=TYPE_CHOICE, default='token')
    def __str__(self):
        return f"{self.apikey} - {self.ctype}"

class Smstosend (SmsProvider):
    created=models.DateTimeField(auto_now_add=True)
    message=models.CharField(max_length=200,blank=True,default='a blanked message')
    receptor=models.CharField(max_length=100, blank=False, default='01')
    def __str__(self):
        f"API Key: {self.apikey}, Message: {self.message}, Receptor: {self.receptor}, Created: {self.created}"

        


