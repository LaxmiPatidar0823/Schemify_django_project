from django.db import models

# Create your models here.
class Userdata(models.Model):


  user_name = models.CharField(max_length=100)
  user_age = models.IntegerField(default=18)
  user_category = models.CharField( max_length=50 , null=False, blank=False)
  user_state = models.CharField(max_length=100, null=True, blank=True )
  user_annualincome = models.CharField(max_length=100, null=True,blank=True)
  user_profession = models.CharField(max_length=100, null=True, blank=True)
  user_gender = models.CharField(max_length=60)
  
  def __str__(self) -> str:
    return self.user_name
      
  class Meta:
    ordering = ['user_name']
        
        
class SchemeData(models.Model):
      scheme_name = models.CharField(max_length = 100)
      scheme_caste = models.CharField(max_length = 100)
      scheme_annualIncome = models.IntegerField()
      scheme_gender = models.CharField(max_length=100, default='All')
      scheme_age = models.IntegerField(default=1)
      scheme_Minage = models.IntegerField(default=1)
      scheme_education_level = models.CharField(max_length = 100, default='NAN')
      scheme_benefits = models.TextField(default='NAN')
      def __str__(self) -> str:
        return self.scheme_name
     
     
      class Meta:
        ordering = ['scheme_name']