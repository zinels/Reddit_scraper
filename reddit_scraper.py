import praw
import pandas as pd

# Reddit API credentials
CLIENT_ID = 'VRS6DQOEozc_el265Y3ENw'          # Replace with your actual Client ID
CLIENT_SECRET = 'u3prqyHtnAyGHm1r480ny9jZhqX9wQ'  # Replace with your actual Client Secret
USER_AGENT = 'Education_post_collector'  # A unique identifier for your app

# Set up Reddit API client
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

# Function to fetch posts from Reddit
def fetch_education_posts(subreddits, query, num_results):
    """
    Fetch posts from subreddits based on a query and the number of results requested.
    Args:
        subreddits (list): List of subreddit names to search in.
        query (str): Keyword to search for.
        num_results (int): Number of results requested.
    Returns:
        list: A list of dictionaries containing post details.
    """
    posts = []
    for subreddit in subreddits:
        print(f"Searching in r/{subreddit}...")
        try:
            subreddit_obj = reddit.subreddit(subreddit)
            for post in subreddit_obj.search(query, limit=num_results):
                # Append post details to the list
                posts.append({
                    'title': post.title,                  # Title of the post
                    'author': post.author.name if post.author else 'N/A',  # Author's name
                    'upvotes': post.score,               # Number of upvotes
                    'comments': post.num_comments,       # Number of comments
                    'subreddit': subreddit               # Subreddit name
                })
                if len(posts) >= num_results:  # Stop once we reach the desired number of results
                    break
        except Exception as e:
            print(f"Error fetching posts from r/{subreddit}: {e}")
        if len(posts) >= num_results:
            break  # Stop searching once the total number of results is reached
    return posts

# Main function to execute the script
def main():
    subreddits = ['education', 'EdTech', 'OnlineLearning']  # List of subreddits to search
    query = "Education"  # Search query
    try:
        num_results = int(input("Enter the number of results to fetch: "))  # Get number of results from the user
    except ValueError:
        print("Invalid input! Please enter an integer value.")
        return

    # Fetch posts
    posts = fetch_education_posts(subreddits, query, num_results)

    # Handle cases where fewer results are available
    if len(posts) < num_results:
        print(f"Only {len(posts)} results were found. This may be due to subreddit or query limitations.")
    else:
        print(f"Fetched {num_results} results successfully.")

    # Save results to CSV
    df = pd.DataFrame(posts)
    csv_filename = 'reddit_education_posts.csv'
    df.to_csv(csv_filename, index=False)
    print(f"Results saved to {csv_filename}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
