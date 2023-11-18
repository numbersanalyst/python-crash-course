import requests
from plotly import offline

URL = "https://api.github.com/search/repositories?q=language:ruby&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(URL, headers=headers, timeout=100)
print(f"Status code: {r.status_code}")

response_dict = r.json()
repo_dicts = response_dict["items"]
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict["stargazers_count"])

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    label = f"{owner}<br />{description}"
    labels.append(label)

data = [
    {
        "type": "bar",
        "x": repo_links,
        "y": stars,
        "hovertext": labels,
        "marker": {
            "color": stars,
            "colorscale": "Plotly3",
            "reversescale": True,
            "line": {"width": 0.5, "color": "darkgray"},
        },
        "opacity": 0.6,
    }
]

my_layout = {
    "title": "Ruby repositories with the highest amouth of stars on Github",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Repository",
    },
    "yaxis": {
        "title": "Stars",
    },
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="ruby_repos.html")