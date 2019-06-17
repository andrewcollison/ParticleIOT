# Particle IoT Interface

# Import required packages
import requests

deviceID = 'e00fce6880bb27262a6341e6'

# Classes for pulling data
class particleFetch:
	
	def pDevices():
		print('Starting Requests')
		resp = requests.get('https://api.particle.io/v1/devices',
			headers={'Content-Type':'application/json'},
			params={'access_token': '91f11bb369cbc3d1110df7d24ec3f02829d5bcda' } )
		print(resp.json())
		print('Finish')


	def gVariable():
		print('Starting Requests')
		resp = requests.get('https://api.particle.io/v1/devices/e00fce6880bb27262a6341e6/temperature',
			headers={'Content-Type':'application/json'},
			params={'access_token': '91f11bb369cbc3d1110df7d24ec3f02829d5bcda' } )
		print(resp.json())
		print('Finish')



def main():
	particleFetch.gVariable()


main()










