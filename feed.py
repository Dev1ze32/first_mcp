from fastmcp import FastMCP
import feedparser

mcp = FastMCP(name="feed_reader")

@mcp.tool(name="free code camp feed search")
def free_code_camp_feed_search(query: str, max_results: int = 3):
    feed = feedparser.parse("https://www.freecodecamp.org/news/rss/")  
    results = []
    for entry in feed.entries:
        title = entry.get("title", "").lower()
        description = entry.get("description", "").lower()
        if query.lower() in title or query.lower() in description:
            results.append({'title': title, 'description': description, 'link': entry.get("link", "")})
        if len(results) >= max_results:
            break
    return results or [{'message': 'No results found.'}]

@mcp.tool(name="fcc_youtube_search")
def fcc_youtube_search(query: str, max_results: int = 3):
    feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ")  
    results = []
    for entry in feed.entries:
        title = entry.get("title", "").lower()
        description = entry.get("description", "").lower()
        if query.lower() in title:
            results.append({'title': title, 'description': description, 'link': entry.get("link", "")})
        if len(results) >= max_results:
            break
    return results or [{'message': 'No results found.'}]

if __name__ == "__main__":
    mcp.run(transport="http")  # http transport
