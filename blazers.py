
from atproto import Client

def blazers_bsky_feed():
    client = Client()
    client.login('mankindrc.bsky.social', 'Korova128!')

    data = client.app.bsky.feed.get_feed({
        'feed': 'at://did:plc:kdmwm6a34224nwf7netdx6gk/app.bsky.feed.generator/ripcity',
        'limit': 15,
    })

    feed = data.feed
    next_page = data.cursor

    parsed_posts = []

    for post in feed:
        post_data = post.post  # Get the PostView object
        
        # Extracting the main details
        try:
            author = post_data.author.display_name if post_data.author else "Unknown Author"
            content = post_data.record.text if hasattr(post_data.record, 'text') else "No content"
            created_at = post_data.record.created_at if hasattr(post_data.record, 'created_at') else "No date available"

            parsed_posts.append({
                'author': author,
                'content': content,
                'created_at': created_at
            })
        except AttributeError as e:
            print(f"Error parsing post: {e}")

    return parsed_posts
