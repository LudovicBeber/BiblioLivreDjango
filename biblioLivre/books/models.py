from django.db import models

class Livre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Avis(models.Model):
    commentaire = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='avis')
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    like = models.ManyToManyField('auth.User', related_name='likes', blank=True)


    class Meta:
        ordering = ['rating']

    def __str__(self):
        return (self.commentaire + ' : ' + str(self.rating) + ' étoiles')
