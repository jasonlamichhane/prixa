from django.db import models

# Create your models here.
class ServerDetails(models.Model):
    servername = models.CharField(max_length=250, unique=True)
    servertype_choices = (
        ('windows','WINDOWS'),
        ('linux', 'LINUX'),
        ('mac','MAC'),
        ('unix','UNIX'),
    )
    servertype = models.CharField(max_length=250, choices = servertype_choices, default= 'windows')
    disktype_choices = (
        ('hdd','HDD'),
        ('sdd','SDD'),
        ('san disk','SAN DISK'),
    )
    disktype = models.CharField(max_length=250, choices= disktype_choices, default='hdd')
    owner_choice = (
        ('ppsc','PPSC'),
        ('fcgo','FCGO'),
    )
    owner = models.CharField(max_length=250, choices= owner_choice, default='ppsc')
    location_choices = (
        ('cloud','CLOUD'),
        ('standalone','STANDALONE'),
        ('aws','AWS'),
        ('azure','AZURE'),
    )
    serverlocation = models.CharField(max_length=250, choices = location_choices, default='cloud')
    cpu = models.CharField(max_length=250)
    ram = models.CharField(max_length=250)
    ipaddress = models.CharField(max_length=250,unique = True)
    username = models.CharField(max_length=250, unique = True)
    password = models.CharField(max_length=250)
    publicip = models.CharField(max_length=250,unique= True)
    privateip = models.CharField(max_length=250,unique= True)
    remarks = models.CharField(max_length=250, null=True , blank= True)
    # status_choices = [('M','Male'),('F','Female')]
    # status = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    status_choices = (
        ('active','ACTIVE'),
        ('inactive','INACTIVE'),
    )
    status = models.CharField(max_length=250, choices= status_choices, default='active' )

    # def __str__(self):
    #     return self.servername