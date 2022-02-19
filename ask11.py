import requests

def randomnessVal(roundNo):
    r = requests.get('https://drand.cloudflare.com/public/'+str(roundNo), headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = r.json() # Round data by draw no.
    val=data['randomness']
    print(data)

r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json() # latest round
lr=data['round'] # Latest round no.
j=0;
for i in range(20):
    randomnessVal(lr-i)
    j+=1
