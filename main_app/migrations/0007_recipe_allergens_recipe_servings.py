# Generated by Django 4.0.3 on 2022-05-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_recipe_ingredients_ingredient_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='allergens',
            field=models.CharField(default=' ', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
