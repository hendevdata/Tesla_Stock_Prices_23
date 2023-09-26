# Simple Stock Price App

This is a simple Python application that displays the closing price and volume of a stock using the [yfinance](https://pypi.org/project/yfinance/) library for retrieving stock data, [pandas](https://pandas.pydata.org/) for data manipulation, and [streamlit](https://streamlit.io/) for creating the user interface.

## Prerequisites
- Python 3.6 or higher
- pip package manager

## Installation
1. Clone the repository or download the code files.
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the required Python packages by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Ensure that you have installed the required packages as mentioned in the Installation section.
2. Run the Python script:
   ```
   python stock_price_app.py
   ```
3. The application will start and display the stock closing price and volume of Tesla from January 1, 2019, to January 1, 2023.
4. You can interact with the charts displayed by zooming in/out, panning, and hovering over data points.

## Customization
- Ticker Symbol: By default, the application retrieves data for the "TSLA" (Tesla) stock. You can modify the `tickerSimbol` variable in the code to change the stock symbol.
- Date Range: The stock data is fetched for the period from '2019-01-01' to '2023-01-01'. You can modify the `start` and `end` parameters in the `tickerData.history()` method to change the date range.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- [yfinance](https://pypi.org/project/yfinance/) - Python library for retrieving stock data.
- [pandas](https://pandas.pydata.org/) - Data manipulation library for Python.
- [streamlit](https://streamlit.io/) - Python library for creating interactive web apps.
