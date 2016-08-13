from Crypto.Cipher import AES
from Crypto import Random
import os
import sys
sys.path.append('../helpers')
from import_keys import load_keys

config = load_keys()

def encrypt_message(msg):

	key = config["AES"].encode('utf-8')
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key, AES.MODE_CFB, iv)
	msg = iv + cipher.encrypt(b'Attack at dawn')


def decrypt_message(msg):
	decrypt = cipher.decrypt(msg)
	print(decrypt)
	
