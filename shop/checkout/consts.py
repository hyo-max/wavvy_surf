from django.db import models


class PaymentEvents(models.TextChoices):
    paid = 'paid', '결제됨'
    cancelled = 'cancelled', '취소됨'
    refunded = 'refunded', '반품됨'
