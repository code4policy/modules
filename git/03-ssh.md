# Git 3: SSH and Security

## Setup

First lets see if you already have SSH keys setup

Follow these instructions for connecting to Github via SSH.

https://help.github.com/articles/connecting-to-github-with-ssh/

## Lets see what we've just done

```
ls -al ~/.ssh/
```

This is your **public key**

```
cat ~/.ssh/id_rsa.pub
```

This is your **private key**

```
cat ~/.ssh/id_rsa
```

## Cryptography Basics

A brief aside...

Videos:

* [Cryptography 101](https://www.youtube.com/watch?v=fNC3jCCGJ0o)
* [What is Cryptography](https://www.youtube.com/watch?v=68Pqir_moqA)
* [What is SSH](https://www.youtube.com/watch?v=zlv9dI-9g1U)

Images below sourced from [David Brumly at Carnegie Mellon University](https://www.youtube.com/watch?v=fNC3jCCGJ0o)

![](https://www.evernote.com/shard/s150/sh/ceba42f8-128c-478b-b857-2b033294a4df/f70388b235260b5a/res/6eaede67-b674-4c28-9306-5b8414d849ae/skitch.png?resizeSmall&width=832)

![](https://www.evernote.com/shard/s150/sh/a5150f27-e630-48fb-8794-a1342cfe5076/0c664f25dd396804/res/51319142-13b1-45cd-af94-1cb7177b5bda/skitch.png?resizeSmall&width=832)

![](https://www.evernote.com/shard/s150/sh/d2a42614-b368-4536-ada4-f2f641832ec9/b13ba0462deb7322/res/bb33443a-bfe6-4002-b98a-d0aa87c73bf9/skitch.png?resizeSmall&width=832)

![](https://www.evernote.com/shard/s150/sh/5614e630-0ea0-4a55-ba14-cf679593fee6/99133c73ac3eca6f/res/30c2aa9c-6fe1-4fae-b8ff-d5b631209b99/skitch.png?resizeSmall&width=832)

## What can you do with these?

* Securely communicate with GitHub.
* Use them to encrypt files or data.
	* https://gist.github.com/colinstein/de1755d2d7fbe27a0f1e
* Use secure shell (`ssh`) to remote into another computer.
	* ssh into 538stats
* Copy a file securely from another computer using secure copy (`scp`).

## So this is what encryption is all about?

Yeah, its a really powerful tool that doesn't require a geeky genius to use.

## Other applications

* [Encrypting Files](https://bjornjohansen.no/encrypt-file-using-ssh-key)
* [HTTPS](https://www.youtube.com/watch?v=w0QbnxKRD0w) - We'll cover this more in a later lesson
* Cryptocurrency - https://walletgenerator.net/
* Verifying Identity, Chat, etc... (see keybase)

## Want to know more?
* Questions
* If we have time I've invited a security expert to come and speak during our final class day.
