from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='customer/avatars/',blank=True,null=True)
    phone_number = models.CharField(max_length=50,blank =True,verbose_name ='Номер телефона',help_text="Номер телефона")
    stripe_customer_id = models.CharField(max_length = 255,blank=True)
    stripe_payment_method_id = models.CharField(max_length = 255,blank=True)
    stripe_card_last4 = models.CharField(max_length = 255,blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Courier(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  lat = models.FloatField(default=0)
  lng = models.FloatField(default=0)
  paypal_email = models.EmailField(max_length=255, blank=True)
  fcm_token = models.TextField(blank=True)

  def __str__(self):
    return self.user.get_full_name()


class Category(models.Model):
    slug = models.CharField(max_length=225,unique =True)
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Job(models.Model):
  SMALL_SIZE = "Размер упаковки не превышает 15х15х15см, вес не более 5 кг."
  MEDIUM_SIZE = "Размер упаковки не превышает 40х40х26см, вес не более 15 кг."
  LARGE_SIZE = "Размер упаковки не превышает 60х60х36см, вес не более 25 кг."
  SIZES = (
    (SMALL_SIZE, 'Размер упаковки не превышает 15х15х15см, вес не более 5 кг.'),
    (MEDIUM_SIZE, 'Размер упаковки не превышает 40х40х26см, вес не более 15 кг.'),
    (LARGE_SIZE, 'Размер упаковки не превышает 60х60х36см, вес не более 25 кг.'),
  )

  CREATING_STATUS = 'creating'
  PROCESSING_STATUS = 'processing'
  PICKING_STATUS = 'picking'
  DELIVERING_STATUS = 'delivering'
  COMPLETED_STATUS = 'completed'
  CANCELED_STATUS = 'canceled'
  STATUSES = (
    (CREATING_STATUS, 'Создана'),
    (PROCESSING_STATUS, 'Ожидание курьера'),
    (PICKING_STATUS, 'Курьер выполняет'),
    (DELIVERING_STATUS, 'Доставляется'),
    (COMPLETED_STATUS, 'Выполнена'),
    (CANCELED_STATUS, 'Удаленна'),
  )

  # Step 1
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name ='Пользователь',help_text="Пользователь")
  courier = models.ForeignKey(Courier, on_delete=models.CASCADE, null=True, blank=True,verbose_name ='Курьер',help_text="Курьер")
  name = models.CharField(max_length=255,verbose_name ='Название',help_text="Название")
  description = models.CharField(max_length=255,verbose_name ='Описание',help_text="Описание")
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,verbose_name ='Категория',help_text="Категория")
  size = models.CharField(max_length=70,choices=SIZES, default=SMALL_SIZE,verbose_name ='Размер',help_text="Размер")
  quantity = models.IntegerField(default=1,verbose_name ='Количество',help_text="Количество")
  photo = models.ImageField(upload_to='job/photos/',verbose_name ='Фото товара',help_text="Фото товара")
  status = models.CharField(max_length=20, choices=STATUSES, default=CREATING_STATUS,verbose_name ='Статус',help_text="Статус")
  created_at = models.DateTimeField(default=timezone.now,verbose_name ='Дата создания',help_text="Дата создания")

  # Step 2
  pickup_address = models.CharField(max_length=255,verbose_name ='Адрес получения посылки',help_text="Адрес получения посылки", blank=True)
  pickup_lat = models.FloatField(default=0,verbose_name ='Широта',help_text="Широта")
  pickup_lng = models.FloatField(default=0,verbose_name ='Долгота',help_text="Долгота")
  pickup_name = models.CharField(max_length=255, verbose_name ='Дополнительные данные',help_text="Дополнительные данные", blank=True)
  pickup_phone = models.CharField(max_length=50, verbose_name ='Номер для связи',help_text="Номер для связи", blank=True)

  # Step 3
  delivery_address = models.CharField(max_length=255, blank=True,verbose_name ='Адрес доставки посылки',help_text="Адрес доставки посылки")
  delivery_lat = models.FloatField(default=0,verbose_name ='Широта',help_text="Широта")
  delivery_lng = models.FloatField(default=0,verbose_name ='Долгота',help_text="Долгота")
  delivery_name = models.CharField(max_length=255, blank=True,verbose_name ='Дополнительные данные',help_text="Дополнительные данные")
  delivery_phone = models.CharField(max_length=50, blank=True,verbose_name ='Номер для связи',help_text="Номер для связи")

  # Step 4
  duration = models.IntegerField(default=0,verbose_name ='Продолжительность',help_text="Продолжительность")
  distance = models.FloatField(default=0,verbose_name ='Расстояние',help_text="Расстояние")
  price = models.FloatField(default=0,verbose_name ='Стоимость',help_text="Стоимость")

  # Extra info
  pickup_photo = models.ImageField(upload_to='job/pickup_photos/', null=True, blank=True,verbose_name ='Фото при получении заказа',help_text="Фото при получении заказа")
  pickedup_at = models.DateTimeField(null=True, blank=True,verbose_name ='Заказ взят в ',help_text="Заказ взят в")

  delivery_photo = models.ImageField(upload_to='job/delivery_photos/', null=True, blank=True,verbose_name ='Фото при доставке заказа',help_text="Фото при доставке заказа")
  delivered_at = models.DateTimeField(null=True, blank=True,verbose_name ='Заказ доставлен в ',help_text="Заказ доставлен в")

  def __str__(self):
    return self.name

class Transaction(models.Model):
  IN_STATUS = "in"
  OUT_STATUS = "out"
  STATUSES = (
    (IN_STATUS, 'In'),
    (OUT_STATUS, 'Out'),
  )

  stripe_payment_intent_id = models.CharField(max_length=255, unique=True)
  job = models.ForeignKey(Job, on_delete=models.CASCADE)
  amount = models.FloatField(default=0)
  status = models.CharField(max_length=20, choices=STATUSES, default=IN_STATUS)
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.stripe_payment_intent_id

