# Generated by Django 4.1.4 on 2023-08-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bba',
            name='first_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bba',
            name='fourth_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bba',
            name='second_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bba',
            name='third_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bbatemp',
            name='first_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bbatemp',
            name='fourth_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bbatemp',
            name='second_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bbatemp',
            name='third_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mba',
            name='cat_or_cmat_rank',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mba',
            name='cat_or_cmat_rollno',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mba',
            name='first_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mba',
            name='fourth_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mba',
            name='second_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mba',
            name='third_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mbatemp',
            name='cat_or_cmat_rank',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mbatemp',
            name='cat_or_cmat_rollno',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mbatemp',
            name='first_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mbatemp',
            name='fourth_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mbatemp',
            name='second_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mbatemp',
            name='third_subject_12th',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
