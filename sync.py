#!/usr/bin/python

import yaml
import sys
import os
from subprocess import call
from distutils.dir_util import copy_tree, remove_tree

config = "sync.yml"
tmp = "sync"

if len(sys.argv) > 1:
  config = sys.argv[1]

if len(sys.argv) > 2:
  print("Invalid usage: ./sync.py <config filename>")

print("Using configuration: " + config)
print("Using tmp directory: " + tmp)

# rm -rf tmp directory
if os.path.exists(tmp):
  print("Cleaining existing tmp...")
  remove_tree(tmp)

with open(config, "r") as file:
  data = yaml.load(file)
  git = data["git"]
  tmp = data["tmp"]
  abort = data["abort-on-failure"]
  repos = data["repositories"]

  successes = 0
  total = len(repos)

  for repo in repos:
    url = repo["url"]
    branch = repo["branch"]
    target = repo["target"]

    print("=== {} ({}) --> {} ===".format(url, branch, target))

    # git clone repo into tmp directory
    print("Cloning repository...")
    call(" ".join([
      git,
      "clone",
      "--depth=1",
      "-b " + branch,
      url,
      tmp
    ]), shell=True)

    dotgit = os.path.join(tmp, ".git")

    if not os.path.exists(dotgit):
      print("WARNING: Nothing cloned/found!")

      if abort:
        print("SEVERE: Aborting sync, as defined in configuration.")
        break
      else:
        continue
    else:
      print("Success!")
      successes += 1

    # unnecessary junk
    print("Removing .git...")
    remove_tree(dotgit)

    # move to desired folder
    print("Moving to target...")
    copy_tree(tmp, target)

    # rm -rf tmp directory
    print("Cleaning...")
    remove_tree(tmp)

print("====================")
print("Sync completed ({}/{})".format(successes, total))