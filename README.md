

# Chris-G-CS-340

## About the Project/Project Title
The *Grazioso Salvare Shelter Dog Finder* was created so that Grazioso Salvare can find candidates for search and rescue training. Through this interface with a previous MongoDB database, the filtering of dogs based of certain criteria can be done. The filtered data is then displayed in a list of entries, a pie chart with the number of each dog breed in the filtered data, and a map showing the location of each dog in the filtered data.
Motivation
This app was created to provide an easy way for Grazioso Salvare to find shelter dogs. Without this interface, it would be much more difficult to find candidate dogs in the MongoDB database.

## Getting Started
To begin with, make sure you have a MongoDB server running with an imported database. In this example, I import a database named “AAC”

<br><image src = "Pictures/Picture1.png"></image><br>

Next, create an admin account for your MongoDB server. In this example I created two accounts, NewAdmin and aacuser.<br>
<br><image src = "Pictures/Picture2.png"></image><br>
<br><image src = "Pictures/Picture3.png"></image><br>

As you can see in the following image, both created users are able to access the test server.
<br><image src = "Pictures/Picture4.png"></image><br>
Next, start your MongoDB server and take note of the port (in this case port 51915).<br>
<br><image src = "Pictures/Picture5.png"></image><br>
Also take note of the desired database (in this case “AAC”) and the desired collection (in this case, animals).
Note:(the app will only work with a database with documents formatted such as in the following screenshot)
<br><image src = "Pictures/Picture6.png"></image><br>

<br><image src = "Pictures/Picture7.png"></image><br>
<br><image src = "Pictures/Picture8.png"></image><br>
<br>Next download the crud.py file, the *GraziosoSalvareShelterDogFinder.ipynb* file, and the *Grazioso Salvare Logo.png* file and put  them in the same folder.

After this, edit the *GraziosoSalvareShelterDogFinder.ipynb* file variables on lines 26-30 with your given port, database, collection, username, and password such as in the following screenshot.
<br><image src = "Pictures/Picture9.png"></image><br>
 
 
## Installation
To use this class, there are a few tools to install.
1. Python 3
To install this, open the terminal and input “sudo apt-get install python3-pip"

2. MongoDB
3. PyMongo
To install this, open the terminal and type “python -m pip install PyMongo”

4. A text editor or python IDE
5. Jupyter Notebook
To install this, open the terminal and type “pip3 install Jupyter”

## Usage
This app consists of 4 elements in the dashboard, the radio buttons,  the data table, the pie chart, and the map. These elements were implemented using the “dash” framework which allows for the use of HTML in python code. 
The dash framework was used for it’s vast capabilities regarding the link between HTML and python, and for it’s extensive collection of useful elements such as the map and pie charts.
The database used was a NOSQL database called MongoDB.  This database type was used because of it’s flexible model and for it’s useful interaction with python through the PyMongo external tool.

To use this app, simple select the desired filer by selecting a radio button (Water Rescue, Wilderness Rescue, Individual Tracking, or Reset), and then looking through the displayed data in each element. 
The data table displays all documents which match the filter, the pie chart displays the number of each breed which match the filter, and the map displays all locations of the dogs that match the filter along with a hover tag which displays the dog breed and a clickable tag which displays the dog name.
The usage and outputs of the radio buttons are shown below with a test database being used.

### *Inputs and outputs*
*Water Rescue Button*<br>
<br><image src = "Pictures/Picture10.png"></image><br>
<br><image src = "Pictures/Picture11.png"></image><br>
<br><image src = "Pictures/Picture12.png"></image><br>

*Wilderness Rescue Button*<br>
<br><image src = "Pictures/Picture13.png"></image><br>

<br><image src = "Pictures/Picture14.png"></image><br>

<br><image src = "Pictures/Picture15.png"></image><br>

*Individual Tracking Button*<br>
<br><image src = "Pictures/Picture16.png"></image><br>
<br><image src = "Pictures/Picture17.png"></image><br>
<br><image src = "Pictures/Picture18.png"></image><br>

*Reset Button*<br>
<br><image src = "Pictures/Picture19.png"></image><br>

<br><image src = "Pictures/Picture20.png"></image><br>
<br><image src = "Pictures/Picture21.png"></image><br>






