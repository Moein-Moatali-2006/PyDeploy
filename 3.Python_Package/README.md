# MIGA (Make Iran Great Again)

## Iran Map with Python Turtle

This project draws a map of **Iran** using Python's **Turtle** graphics library. The map data is fetched from a GeoJSON file on GitHub. The program visualizes the country with a simple filled shape and displays the text "IRAN" on top.

## Features

- Draws the map of Iran using turtle graphics.
- Fetches country boundary data from GeoJSON.
- Scales and centers the map automatically.
- Adds title text "IRAN" above the map.
- Simple and visually clean design.

## Screenshot

![Iran Map](https://github.com/Moein-Moatali-2006/MIGA/blob/main/images/Iran.png)  
*(You can add a screenshot of the map here.)*

## Requirements

- Python 3.x
- `turtle` (built-in)
- `requests` library

Install `requests` if you don't have it:

```bash
pip install requests
```

## How to Run

1. Clone this repository or download the `iran_map.py` file.
2. Run the script:

```bash
python iran_map.py
```

3. A window will open showing the map of Iran. Click on the window to close it.

## How It Works

- The program fetches Iran's GeoJSON coordinates from a GitHub repository.
- Each coordinate is converted into **x** and **y** positions for Turtle graphics.
- The map is scaled and offset to fit nicely in the Turtle window.
- A filled shape is drawn using the turtle, and text is added for labeling.

## Customization

- You can change the **scale** or **offset_x / offset_y** values to adjust the map size and position.
- Change the colors by editing `t.color("black", "#f4d27a")` for outline and fill.
- Change the title text font or position by editing the `t.write` parameters.

## License

This project is open-source and free to use.

## Created with ❤️by Moein Moatali
