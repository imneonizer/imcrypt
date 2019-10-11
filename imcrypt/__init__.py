from imcrypt.imcrypt import imcrypt as im

__version__ = im.__version__
key = im.private_key
encrypt = im.encrypt
decrypt = im.decrypt
new_key = im.generate_new_key