from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dealers.models import Dealer, Review, CarMake

class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        u,_=User.objects.get_or_create(username="root")
        u.set_password("rootpass123"); u.is_staff=True; u.is_superuser=True; u.save()
        data=[
            ("Kansas City Motors","Kansas City","Kansas","1200 Main St","555-0101"),
            ("Wichita Auto Center","Wichita","Kansas","800 Market St","555-0102"),
            ("Denver Auto Group","Denver","Colorado","44 Central Ave","555-0103"),
        ]
        for x in data: Dealer.objects.get_or_create(name=x[0],defaults=dict(city=x[1],state=x[2],address=x[3],phone=x[4]))
        if not Review.objects.exists():
            d=Dealer.objects.first(); Review.objects.create(dealer=d,username="demo",text="Fantastic services",sentiment="positive")
        if not CarMake.objects.exists():
            for make,mods in [("Toyota",["Camry","Corolla","RAV4"]),("Honda",["Civic","Accord","CR-V"]),("Ford",["Mustang","F-150","Explorer"])]:
                CarMake.objects.create(make=make,models=mods)
        self.stdout.write(self.style.SUCCESS("Demo data seeded."))
