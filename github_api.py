import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)
# saving response of api in variable
response_dict = r.json()

print("Total repos: ", response_dict['total_count'])

repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    
# start visualizating 
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_labels = True
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most starred XX repos on GitHub"

chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')

