from django.db import models


class Contact(models.Model):
    STATUSES = [("N", "New contact"), ("P", "In process"), ("D", "Processed")]

    name = models.CharField(max_length=30, verbose_name="User name")
    email = models.EmailField(verbose_name="User email")
    subject = models.CharField(max_length=50, verbose_name="Subject")
    message = models.TextField(max_length=500, verbose_name="Message")
    status = models.CharField(max_length=1, choices=STATUSES, default="N", verbose_name="Contact status")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created time")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated time")

    class Meta:
        db_table = "contact"
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name
