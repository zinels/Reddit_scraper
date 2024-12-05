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
---



