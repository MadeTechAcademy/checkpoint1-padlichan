_duties_list = [
    "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.",
    "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members.",
    "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review.",
    "Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture.",
    "Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts",
    "Duty 6 Implement and improve release automation & orchestration, often using Application Programming Interfaces (API), as part of a continuous delivery and continuous deployment pipeline, ensuring that team(s) are able to deploy new code rapidly and safely.",
    "Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers). Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance.",
    "Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance.",
    "Duty 9 Apply leading security practices throughout the Software Development Lifecycle (SDLC).",
    "Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable.",
    "Duty 11 Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications.",
    "Duty 12 Look to automate any manual tasks that are repeated, often using APIs.",
    "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience."
]

_themes = {"Bootcamp": [1,2,3,4,13],
           "Automate!": [5,7,10],
           "Houston, Prepare to Launch": [6,7,10,12],
           "Going Deeper": [11],
           "Assemble!": [8],
           "Call Security": [9]}

def print_duties():
    for duty in _duties_list:
       print("{0}".format(duty))

def duties_to_html(path):
    with open(f"{path}/duties.html", 'w') as f:
        f.write("<html>\n")
        f.write("<body>\n")
        f.write("<ul>\n")
        for duty in _duties_list:
            f.write(f"\t<li>{duty}</li>\n\t<br>\n")
        f.write("</ul>\n")
        f.write("</body>\n")
        f.write("</html>\n")

def themes_to_html(path):
        with open(f"{path}/themes.html", 'w') as f:
            for theme in _themes:
                f.write(f"{theme}: {', '.join(str(x) for x in _themes[theme])}\n")

if __name__=="__main__":
    x = input("""
    Welcome to apprentice themes!\n
    Press (1) to list all the duties\n
    Press (2) to save all the duties to html\n
    Enter your choice:
    """)
    if x == '1':
        print_duties()
    elif x == '2':
        duties_to_html("./")