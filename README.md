# GeoSense 🪨

GeoSense is a simple Python application that helps identify minerals based on their physical properties. It uses a graphical user interface (GUI) built with Tkinter where users can enter mineral characteristics and compare them with a built-in mineral database.

## Features

- Simple and easy-to-use graphical interface
- Mineral identification using:
  - Hardness (Mohs scale)
  - Density
  - Luster
  - Streak color
- Displays the percentage match for each mineral
- Highlights the mineral with the highest matching score (above 50%)
- Contains a database of 40+ common minerals

## Technologies Used

- Python 3
- Tkinter (GUI)
- Python Dictionaries
- Message Boxes

## How It Works

1. Enter the mineral's hardness.
2. Enter its density.
3. Enter the luster.
4. Enter the streak color.
5. Click the **Submit** button.
6. The application compares the entered values with the mineral database.
7. It displays the matching percentage for every mineral and suggests the closest match.

## Project Structure

```
GeoSense/
│── main.py
│── README.md
```

## Installation

1. Clone this repository.

```bash
git clone https://github.com/your-username/GeoSense.git
```

2. Move into the project folder.

```bash
cd GeoSense
```

3. Run the program.

```bash
python main.py
```

## Example Input

| Property | Example |
|----------|---------|
| Hardness | 7 |
| Density | 2.65 |
| Luster | vitreous |
| Streak | white |

The program compares these values with its database and displays the matching results.

## Future Improvements

- Add more mineral properties such as color and crystal system
- Improve the matching algorithm using weighted scoring
- Allow approximate numeric matching instead of exact values
- Add mineral images
- Export identification results
- Convert the application into a web application

## Learning Outcomes

This project helped me learn:

- Building desktop GUI applications using Tkinter
- Working with Python dictionaries
- Handling user input
- Using functions and loops
- Comparing datasets using simple matching logic
- Displaying results using message boxes

## Author

Created by **AryamanSharmaTheKing and nandinisharma19*
