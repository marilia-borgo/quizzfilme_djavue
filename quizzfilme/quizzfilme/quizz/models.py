from django.db import models


class Personalidade(models.Model):
    resultado = models.CharField(max_length=512)

    def to_dict_json(self):
        return {
            'id': self.id,
            'resultado': self.resultado,
        }

# Create your models here.
