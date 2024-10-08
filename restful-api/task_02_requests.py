#!/usr/bin/python3
"""This module handles a method to fetch posts
from JSONPlaceholder using requests.get()
"""
import requests
import json
import csv


def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response:
        data = response.json()
    for post in data:
        print(post["title"])

def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response:
        data = response.json()
    fields = ['id', 'title', 'body']
    with open('posts.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for post in data:
            writer.writerow({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
