# Toolbox-CS-SLD

## Description

Toolbox-CS-SLD is a cybersecurity toolbox designed to assist security professionals in their daily tasks. It includes various scripts for common security operations such as SSH brute-forcing, password checking, and network scanning.

## Features

- **SSH Brute Force**: Attempts to gain SSH access using a list of usernames and passwords.
- **Password Checker**: Validates password strength and compliance with security policies.
- **Network Scanner**: Uses Nmap to scan and report on network devices.

## Installation

### Prerequisites

- Python 3.x

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Momollait/toolbox-CS-SLD.git
   cd toolbox-CS-SLD
   ```

2. **Run the toolbox**:
   ```bash
   python main.py
   ```

## Usage

Each script can be executed through the main interface provided by `main.py`.

### SSH Brute Force

The SSH Brute Force tool attempts to connect to a machine via SSH using a list of usernames and passwords. It is useful for testing the strength of SSH passwords.

### Password Checker

This tool checks the strength of a password by evaluating its length, complexity, and compliance with security policies.

### Network Scanner

The Network Scanner uses Nmap to scan a network and identify connected devices, open ports, and running services.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests for new features or bug fixes.

## License

This project is licensed under the SupDeVinci License. Thanks to you

## Contact

For any questions or feedback, please contact me on Discord : Momolle.

## Repository Structure

- `main.py`: Main interface for the toolbox.
- `bruteforcessh.py`: Script for SSH brute force attacks.
- `check_password.py`: Script for checking password strength.
- `scannmap.py`: Script for network scanning.
- `web_vuln_scanner.py` : Script for IP Address scanning. 
- `README.md`: Project documentation.

