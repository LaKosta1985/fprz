from django.db import models
from django_resized import ResizedImageField
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from PIL import Image

CHOICES_GENDER = (
    ("мужской", "мужской"),
    ("женский", "женский"),
)

CHOICES_equipment = (
    ("классика", "классика"),
    ("экипировка", "экипировка"),
)
CHOICES_сompetition = (
    ("троеборье", "троеборье"),
    ("жим", "жим"),
)
CHOICES_category = (
    ("53", "53"),
    ("59", "59"),
    ("66", "66"),
    ("74", "74"),
    ("83", "83"),
    ("93", "93"),
    ("105", "105"),
    ("120", "120"),
    ("120+", "120+"),
    ("43", "43-жен"),
    ("47", "47-жен"),
    ("52", "52-жен"),
    ("57", "57-жен"),
    ("63", "63-жен"),
    ("69", "69-жен"),
    ("72", "72-жен"),
    ("76", "76-жен"),
    ("84", "84-жен"),
    ("84+", "84+-жен"),
)


CHOICES_DISCPLINA = (
    ("ТЭ", "ТЭ"),
    ("ТК", "ТК"),
    ("ЖЭ", "ЖЭ"),
    ("ЖК", "ЖК"),
    ("Все дисциплины", "Все дисциплины"),
)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "news/{0}/{1}".format(instance.title, filename)


class New(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст")
    img_Head = models.ImageField(upload_to=user_directory_path,verbose_name="Аватарка ленты")
    date = models.DateTimeField(blank=True, null=True,verbose_name="Дата новости")
    count_view = models.IntegerField(blank=True, null=True, default=1,verbose_name="Счетчик просмотров")
    img_Body_1 = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True, verbose_name="Фото1 ленты"
    )
    img_Body_2 = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True, verbose_name="Фото2 ленты"
    )
    img_Body_3 = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True, verbose_name="Фото3 ленты"
    )
    img_Body_4 = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True, verbose_name="Фото4 ленты"
    )
    img_Body_5 = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True, verbose_name="Фото5 ленты"
    )
    img_Body_6 = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True, verbose_name="Фото6 ленты"
    )
    video = models.URLField(blank=True, null=True,verbose_name="ссылка с ютуб")
    like = models.IntegerField(blank=True, null=True, default=1,verbose_name="Лайки(не собаки)")
    

    class Meta:
        db_table = "new"
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
    def save(self):
        super().save()  # saving image first
        try:
            img = Image.open(self.img_Head.path) # Open image using self

            if img.height > 1200 or img.width > 1200:
                new_img = (1200, 700)
                img.thumbnail(new_img)
                img.save(self.img_Head.path)  # saving image at the same path
        except():
            print("Ошибка")


@receiver(pre_delete, sender=New)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.img_Head.delete(False)


class Doc(models.Model):
    docpath = models.FileField(upload_to="doc/doc/")
    title = models.CharField(max_length=100, verbose_name="Заголовок")

    class Meta:
        db_table = "doc"
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title


class Table_Norm(models.Model):
    title = models.CharField(max_length=100, verbose_name="Нормативы")
    gender = models.CharField(
        max_length=100, verbose_name="Пол", choices=CHOICES_GENDER
    )
    equipment = models.CharField(
        max_length=100, verbose_name="Экипировка", choices=CHOICES_equipment
    )
    Competition = models.CharField(
        max_length=100, verbose_name="Упражнение", choices=CHOICES_сompetition
    )
    note = models.TextField(verbose_name="Примечание", null=True, blank=True)

    class Meta:
        db_table = "norm"
        verbose_name = "Таблица с нормативом"
        verbose_name_plural = "Таблица с нормативом"

    def __str__(self):
        return self.title


