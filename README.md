# Chris-G-CS-340
Portfolio of projects for the SNHU CS-340 Client Server Class Assignment 8-2 

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
