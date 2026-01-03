---
nid: 2788
title: "Mount an AWS EFS filesystem on an EC2 instance with Ansible"
slug: "mount-aws-efs-filesystem-on-ec2-instance-ansible"
date: 2017-06-22T13:14:41+00:00
drupal:
  nid: 2788
  path: /blog/2017/mount-aws-efs-filesystem-on-ec2-instance-ansible
  body_format: markdown
  redirects: []
tags:
  - ansible
  - automation
  - aws
  - efs
  - filesystem
  - mount
  - nfs
---

If you run your infrastructure inside Amazon's cloud (AWS), and you need to mount a shared filesystem on multiple servers (e.g. for Drupal's shared files folder, or Magento's media folder), Amazon Elastic File System (EFS) is a reliable and inexpensive solution. EFS is basically a 'hosted NFS mount' that can scale as your directory grows, and mounts are free—so, unlike many other shared filesystem solutions, there's no per-server/per-mount fees; all you pay for is the storage space (bandwidth is even free, since it's all internal to AWS!).

I needed to automate the mounting of an EFS volume in an Amazon EC2 instance so I could perform some operations on the shared volume, and Ansible makes managing things really simple. In the below playbook—which easily works with any popular distribution (just change the `nfs_package` to suit your needs)—an EFS volume is mounted on an EC2 instance:

```
- hosts: ec2_server
  become: yes
  gather_facts: yes

  vars:
    aws_profile: default
    aws_region: us-east-1
    nfs_package: nfs-common # nfs-utils on RHEL/CentOS/Amazon Linux
    efs_file_system_id: [ID here]
    efs_mount_dir: /efs

  tasks:
    - name: Ensure NFS is installed.
      package: "name={{ nfs_package }} state=installed"

    - name: Ensure mount directory exists.
      file:
        path: "{{ efs_mount_dir }}"
        state: directory
        mode: 0755

    - name: Get current AZ from AWS.
      uri:
        url: http://169.254.169.254/latest/meta-data/placement/availability-zone
        return_content: yes
      register: aws_current_az

    - name: Ensure EFS volume is mounted.
      mount:
        name: "{{ efs_mount_dir }}"
        src: "{{ aws_current_az.content }}.{{ efs_file_system_id }}.efs.{{ aws_region }}.amazonaws.com:/"
        fstype: nfs4
        opts: nfsvers=4.1
        state: mounted

    # Print the contents of the mount to the log.
    - command: "ls -lah {{ efs_mount_dir }}"
      register: efs_contents
    - debug: var=efs_contents
```

You need to provide the `efs_file_system_id`, and you also need to make sure the EFS volume [has a mount target](http://docs.aws.amazon.com/efs/latest/ug/manage-fs-access-create-delete-mount-targets.html) in the same Availability Zone (AZ) as the EC2 instance where this playbook is run.

After you supply those variables, you can run the playbook against your EC2 instance, and it will mount the volume at `/efs`, then list the contents of the volume.

> Wondering what the request to 169.254.169.254 is doing? AWS provides a metadata service at that address so you can look up information about the EC2 instance, from within the EC2 instance. See [http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)
