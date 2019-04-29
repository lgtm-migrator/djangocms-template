# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 10:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('testimonials', '0004_testimonialsteasercmsplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialLinkModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='testimonials_testimoniallinkmodel', serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=2048)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testimonials.Testimonial')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]