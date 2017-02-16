# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=40, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
