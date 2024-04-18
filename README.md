# URL Status Checker

This Python script checks the status of URLs derived from .png files in a specified directory and writes the results to a CSV file.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.x
- requests library

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. Clone the repo
```bash
git clone https://github.com/your_username_/Project-Name.git
```

2. Install Python packages
```bash
pip install -r requirements.txt
```

## Running the script

You can run the script using the following command:

```bash
python main.py
```

## How it works

1. The script first gets all filenames in the specified directory.
2. It then filters for .png files.
3. These filenames are then converted to URLs using a base URL.
4. The script then checks if these URLs exist and writes the status to a CSV file.

## Authors

* **Your Name** - *Initial work* - [YourUsername](https://github.com/your_username_)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details