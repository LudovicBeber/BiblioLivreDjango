from django.db import models

class Livre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Avis(models.Model):
    commentaire = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)

    class Meta:
        ordering = ['rating']

    def __str__(self):
        return (self.commentaire + ' : ' + str(self.rating) + ' étoiles')
