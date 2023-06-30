from django.db import models

class Base(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)

    class Meta:
        abstract = True

class activities(Base):
    value = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    input = models.BooleanField('Entrada?', default=True)
    description = models.TextField('Descrição', max_length=200)
    
    BANK_CHOICES = (
        ('Picpay', 'Picpay'),
        ('Nubank', 'Nubank'),
        ('Banco do Brasil', 'Banco do Brasil'),
        ('Espécie', 'Espécie'),
    )

    bank = models.CharField(max_length=15, choices=BANK_CHOICES)

    proof = models.FileField(upload_to='comprovantes/', blank=True, null=True)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
    
    def __str__(self):
        return self.value
