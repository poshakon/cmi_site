from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    id_event = models.IntegerField(primary_key=True)
    login = models.ForeignKey(
        'Organizer', models.DO_NOTHING, db_column='login', blank=True, null=True, verbose_name='Пользователь')
    name_event = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название события')
    document = models.FileField(upload_to='event_docs', blank=True, null=True, verbose_name='Документ')
    logo = models.ImageField(upload_to='event', blank=True, null=True, verbose_name='Логотип')
    id_level = models.ForeignKey(
        'Level', models.DO_NOTHING, db_column='id_level', blank=True, null=True, verbose_name='Уровень')
    id_type = models.ForeignKey(
        'EventType', models.DO_NOTHING, db_column='id_type', blank=True, null=True, verbose_name='Тип события')

    def __str__(self):
        return '%s' % self.name_event

    class Meta:
        managed = True
        db_table = 'event'
        verbose_name_plural = 'События'


class EventType(models.Model):
    id_type = models.IntegerField(primary_key=True)
    name_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Наименование типа')

    def __str__(self):
        return '%s' % self.name_type

    class Meta:
        managed = True
        db_table = 'event_type'
        verbose_name_plural = 'Типы событий'


class Level(models.Model):
    id_level = models.IntegerField(primary_key=True)
    name_level = models.CharField(max_length=200, blank=True, null=True, verbose_name='Наименование уровня')

    def __str__(self):
        return '%s' % self.name_level

    class Meta:
        managed = True
        db_table = 'level'
        verbose_name_plural = 'Уровни'


class ListPart(models.Model):
    login = models.ForeignKey(
        'Participant', models.DO_NOTHING, db_column='login', verbose_name='Пользователь')
    id_notice = models.ForeignKey(
        'Notice', models.DO_NOTHING, db_column='id_notice', verbose_name='Мероприятие')
    date_record = models.DateField(blank=True, null=True, verbose_name='Дата записи')

    class Meta:
        managed = True
        db_table = 'list_part'
        unique_together = (('login', 'id_notice'),)
        verbose_name_plural = 'Списки участников'


class News(models.Model):
    id_news = models.IntegerField(primary_key=True)
    information = models.TextField(blank=True, null=True, verbose_name='Информация')
    photos = models.ImageField(upload_to='news', blank=True, null=True, verbose_name='Фото')
    id_notice = models.ForeignKey(
        'Notice', models.DO_NOTHING, db_column='id_notice', blank=True, null=True, verbose_name='Мероприятие')
    date_news = models.DateField(blank=True, null=True, verbose_name='Дата')

    def __str__(self):
        return '%s...' % self.information[:20]

    class Meta:
        managed = True
        db_table = 'news'
        verbose_name_plural = 'Новости'


class Notice(models.Model):
    id_notice = models.IntegerField(primary_key=True)
    id_event = models.ForeignKey(
        Event, models.DO_NOTHING, db_column='id_event', blank=True, null=True, verbose_name='Событие')
    id_purpose = models.ForeignKey(
        'Purpose', models.DO_NOTHING, db_column='id_purpose', blank=True, null=True, verbose_name='Цель')
    date_notice = models.DateField(blank=True, null=True, verbose_name='Дата')
    max_part = models.IntegerField(blank=True, null=True, verbose_name='Максимальное кол-во участников')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    time_n = models.TimeField(blank=True, null=True, verbose_name='Время')
    location = models.CharField(max_length=300, blank=True, null=True, verbose_name='Местоположение')
    status = models.IntegerField(blank=True, null=True, verbose_name='Статус')

    def __str__(self):
        return '%s...' % self.description[:20]

    class Meta:
        managed = True
        db_table = 'notice'
        verbose_name_plural = 'Мероприятия'


class Organizer(models.Model):
    login = models.OneToOneField(
        User, models.DO_NOTHING, db_column='login', primary_key=True, verbose_name='Пользователь')
    full_name_org = models.CharField(max_length=400, blank=True, null=True, verbose_name='Полное название организации')
    short_name_org = models.CharField(max_length=40, blank=True, null=True, verbose_name='Короткое название организации')
    address = models.CharField(max_length=300, blank=True, null=True, verbose_name='Адрес')
    full_name_head = models.CharField(max_length=50, blank=True, null=True, verbose_name='ФИО директора')
    email_org = models.CharField(max_length=30, blank=True, null=True, verbose_name='Email организации')
    phone_org = models.CharField(max_length=12, blank=True, null=True, verbose_name='Телефон организации')
    # Field name made lowercase.
    inn = models.BigIntegerField(db_column='INN', blank=True, null=True, verbose_name='ИНН')
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    ogrn_ogrnip = models.BigIntegerField(
        db_column='OGRN/OGRNIP', blank=True, null=True, verbose_name='ОГРН/ОГРНИП')

    def __str__(self):
        return '%s' % self.short_name_org

    class Meta:
        managed = True
        db_table = 'organizer'
        verbose_name_plural = 'Организаторы'


class Participant(models.Model):
    login = models.OneToOneField(
        User, models.DO_NOTHING, db_column='login', primary_key=True, verbose_name='Пользователь')
    full_name_part = models.CharField(max_length=60, blank=True, null=True, verbose_name='ФИО')
    date_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    email_part = models.CharField(max_length=30, blank=True, null=True, verbose_name='Email')
    passport = models.CharField(max_length=10, blank=True, null=True, verbose_name='Серия и номер паспорта')
    phone_part = models.CharField(max_length=12, blank=True, null=True, verbose_name='Телефон')

    def __str__(self):
        return '%s' % self.full_name_part

    class Meta:
        managed = True
        db_table = 'participant'
        verbose_name_plural = 'Участники'


class Purpose(models.Model):
    id_purpose = models.IntegerField(primary_key=True)
    name_purpose = models.CharField(max_length=200, blank=True, null=True, verbose_name='Наименование предназначения')

    def __str__(self):
        return '%s' % self.name_purpose

    class Meta:
        managed = True
        db_table = 'purpose'
        verbose_name_plural = 'Цели'


class Criteria(models.Model):
    name_criteria = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя критерия')
    weight = models.FloatField(verbose_name='Вес')
    maximum = models.IntegerField(verbose_name='Максимум оценки')
    minimum = models.IntegerField(verbose_name='Минимум оценки')

    def __str__(self):
        return '%s' % self.name_criteria

    class Meta:
        managed = True
        db_table = 'criteria'
        verbose_name_plural = 'Критерии'


class Rating(models.Model):
    login = models.ForeignKey(
        'Participant', models.DO_NOTHING, db_column='login', blank=True, verbose_name='Пользователь')
    id_notice = models.ForeignKey(
        'Notice', models.DO_NOTHING, db_column='id_notice', blank=True, null=True, verbose_name='Мероприятие')
    id_criteria = models.ForeignKey(
        'Criteria', models.DO_NOTHING, blank=True, null=True, verbose_name='Критерий')
    evaluation = models.IntegerField(default=0, verbose_name='Оценка')

    def __str__(self):
        return '%s: %s (крит. %s, соб. %s)' % (self.login, self.evaluation, self.id_criteria, self.id_notice)

    class Meta:
        managed = True
        db_table = 'rating'
        verbose_name_plural = 'Рейтинги'
