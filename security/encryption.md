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

A brief aside...

A system with a public and private key is known as asymmetric encrpytion, or private key encryption. Check out this video from [David Brumly at Carnegie Mellon University](https://www.youtube.com/watch?v=fNC3jCCGJ0o) for a quick overview of the basics of cryptography.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/fNC3jCCGJ0o/0.jpg)](https://www.youtube.com/watch?v=fNC3jCCGJ0o)

### What can you do with cryptographic keys?

* Share our public key to securely communicate with GitHub (or other services).
* Use someone else's public key to [encrypt](https://gist.github.com/colinstein/de1755d2d7fbe27a0f1e) and send a message only they can read.
* Encrypt or sign a document with your private key to prove that it originated with you (anyone can use your public key to decrypt, or verify your signature)
* Remotely login into another computer with a program known as secure shell (`ssh`).
* Copy a file securely from another computer using secure copy (`scp`).
* Lots of other things....

### So this is what encryption is all about?

Yeah, its a really powerful tool that doesn't require a geeky genius to use.

### Other applications

* Encrypting Files: https://bjornjohansen.no/encrypt-file-using-ssh-key
* HTTPS (We'll cover this more in a later lesson)

	[![How HTTPS works](https://img.youtube.com/vi/w0QbnxKRD0w/0.jpg)](https://www.youtube.com/watch?v=w0QbnxKRD0w)

	- https://18f.gsa.gov/2014/11/13/why-we-use-https-in-every-gov-website-we-make/
	- https://https.cio.gov/
* Cryptocurrency: https://walletgenerator.net/
* Chat (Signal, WhatsApp, Ketbase etc... are end-to-end encrypted chat platforms)
* Digital Signatures: https://us-cert.cisa.gov/ncas/tips/ST04-018
* Voting (in Estonia, at least): https://www.youtube.com/watch?v=GuKiJKL4WdI
* Identification https://www.youtube.com/watch?v=9POUIiyhowk

Check out [this video](https://www.youtube.com/watch?v=9POUIiyhowk) about all of the digital services Estnoia has been able to provide by issuing a public/private key pair to each citizen:

[![Digital services in Estonia.](https://img.youtube.com/vi/9POUIiyhowk/0.jpg)](https://www.youtube.com/watch?v=9POUIiyhowk)

### Want to try it out?

Finally, if you want to play around more with encryption, I'd highly reccomend [Keybase](https://keybase.io/). Keybase allows you to encrpyt messages as you can see in the gif below using someone else's public key. Then, you can send that message to them over any public medium and ONLY they can read it. You can also encrypt a message with multiple keys. Keybase has a lot of other great features including secure chat, idenity verification, file transfer, and more. I would encourage you to play around with it and learn more and really bring the idea of public and private keys to life!

![](https://i.gyazo.com/603c3f0335d2966282b0f9e7ed71ff84.gif)


Later in class, if there is time, we will learn how to send each other encrypted messages using the SSH keys we just created today! ([modules/security/encryption.md](../security/encryption.md#-example))

### Misc

The math behind Cryptography has something to do with finding the factors of really large prime numbers. This article on arstechnica provides a great rundown!
https://arstechnica.com/information-technology/2013/02/lock-robster-keeping-the-bad-guys-out-with-asymmetric-encryption/

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
	openssl rsautl -encrypt -oaep -pubin -inkey <(ssh-keygen -e -f dhrumilskey.pub -m PKCS8) -in secretmessage.txt -out secretmessage.txt.enc
	```
5. Send your encrpyted file to Dhrumil on Slack, you can use the #scratchwork channel, a public network. Nobody other than Dhrumil will be able to read it anyway!!!

6. Wait for dhrumil to decrypt your message! (he will use the following command)
	```
	ssh-keygen -p -m PEM -f ~/.ssh/id_rsa
	openssl rsautl -decrypt -oaep -inkey ~/.ssh/id_rsa -in secretmessageal.txt.enc -out /dev/stdout
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

## Questions?

Discuss with your classmates in the #encryption channel in Slack! If I'm around, I can chime in too. Or ask me during class!
