from django.db import models
from main_page.models import UserAccount
from orders.models import OrderModel


class CardModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField('тип - кухня, гостиная', max_length=20, null=True)

    class Meta:
        verbose_name = 'Тип комнаты - CardModel'
        verbose_name_plural = 'Тип комнаты - CardModel'

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    card = models.ManyToManyField(CardModel)
    name = models.CharField('тип мебели - кровать, ящик... ', max_length=20, null=True)

    class Meta:
        verbose_name = 'Тип мебели - Category'
        verbose_name_plural = 'Тип мебели - Category'

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=False,  blank=True)
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, null=True,  blank=True)
    product_price = models.IntegerField('цена предмета', null=True, blank=True)
    product_size = models.CharField('размеры высота x ширина x длина', max_length=20, null=True, blank=True)
    product_description = models.CharField('описание', max_length=350, null=True, blank=True)
    product_units = models.IntegerField('количество предметов в шт.', null=True, blank=True)
    is_ended = models.BooleanField('завершено ли создание предмета заказа?', default=False)

    class Meta:
        verbose_name = 'Предмет для заказа'
        verbose_name_plural = 'Предмет для заказа'

    def __str__(self):
        return str(self.id)


# создаем путь - папка image далее папка(id пользователя), далее папка(id продукта)
def nameFile(instance, filename):
    return '/'.join(['images', str(instance.order_id.user_account.id), str(instance.order_id.id), filename])


class QuestionsProductsModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=False)
    question = models.CharField('вопрос по заказу', max_length=120, null=True, blank=True)
    position = models.IntegerField('номер вопроса по порядку', null=True, blank=True)

    class Meta:
        verbose_name = 'Бланк вопросов'
        verbose_name_plural = 'Бланк вопросов'

    def __str__(self):
        return 'id - ' + str(self.id) + ' ' + self.question


class QuestionOptionsModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    question = models.ForeignKey(QuestionsProductsModel, on_delete=models.CASCADE, null=False, blank=True)
    option = models.CharField('вариант ответа', max_length=120, null=True, blank=True)

    class Meta:
        verbose_name = 'Опции'
        verbose_name_plural = 'Опции'

    def __str__(self):
        return 'id - ' + str(self.id) + ' ' + self.option


class ResponseModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    question = models.ForeignKey(QuestionsProductsModel, on_delete=models.CASCADE, null=False)
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=False)
    response = models.CharField('ответ по заказу', max_length=120, null=True, blank=True)
    position = models.CharField('номер ответа по порядку', max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = 'Бланк ответов клиента'
        verbose_name_plural = 'Бланк ответов клиента'

    def __str__(self):
        return str(self.id)


