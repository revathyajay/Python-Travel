from django.db import models

class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
# class Team(models.Model):
#     teamname=models.CharField(max_length=250)
#     teamimage=models.ImageField(upload_to='photos')
#     teamdesc=models.TextField()

    def __str__(self):
        return self.name
        # return self.teamname


