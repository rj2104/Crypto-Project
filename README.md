# PassHub_sync
PassHub_sync is a simple open stateless password manager. 
The significant function is that it allows users to store profiles (like-site, username, password length, etc.) locally, instead of  creating an account. 
Therefore, no establishing of online accounts.

Stateless: 
Stateless simply means that your password is not being stored. You have to store some information about your account locally.
And, Passwords get generated on the fly depending on the account info you provided and the secret key. There is no master password. 
Every secret key is master password.

Working:
PassHub_sync asks you four simple questions site, username / e-mail, length, counter.

Counter is just an integer which has a default value of 1. counter can be used to change the password of any profile that you saved before. 
For instance, if you have any websites account and after some time you want to change its password without changing the basic parameters like 
site, username/e-mail, length then you can change the value of counter may be like 2.
