import subprocess
from github import Github
import os

DIR_PATH = 'auto-commit/foo'


def list_all_files(directory: str):
    all_entries = os.listdir(directory)
    files = [entry for entry in all_entries if os.path.isfile(os.path.join(directory, entry))]

    return files


def get_day_number():
    file_names = list_all_files(DIR_PATH)
    max_cnt = -1
    for file in file_names:
        if file.startswith('day_'):
            max_cnt = max(max_cnt, int(file.split('.')[0][4:]))
    return max_cnt + 1


def commit_file(file: str):
    cmd = ['git', 'add', file]
    subprocess.run(cmd)

    cmd = ['git', 'commit', '-m', f'adding {file}']
    subprocess.run(cmd)

    cmd = ['git', 'push', 'origin', 'master']
    subprocess.run(cmd)


def add_content_to_file(file: str, day_number: int):
    g = Github()
    repo_name = "kamyu104/LeetCode-Solutions"
    path = "Python"

    repo = g.get_repo(repo_name)
    dir_content = repo.get_contents(path)
    cnt = 0
    for content_file in dir_content:
        if content_file.type == "file":
            print(cnt, day_number, content_file.type)
            if cnt == day_number:
                file_content = content_file.decoded_content.decode("utf-8")
                with open(file, "w") as f:
                    f.write(file_content)
                print("Done writing to file", file)
                break
            cnt += 1


def create_file_and_commit():
    day_number = get_day_number()
    file = 'day_' + str(day_number) + '.py'
    file = os.path.join(DIR_PATH, file)
    print("Writing to file", file)
    add_content_to_file(file, day_number)
    commit_file(file)


if __name__ == '__main__':
    create_file_and_commit()
