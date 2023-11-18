import requests
from plotly import offline

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url, timeout=100)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
links, titles, comments = [], [], []
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url, timeout=100)
    print(f"id: {submission_id}\tstatus code: {r.status_code}")
    response_dict = r.json()

    titles.append(response_dict["title"])
    link_title = titles[-1][:30] + "..." if len(titles[-1]) > 30 else titles[-1]
    link = f"<a href='https://news.ycombinator.com/item?id={submission_id}'>{link_title}</a>"
    links.append(link)
    comments.append(response_dict.get("descendants", 0))

data = [
    {
        "type": "bar",
        "x": links,
        "y": comments,
        "hovertext": titles,
        "marker": {
            "color": comments,
            "colorscale": "Plotly3",
        },
    }
]

my_layout = {
    "title": "Hacker News top 30",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "News",
        "categoryorder": "total descending",
    },
    "yaxis": {
        "title": "Comments",
    },
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="hacker_news_top30.html")
