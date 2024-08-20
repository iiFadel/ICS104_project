# ICS 104 - Introduction to Programming in Python and C

## Project Overview

This project is a program designed to manage and manipulate student information based on several options. It was developed as part of the ICS 104 course. The program processes student data, performs validations, and allows users to interact with the data through various functionalities.

### Contributors

|     Name     | Contribution Description |
|:------------:|:-------------------------:|
| **Fadel Al Abbas** | Worked on input conditions, ensuring user inputs are restricted to specific valid entries and matched against the main dataset. |
| **Ziyad Aljadhai** | Developed the main function, including its various options, ensuring they properly interact with the dataset. |

### Project Description

The project code was developed by organizing the data into multiple lists, each containing specific information about students. Various functions were then created to process these lists and produce the desired outputs. The functions are designed to handle potential user errors, with built-in validation to prompt users to correct their inputs with a limited number of attempts.

### Challenges Faced

- **Avoiding the use of global variables:** The code was designed without relying on global variables, which required careful structuring of functions and data management.
- **User input validation:** Ensuring that the program could handle and correct invalid user inputs was a significant challenge.

### Design Considerations

One alternative design approach that was considered but not implemented was using classes and Object-Oriented Programming (OOP) to structure the code. However, the final design was implemented using functions and lists to maintain simplicity and focus on core programming concepts.

### Project Code

The project code includes a test phase where a names generator was used to create a sample dataset of students. This dataset was then utilized to test the main program functionalities. Below is an overview of the initial setup:

#### Names Generator

```python
f = open("info.txt", "w")
f.write("ID             Name            Absences        Midterm(35%)        Classwork(25%)      Final(40%)\\n")
f.write("201911111   Abdullah hassan        0                30                   23                 34   \\n")
f.write("201922222   Mohammed ali           3                28                   20                 30   \\n")
f.write("201933333   Hazem selmi            0                35                   25                 40   \\n")
```
This script generates a text file with a list of students and their respective information, which is then processed by the main program.

## How to Run the Project

1. Ensure you have Python installed on your system.
2. Clone the repository to your local machine.
3. Run the notebook or the associated Python scripts to execute the program.
4. Follow the prompts to interact with the student information system.

## Future Enhancements

- **Transition to Object-Oriented Programming:** Future versions of the project could incorporate OOP principles to enhance code modularity and reusability.
- **Enhanced User Interface:** Developing a graphical user interface (GUI) could make the program more user-friendly and accessible to non-technical users.

## License

This project is part of an educational course and is intended for learning purposes. Please refer to the course guidelines for any restrictions on code usage and distribution.
