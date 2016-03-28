__author__ = 'Gaston'

import requests
import requests_oauthlib

class RestAPIClient(object):
	"""
		Class to use to communicate by request with the module
		This class have POST, GET, PUT, DELETE, AUTHS TYPES
	"""

	# Init of the class
	def __init__(self, ip, port):
		"""
		:param ip: ip to send the request.
		:param port: port to send to the request
		:return:
		"""
		self.url = "http://%s:%s" % (ip, port)
		self.auth = None  # No authentication by default
		self.ip = ip
		self.port = port

	# Function to extend the url of the request
	def extend_url(self, resource):
		"""
		:param resource: url to add to end.
		:return:
		"""
		self.url += resource

	# Set a new url using the ip and port of the client.
	def new_url(self, resource):
		"""
		:param resource: extra url
		:return:
		"""
		self.url = "http://%s:%s" % (self.ip, self.port) + resource

	def do_get(self, params=None, headers=None, timeout=None, extend_url=''):
		if not headers:
			headers = {}
		self.url += extend_url
		return do_GET(self.url, params=params, headers=headers, auth=self.auth, timeout=timeout)

	def do_post(self, data=None, params=None, headers=None, timeout=None, extend_url=''):
		if not headers:
			headers = {}
		self.url += extend_url
		return do_POST(self.url, data=data, params=params, headers=headers, auth=self.auth, timeout=timeout)

	def do_put(self, params=None, headers=None):
		if not headers:
			headers = {}
		return do_PUT(self.url, params=params, headers=headers, auth=self.auth)

	def do_delete(self, params=None, headers=None):
		if not headers:
			headers = {}
		return do_DELETE(self.url, params=params, headers=headers, auth=self.auth)

	def set_auth_basic(self, username, password):
		self.auth = requests.auth.HTTPBasicAuth(username, password)
		self.username = username
		self.password = password

	def set_auth_digest(self, username, password):
		self.auth = requests.auth.HTTPDigestAuth(username, password)
		self.username = username
		self.password = password

	def set_auth_oauth(self, app_key, app_secret, user_token, user_token_secret):
		self.auth = requests_oauthlib.OAuth1(app_key, app_secret, user_token, user_token_secret)
		self.app_key = app_key
		self.app_secret = app_secret
		self.user_token = user_token
		self.user_token_secret = user_token_secret



def do_GET(url, headers=None, params=None, auth=None, timeout=None):
	# check_ssl_certs = False
	# requests.packages.urllib3.disable_warnings()
	# response = requests.get(url, params=params, headers=headers, verify=check_ssl_certs, auth=auth, timeout=timeout)
	response = requests.get(url, params=params, timeout=timeout)
	return response


def do_POST(url, headers=None, data=None, params=None, auth=None, timeout=None):
	# check_ssl_certs = False
	# requests.packages.urllib3.disable_warnings()
	# response = requests.post(url, params=params, data=data, headers=headers, verify=check_ssl_certs, auth=auth)
	response = requests.post(url, params=params, timeout=timeout)
	return response


def do_PUT(url, headers=None, params=None, auth=None):
	check_ssl_certs = False
	requests.packages.urllib3.disable_warnings()
	response = requests.put(url, params=params, headers=headers, verify=check_ssl_certs, auth=auth)
	return response


def do_DELETE(url, headers=None, params=None, auth=None):
	check_ssl_certs = False
	requests.packages.urllib3.disable_warnings()
	response = requests.delete(url, params=params, headers=headers, verify=check_ssl_certs, auth=auth)
	return response
