from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
	"""Helps Django work with our customer user model."""

	def create_user(self, email, name, password=None):
		"""Creates a new user profile object."""

		if not email: 
			raise valueError('Users must have an email address.')

		email = self.normalize_email(email)
		user = self.model(email=email, name=name)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, name, password): 
		"""creates and saves a new superuser with given details"""

		user = self.create_user(email, name, password)
		user.is_superuser = True
		user.is_staff = True

		user.save(using=self._db)

		return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
	""" Represents a user profile inside our system"""
	#we are establishing the key fields that will be saved in our database
	#For our medical device fields we can save different types of fields

	email = models.EmailField(max_length=255,unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	college = models.CharField(max_length=255)
	academic_year = models.CharField(max_length = 255)
	#medications = models.CharField(max_length = 255)

	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']


	def get_full_name(self):
		"""Used to get a users full name. """

		return self.name

	def get_short_name(self):
		"""Used to get user short name """

		return self.name

	def __str__(self):
		"""django uses this when it needs to convert an object to a string"""

		return self.email
