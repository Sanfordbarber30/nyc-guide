
# NYC-Guide App

**Created by:**

Sanford Barber  
**Github**: <https://github.com/Sanfordbarber30>

*and*

Daniel Cho  
**Github**: <https://github.com/Daniel165c>



**Preliminary setup**   


>In order to run and view the Django application you will need to:  
> -create and run a virtual environment,  
> -install project dependencies,  
> -and then run the server from your localhost. 



**Creating and running a virtual environment**  

At the root folder that contains the app folder, run the following command on your command line:  


>python3 -m venv venv    *or if your running on a later version of python*      py -m venv venv  


Activate your virtual environment according to your operating system:  


>for Windows users: venv\Scripts\activate  
>    Bash users: source venv/Scripts/activate  
>    Unix or MacOS users: source venv/bin/activate  



**Install project dependencies**  

In order to run the app successfully, you will need to install all of the app dependencies into your virtual environment. Please be sure to have your virtual environment activated. You can install the dependencies using the following command:  


>pip install -r requirements.txt



**Running Django through your local host**

You can now run the application by executing the following command in the terminal:  


>python manage.py runserver   *or*      py manage.py runserver  



Go to your web browser and go to http://localhost:8000.



