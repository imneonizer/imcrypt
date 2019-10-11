from math import remainder
from Crypto.Cipher import AES
import base64
import random
import pickle
import os
import shutil
from sys import platform
platform = platform.lower()
import getpass
user = getpass.getuser()

class ImCrypt:
    def __init__(self):
        if platform == "linux" or platform == "linux2":
            #import pwd
            self.config_dir = f"/home/{str(user)}/.local/share/.imcrypt"

        elif platform == "darwin":
            self.config_dir = '.imcrypt'

        elif platform == "win32":
            self.config_dir = f"{str(os.environ['SYSTEMDRIVE'])}/Users/{str(user)}/AppData/Local/.imcrypt"

        else:
            print('undefined os')
            self.config_dir = '.imcrypt'

        self.config_file = os.path.join(self.config_dir, 'imcrypt.key')

    @property
    def __version__(self):
        return 1.0

    def private_key(self):
        key = self.validate_key(key='')
        return self.validate_key(key='')


    def generate_new_key(self):
        try:
            shutil.rmtree(self.config_dir)
            key = self.validate_key(key='')
        except Exception as e:
            pass


    def generate_unique_key(self):
        unique_key = str.encode(str(random.randint(100000000000000, 199999999999999)))
        unique_key = str(base64.b64encode(unique_key))
        return unique_key[2:18]

    def write_new_key(self):
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)

        key = self.generate_unique_key()
        f = open(self.config_file, 'w+')
        f.write(key)
        f.close()

        return key

    def validate_key(self, key):
        if key == '':
            try:
                #trying to read the key file
                config_file = open(self.config_file, 'r').readlines()
                key = config_file[0]
            except Exception as e:
                key = self.write_new_key()

            return key

        elif len(key)< 16:
            key = key + '='*(16-len(key))
            return key
        elif len(key)>16:
            key = key[0:16]
            return key
        else:
            return key

    def validate_text_data(self, data, size):
        if size<16:
            return data.rjust(16)
        elif size>16:
            x = 0
            while True:
                y = 16*x
                if y>size:
                    data =  data.rjust(size+(y-size))
                    break
                x+=1

            return data
        else:
            return data

    def encrypt(self, data=None, key=''):
        key = self.validate_key(key)

        if type(data) == str:
            data = self.validate_text_data(data=data, size=len(data))
            cipher = AES.new(key, AES.MODE_ECB)
            encoded = str(base64.b64encode(cipher.encrypt(data)))
            return encoded[2:len(encoded)-1]
        else:
            #encryption: unknown => pickle => base64 => rjust => encrypted => pickle
            data = pickle.dumps(data)
            data = base64.b64encode(data)
            data = self.validate_text_data(data=data, size=len(data))
            cipher = AES.new(key, AES.MODE_ECB)
            encoded = base64.b64encode(cipher.encrypt(data))
            encoded = pickle.dumps(encoded)
            return encoded


    def decrypt(self, data=None, key=''):
        key = self.validate_key(key)

        if type(data) == str:
            data = self.validate_text_data(data=data, size=len(data))
            cipher = AES.new(key, AES.MODE_ECB)
            decoded = str(cipher.decrypt(base64.b64decode(data)).strip())
            return decoded[2:len(decoded)-1]
        else:
            #decryption: pickle => decrypted => strip => base64 => pickle => unknown
            data = pickle.loads(data)
            cipher = AES.new(key, AES.MODE_ECB)
            decoded = cipher.decrypt(base64.b64decode(data)).strip()
            decoded = base64.b64decode(decoded)
            decoded = pickle.loads(decoded)
            return decoded

imcrypt = ImCrypt()
