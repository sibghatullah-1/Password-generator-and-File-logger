# 🔒 Secure Password Generator and Logger

A Python script that generates cryptographically secure, random passwords and securely logs them, along with a timestamp, to a local JSON file for later retrieval.

## How It Works

1.  The script presents a simple command-line interface (CLI) menu.
2.  **Password Generation:** When selected, the user is prompted to enter the desired length of the password. It uses the `secrets` module to generate a strong password consisting of letters, digits, and punctuation.
3.  **Logging:** The newly generated password and the exact date and time are automatically saved into a file named `password_logger.json`.
4.  **Search:** Users can search for previously generated passwords by their assigned numerical ID (key in the JSON file).

## Supported Features

| Option | Description |
| :--- | :--- |
| **Generate Password** | Creates a new random password of a specified length and logs it. |
| **Search Passwords** | Retrieves a previously logged password by its ID. |
| **Exit** | Closes the application. |

## 🚀 Usage

1.  Make sure **Python 3** is installed.
2.  **Save the script** as `password_generator.py`.
3.  **Run the script** from your terminal:

    ```bash
    python password_generator.py
    ```

4.  Follow the on-screen menu instructions.

### Output File Location

The script stores generated passwords in a JSON file called `password_logger.json`.

## ✨ Customization

### 1. File Path **(CRITICAL)**

### The script currently uses a hardcoded file path for the log file which you can change inside the script and provide your own path by replacing the path inside the the script with the path where you place the 'password_logger.json' :

```python
filename = "Enter your file path here for the password logger json file "
