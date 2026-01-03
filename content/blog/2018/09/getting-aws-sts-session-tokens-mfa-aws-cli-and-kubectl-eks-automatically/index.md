---
nid: 2873
title: "Getting AWS STS Session Tokens for MFA with AWS CLI and kubectl for EKS automatically"
slug: "getting-aws-sts-session-tokens-mfa-aws-cli-and-kubectl-eks-automatically"
date: 2018-09-19T16:16:27+00:00
drupal:
  nid: 2873
  path: /blog/2018/getting-aws-sts-session-tokens-mfa-aws-cli-and-kubectl-eks-automatically
  body_format: untouched
  redirects: []
tags:
  - ansible
  - aws
  - cli
  - executable
  - mfa
  - playbook
  - security
  - sts
---

<p>I've been working on some projects which require MFA for all access, including for CLI access and things like using <code>kubectl</code> with Amazon EKS. One super-annoying aspect of requiring MFA for CLI operations is that every day or so, you have to update your STS access token—and also for that token to work you have to update an AWS profile's Access Key ID and Secret Access Key.</p>

<p>I had a little bash function that would allow me to input a token code from my MFA device and it would spit out the values to put into my <code>.aws/credentials</code> file, but it was still tiring copying and pasting three values <em>every single morning</em>.</p>

<p>So I wrote a neat little <em>executable</em> Ansible playbook which does everything for me:</p>

<script src="https://gist.github.com/geerlingguy/0a524082674e72132b1dea44df275cbb.js"></script>

<p>To use it, you can download the contents of that file to <code>/usr/local/bin/aws-sts-token</code>, make the file executable (<code>chmod +x /usr/local/bin/aws-sts-token</code>), and run the command:</p>

```
./aws-sts-token -e aws_userarn=ARN_FROM_IAM -e aws_profile=PROFILE -e aws_sts_profile=STS_PROFILE -e token_code=TOKEN
```

<p>This assumes you have Ansible and the AWS CLI installed on your workstation. I wrapped the call to the executable in my original bash function so I can, once a day, run the following command to 'log in' via MFA to use AWS CLI and other applications which require a session token in the AWS profile:</p>

```
awssts MFA_TOKEN_HERE
```

<p>The bash function is:</p>


```
# AWS STS Token.
function awssts() {
  if [[ ! "$1" ]] ; then
    echo "You must supply a token code."
    return 0
  fi

  aws-sts-token -e "aws_userarn=IAM_ARN_FOR_MFA" -e aws_profile="PROFILE_WITHOUT_TOKEN" -e aws_sts_profile="PROFILE_FOR_STS" -e token_code=$1
  return 0
}
```

