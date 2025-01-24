# Password Generator and Strength Checker

This repository provides a Python-based password utility that includes functionalities for generating strong passwords,checking password strength, and estimating the time it would take to crack a given password. Additionally, it verifies if a password is commonly used by checking against the `rockyou.txt` password dataset.

## Features

- **Password Strength Checker**:
  - Evaluates the strength of a password based on length and character diversity.
  - Provides feedback on whether the password is strong, weak, or very weak.
  - Scores passwords out of 7 points for better visualization of strength.

- **Password Generator**:
  - Generates secure passwords of random lengths between 16-20 characters.
  - Combines uppercase, lowercase, digits, and special characters for maximum strength.

- **Time to Crack Estimator**:
  - Estimates the time required to crack a password based on its character set and length.
  - Formats the time duration into a human-readable format.

- **Common Password Check**:
  - Verifies if a password exists in the `rockyou.txt` dataset.
  - Prompts the user to generate a stronger password if the entered password is commonly used.

## Requirements

- Python 3.x
- A copy of `rockyou.txt` for the common password check.
- 

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/AbdulhameedAjibola/Password-Generator.git
