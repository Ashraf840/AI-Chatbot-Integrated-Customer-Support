from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager   # Manages "Super & Regular Users"
from django.contrib.auth.validators import UnicodeUsernameValidator
import random, string


username_validator = UnicodeUsernameValidator()

GENDERCHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

def random_string_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class User(AbstractBaseUser, PermissionsMixin):
    # User Info
    ibas_user_id = models.CharField(verbose_name='iBAS++ User Id', max_length=150, blank=True, null=True, help_text='ibas_uid_[Id Num]')
    email = models.EmailField(verbose_name='Email', max_length=60, unique=True)
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists!",
        },
    )
    first_name = models.CharField(verbose_name='First Name', max_length=50, blank=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=50, blank=True)
    gender = models.CharField(verbose_name='Gender', max_length=6, choices=GENDERCHOICES, blank=True)
    phone = models.CharField(verbose_name='Primary Contact', max_length=20, blank=True, unique=True)
    profile_pic = models.ImageField(upload_to='profilePicture', default='profilePicture/default_avatar.png', blank=True)
    initial_password = models.CharField(max_length=150, blank=True, null=True)
    is_first_login = models.BooleanField(default=True)
    # Registration, Activity
    date_joined = models.DateField(verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last Update", auto_now=True)
    # Extend Roles & Permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_cso = models.BooleanField(verbose_name='is_hdo', default=False)
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "User (Staff, HDO, Admin, User, Superuser)"

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def has_module_perms(self, app_label):
       return True
    
    def has_perm(self, perm, obj=None):
        return True

    def save(self, *args, **kwargs):
        # TODO: halt save method, create random password, store into "first_time_pass" field, lastly set that random password into the "password" field.
        # TODO: define a field "is_first_login(bool)" to track first-time-login of users.
        # TODO: Hide the two "password" fields while creating new user from dj-admin-panel
        # TODO: make sure to check the password is set only at the user-creation.
        try:
            if self.ibas_user_id is None:
                self.ibas_user_id = "ibas_uid_" + random_string_generator()
        except:
            True
        super(User, self).save(*args, **kwargs)




# Get automatically from "User.phone", ("User.first_name" + "User.last_name"), "User.email" from the "User" model
class User_Profile(models.Model):
    # TODO: "user_email" will only have "unique=True" instead of "blank=True, null=True" later after development phase of "User_Profile"
    user_email = models.EmailField(verbose_name='User Email', max_length=60, blank=True, null=True)
    user_address = models.TextField(verbose_name='User Address', blank=True, null=True)
    user_name_bn = models.CharField(verbose_name='ইউজার নাম (বাংলা)', max_length=255, blank=True, null=True)
    user_father_name = models.CharField(verbose_name='Father Name', max_length=255, blank=True, null=True)
    user_mother_name = models.CharField(verbose_name='Mother Name', max_length=255, blank=True, null=True)
    user_NID_no = models.CharField(verbose_name='NID no.', max_length=255, blank=True, null=True)
    user_organization = models.CharField(verbose_name='Organization', max_length=100, blank=True, null=True)
    location = models.CharField(verbose_name='Location', max_length=100, blank=True, null=True)
    district = models.CharField(verbose_name='District', max_length=100, blank=True, null=True)
    division = models.CharField(verbose_name='Division', max_length=100, blank=True, null=True)


    class Meta:
        verbose_name_plural = "User Profile"


# Store user-signin-token-tms
class User_signin_token_tms(models.Model):
    user_email = models.EmailField(verbose_name='User Email', max_length=60, blank=True, null=True)
    user_id = models.CharField(verbose_name='User id (TMS)', max_length=200, blank=True, null=True,
                               help_text="TMS 'user_id' is the 'uesrname' of the COS",)
    user_token = models.CharField(verbose_name='Access Token', max_length=300, blank=True, null=True)
    token_type = models.CharField(verbose_name='Token Type', max_length=10, blank=True, null=True)

    class Meta:
        verbose_name_plural = "User Signin Token (TMS)"
