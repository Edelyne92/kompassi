# Generated by Django 4.2.1 on 2023-09-03 15:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import labour.models.signup_extras


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("enrollment", "0009_alter_enrollment_is_public_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SignupExtra",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("is_active", models.BooleanField(default=True)),
                (
                    "shift_type",
                    models.CharField(
                        choices=[
                            ("yksipitka", "Yksi pitkä vuoro"),
                            ("montalyhytta", "Monta lyhyempää vuoroa"),
                            ("kaikkikay", "Kumpi tahansa käy"),
                        ],
                        help_text="Haluatko tehdä yhden pitkän työvuoron vaiko monta lyhyempää vuoroa?",
                        max_length=15,
                        verbose_name="Toivottu työvuoron pituus",
                    ),
                ),
                (
                    "total_work",
                    models.CharField(
                        choices=[("10h", "Minimi - 10 tuntia"), ("yli10h", "Työn Sankari! Yli 10 tuntia!")],
                        help_text="Kuinka paljon haluat tehdä töitä yhteensä tapahtuman aikana? Minimi on pääsääntöisesti kymmenen tuntia.",
                        max_length=15,
                        verbose_name="Toivottu kokonaistyömäärä",
                    ),
                ),
                (
                    "overseer",
                    models.BooleanField(
                        default=False,
                        help_text="Vuorovastaavat ovat kokeneempia conityöläisiä, jotka toimivat oman tehtäväalueensa tiiminvetäjänä.",
                        verbose_name="Olen kiinnostunut vuorovastaavan tehtävistä",
                    ),
                ),
                (
                    "want_certificate",
                    models.BooleanField(default=False, verbose_name="Haluan todistuksen työskentelystäni"),
                ),
                (
                    "special_diet_other",
                    models.TextField(
                        blank=True,
                        help_text="Jos noudatat erikoisruokavaliota, jota ei ole yllä olevassa listassa, ilmoita se tässä. Tapahtuman järjestäjä pyrkii ottamaan erikoisruokavaliot huomioon, mutta kaikkia erikoisruokavalioita ei välttämättä pystytä järjestämään.",
                        verbose_name="Muu erikoisruokavalio",
                    ),
                ),
                (
                    "prior_experience",
                    models.TextField(
                        blank=True,
                        help_text="Kerro tässä kentässä, jos sinulla on aiempaa kokemusta vastaavista tehtävistä tai muuta sellaista työkokemusta, josta arvioit olevan hyötyä hakemassasi tehtävässä.",
                        verbose_name="Työkokemus",
                    ),
                ),
                (
                    "free_text",
                    models.TextField(
                        blank=True,
                        help_text="Jos haluat sanoa hakemuksesi käsittelijöille jotain sellaista, jolle ei ole omaa kenttää yllä, käytä tätä kenttää.",
                        verbose_name="Vapaa alue",
                    ),
                ),
                (
                    "shift_wishes",
                    models.TextField(
                        blank=True,
                        help_text="Jos tiedät, ettet pääse paikalle johonkin tiettyyn aikaan tai haluat esimerkiksi osallistua johonkin tiettyyn ohjelmanumeroon, mainitse siitä tässä. HUOM! Muistathan mainita kellonajat (myös ohjelmanumeroista).",
                        verbose_name="Työvuorotoiveet",
                    ),
                ),
                (
                    "email_alias",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Coniitit saavat käyttöönsä nick@kotae.fi-tyyppisen sähköpostialiaksen, joka ohjataan coniitin omaan sähköpostilaatikkoon. Tässä voit toivoa haluamaasi sähköpostialiaksen alkuosaa eli sitä, joka tulee ennen @kotae.fi:tä. Sallittuja merkkejä ovat pienet kirjaimet a-z, numerot 0-9 sekä väliviiva.",
                        max_length=32,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.",
                                regex="[a-z0-9-]+",
                            )
                        ],
                        verbose_name="Sähköpostialias",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_signup_extras",
                        to="core.event",
                    ),
                ),
                (
                    "person",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_signup_extra",
                        to="core.person",
                    ),
                ),
                (
                    "special_diet",
                    models.ManyToManyField(
                        blank=True,
                        related_name="kotaeexpo2024_signup_extras",
                        to="enrollment.specialdiet",
                        verbose_name="Erikoisruokavalio",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(labour.models.signup_extras.SignupExtraMixin, models.Model),
        ),
    ]
