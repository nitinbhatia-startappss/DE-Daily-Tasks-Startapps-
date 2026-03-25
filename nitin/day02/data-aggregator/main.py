import requests
import pandas as pd

BASE_URL = "https://jsonplaceholder.typicode.com"
# Fetching POSTS
response = requests.get(f"{BASE_URL}/posts")
posts = response.json()

print(type(posts))
print(len(posts))
print(posts[0])

#Fetching COMMENTS
comment_response = requests.get(f"{BASE_URL}/comments")
comments = comment_response.json()
print(type(comments))
print(len(comments))
print(comments[0])

#counting comments per post 
comments_counts = {}
for comment in comments:
    post_id = comment["postId"]
    if post_id in comments_counts:
        comments_counts[post_id] +=1
    else:
        comments_counts[post_id] = 1
print(comments_counts)

# Creating DATAFRAME
df = pd.DataFrame(posts)
df["comment_count"] = df["id"].apply(lambda post_id: comments_counts.get(post_id, 0))
print(df.head())

# Creating CSV
df.to_csv("posts_with_comment_counts.csv", index=False)
print("Saved")

