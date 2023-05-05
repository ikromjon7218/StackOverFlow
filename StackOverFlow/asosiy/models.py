from django.db import models
from django.contrib.auth.models import User

class Savol(models.Model):
    matn = models.CharField(max_length=30)
    sana = models.DateField(auto_now_add=True)
    sarlavha = models.CharField(max_length=900)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    texnologiya = models.CharField(max_length=30, default="Python")
    def __str__(self):
        return f"{self.sarlavha}"

class Javob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    savol = models.ForeignKey(Savol, on_delete=models.CASCADE)
    matn = models.CharField(max_length=900)
    sana = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.matn}"

class Reaksiya(models.Model):
    baho = models.SmallIntegerField()
    javob = models.ForeignKey(Javob, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.javob} {self.baho}"

class Nishon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=30)
    sana = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.nom}"


class Izoh(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    javob = models.ForeignKey(Javob, on_delete=models.CASCADE)
    matn = models.CharField(max_length=300)
    sana = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.matn}"
