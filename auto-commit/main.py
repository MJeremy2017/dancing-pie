import subprocess


def create_file(file: str):
    with open(file, 'w') as f:
        f.write("this is a test file")
    print("created file", file)


def commit_file(file: str):
    cmd = ['git', 'add', file]
    subprocess.run(cmd)

    cmd = ['git', 'commit', '-m', f'adding {file}']
    subprocess.run(cmd)

    cmd = ['git', 'push', 'origin', 'master']
    subprocess.run(cmd)


def add_content_to_file(file: str):
    # TODO
    pass


def make_new_file_commit(file: str):
    create_file(file)
    add_content_to_file(file)
    commit_file(file)


if __name__ == '__main__':
    # TODO schedule
    make_new_file_commit("auto-commit/foo/day-1.py")
