from github import Github
import os
import re

def get_latest_release(user, repo):
    g = Github(os.getenv('GITHUB_TOKEN'))
    repo = g.get_user(user).get_repo(repo)
    releases = repo.get_releases()
    for release in releases:
        if release.tag_name.startswith('v4.'):
            return release.tag_name
    return None

def replace_version_in_files(version):
    template_files = ['kilosort4/Dockerfile.template', 'kilosort4/build.sh.template']
    output_files = ['kilosort4/Dockerfile', 'kilosort4/build.sh']
    for i in range(len(template_files)):
        with open(template_files[i], 'r') as f:
            content = f.read()
        content = re.sub(r'KILOSORT_VERSION', version, content)
        with open(output_files[i], 'w') as f:
            f.write(content)

def main():
    latest_release = get_latest_release('mouseland', 'kilosort')
    latest_version_location='./.github/artifacts/kilosort4-latest-version.txt'
    if latest_release:
        with open(latest_version_location, 'r') as f:
            last_checked_version = f.read().strip()
        if latest_release != last_checked_version:
            replace_version_in_files(latest_release)
            with open(latest_version_location, 'w') as f:
                f.write(latest_release)
            return 'true'
    return 'false'

if __name__ == "__main__":
    main()