class Table_Cat(models.Model):
    category = models.CharField(
        max_length=100, verbose_name="Категории", choices=CHOICES_category
    )
    third_j = models.CharField(verbose_name="Третий юн.", null=True)
    second_j = models.CharField(verbose_name="Второй юн.", null=True)
    first_j = models.CharField(verbose_name="Первый юн.", null=True)
    third = models.CharField(verbose_name="Третий", null=True)
    second = models.CharField(verbose_name="Второй", null=True)
    first = models.CharField(verbose_name="Первый", null=True)
    kms = models.CharField(verbose_name="КМС", null=True)
    ms = models.CharField(verbose_name="МС", null=True)
    msmk = models.CharField(verbose_name="МСМК", null=True)
    cut = models.ForeignKey("Table_Norm", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "cut"
        verbose_name = "Категория норматива"
        verbose_name_plural = "Категория норматива"

    def __str__(self):
        return self.category


class Calendar(models.Model):
    status = models.CharField(max_length=100, verbose_name="Статус")
    dopusk = models.CharField(verbose_name="Допуск", max_length=100)
    name = models.TextField(verbose_name="Название соревнований")
    disciplina = models.CharField(verbose_name="Дисциплина", choices=CHOICES_DISCPLINA)
    vozrast = models.CharField(verbose_name="Возрастная группа", max_length=100)
    start = models.DateField(blank=True, null=True, verbose_name="Начало соревнований")
    finish = models.DateField(blank=True, null=True, verbose_name="Конец соревнований")
    place = models.CharField(max_length=100, verbose_name="Место соревнований")
    srok = models.DateField(blank=True, null=True, verbose_name="Срок приема заявок")
    srokEdit = models.DateField(
        blank=True, null=True, verbose_name="Срок редактирования заявок"
    )
    zayav = models.CharField(
        blank=True, null=True, verbose_name="Ссылка на заявку, если нужно"
    )

    class Meta:
        db_table = "calendar"
        verbose_name = "Календарь"
        verbose_name_plural = "Календарь"

    def __str__(self):
        return self.name


class Table_Record(models.Model):
    title = models.CharField(max_length=100, verbose_name="Таблица рекорда")
    gender = models.CharField(
        max_length=100, verbose_name="Пол", choices=CHOICES_GENDER
    )
    equipment = models.CharField(
        max_length=100, verbose_name="Экипировка", choices=CHOICES_equipment
    )
    Competition = models.CharField(
        max_length=100, verbose_name="Упражнение", choices=CHOICES_сompetition
    )

    class Meta:
        db_table = "record"
        verbose_name = "Добавление\редактирование таблицы рекорда"
        verbose_name_plural = "Добавление\редактирование таблицы рекорда"

    def __str__(self):
        return self.title


class Table_Cat_Record(models.Model):
    category = models.CharField(
        max_length=100, verbose_name="Категории", choices=CHOICES_category
    )
    squat_name = models.CharField(
        max_length=100, verbose_name="Имя рекордсмена в приседе", blank=True, null=True
    )
    squat = models.FloatField(
        max_length=100,
        verbose_name="Приседание, кг",
        blank=True,
        null=True,
    )
    date_squat = models.DateField(
        blank=True, null=True, verbose_name="Дата рекорда в приседании"
    )
    place_squat = models.CharField(
        max_length=100, verbose_name="Место рекорда в приседании", blank=True, null=True
    )

    press_name = models.CharField(max_length=100, verbose_name="Имя рекордсмена в жиме")
    press = models.FloatField(max_length=100, verbose_name="Жим, кг")
    date_press = models.DateField(
        blank=True, null=True, verbose_name="Дата рекорда в жиме"
    )
    place_press = models.CharField(max_length=100, verbose_name="Место рекорда в жиме")

    lift_name = models.CharField(
        max_length=100, verbose_name="Имя рекордсмена в тяге", blank=True, null=True
    )
    lift = models.FloatField(
        max_length=100,
        verbose_name="Тяга, кг",
        blank=True,
        null=True,
    )
    date_lift = models.DateField(
        blank=True, null=True, verbose_name="Дата рекорда в тяге"
    )
    place_lift = models.CharField(
        max_length=100, verbose_name="Место рекорда в тяге", blank=True, null=True
    )

    sum_name = models.CharField(
        max_length=100, verbose_name="Имя рекордсмена в сумме", blank=True, null=True
    )
    sum = models.FloatField(
        max_length=100,
        verbose_name="Сумма, кг",
        blank=True,
        null=True,
    )
    date_sum = models.DateField(
        blank=True, null=True, verbose_name="Дата рекорда в сумме"
    )
    place_sum = models.CharField(
        max_length=100, verbose_name="Место рекорда, сумма", blank=True, null=True
    )

    cut_rec = models.ForeignKey("Table_Record", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "cut_rec"
        verbose_name = "Добавление\редактирование рекорда"
        verbose_name_plural = "Добавление\редактирование рекорда"

    def __str__(self):
        return self.category


def foto_directory_path(instance, filename):
    return "img//{0}/{1}".format(instance.title, filename)

class Foto(models.Model):
    title = models.CharField(
        max_length=20, verbose_name="Заголовок альбома", blank=True, null=True
    )
    name = models.CharField(
        max_length=100, verbose_name="Описание альбома", blank=True, null=True
    )
    image = models.ImageField(
        upload_to=foto_directory_path,
        blank=True,
        null=True,
        verbose_name="Аватар альбома",
    )
    date = models.DateField(
        blank=True, null=True, verbose_name="Дата опубликования альбома"
    )
    class Meta:
        db_table = "Albom"
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    def __str__(self):
        return self.title
    def save(self):
        super().save()  # saving image first
        try:
            img = Image.open(self.image.path) # Open image using self

            if img.height > 300 or img.width > 300:
                new_img = (300, 300)
                img.thumbnail(new_img)
                img.save(self.image.path)  # saving image at the same path
        except:
            print("Ошибка")