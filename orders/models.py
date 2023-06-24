from django.db import models
from main_page.models import UserAccount, SellerData


STATE_CHOICES = (
    ('creating', 'Создание заказа'),
    ('auction', 'Аукцион'),
    ('new', 'Новый'),
    ('confirmed', 'Подтвержден'),
    ('assembled', 'Собран'),
    ('sent', 'Отправлен'),
    ('delivered', 'Доставлен'),
    ('canceled', 'Отменен'),
)


class OrderModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True)
    order_time = models.DateTimeField('Дата создания заказа', auto_now=True)
    order_description = models.CharField('Описание заказа', max_length=300, blank=True)
    state = models.CharField(verbose_name='Статус', choices=STATE_CHOICES, max_length=15)

    class Meta:
        verbose_name = 'Заказ состоящий из продуктов'
        verbose_name_plural = 'Заказ состоящий из продуктов'

    def __str__(self):
        return 'id:' + ' ' + str(self.id) + ' - ' + str(self.order_time)


# создаем путь - папка image далее папка(id пользователя), далее папка(id продукта)
def nameFile(instance, filename):
    return '/'.join(['images', str(instance.order_id.user_account.id), str(instance.order_id.id), filename])


class OrderImageModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    order_id = models.ForeignKey(OrderModel, related_name='order_id', on_delete=models.CASCADE, null=False)
    image_1 = models.ImageField(upload_to=nameFile, blank=True, null=True)
    image_2 = models.ImageField(upload_to=nameFile, blank=True, null=True)
    image_3 = models.ImageField(upload_to=nameFile, blank=True, null=True)
    image_4 = models.ImageField(upload_to=nameFile, blank=True, null=True)
    image_5 = models.ImageField(upload_to=nameFile, blank=True, null=True)
    image_6 = models.ImageField(upload_to=nameFile, blank=True, null=True)

    class Meta:
        verbose_name = 'Изображения - заказ пользователя'
        verbose_name_plural = 'Изображения - заказ пользователя'

    def __str__(self):
        return str(self.id)




class OrderOffer(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True)
    order_id = models.ForeignKey(OrderModel, on_delete=models.CASCADE, null=True)
    offer_create_at = models.DateTimeField('Дата создания офера', auto_now=True)
    offer_price = models.CharField('Цена офера', max_length=300, blank=True)
    offer_execution_time = models.CharField('Время выполнения офера', max_length=300, blank=True)
    offer_description = models.CharField('Описание офера', max_length=300, blank=True)
    offer_status = models.BooleanField('Принят офер или нет', default=False)

    class Meta:
        verbose_name = 'Офер'
        verbose_name_plural = 'Офер'

    def __str__(self):
        return 'офер на заказ №' + ' ' + str(self.order_id)

