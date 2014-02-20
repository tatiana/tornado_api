"""
Module for retrieving git information, e.g. current hash.
"""

import subprocess


GET_BRANCH = 'git rev-parse --abbrev-ref HEAD'
GET_TAG = 'git describe --exact-match --tags HEAD'
GET_COMMIT = 'git rev-parse --verify HEAD'


def run(cmd):
    """
    Run a command on terminal and return the first line response
    """
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.stdout.readline().split('\n')[0]


def get_version_label():
    """
    Return current branch or tag, if any, otherwise return <DEFAULT_VERSION>
    """

    tag = run(GET_TAG)
    branch = run(GET_BRANCH)
    label = tag or branch
    if label == 'HEAD':
        label = 'unstaged'
    return label


def get_version_hash():
    """
    Return current git hash.
    """
    return run(GET_COMMIT)


def get_code_version():
    """
    Return <git branch or tag> | <git hash> of source code.
    """
    label = get_version_label()
    commit = get_version_hash()
    version = u"%s | %s" % (unicode(label), unicode(commit))
    return version
