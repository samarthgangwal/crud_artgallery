from django.db import models
import datetime
# Create your models here.

class Seller(models.Model): 

     # For Gender
    Male = 'M'
    Female = 'F'
    Others = 'O'
    Unspecified = 'U'
    GENDER = [('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),]
    ## Ends

    # For Categories
    Contemporary = 'C'
    Pop = 'P'
    Impressionism = 'I'
    Surrealism = 'S'
    CATEGORY = [('Contemporary','Contemporary'),
         ('Pop', 'Pop'),
         ('Impressionism', 'Impressionism'),
         ('Surrealism', 'Surrealism')]
    ## Ends

    Bidval = 0

    sid = models.IntegerField()  

    sfname = models.CharField(max_length=100)
    slname = models.CharField(max_length=100)
    saddress = models.TextField(max_length=100)  
    semail = models.EmailField() 
      
    sgender = models.CharField(
        max_length=8,
         choices=GENDER,
         default=Unspecified,
     )
    

    scategory = models.CharField(
           max_length=15,
           choices=CATEGORY,
           default=Unspecified,
       )
    tnc = models.BooleanField(
           default=False,
       )
    sbid = models.FloatField(
           max_length=10,
           default=Bidval,
       )
    sdate = models.DateField(default=datetime.date.today) 

    class Meta:  
        db_table = "seller"  