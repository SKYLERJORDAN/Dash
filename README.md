# NYC AirBnB Analysis Dashboard

This project is a Dash application that visualizes AirBnB listings data for New York City in 2019. The interactive dashboard allows users to filter listings based on neighborhood, minimum nights, and price range, and displays the results on a map.

## Dataset

The dataset used in this project is `AB_NYC_2019.csv`, which contains information about AirBnB listings in New York City for the year 2019. The dataset includes details such as listing name, host name, neighbourhood group, neighbourhood, latitude, longitude, room type, price, minimum nights, number of reviews, last review, reviews per month, calculated host listings count, availability 365, and number of reviews.

## Features

- Interactive map displaying AirBnB listings in New York City
- Filter listings by neighborhood, minimum nights, and price range
- Hover over listings to view additional details
- Color-coded markers based on price

## Requirements

- Python 3.x
- Dash
- Dash Bootstrap Components
- Plotly Express
- Pandas

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/nyc-airbnb-analysis.git
   ```

2. Navigate to the project directory:

   ```bash
   cd nyc-airbnb-analysis
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Dash application:

   ```bash
   python dash.py
   ```

2. Open a web browser and navigate to `http://localhost:8050`.

3. Use the dropdown menu to select a neighborhood, input the desired minimum number of nights, and adjust the price range slider to filter the listings.

4. Hover over the markers on the map to view additional details about each listing.

## File Structure

- `dash.py`: The main Dash application file containing the layout and callback functions.
- `AB_NYC_2019.csv`: The dataset file containing AirBnB listings data for New York City in 2019.
- `README.md`: This readme file providing an overview of the project.
- `requirements.txt`: A file listing the required Python packages for the project.
- `.gitignore`: A file specifying which files and directories should be ignored by Git.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
