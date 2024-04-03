from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    
    def create_superuser(self, email, first_name, last_name,  password=None, **extra_fields):
      """
      Creates and saves a superuser with the given email, name, tc and password.
      """
      user = self.create_user(
          email=email,
          first_name=first_name,
          last_name=last_name,
        #   DOB=DOB,
          password=password,
        #   is_staff=True,
        #   is_admin=True
      )
      user.is_admin = True
      user.is_staff=True
    #   user.is_staff = True
      user.is_superuser = True
      user.save(using=self._db)
      return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image= models.ImageField(upload_to="account", null=True, blank=True)
    DOB= models.DateField(null=True, blank=True)
    staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email
