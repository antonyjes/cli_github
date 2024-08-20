from dotenv import load_dotenv
load_dotenv()

import click
import os
import requests

@click.command()
@click.argument('username')
def activity(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {"X-GitHub-Api-Version": "2022-11-28", "Accept": "application/vnd.github+json"}

    if os.environ['GITHUB_TOKEN']:
        headers['Authorization'] = f"Bearer {os.environ.get('GITHUB_TOKEN')}"
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        events = response.json()

        for event in events:
            click.echo(f"Event type: {event['type']}")
            click.echo(f"Repository: {event['repo']['name']}")
            click.echo(f"Created at: {event['created_at']}")
            click.echo("---" * 10)
    else:
        click.echo(f"Error: {response.status_code}")