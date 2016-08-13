import unittest
from data_cryptography import SHA_256, hash_check

class TestUnderscore(unittest.TestCase):

	# use a SHA256 function to create a hash of whatever string is passed in
	def test_SHA_256(self):
		hashed_value = SHA_256("empowersecurityacademy")
		self.assertEqual(hashed_value, "5b289653293f4101361ee673deec37bc99b10af868997289fa5f1c78709da118")

	# create a function that takes a value and a hash, return true if the value is in fact the the true value of the hash, false if it is not
	def test_hash_check(self):
		check = hash_check("crushcodelikeaboss", "ee95d089438d1a7e0280953029399c21c1aef3dcf426d149e0f7090acbc29cdb")
		self.assertEqual(check, True)

		check = hash_check("crushcodelikeanamateur", "ee95d089438d1a7e0280953029399c21c1aef3dcf426d149e0f7090acbc29cdb")
		self.assertEqual(check, False)






if __name__ == '__main__':
    unittest.main()
