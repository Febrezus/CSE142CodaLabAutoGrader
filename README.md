# CSE142CodaLabAutoGrader

## How to use:
1. Move all repo files into unzipped CodaLab folder
2. Move csv leaderboard file into unzipped CodaLab folder
3. Move moss.pl into unzipped CodaLab folder

4. Run:
```
$ python3 separate.py
```
*(This will separate and organize all participant submissions for use in the future)*

5. Run:
```
$ python3 scores.py
```
*(Important! Change the grading formula for the submissions. This will also save the scores to scores.csv)*

6. Run:
```
$ python3 checker.py
```
*(This will check all the submissions imports, checking if they imported any modules that are blacklisted or not whitelisted. Optionally, run it with --moss to also run moss on all submissions)*