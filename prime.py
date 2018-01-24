import sys, time, json, requests

params = sys.argv[1]
worker_id = sys.argv[2]
print("------------------------------------------------------")
print(params)
print("------------------------------------------------------")
data_json = json.loads(params)
print(data_json)
print("------------------------------------------------------")
m= int(data_json['from'])
n= int(data_json['to'])
start = time.time()
print("------------------------------------------------------")
print(" Finding prime numbers from {} to {} , start time {}".format(str(m), str(n), str(start)))
total = 0
total_prime = 0
total_not_prime = 0
for p in range(m, n+1):
	total += 1
	for i in range(2, p):
		if ((p % i) == 0):
			total_not_prime += 1
			break
	else:
		total_prime += 1
		prime_result = {'worker_id': worker_id, 'data': str(p)}
		local_url =  data_json['result_server'] #+ str(prime_result)
		try:
			requests.post(local_url,json = prime_result)
			print("{} has been uploaded to the server {}".format(str(prime_result), local_url))
		except Exception as e:
			print("Can't upload {} to the server {}".format(str(prime_result), local_url))
end = time.time()
latency= end - start
result = {
	'worker_id': worker_id, 
	'start' : str(start),
	'from'  : m,
	'to'    : n,
	'end'   : str(end),
	'total' : str(total),
	'prime' : str(total_prime),
	'not_prime': str(total_not_prime),
	'latency' : str(latency)
}

print("Result: " + str(result))
local_url =  data_json['result_server'] 
try:
	requests.post(local_url,json = result)
	print("{} has been uploaded to the server {}".format(str(result), local_url))
except Exception as e:
	print("Can't upload {} to the server {}".format(str(result), local_url))

#print('Done in {}, processed {} numbers, found {} prime numbers and {} not-prime numbers'.format(str(latency), str(total), str(total_prime), str(total_not_prime)))
