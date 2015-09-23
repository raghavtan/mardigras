from django.db import models

class menuList(models.Model):
    displayName = models.CharField(max_length=40,primary_key=True)
    details = models.TextField(blank=True)
    menuUrl = models.CharField(max_length=40,null=False)
    def __str__(self):
        return self.displayName

class subMenu(models.Model):
    subParent = models.ForeignKey(menuList)
    subName = models.CharField(max_length=20)
    def __str__(self):
        return self.subName
