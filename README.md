## imcrypt

A tiny python module, which wraps around famous Crypto  library to give you AES level encryption with very few lines of code.

The basic idea is, you can encrypt any string or file with a private key which can only be decrypted if you have that key.

### Installation

````python
>> pip install imcrypt
````

All the features are developed keeping convenience in mind, so that you don't need to do any extra work just pass in the string and get the encrypted version, this can really be helpful if you need to transfer any confidential information over the network. More advanced feature includes generation of secret key for a particular project so that your code will only work in your system without authentication but not in other systems.

****

#### Example 1

a) Let say, you want to Encrypt a piece of text with your own password:

````python
import imcrypt

text = 'Hello World!'
password = 'your_password'

print(f'Text: {text}')

encrypted = imcrypt.encrypt(text, key=password)
print(f'Encrypted: {encrypted}')
````

Output:

````
Text: Hello World!
Encrypted: PmqCoAXpB03kEqKjEjyvPg==
````



b) Lets try to Decrypt it:

````python
import imcrypt

encrypted_text = 'PmqCoAXpB03kEqKjEjyvPg=='
password = 'your_password'

decrypted = imcrypt.decrypt(encrypted_text, key=password)
print(f'Decrypted: {decrypted}')
````

Output:

````
Decrypted: Hello World!
````

This is how we can do it with fewer lines of codes. #Encryption_made_simple

****

#### Example 2

Now we are going to see the more advanced features, i.e auto private key generation. so what happens in this case is, you don't need to provide any key/password to encrypt your texts, the program will automatically generate a password and will use it to encrypt and decrypt the data as long as the project is inside your computer, once it is been moved to other computer the private key expires and it doesn't works.

```python
import imcrypt

text = 'Hello World!'
print(f'Text: {text}')

encrypted = imcrypt.encrypt(text)
print(f'Encrypted: {encrypted}')

decrypted = imcrypt.decrypt(encrypted)
print(f'Decrypted: {decrypted}')
```

Output:

````
Text: Hello World!
Encrypted: LLkwMIuN9tEXMTkQWdB4lg==
Decrypted: Hello World!
````

As you can see, the encrypted text has changed even when our text is same, that's because our key has changed. so anytime you encrypt or decrypt anything without any key, computer will generate a private key for the first time and will use it as long as the project is inside your computer, you can generate new keys if required.

****

#### Example 3

With all said and done, here comes the super power... we can encrypt any file type with imcrypt though the encrypted version will be a pickle file of byte type. but we can later decrypt it into its original file. let's see an example to get the perspective.

````python
import imcrypt
import cv2

image = cv2.imread('sample.jpg')

print(f'File: {type(image)}')

encrypted = imcrypt.encrypt(image)
print(f'Encrypted: {type(encrypted)}')

decrypted = imcrypt.decrypt(encrypted)
print(f'Decrypted: {type(decrypted)}')
````

Output

````
File: <class 'numpy.ndarray'>
Encrypted: <class 'bytes'>
Decrypted: <class 'numpy.ndarray'>
````

It is very clear here that the original file was a cv2 image i.e, numpy array. we encrypted it and dumped it as pickle file, later we can read that pickle file to decrypt it and as it is shown in the output the decrypted file is again an numpy array. you can save that encrypted pickle to a txt file or transfer it anywhere via network.

****

#### Current Private Key

In case you want to see the current private key being used for encryption you can see them:

```python
import imcrypt

print(f'key: {imcrypt.key()}')
```

Output:

````
key: MTM2Mzg2MTIwMDkx
````

****

#### Change Private Key

Or if you want to change the private key, you can do that too:

````python
import imcrypt

imcrypt.new_key()

print(f'key: {imcrypt.key()}')
````

Output:

````
Key: MTc3MjgwNTM3Mjky
````

This can be very useful, if you are transferring your personal information over a network and want to encrypt information with a new key every time.

## Web app
I built a web-app around this library, go and checkout [here.](https://github.com/imneonizer/imcrypt-app)
![](https://github.com/imneonizer/imcrypt-app/blob/master/2.png)
