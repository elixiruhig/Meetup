import uuid
from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

# Create your models here.


MY_INTERESTS = (
                ('Adventure','Adventure'),
                ('Food','Food'),
                ('Tech','Tech'),
                ('Family','Family'),
                ('Health','Health'),
                ('Sports','Sports'),
                ('Film','Film'),
                ('Books','Books'),
                ('Dance','Dance'),
                ('Arts','Arts'),
                )

class UserManager(BaseUserManager):

    def create_user(self,email,password=None):
        if not email:
            raise ValueError("Please enter an email")

        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_host(self,email,password):
        user = self.create_user(email,password=password)
        user.host = True
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user = self.create_user(email, password=password)
        user.admin = True
        user.staff = True
        user.host = True
        user.save(using=self._db)
        return user

    def create_staff(self,email,password):
        user = self.create_user(email,password=password)
        user.staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length=255, blank=False)
    user_id = models.UUIDField(unique=True, default=uuid.uuid4)
    email = models.EmailField(max_length=255, unique=True)
    host = models.BooleanField(default=False)
    interests = MultiSelectField(choices=MY_INTERESTS)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="group_photos", null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_host(self):
        return self.host

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff


class Interest(models.Model):
    interest = models.CharField(max_length=255,blank=False, null=False)

    def __str__(self):
        return self.interest

class Group(models.Model):
    name = models.CharField(max_length=255,blank=False, null=False)
    group_id = models.UUIDField(unique=True, default=uuid.uuid4)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(Interest,on_delete=models.CASCADE)
    location = models.CharField(max_length=55,blank=False, null=False)
    photo = models.ImageField(upload_to="group_photos", default='group_photos/film.jpg')

    def __str__(self):
        return self.name

class GroupMemberDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        str = "{} {}".format(self.user.email,self.group.name)
        return str

class Meetup(models.Model):
    name = models.CharField(max_length=255,blank=False, null=False)
    meetup_id = models.UUIDField(unique=True, default=uuid.uuid4)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group ,on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now())
    photo = models.ImageField(upload_to="group_photos",default='group_photos/film.jpg')
    fee = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class MeetupMemberDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meetup = models.ForeignKey(Meetup, on_delete=models.CASCADE)

    def __str__(self):
        str = "{} {}".format(self.user.email,self.meetup.name)
        return str