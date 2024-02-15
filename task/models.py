from django.db import models
# from users .models import Users
from django.contrib.auth.models import User

class Catagories(models.Model):
    title=models.CharField(max_length=225)
    description=models.TextField()

class Task(models.Model):
    title=models.CharField(max_length=225)
    description=models.TextField()
    due_date=models.DateTimeField()
    status=models.CharField(max_length=225)
    priority=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    # relationship
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='usser_id')
    Catagories_id=models.ManyToManyField(Catagories)

    


    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Task_detail", kwargs={"pk": self.pk})


    

    class Meta:
        verbose_name = ("Catagories")
        verbose_name_plural = ("Catagoriess")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Catagories_detail", kwargs={"pk": self.pk})


