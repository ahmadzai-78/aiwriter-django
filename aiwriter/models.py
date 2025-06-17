from django.db import models

class Document(models.Model):
    client_name = models.CharField(max_length=100)
    service = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    style = models.CharField(max_length=50, default='formel')
    generated_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.service} ({self.style})"