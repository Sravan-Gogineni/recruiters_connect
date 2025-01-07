
# LinkedIn Recruiter Connection Automation

This Python script automates the process of connecting with recruiters on LinkedIn. It simplifies the task of sending connection requests to recruiters, helping to expand your professional network.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Requirements](#requirements)
4. [License](#license)

## Installation

### Step 1: Clone the Repository
Clone the repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/linkedin-recruiter-automation.git
cd linkedin-recruiter-automation
```

### Step 2: Install Dependencies
The script requires the `selenium` package to automate the browser. Install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Ensure that you have Google Chrome or Chromium installed on your machine, along with the corresponding [ChromeDriver](https://sites.google.com/chromium.org/driver/).

## Usage

### Step 1: Set up LinkedIn Credentials
Store your LinkedIn username and password in the script or through an appropriate method for security.

### Step 2: Run the Script
To start the automation, run the following command:

```bash
python connect_to_recruiters.py
```

The script will automatically log into LinkedIn and begin sending connection requests to recruiters.

## Requirements

- Python 3.12
- Google Chrome (or Chromium)
- ChromeDriver
- Selenium (`pip install selenium`)

