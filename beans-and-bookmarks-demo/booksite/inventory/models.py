from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length = 20)
    title = models.CharField(max_length = 200)
    date_received = models.DateTimeField('Date Recieved')
    price = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0.00)
    photo = models.ImageField(upload_to='books', default='static/Question_mark_(black).svg.png')

    def __str__(self):
        return self.title