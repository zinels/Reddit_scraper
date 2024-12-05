# **Reddit Education Post Collector**

This project is a Python-based tool designed to collect education-related posts from Reddit. Using the PRAW (Python Reddit API Wrapper) library, the script fetches data from multiple subreddits, including titles, authors, upvotes, comments, and subreddit names. The collected data is saved in a structured CSV file, making it easy to analyze.

---

## **Features**

- **Search Across Subreddits**: Fetch education-related posts from subreddits like `r/Education`, `r/EdTech`, and `r/OnlineLearning`.
- **Dynamic Input**: Specify how many posts to fetch.
- **Error Handling**: Handles invalid inputs and API constraints (e.g., Reddit’s limits on the number of results).
- **CSV Export**: Saves the data in a user-friendly CSV format.

---

## **Technologies Used**

- **Python**: Core programming language for scripting.
- **PRAW**: Python Reddit API Wrapper for accessing Reddit data.
- **Pandas**: Used for structuring data and exporting to CSV.

---

## **Project Structure**

```plaintext
reddit-education-post-collector/
│
├── reddit_scraper.py       # Main Python script for fetching and saving Reddit data
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── reddit_education_posts.csv # Example output file (generated after running the script)
Installation and Setup
Prerequisites
Python 3.6+ installed on your system.
A Reddit account with API credentials. Follow these steps:
Go to the Reddit Developer Portal.
Create a new application of type script.
Obtain your Client ID, Client Secret, and set a User Agent.
Clone the Repository
bash
Copy code
git clone https://github.com/your-username/reddit-education-post-collector.git
cd reddit-education-post-collector
Install Dependencies
Use pip to install the required Python libraries:

bash
Copy code
pip install -r requirements.txt
Set Up the Script
Edit the reddit_scraper.py file to include your Reddit API credentials:

python
Copy code
CLIENT_ID = 'your_client_id'          # Replace with your actual Client ID
CLIENT_SECRET = 'your_client_secret'  # Replace with your actual Client Secret
USER_AGENT = 'Education_post_collector'  # Replace with your app's user agent
Usage
Run the Script: Execute the script with:

bash
Copy code
python reddit_scraper.py
Enter User Input: When prompted, specify the number of posts to fetch. If the number exceeds Reddit's API constraints (e.g., 1000 posts), the script will adjust and notify you.

Check the Output: The results will be saved to a CSV file named reddit_education_posts.csv in the project directory.

Example Output
Sample Console Output
plaintext
Copy code
Enter the number of results to fetch (Maximum 1000): 50
Searching in r/education...
Searching in r/EdTech...
Searching in r/OnlineLearning...
Fetched 50 results successfully.
Results saved to reddit_education_posts.csv
Sample CSV File
Title	Author	Upvotes	Comments	Subreddit
"Online Education Pros/Cons"	JohnDoe	123	45	education
"EdTech Tools for Schools"	JaneSmith	89	12	EdTech
Limitations
Reddit API Limits: The script is subject to Reddit's API constraints:
A maximum of 1000 results can be fetched per query.
Pagination beyond 1000 posts is not supported.
Query-Specific Results: If fewer matching posts are available, the script will only fetch the available ones.
Enhancements (Future Scope)
Data Visualization:
Generate charts for post engagement metrics (e.g., upvotes vs. comments).
Web Interface:
Build a user-friendly web interface using Streamlit for non-technical users.
Scheduled Automation:
Automate the script to run periodically and update the CSV file.
Contributing
Contributions are welcome! If you have suggestions or ideas, feel free to:

Fork this repository.
Create a new branch for your feature or fix.
Submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For questions or suggestions, feel free to reach out:

GitHub: your-username
Email: your-email@example.com
markdown
Copy code

---

### **How to Use This**

1. Go to your GitHub repository.
2. Click on the **README.md** file or create one if it doesn’t exist.
3. Click the **Edit (pencil)** icon or create a new file.
4. Paste the entire code block above into the README file.
5. Replace placeholders:
   - `your-username` with your GitHub username.
   - `your-client-id`, `your-client-secret`, and `your-email@example.com` with your actual details.
6. Commit the changes with a meaningful commit message like:
   ```text
   Added detailed README for Reddit Education Post Collector project
Save the file.
This will create a professional-looking README for your project. Let me know if you need further assistance! 😊
