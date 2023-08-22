from django.db import models

# Create your models here.



class dept(models.Model):
    name=models.CharField(max_length=100)
    deptno=models.IntegerField(primary_key=True)
    location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.deptno
    


class emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField(null=True)
    deptno=models.ForeignKey(dept,on_delete=models.CASCADE)
    


    def __str__(self):
        return self.empno
