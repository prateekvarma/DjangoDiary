from django.db import models

# Create your models here.
class Entry(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    # this formats your DB row in admin as Entry #1, insted of Entry object (1)
    def __str__(self):
        return 'Entry #{}'.format(self.id)