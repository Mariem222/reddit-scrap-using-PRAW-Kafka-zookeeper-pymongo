import datetime
import praw
from confluent_kafka import Producer
from pymongo import MongoClient

# Reddit API credentials
client_id = 'your client_id'
client_secret = 'your client_secret'
user_agent = 'your reddit username'

# Kafka settings
kafka_bootstrap_servers = 'host.docker.internal:29092'
kafka_topic = 'your_topic'


# Initialize PRAW Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)
# Subreddits related to our subject
subreddits = ['keyword(s)','of interst']

# Initialize Kafka Producer
producer = Producer({'bootstrap.servers': kafka_bootstrap_servers})

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def scrape_and_produce(subreddits):
    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        for post in subreddit.hot(limit=10):
            if post.selftext != '':
                message = f"\nID: {post.id}\n" \
                          f"URL: {post.url}\n" \
                          f"Name: {post.author.name if post.author else None}\n" \
                          f"Subreddit: {post.author.subreddit.display_name_prefixed if post.author else None}\n" \
                          f"Title: {post.title}\n" \
                          f"Upvotes: {post.score}\n" \
                          f"Comments: {post.num_comments}\n" \
                          f"Shares: {post.num_crossposts if hasattr(post, 'num_crossposts') else 0}\n" \
                          f"Date: {datetime.datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')}\n" \
                          f"Content: {post.selftext}\n" \
                          f"***********************************************************************"

                # Produce message to Kafka topic
                producer.produce(kafka_topic, value=message, callback=delivery_report)

    producer.flush()

# Call the function to scrape Reddit and produce to Kafka
scrape_and_produce(subreddits)
