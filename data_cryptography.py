from Crypto.Hash import SHA256

def SHA_256(value):
	hashed_value = SHA256.new(value).hexdigest()
	return hashed_value

def hash_check(value, expected_hash):
	hashed_value = SHA256.new(value).hexdigest()
	if hashed_value == expected_hash:
		return True

	return False