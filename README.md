## SDSS Computing Studies Python Assignment
### Assignment 302 Javascript Object Notation (JSON) (Total Marks 5)

Objectives:
* Encode a list or dictionary as a json object
* Decode a json object
* Store more complex data in a JSON encoded format

One advancement made in storing data in non-volatile memory, was to store entire sets of data that are related as an easy to read format.  For example, a student might have a number of different pieces of data associated with him.  Consider the two different ways to do so:
```
# student data
# option 1
first_name = "Joe"
last_name = "Lunchbox"
grade = 12
student_number = 19333
blockA = "Math"
blockB = "English"
blockC = "PE"
blockD = "Basket Weaving"

# option 2
student = {
    'firstName' : 'Joe',
    'lastName' : "Lunchbox",
    'grade' : 12,
    'studentNumber' : 19333,
    'block' : {
        'A' : "Math",
        'B' : "English",
        'C' : "PE",
        'D' : "Basket Weaving"

    }
}
```

The second method is clearly better, as it stores all of the data together in one student, instead of having multiple variables.  If you were to ever keep track of multiple students, it's better to have multiples of the student variable instead of multiples of multiples

JSON (Javascript Object Notation) is a way of encoding a complex variable, like a dictionary, into a single text string that can be store in a file on a single line, or in a database.  Think of it kind of like using .zip to compress a file and store it, and then unzip it later on when you need to use it.  JSON does something similar.

Consider the output of the code in example02.py
```
numbers [3, 4, 5]
numbers is a variable of type : <class 'list'> and contains [3, 4, 5]
encodedNumbers is a variable of type <class 'str'> and contains [3, 4, 5]```
We use json.dumps to convert a variable into a json encoded object.  In this case, encoding the data doesn't appear to make any difference to how the data appears when we print it, but the **type** of the variable has changed from a list to a string.  As a single string, we can store it more easily and then decode it at a later date.

example02.py
line 12 adds a json decoding command "json.loads()"
This allows us to easily decode some json encoded data and store it into a new variable.
