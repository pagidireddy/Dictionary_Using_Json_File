# JSON Dictionary Project

This project is designed to provide a simple dictionary functionality using a JSON file as the data source.

## Files

### data/dictionary.json

This folder contains the JSON file used as the dictionary data source.

### src/utils.py

This file contains the code responsible for fetching information from the JSON file.

### Dictionary_Using_Json_File/dictionary.py

This file contains the main functionality of the dictionary project. It takes inputs from the user and returns the corresponding data.

## How to Use

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Install any dependencies by running `pip install -r requirements.txt` (if there are any).
5. Run the `dictionary.py` file using Python by running `python Dictionary_Using_Json_File/dictionary.py`.
6. Follow the instructions provided by the program to interact with the dictionary.

## Usage Example

```python
# Import the dictionary function from dictionary.py
from src import dictionary

# Call the function with a word to look up
result = dictionary.lookup_word("your_word")

# Print the result
print(result)
