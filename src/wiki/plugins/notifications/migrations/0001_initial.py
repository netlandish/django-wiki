# Generated by Django 2.2.5 on 2019-10-09 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_nyt', '0008_auto_20161023_1641'),
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleSubscription',
            fields=[
                ('articleplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wiki.ArticlePlugin')),
                ('subscription', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='django_nyt.Subscription')),
            ],
            options={
                'db_table': 'wiki_notifications_articlesubscription',
                'unique_together': {('subscription', 'articleplugin_ptr')},
            },
            bases=('wiki.articleplugin',),
        ),
    ]
