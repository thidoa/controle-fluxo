from django.db import models

class Base(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)

    class Meta:
        abstract = True

class Bank(Base):
    name = models.CharField('Name', max_length=100)
    value = models.DecimalField('Value', max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'
    
    def __str__(self):
        return self.name
    
class Owner(Base):
    name = models.CharField('Name', max_length=100)
    value = models.DecimalField('Value', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'

    def __str__(self):
        return self.name

class Activities(Base):
    value = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    input = models.BooleanField('Entrada?', default=True)
    description = models.TextField('Descrição', max_length=200)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    proof = models.FileField(upload_to='comprovantes/', blank=True, null=True)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
    
    def __str__(self):
        return str(self.value)