### *Radio Buttons*
There are 4 radio buttons that each filter the raw data in specific ways. Depending which button is pressed, a different database read query will be used to retrieve the data from the database and display it in the subsequent elements. 
. The “Water Rescue” button displays all dogs matching the attributes defined in the specification document for Water Rescue dogs. The “Wilderness Rescue” button displays all dogs matching the attributes defined in the specification document for Mountain or Wilderness dogs. The “Individual Tracking” button displays all dogs matching the attributes defined in the specification document for Disaster or Individual Tracking dogs.  And finally, the reset button displays all dogs in the database without any filtering. This created directly in an HTML element.
These buttons were fairly easy to implament and simply consisted of creating radio buttons elements with the dash “RadioItems” element. A value was then set to each radio option and each value set to the id “filter-type”.

### *Data Table*
This data table displays all documents which match the filter set by the radio button element.
It is created with the dash “dataTable” element. There is a function called “update_Dashboard’ which handles the filtering and takes the filter from the radio buttons.  With this filter, it creates a new dataframe replacing the old dataframe which only reads filtered documents from the database.
The dataframe is then filled with this data and the data is also passed to the other elements through the variables “data” and “columns”. This is then displayed in an HTML element with the id of “datatable-id”.
This was pretty easy to implament and after some minor query formatting issues, it was up and running.

### *Pie Chart*
The pie chart is created in a function called “update-graph” which takes the data variable from the “update_graphs” function. At this point, the data variable is basically a list of documents which are in the form of python dictionaries.  In order for the pie graph to behave like I wanted it to (to list the number of each breed) I appended a new entry to each dictionary in the list called “count” each with a value of 1. With this, I was able to return a pie chart dash element with the new data table, the values of count, and the names of breed. From this point the graphs automatically adds up the value of count for each dictionary and successfully displays the proper breed numbers. This is displayed in an HTML element with the id of “graph-id”.
This feature took me a really long time to implament because I was misunderstanding the datatype passed to this function. As such , I was trying to make changes to the data variable in ways that don’t make sense for it’s datatype.

### *Map*
The map is created in the “update_map” function which takes the data variable and then uses that information for return a map element with the proper number of children and proper data. To do this, an array is created with information from the data variable which is appended to the end of the created array using a for loop. This array is then used in the return of the dash map element.  This is then displayed in the HTML element with the id of “map-id”.
This element wasn’t too hard to create and just required a little knowledge about dictionaries to complete.

# Questions and Answers

Q: How do you write programs that are maintainable, readable, and adaptable?
Especially consider your work on the CRUD Python module from Project One, which you used to
connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way?
How else could you use this CRUD Python module in the future?

A: For the CRUD file, I wanted to make sure that this was something that could be used again.
To this end, I created it in such a way where it could be imported as a module where you didn’t have to touch the code to use. 
This helped ensure that this program could be reused with any mongodb database with any collection. 
I did however skimp on the comments, so this would make maintaining the code more difficult. 
In the future, this file would be really easy to import using mongopy and use for any future mongodb database I create.
Overall, I really try to write code in a way that can be reused and adapted, but I should really focus on writing better documentation especially inline comments.


Q:How do you approach a problem as a computer scientist?
Consider how you approached the database or dashboard requirements that Grazioso Salvare requested.
How did your approach to this project differ from previous assignments in other courses?
What techniques or strategies would you use in the future to create databases to meet other client requests?

A: My methodology usually involves taking incremental steps to get closer to a solution until the problem has been solved. As an example,
for the final dashboard project, I first focused on getting the starter code running, then working on the radio buttons, after that getting
the sorting done, then the pie chart, then the map. Just starting with the lowest level dependencies and working from there has served me
well on previous assignments and on this one. 
In the future, I would probably end up using aggregated pipelines a lot. After working with them this week, it seems that they
are a verypowerful tool for collecting data from databases. 
Using pymongo is also a great tool for automatically creating documents and entries automatically, so I will definitely be using that more in the future. 


Q: What do computer scientists do, and why does it matter?
How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

A: A computer scientists’ job is to solve problems in the most efficient way possible.
Whether that be detecting the existence of exoplanets, defining the future of ai, of even making a fun app.
In the case of the Grazioso Salvare app, if they were a real compony then chances are, there were
trying to find candidates for training dogs by hand, searching through hundreds of files. 
By applying computer science to this problem, the developed app makes not only could save the business a lot of time and money,
but also help save the lives of their customers.
