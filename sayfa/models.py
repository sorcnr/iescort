from datetime import timedelta
from email.policy import default
from django.db import models
from multiselectfield import MultiSelectField
from tinymce.models import HTMLField
#from sayfa.views import escort_view
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Eskort(models.Model):
    class Rank(models.IntegerChoices):
        GOLD = 1
        SILVER = 2
        BRONZE = 3

    class Status(models.IntegerChoices):
        ACIK = 1
        KAPALI = 0

    class Ilceler(models.TextChoices):
        aliaga = 'Aliağa'
        balcova = 'Balçova'
        bayrakli = 'Bayraklı'
        bornova = 'Bornova'
        buca = 'Buca'
        cesme = 'Çeşme'
        cigli = 'Çiğli'
        gaziemir = 'Gaziemir'
        guzelbahce = 'Güzelbahçe'
        karabaglar = 'Karabağlar'
        karaburun = 'Karaburun'
        karsiyaka = 'Karşıyaka'
        konak = 'Konak'
        menemen = 'Menemen'
        narlidere = 'Narlıdere'
        seferihisar = 'Seferihisar'
        urla = 'Urla'

    name = models.CharField(_("İsim"),max_length=100)
    tel = models.CharField(_("Telefon"),max_length=20)
    text = HTMLField(_("Açıklama"))
    duration = models.DurationField(_("Süre"),default=timedelta(days=7))
    ilceler = MultiSelectField(_("İlçeler"),max_length=200, choices=Ilceler.choices,default=Ilceler.buca)
    rank = models.IntegerField(choices=Rank.choices)
    status = models.IntegerField(_("Durum"),choices=Status.choices, default=1)
    

    def get_absolute_url(self):
        return reverse("escort_view", kwargs={"id": self.id})
    def __str__(self):
        return f"{self.name} ({self.tel})"

class Image(models.Model):

    img = models.ImageField(upload_to='esc-img')
    esc = models.ForeignKey(Eskort, on_delete=models.CASCADE,related_name="images")

class Blog(models.Model):
    title = models.CharField(_("Başlık"), max_length=100)
    text = HTMLField(_("Metin"))
    date = models.DateField(_("Tarih"), auto_now=True)  

class KeyWord(models.Model):
    class WordChoices(models.TextChoices):
        buca_escort = "Buca Escort"
        izmir_buca_escort = "İzmir Buca Escort"
        buca_escort_bayanlar = "Buca Escort Bayanlar"
        buca_escort_bayan = "Buca Escort Bayan"
        bornova_escort = "Bornova Escort"
        izmir_bornova_escort = "İzmir Bornova Escort"
        alsancak_escort = "Alsancak Escort"
        izmir_alsancak_escort = "İzmir Alsancak Escort"
        izmir_escort = "İzmir Escort"
        izmir_escort_bayanlar = "İzmir Escort Bayanlar"
        izmir_escort_bayan = "İzmir Escort Bayan"
        izmir_escort_kizlar = "İzmir Escort Kızlar"

    key = models.CharField(_("Keyword"),choices=WordChoices.choices, max_length=50)
    blog = models.ForeignKey("Blog", related_name=_("keywords"), on_delete=models.CASCADE)

   

