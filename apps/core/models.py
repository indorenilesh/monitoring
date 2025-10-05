from django.db import models

class Servers(models.Model):
    hostname = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)

    def __str__(self):
        return self.hostname
