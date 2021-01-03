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