import os
import random
from datetime import datetime, timedelta

def make_commits():
    # Verify Git configuration
    if not os.system('git config user.name'):
        os.system('git config --global user.name "Your Name"')
    if not os.system('git config user.email'):
        os.system('git config --global user.email "your@email.com"')

    # Initialize file
    with open('contributions.txt', 'a') as f:
        f.write('Initialized\n')

    # Date range (2024 only)
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    current_date = start_date

    while current_date <= end_date:
        # Skip weekends more often
        if current_date.weekday() >= 5 and random.random() < 0.7:
            current_date += timedelta(days=1)
            continue

        # Random commits (1-4 on weekdays)
        commits_today = random.choices(
            [1, 2, 3, 4, 5, 6,7,8,9,10],
            weights=[0.3, 0.3, 0.2, 0.1, 0.05, 0.05,0.4,0.25],
            k=1
        )[0]

        for _ in range(commits_today):
            # Work hours (9-17) have 80% probability
            hour = random.choices(
                [random.randint(9, 17), random.randint(0, 23)],
                weights=[0.8, 0.2],
                k=1
            )[0]

            commit_date = current_date.replace(
                hour=hour,
                minute=random.randint(0, 59),
                second=random.randint(0, 59)
            )

            # Format for Git
            git_date = commit_date.strftime('%Y-%m-%d %H:%M:%S')

            # Make a unique change
            with open('contributions.txt', 'a') as f:
                f.write(f'{git_date}\n')

            # Critical: Set both author and committer dates
            os.system('git add contributions.txt')
            os.system(f'GIT_AUTHOR_DATE="{git_date}" GIT_COMMITTER_DATE="{git_date}" git commit -m "Contribution: {git_date}"')

        # Move to next day
        current_date += timedelta(days=1)

    # Push to main branch
    os.system('git branch -M main')
    os.system('git push -u origin main')

def setup_repository():
    if not os.path.exists('.git'):
        os.system('git init')
    
    # Verify remote exists
    if not os.system('git remote get-url origin'):
        print("Error: No remote repository configured!")
        print("Create a new empty repository on GitHub and run:")
        print("git remote add origin https://github.com/D-nduati/daudi.git")
        exit(1)

if __name__ == '__main__':
    setup_repository()
    make_commits()
    print("Commit generation complete. Check your GitHub contributions graph!")