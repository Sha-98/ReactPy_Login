# ReactPy_Login

![image](https://github.com/Sha-98/ReactPy_Login/assets/89126969/1abe2acf-32f0-4a26-bb34-121131e88bad)

![image](https://github.com/Sha-98/ReactPy_Login/assets/89126969/74fbe25d-56fd-4c13-8dc2-c38a60b649b9)

![image](https://github.com/Sha-98/ReactPy_Login/assets/89126969/56fa89cb-f623-4684-844e-d78e74895ab1)


To create a basic registration form using ReactPy, which is connected with  the MongoDB database, you can follow the below mentioned steps and code. Please note that all the dependencies and libraries used in the code must be installed in your system. One thing to note here is that reactpy is a python library and thus we do not need any specific commands to start a new project in reactpy. Just install it as explained above and import the library and required module to create an app.

### Step 0: Install ReactPy
To install the new python library ‘ReactPy’, which is based on React, a JavaScript library for building user interfaces. ReactPy is a python-based version of this library using which we can now build user interfaces using python. For installing this library into your system, we can use ‘pip’. Now, ReactPy currently can be downloaded in multiple formats, in combination with different backends as listed below.
•	fastapi – https://fastapi.tiangolo.com 
•	flask –  https://palletsprojects.com/p/flask/ 
•	sanic – https://sanicframework.org 
•	starlette – https://www.starlette.io/ 
•	tornado – https://www.tornadoweb.org/en/stable/ 

ReactPy includes build-in support for the implementation of these backend, and to install the required dependencies for each of these, the following code should be used, by choosing one of these from the list in the code. Also note, that you can install more than one options separated from a comma.

pip install "reactpy[fastapi,flask,sanic,starlette,tornado]"
pip install "reactpy[fastapi]"

If  you want to install a “pure” version of ReactPy without a backend implementation, you can also do so without any installation extras using the “pip” command as follows.

pip install reactpy

Now if you are using visual studio code, installation would require one more step, so that you do not get error for “ModuleNotFound”. For this, first open the folder for your project in VS Code and create a python file there.
Now, for installing python libraries, we need to create the virtual environment here first, using the following line of code.

python -m venv “Path of your folder with ‘venv’ folder”
python -m venv c:/Users/Asus/Desktop/Project/venv

![image](https://github.com/Sha-98/ReactPy_Login/assets/89126969/b2edf2d1-2081-4e3e-aa04-588037e0b5b2)


### Step 1: Setting up the Backend Server and MongoDB Connection

•	Import the necessary modules and libraries, including ‘FastAPI’, ‘MongoClient’, and ‘ServerApi’.
•	Create a FastAPI application instance using ‘FastAPI()’.
•	Define the MongoDB connection as explained in previous question.

### Step 2: Define the Login Endpoint

•	Define a login function to store the input name and password of the user.
•	Create a document to be inserted into collection which has these input details from the form.
•	Print the created document to the console.
•	Insert the document into the collection and retrieve the inserted document’s ID.
•	Print the document’s id to check if data is being inserted well, you can also check the database.
•	Return the success message.

### Step 3: Define the Frontend component for your application

•	Install ReactPy and import the necessary modules and functions from ‘reactpy’ and ‘reactpy.backend.fastapi’, as we are using FastAPI for our backed part.
•	Create a ReactPy component using the ‘@component’ decorator.
•	Define the necessary state variables using the ‘use_state’ hook, including ‘alltodo’.
•	Create  a form submission function, here as ‘mysubmit’ which creates a new todo object and adds it to the ‘alltodo’ state.
•	Now, this one is optional. We can print all the input data in an instance on the screen of the user. This will help us check what all data is sent to the database. For this, we would loop through the ‘alltodo’ state to generate a list of html, using ‘html.li’ command from reactpy. This list will then be printed on the html form using the ‘html.ul’ command.
•	Define an event handler ‘handle_event’ which prints the event to the console.
•	Return an html div element with the form, including the input fields for name and password, a submit button with a condition for preventing reload on submit, and the generated list of todos.

### Step 4: Configure the FastAPI Backend with the Frontend component

•	Use the ‘configure’ function from ‘reactpy.backend.fastapi’ to configure the FastAPI app with the ‘MyCrud’ component.

### Step 5: Run the application

•	Start the FastAPI server by running the Python script. For this, open the terminal, in VS Code (if using that, otherwise open the terminal at the location of your python file). Now, type the following ‘uvicorn main:app --reload’
•	Open the web browser and navigate to the appropriate url to see the rendered ReactPy component and the login form.
•	Interact with the form by entering a name and password and clicking the submit button.
•	Check the console for any logged events or messages.

