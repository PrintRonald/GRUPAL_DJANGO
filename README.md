# GRUPAL_DJANGO
 trabajo final


# Objetivo Principal

  Crear una aplicación con el framework django,para entregar 
  a los usuarios un espacio donde reproducir una selección de películas que se 
  encuentran liberadas en la web (Youtube).

# Para ver la aplicación vea los siguientes pasos

Para crear un repositorio local
$ git init 

Clonas el repositorio en tu repositorio local
$ git clone 

Para agregar archivos al área de trabajo 
$ git add 

Luego, navegas a la carpeta clonada
Se ejecuta el entorno virtual, se debe navegar hasta la carpeta que contenga
el entorno virtual
call venvGrupal_3/Scripts/activate

Se navega a la carpeta que contenga el archivo manage.py
en esta carpeta se ejecuta el siguiente comando
python manage.py runserver

Se realizan las migraciones correspondientes
python manage.py makemigrations
python manage.py migrate

Se crea el superusuraio administrador
python manage.py createsuperuser

Se vuelce a ejecutar el proyecto 
python manage.py runserver

¡¡¡¡ A DISFRUTAR DE ESTA SELECCIÓN ¡¡¡¡¡


# Desarrollo

Principales librerias que se ocupan en la aplicación   
asgiref==3.4.1
Django==3.2.9
Pillow==8.4.0
psycopg2==2.9.2
psycopg2-binary==2.9.2
pytz==2021.3
sqlparse==0.4.2

# Bases de datos

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

Almacena los perfiles de cada usuario.

class Cliente(models.Model):
    rut = models.CharField(max_length= 10, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

Almacena los clientes que se registren en la aplicación.

class Contacto(models.Model):
    nombre = models.CharField(max_length= 50)
    correo = models.EmailField()
    tipo_consulta=models.IntegerField(choices= opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

Almacena los Contactos que se registren en la aplicación.

class productos(models.Model):
    pelicula = models.CharField(max_length=50)
    url = models.CharField(max_length=300)
    image = models.ImageField(null=True, blank=True)
    descripcion = models.TextField(max_length=500)

Almacena los Productos que se registren en la aplicación.

# Formularios

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["nombre", "correo","tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'

Este formulario nos permite almacenar los datos que los usuarios nos entreguen cuando
deseen tomar contacto con nosotros, como un proceso de feedback.

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña',widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = { k:"" for k in fields }

Este formulario es para los usuarios que se registren en nuestra aplicación, viene por defecto en django.

