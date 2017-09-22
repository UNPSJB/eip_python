import requests, json

def get_genders(names, language_id="es"):
	url = ""
	cnt = 0
	if not isinstance(names,list):
		names = [names,]
	
	for name in names:
		if url == "":
			url = "name[0]=" + name
		else:
			cnt += 1
			url = url + "&name[" + str(cnt) + "]=" + name
		url += "&language_id=" + language_id

	req = requests.get("https://api.genderize.io?" + url)
	print(req.headers)
	results = json.loads(req.text)
	
	retrn = []
	for result in results:
		if result["gender"] is not None:
			retrn.append((result["gender"], result["probability"], result["count"]))
		else:
			retrn.append((u'None',u'0.0',0.0))
	return retrn

if __name__ == '__main__':
	print(get_genders(["Brian","Apple","Jessica","Zaeem","NotAName"]))
