from github import *
import yaml
import os
import sys

stream = file(sys.path[0] + '/config.yml', 'r') 
config = yaml.load(stream)
login = config['login']
token = config['token']
repo_dir = config['repo_dir']
repo_owner = config['repo_owner']

gh = github.GitHub(login, token)
for r in gh.repos.forUser(repo_owner):
    target_dir = "%s/%s" % (repo_dir, r.name)
    if ( os.path.exists(target_dir) & os.path.isdir(target_dir)) :
        print "target " +  target_dir + " exists already"
    else :
        git_url = "git@github.com:%s/%s.git" % (repo_owner, r.name)
        cmd = "pushd %s; git clone %s; popd" % (repo_dir, git_url)
        print cmd 
        os.system(cmd)

