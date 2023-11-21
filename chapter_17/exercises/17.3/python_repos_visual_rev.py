import requests
from plotly import offline

URL = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}


def get_data(URL, headers):
    """Get json data from API about repos"""
    r = requests.get(URL, headers=headers, timeout=100)
    return r


def get_repo_dicts(r):
    """Convert json data info about repos into python dict"""
    response_dict = r.json()
    repo_dicts = response_dict["items"]
    return repo_dicts


def get_project_data(repo_dicts):
    """Get data about repos to create a chart"""
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

    return repo_links, stars, labels


def make_data_visualization(repo_links, stars, labels):
    """Create a chart, data visualization"""
    data = [
        {
            "type": "bar",
            "x": repo_links,
            "y": stars,
            "hovertext": labels,
            "marker": {
                "color": "rgb(60,100,150)",
                "line": {"width": 1.5, "color": "rgb(25,25,25)"},
            },
            "opacity": 0.6,
        }
    ]

    my_layout = {
        "title": "Python repositories with the highest amouth of stars on Github",
        "titlefont": {"size": 28},
        "xaxis": {
            "title": "Repository",
            "titlefont": {"size": 24},
            "tickfont": {"size": 14},
        },
        "yaxis": {
            "title": "Stars",
            "titlefont": {"size": 24},
            "tickfont": {"size": 14},
        },
    }

    fig = {"data": data, "layout": my_layout}
    offline.plot(fig, filename="python_repos.html")


if __name__ == "__main__":
    r = get_data(URL, headers)
    repo_dicts = get_repo_dicts(r)
    repo_links, stars, labels = get_project_data(repo_dicts)
    make_data_visualization(repo_links, stars, labels)
