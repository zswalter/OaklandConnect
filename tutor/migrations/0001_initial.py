# Generated by Django 2.1.7 on 2019-04-10 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mon_start', models.CharField(choices=[('1:00', '1AM'), ('2:00', '2AM'), ('3:00', '3AM'), ('4:00', '4AM'), ('5:00', '5AM'), ('6:00', '6AM'), ('7:00', '7AM'), ('8:00', '8AM'), ('9:00', '9AM'), ('10:00', '10AM'), ('11:00', '11AM'), ('12:00', '12PM'), ('13:00', '1PM'), ('14:00', '2PM'), ('15:00', '3PM'), ('16:00', '4PM'), ('17:00', '5PM'), ('18:00', '6PM'), ('19:00', '7PM'), ('20:00', '8PM'), ('21:00', '9PM'), ('22:00', '10PM'), ('23:00', '11PM'), ('24:00', '12AM')], max_length=200)),
                ('mon_end', models.CharField(choices=[('1:00', '1AM'), ('2:00', '2AM'), ('3:00', '3AM'), ('4:00', '4AM'), ('5:00', '5AM'), ('6:00', '6AM'), ('7:00', '7AM'), ('8:00', '8AM'), ('9:00', '9AM'), ('10:00', '10AM'), ('11:00', '11AM'), ('12:00', '12PM'), ('13:00', '1PM'), ('14:00', '2PM'), ('15:00', '3PM'), ('16:00', '4PM'), ('17:00', '5PM'), ('18:00', '6PM'), ('19:00', '7PM'), ('20:00', '8PM'), ('21:00', '9PM'), ('22:00', '10PM'), ('23:00', '11PM'), ('24:00', '12AM')], max_length=200)),
                ('tue_start', models.CharField(choices=[('1:00', '1AM'), ('2:00', '2AM'), ('3:00', '3AM'), ('4:00', '4AM'), ('5:00', '5AM'), ('6:00', '6AM'), ('7:00', '7AM'), ('8:00', '8AM'), ('9:00', '9AM'), ('10:00', '10AM'), ('11:00', '11AM'), ('12:00', '12PM'), ('13:00', '1PM'), ('14:00', '2PM'), ('15:00', '3PM'), ('16:00', '4PM'), ('17:00', '5PM'), ('18:00', '6PM'), ('19:00', '7PM'), ('20:00', '8PM'), ('21:00', '9PM'), ('22:00', '10PM'), ('23:00', '11PM'), ('24:00', '12AM')], max_length=200)),
                ('tue_end', models.CharField(choices=[('1:00', '1AM'), ('2:00', '2AM'), ('3:00', '3AM'), ('4:00', '4AM'), ('5:00', '5AM'), ('6:00', '6AM'), ('7:00', '7AM'), ('8:00', '8AM'), ('9:00', '9AM'), ('10:00', '10AM'), ('11:00', '11AM'), ('12:00', '12PM'), ('13:00', '1PM'), ('14:00', '2PM'), ('15:00', '3PM'), ('16:00', '4PM'), ('17:00', '5PM'), ('18:00', '6PM'), ('19:00', '7PM'), ('20:00', '8PM'), ('21:00', '9PM'), ('22:00', '10PM'), ('23:00', '11PM'), ('24:00', '12AM')], max_length=200)),
                ('wed_start', models.CharField(choices=[('1:00', '1AM'), ('2:00', '2AM'), ('3:00', '3AM'), ('4:00', '4AM'), ('5:00', '5AM'), ('6:00', '6AM'), ('7:00', '7AM'), ('8:00', '8AM'), ('9:00', '9AM'), ('10:00', '10AM'), ('11:00', '11AM'), ('12:00', '12PM'), ('13:00', '1PM'), ('14:00', '2PM'), ('15:00', '3PM'), ('16:00', '4PM'), ('17:00', '5PM'), ('18:00', '6PM'), ('19:00', '7PM'), ('20:00', '8PM'), ('21:00', '9PM'), ('22:00', '10PM'), ('23:00', '11PM'), ('24:00', '12AM')], max_length=200)),
                ('wed_end', models.CharField(choices=[('1:00', '1AM'), ('2:00', '2AM'), ('3:00', '3AM'), ('4:00', '4AM'), ('5:00', '5AM'), ('6:00', '6AM'), ('7:00', '7AM'), ('8:00', '8AM'), ('9:00', '9AM'), ('10:00', '10AM'), ('11:00', '11AM'), ('12:00', '12PM'), ('13:00', '1PM'), ('14:00', '2PM'), ('15:00', '3PM'), ('16:00', '4PM'), ('17:00', '5PM'), ('18:00', '6PM'), ('19:00', '7PM'), ('20:00', '8PM'), ('21:00', '9PM'), ('22:00', '10PM'), ('23:00', '11PM'), ('24:00', '12AM')], max_length=200)),
                ('thur_start', models.CharField(choices=[('1:00', '1AM'), ('2:00', '2AM'), ('3:00', '3AM'), ('4:00', '4AM'), ('5:00', '5AM'), ('6:00', '6AM'), ('7:00', '7AM'), ('8:00', '8AM'), ('9:00', '9AM'), ('10:00', '10AM'), ('11:00', '11AM'), ('12:00', '12PM'), ('13:00', '1PM'), ('14:00', '2PM'), ('15:00', '3PM'), ('16:00', '4PM'), ('17:00', '5PM'), ('18:00', '6PM'), ('19:00', '7PM'), ('20:00', '8PM'), ('21:00', '9PM'), ('22:00', '10PM'), ('23:00', '11PM'), ('24:00', '12AM')], max_length=200)),
                ('thur_end', models.CharField(choices=[('1:00', '1AM'), ('2:00', '2AM'), ('3:00', '3AM'), ('4:00', '4AM'), ('5:00', '5AM'), ('6:00', '6AM'), ('7:00', '7AM'), ('8:00', '8AM'), ('9:00', '9AM'), ('10:00', '10AM'), ('11:00', '11AM'), ('12:00', '12PM'), ('13:00', '1PM'), ('14:00', '2PM'), ('15:00', '3PM'), ('16:00', '4PM'), ('17:00', '5PM'), ('18:00', '6PM'), ('19:00', '7PM'), ('20:00', '8PM'), ('21:00', '9PM'), ('22:00', '10PM'), ('23:00', '11PM'), ('24:00', '12AM')], max_length=200)),
                ('fri_start', models.CharField(choices=[('1:00', '1AM'), ('2:00', '2AM'), ('3:00', '3AM'), ('4:00', '4AM'), ('5:00', '5AM'), ('6:00', '6AM'), ('7:00', '7AM'), ('8:00', '8AM'), ('9:00', '9AM'), ('10:00', '10AM'), ('11:00', '11AM'), ('12:00', '12PM'), ('13:00', '1PM'), ('14:00', '2PM'), ('15:00', '3PM'), ('16:00', '4PM'), ('17:00', '5PM'), ('18:00', '6PM'), ('19:00', '7PM'), ('20:00', '8PM'), ('21:00', '9PM'), ('22:00', '10PM'), ('23:00', '11PM'), ('24:00', '12AM')], max_length=200)),
                ('fri_end', models.CharField(choices=[('1:00', '1AM'), ('2:00', '2AM'), ('3:00', '3AM'), ('4:00', '4AM'), ('5:00', '5AM'), ('6:00', '6AM'), ('7:00', '7AM'), ('8:00', '8AM'), ('9:00', '9AM'), ('10:00', '10AM'), ('11:00', '11AM'), ('12:00', '12PM'), ('13:00', '1PM'), ('14:00', '2PM'), ('15:00', '3PM'), ('16:00', '4PM'), ('17:00', '5PM'), ('18:00', '6PM'), ('19:00', '7PM'), ('20:00', '8PM'), ('21:00', '9PM'), ('22:00', '10PM'), ('23:00', '11PM'), ('24:00', '12AM')], max_length=200)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]