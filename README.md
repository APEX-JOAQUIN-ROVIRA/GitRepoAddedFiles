# GitRepoAddedFiles

This script retrieves infromation about all new files that have been added to a certain repository branch in a specific time frame.

## Requirements

```bash
sudo apt install python3 python3-pip
pip install -r requirements.txt
```

## Usage

Set environment variables or configure the `.env` file with the following variables

- `GH_TOKEN=<YOUR_GITHUB_TOKEN>`, GitHub access token to be used for login.
- `BRANCH=master`, Search for commits in this branch.
- `TARGET=myOrg/projectA`, Name of the GitHub repository. The user must have read access.
- `DATE_START=1939/09/01 00:00:00`, List all commits from this date. Format `YYYY/MM/DD hh:mm:ss`.
- `DATE_END=1945/09/02 00:00:00`, List all commits upto this date. Format `YYYY/MM/DD hh:mm:ss`.

```bash
❯ python main.py
Some/New/File.txt
Another/File.pdf
...
```

> _**Note**: There is little/no error handling as this is just a simple automation script._
