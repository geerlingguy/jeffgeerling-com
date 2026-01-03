---
nid: 2942
title: "Molecule fails on converge and says test instance was already 'created' and 'prepared'"
slug: "molecule-fails-on-converge-and-says-test-instance-was-already-created-and-prepared"
date: 2019-10-09T21:44:03+00:00
drupal:
  nid: 2942
  path: /blog/2019/molecule-fails-on-converge-and-says-test-instance-was-already-created-and-prepared
  body_format: markdown
  redirects: []
tags:
  - ansible
  - docker
  - molecule
  - test
  - testing
---

I hit this problem every once in a while; basically, I run `molecule test` or `molecule converge` (in this case it was for a Kubernetes Operator I was building with Ansible), and it says the instance is already created/prepared—even though it is not—and then Molecule fails on the 'Gathering Facts' portion of the converge step:

```
--> Scenario: 'test-local'
--> Action: 'dependency'
Skipping, missing the requirements file.
--> Scenario: 'test-local'
--> Action: 'create'
Skipping, instances already created.
--> Scenario: 'test-local'
--> Action: 'prepare'
Skipping, instances already prepared.
--> Scenario: 'test-local'
--> Action: 'converge'
    
    PLAY [Build Operator in Kubernetes docker container] ***************************
    
    TASK [Gathering Facts] *********************************************************
    fatal: [kind-test-local]: UNREACHABLE! => {"changed": false, "msg": "Authentication or permission failure. In some cases, you may have been able to authenticate and did not have permissions on the target directory. Consider changing the remote tmp path in ansible.cfg to a path rooted in \"/tmp\". Failed command was: ( umask 77 && mkdir -p \"` echo ~/.ansible/tmp/ansible-tmp-1570656925.36-200640620205465 `\" && echo ansible-tmp-1570656925.36-200640620205465=\"` echo ~/.ansible/tmp/ansible-tmp-1570656925.36-200640620205465 `\" ), exited with result 1", "unreachable": true}
```

This usually happens when I cleaned up a Molecule test container or VM myself, without using `molecule` to do so. And usually, it's fixed by running:

    molecule destroy

But in one case, I used a custom scenario, so I should've used:

    molecule destroy -s [scenario-name]

But I forgot to do that, so was puzzling over why deleting the `molecule/` directory from `/tmp` and `$TMPDIR` didn't fix any problems.

Eventually I ran `molecule --debug converge` to see all the paths in use, and noticed that some configs are stored in `~/.cache/molecule`.

So I went ahead and deleted the entire `~/.cache/molecule` directory (don't do this unless you know there aren't other active molecule environments that are being used!), and then ran `molecule converge -s [scenario-name]` again... and it worked!

In the future, I might remember to just make sure I do `molecule destroy` _with_ the scenario... or I'll Google the problem and find this blog post and _then_ do it :)
