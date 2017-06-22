# sync-with-git

With this small Python tool, you can copy the contents of a set of Git repositories into local directories.

## Usage

First modify the `sync.yml` file, then run the script, `./sync.py` with an optional parameter to specify a different YAML configuration file.

## Configuration

The template is self-explanatory!

```yaml
# the git command (may have to specify "/usr/bin/git" for example)
git: git

# the temp directory that sync will use for cloning
tmp: tmp-sync

# set to true to stop subsequent cloning upon failing to clone any repository 
abort-on-failure: false

# the list of repositories to clone, in the order provided
repositories:

# this will clone the specified repo with the branch dev into the working directory
- url: git@github.com:thekeenant/cloudflare-mc.git
  branch: master
  target: ./

# this will clone the specified repo with the branch dev into ./repo2-copy
- url: git@github.com:thekeenant/repo2.git
  branch: dev
  target: ./repo2-copy
```