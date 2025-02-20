# OLX Mobile Phones Scraper & AI Analysis

## Overview

This script scrapes mobile phone listings from OLX Pakistan (specifically Lahore) and categorizes them based on condition (New, Used, Open-Box, etc.). The extracted data is then structured into a Pandas DataFrame and processed further with a transformer-based AI model for analysis.

## Features

- **Web Scraping**: Extracts mobile phone listing counts from OLX using BeautifulSoup.
- **Data Processing**: Structures the data into a Pandas DataFrame and removes duplicates.
- **AI Integration**: Uses the `DeepSeek` transformer model to analyze the extracted data.
- **Progress Indicator**: Displays a loading effect to indicate data processing progress.

## Dependencies

Ensure you have the following Python packages installed:

```sh
pip install requests beautifulsoup4 pandas transformers torch
```

## How It Works

1. **Scrapes OLX**:

   - The script iterates over different conditions (New, Used, etc.) and scrapes relevant listing data.
   - Uses regex to extract brand names and their corresponding counts.

2. **Processes Data**:

   - The extracted data is structured into a Pandas DataFrame.
   - Duplicate entries are removed.

3. **AI Analysis**:

   - Uses the `DeepSeek` transformer model to generate insights from the dataset.

4. **Displays Results**:

   - The cleaned DataFrame is printed.
   - AI-generated insights are displayed.

## Installation

Clone the repository and navigate to the project directory:

```sh
git clone https://github.com/your-username/olx-scraper-ai.git
cd olx-scraper-ai
```

Install dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Run the script using:

```sh
python script.py
```

## Output Example

The script will print a DataFrame summarizing the available listings and AI-generated insights based on the extracted data.

## Notes

- Ensure that OLX's website structure remains unchanged, as modifications may require updates to the scraping logic.
- The AI model requires internet access to download pre-trained weights if not available locally.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License 
## Author

MuhammadAhmad

