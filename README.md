# Market Researcher

App to leverage LLMs to research a company type and return a report.

## Features

- Researches a given company type using LLMs.
- Identifies top companies in the specified category.
- Gathers details for each identified company.
- Generates a consolidated report based on the research.

## How to Use

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the application:**
    ```bash
    streamlit run app.py
    ```
3.  Enter the company type you want to research in the input field.
4.  Click "Submit".
5.  The research report will be displayed in the text area below.

## Project Structure

-   `app.py`: Main Streamlit application file.
-   `researcher.py`: Contains the core logic for market research, including classes for finding companies, getting details, and generating reports.
-   `ai_providers.py`: Manages interactions with the AI model provider (e.g., Bedrock).
-   `models.py`: Defines data structures used in the project (e.g., `Company` class).
-   `utils.py`: Contains utility functions, such as the `retry` decorator.
-   `requirements.txt`: Lists the Python dependencies for the project.
-   `README.md`: This file, providing an overview of the project.
-   `test.py`: Contains tests for the project (Note: This file was observed in `ls` but not read. Assuming it contains tests).
-   `.gitignore`: Specifies intentionally untracked files that Git should ignore.


## Dependencies

The project relies on the following Python libraries:

- streamlit
- boto3
- python-dotenv
- anthropic (implicitly, via Bedrock)

These can be installed by running `pip install -r requirements.txt`.

## TODO

The following tasks are pending based on comments in the code:

-   **ai_providers.py:**
    -   Make computer use work on Mac Chrome.
    -   Define the response format for computer use.
    -   Optimize the system prompt.
    -   Increase `max_attempts` for retry after more testing and add timeout.
-   **models.py:**
    -   Add more fields to the `Company` class.
-   **researcher.py:**
    -   Parse LLM response into a list of company names in `find_top_companies`.
    -   Call LLM and parse results into a `Company` object in `get_company_details`.
    -   Call LLM and parse results into a report in `generate_report`.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch for your changes.
3.  Make your changes, including clear comments and tests where applicable.
4.  Submit a pull request for review.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details. (Note: A `LICENSE` file will need to be created if one doesn't exist).
