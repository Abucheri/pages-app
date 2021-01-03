# Introduction to templates
create a pages app
add to installed apps in settings.py
Then create a project-level folder called templates and an HTML file called home.html 
Update settings.py, to the setting 'DIRS' under TEMPLATES add 'DIRS': [os.path.join(BASE_DIR, 'templates')],
Add a simple <h1></h1>h1> tag to the home.html file
We will use class-based views to avoid repeating
Go to pages/views.py and import 'TemplateView' since we haven't started using models
Create a HomePageView class and call our template to display using 'template_name'
Let's create urls for our app, we will start with the project level urls.py to include our app urls
Now create app level urls for the pages app 'touch pages/urls.py'
Let's add an about page and link the two of them
The process is still the same for the about page
Add a url pattern for the about page in app level urls.py 'pages/urls.py'
Since the structure of the templates are similar, we are going to use template extending using 'base.html'
Create base.html file in templates folder 'touch templates/base.html'
We use blocks in our base file to specify where to render content in our pages, using this files helps us to implement DRY (Do Not Repeat Yourself)
Let's extend the base templates to our other templates
Finally, let's do some tests on our app, Writing tests is important because it automates the process of confirming that the
code works as expected, Django comes with robust, built-in testing tools for writing and running tests
We will us the tests.py file that comes with django to do this

# Now we are going to deploy heroku
we will add a procfile by using this command: touch procfile
add the following line in the procfile 'web: gunicorn pages_project.wsgi --log-file -'
then install gunicorn using pip
Add a runtime.txt file in the project root directory and specify the correct Python version
Install the following packages in the environment "pip install gunicorn dj-database-url whitenoise psycopg2"
Add a requirements.txt file "pip freeze > requirements.txt"
Heroku will recognize a deployed application as a Python application only if it has a requirements.txt file in the root directory. Even if your application has no module dependencies, it should include an empty requirements.txt file to indicate that your app has no dependencies.

# Setting up static assets for heroku
Open up settings.py file and some minor changes, preferably at the bottom of the file
Add whitenoise middleware at the top of the middleware list in settings.py
Update Database Configuration in settings.py (at the bottom of the file)
push changes to gitnub first and then create an app and deploy

# Deployment
 Create App in Heroku from terminal "Choose any name for your app. Heroku will inform you if the name already exists"
 heroku create app_name - to create app/ours we'll call 'pagesdemo'
 Add your app domain name to ALLOWED_HOSTS in settings.py.
 Initialize Git and connect your new app (or existing one) to Heroku Git remote repository if not initialized
 connect to heroku using "heroku git:remote -a app_name"
 tell heroku to ignore static files using "heroku config:set DISABLE_COLLECTSTATIC=1"
 Add files to the staging area and commit changes.
 Push the project to the remote repository (deploy app to Heroku) using "git push heroku main"
we need to set some web traffic usind "heroku ps:scale web=1"
finally let's confirm our app is live and online using "heroku open"
