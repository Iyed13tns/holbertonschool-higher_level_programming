
#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print their titles."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {response.status_code}')
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts")

def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save them to a CSV file."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['userId', 'id', 'title', 'body'])
            writer.writeheader()
            for post in posts:
                writer.writerow(post)
        print("Posts saved to posts.csv")
    else:
        print("Failed to fetch posts")

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()