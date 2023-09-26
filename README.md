# Gmail Automation Project

This project aims to automate various tasks related to Gmail using the Gmail API. It provides functionalities to manage labels, retrieve emails based on specific queries, and apply labels to them.

## Prerequisites

- Python 3.x
- Libraries:
  - google-auth-oauthlib
  - google-auth-httplib2
  - google-api-python-client

## Getting Started

1. **Clone the repository:**

    ```
    git clone https://github.com/yourusername/gmail-automation.git
    ```

2. **Set up Google API credentials:**

   - Create a project in the [Google Developer Console](https://console.developers.google.com/).
   - Enable the Gmail API for the project.
   - Create credentials (OAuth 2.0 client ID) and download the `credentials.json` file. Place it in the project directory.

3. **Install dependencies:**

    ```
    pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
    ```

## Usage

### Quickstart

- Run the `quickstart.py` file to start the Gmail automation. This file demonstrates basic functionalities such as retrieving emails and applying labels.

### User Class

- The `user.py` file contains a `user` class that helps in managing labels.
- The `find_labelid` method retrieves the label ID for a given label name.

### Label Class

- The `label.py` file defines a `label` class that represents a Gmail label.
- The `createLabel` method creates a new label with the specified color and name.

### Generate Labels

- The `generateLabels` function in `quickstart.py` generates labels for common senders based on a specified query. It retrieves emails and creates labels for them.

### Additional Notes

- Modify the `SCOPES` variable in `quickstart.py` to request additional permissions as needed.

## Contributing

Contributions are welcome! Feel free to submit pull requests for new features, bug fixes, or enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
