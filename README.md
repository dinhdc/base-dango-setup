# Base Project Django

---

## Installation

- You must install somepack necessary in `requirements.txt` file to run django by run this command:
  - with Windows:

    ``` Python
    python3 -m venv venv
    venv/bin/Activate
    pip install -r requirements.txt
    ```

  - with Linux:

    ```Python
    python3 -m venv venv
    source venv/bin/active
    pip install -r requirements.txt
    ```

---

## Feature Core

### 1. Custom Model User

- We have custom some field in model User in CustomUser model
- CustomUser model in app label 'user'
- You can add or remove field which you want

  ```Python
  class CustomUser(AbstractBaseUser, PermissionsMixin):
      email = models.EmailField(_('email address'))
      uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
      username = models.CharField(max_length=255, unique=True)
      cccd = models.CharField(max_length=20,)
      date_of_birth = models.DateField(null=True)
      sex = models.CharField(max_length=10)
      city = models.ForeignKey(City, to_field="uid",
                               on_delete=models.SET_NULL, null=True)
      district = models.ForeignKey(
          District, to_field="uid", on_delete=models.SET_NULL, null=True)
      ward = models.ForeignKey(Ward, to_field="uid",
                               on_delete=models.SET_NULL, null=True)
      phone_number = models.CharField(max_length=30)
      is_staff = models.BooleanField(default=False)
      is_active = models.BooleanField(default=True)
      date_joined = models.DateTimeField(default=timezone.now)

      USERNAME_FIELD = 'username'
      REQUIRED_FIELDS = []

      objects = CustomUserManager()

      def __str__(self):
          return self.username
  ```

  - You can change orther field as username by `USERNAME_FIELD`
  - After all, you must this line to `settings.py`:

    ```Python
    AUTH_USER_MODEL = 'user.CustomUser' # app.ModelName
    ```

### 2. Address Vietname

- We have model City, District, Ward and data of them in `address.json` file
- You can load / import data from file to db by run this command:

```Python
    python manage.py loaddata address.json
```

### 3. Custom Tag Swagger / Schema

- We have core/custom_tag to change that way assign name of swagger
- We custom asign name of module for api by using keyword `module`

### 4. Github Workflow

- We put action in `django.yml` file in `.github/workflows`
- That name of action is `Flake8` to check lint and config of them in `.flake8` file

### 5. Auto convert snake case field name to camel case in api response

- In CustomUser model, we have some field name same snake case: `phone_number, date_of_birth, v.v..`, but when response auto convert to `phoneNumber, dateOfBirth`
