# Selenium Automated Tests

## Overview

This repository contains a Python script that automates interactions with a web application using Selenium. The script logs into the application with multiple user accounts, performs various actions such as adding and deleting tasks, and then logs out.

## Requirements

To run these tests, you need:

1. **Python**: Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Selenium**: Install the Selenium library using pip. Run the following command to install it:
   ```bash
   pip install selenium
    ```
## Setup

3. **Download and Install ChromeDriver**: Place the `chromedriver.exe` file in a directory of your choice. Update the `chrome_driver_path` variable in the script to point to this location.


## Running the Tests

1. **Update the Script**: Ensure the `chrome_driver_path` in the script points to the location of your `chromedriver.exe` file.

2. **Execute the Script**: Run the script using Python:
   ```bash
   python your_script_name.py
    ```

## Notes

- The script will perform the following actions for each user account: log in, add tasks, delete tasks, and log out.
- The number of instances is set to 3 by default, corresponding to the number of credentials provided. Adjust `num_instances` in the script if you need more or fewer test instances.

## Troubleshooting

- **Driver Not Found**: Ensure that the path to ChromeDriver is correctly set in the script.
- **Browser Version Mismatch**: Make sure the version of ChromeDriver matches the version of Google Chrome installed on your machine.
