import os
import time
import multiprocessing

from datetime import datetime
from dotenv import load_dotenv
from github import Github, Commit
from rich import print
from rich.console import Console
from rich.progress import Progress

"""
This script retrieves infromation about all new files that have
been added to a certain repository branch in a specific time frame.

Reads certain variables from the environment or a .env file. All are required:

    GH_TOKEN          GitHub account access token.
    BRANCH            Branch to search commits from.
    TARGET            Name of the GitHub repository. The user must have read access.
    DATE_START        List all commits from this date. Format YYYY/MM/DD hh:mm:ss.
    DATE_END          List all commits upto this date. Format YYYY/MM/DD hh:mm:ss.
"""
load_dotenv()


branch = os.environ.get("BRANCH")
target = os.environ.get("TARGET")
g = Github(os.environ.get("GH_TOKEN"))
date_start = datetime.strptime(os.environ.get("DATE_START"), '%Y/%m/%d %H:%M:%S') 
date_end = datetime.strptime(os.environ.get("DATE_END"), '%Y/%m/%d %H:%M:%S') 
repo = None
# Gather target repo data
with Console().status(
    "[yellow]Fetching repository metadata from GitHub...", spinner="bouncingBar"
) as status:
    repo = list(filter(lambda f: f.full_name == target or f.name == target, g.get_user().get_repos()))[0]
    commits = repo.get_commits(sha=branch, since=date_start, until=date_end)


all_added_files = set()

with Progress(transient=True) as progress:
    task = progress.add_task(f"[yellow]Processing commits between {date_start} and {date_end}...", total=commits.totalCount)
    
    for commit in commits:
        progress.update(task, description=f"[yellow]Processing commits between {date_start} and {date_end}...\n[blue][ Added files: {len(all_added_files)} ] [yellow]{commit.sha}")
                        
        files = set(map(lambda f: f.filename, filter(lambda f: f.status == "added", commit.files)))
        all_added_files |= files
        
        progress.advance(task)
    
    progress.update(task, description="[blue]Complete Task", completed=True)

print(*all_added_files,sep='\n')
