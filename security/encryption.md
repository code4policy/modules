# Encryption

Remember when we set up SSH keys to set up a secure connection between GitHub and your local machine so that it doesn't ask you for your password every time you run `git pull`? That was an example of encryption, specifically asymmetric encryption.


This is your **public key**

```
cat ~/.ssh/id_rsa.pub
```

This is your **private key**

```
cat ~/.ssh/id_rsa
```

## Cryptography Basics

Videos:

* [Cryptography 101](https://www.youtube.com/watch?v=fNC3jCCGJ0o)
* [What is Cryptography](https://www.youtube.com/watch?v=68Pqir_moqA)
* [What is SSH](https://www.youtube.com/watch?v=zlv9dI-9g1U)

Images below sourced from [David Brumly at Carnegie Mellon University](https://www.youtube.com/watch?v=fNC3jCCGJ0o)

![](https://www.evernote.com/shard/s150/sh/ceba42f8-128c-478b-b857-2b033294a4df/f70388b235260b5a/res/6eaede67-b674-4c28-9306-5b8414d849ae/skitch.png?resizeSmall&width=832)

![](https://www.evernote.com/shard/s150/sh/a5150f27-e630-48fb-8794-a1342cfe5076/0c664f25dd396804/res/51319142-13b1-45cd-af94-1cb7177b5bda/skitch.png?resizeSmall&width=832)

![](https://www.evernote.com/shard/s150/sh/d2a42614-b368-4536-ada4-f2f641832ec9/b13ba0462deb7322/res/bb33443a-bfe6-4002-b98a-d0aa87c73bf9/skitch.png?resizeSmall&width=832)

![](https://www.evernote.com/shard/s150/sh/5614e630-0ea0-4a55-ba14-cf679593fee6/99133c73ac3eca6f/res/30c2aa9c-6fe1-4fae-b8ff-d5b631209b99/skitch.png?resizeSmall&width=832)

## Asymmetric vs Symmetric

* Asymmetric - encrypt with public key, decrypt with private key
* Symmetric - encrypt and decrypt with same key.

## HTTPS

### How it works:

> ...This pair of asymmetric keys is used in the SSL handshake to exchange a further key for both parties to symmetrically encrypt and decrypt data. The client uses the server's public key to encrypt the symmetric key and send it securely to the server, and the server uses its private key to decrypt it.

*source*: https://robertheaton.com/2014/03/27/how-does-https-actually-work/

1. Asymmetric encryption for handshake
2. Symmetric encryption for communication

A quick video: https://www.youtube.com/channel/UCLMgZUQzqdZ6z-_13OWUX7g

### HTTPS in Government

* https://obamawhitehouse.archives.gov/blog/2015/06/08/https-everywhere-government
* https://https.cio.gov/
* https://pulse.cio.gov/https/domains/
* Talk to Eric Mill! https://18f.gsa.gov/2014/11/13/why-we-use-https-in-every-gov-website-we-make/

## What can you do with these?

* Securely communicate with GitHub.
* Use them to encrypt files, data, or messages.
	* https://gist.github.com/colinstein/de1755d2d7fbe27a0f1e
* Securely leak sensitive information to journalists - 
	* https://securedrop.org/
	* https://www.propublica.org/article/how-to-leak-to-propublica
* Use secure shell (`ssh`) to remote into another computer.
	* `ssh fivethirtyeight@538stats` 
	*  and also show it on VNC (remote login)
* Copy a file securely from another computer using secure  copy (`scp`).
* Encryption also is at the core of cryptocurrencies. To transfer a cryptocurrency.
	* https://walletgenerator.net/
* Verifying Identity, Chat, etc... (see keybase)

## So this is what encryption is all about?

Yeah, its a really powerful tool that doesn't require a geeky genius to use.

## Other applications

* [Encrypting Files](https://bjornjohansen.no/encrypt-file-using-ssh-key)
* [HTTPS](https://www.youtube.com/watch?v=w0QbnxKRD0w) - We'll cover this more in a later lesson
* Cryptocurrency - https://walletgenerator.net/

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

1. Create a new empty folder and cd into it.

	```
	cd ~/Development
	mkdir encryption
	cd ~/Development/encryption
	touch secretmessage.txt
	```
2. Save your secret message inside `secretmessage.txt`
	
3. Grab Dhrumil's public key from slack's #general channel and save it in your folder.

4. Encrypt a message with Dhrumil's public key

	```
	openssl rsautl -encrypt -oaep -pubin -inkey <(ssh-keygen -e -f dhrumilskey.pub -m PKCS8) -in secretmessage.txt -out secretmessage.text.enc
	```
5. Send your encrpyted file to Dhrumil on Slack, you can use the #scratchwork channel, a public network. Nobody other than Dhrumil will be able to read it anyway!!!

	```
	openssl rsautl -decrypt -oaep -inkey ~/.ssh/id_rsa -in message.txt.enc -out decoded.txt
	```
6. Wow! I feel so secure! Except here is a more secure way that is recommended. Also I might consider using a PGP key 
	
	https://bjornjohansen.no/encrypt-file-using-ssh-key

## Types of Keys: SSH, PGP, GPG


## Encryption and Policy

Lot of thorny policy issues related to:

- proposals to restrict encryption
- install backdoors
- law enforcement investigations

## Resources

* Check out https://keybase.io/
* Prime numbers and whatnot: https://arstechnica.com/information-technology/2013/02/lock-robster-keeping-the-bad-guys-out-with-asymmetric-encryption/
