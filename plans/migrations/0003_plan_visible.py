# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='visible',
            field=models.BooleanField(default=True, help_text='Is visible in current offer', db_index=True, verbose_name='visible'),
            preserve_default=True,
        ),
    ]
