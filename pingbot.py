import platform, subprocess, random, socket, struct, mysql.connector    # For getting the operating system name # For executing a shell command
from dns import reversename, resolver, exception
idip = 0
sqlconnection = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='worldping')
#nm = nmap.PortScanner()
while True:
    host = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    '0.0.0.1'
    host = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    '255.255.255.254'
  # For executing a shell command
    os = platform.system().lower()

    #nmap scan
    #status,result = nm.scan(host, "25565")

    status,result = subprocess.getstatusoutput("ping -c1 -w2 " + host)

    if status == 0: 
        print(os + ' ' + host + " is UP !")
        updown = 'UP'
    else:
        print(os + ' ' + host + " is DOWN !")
        updown = 'DOWN'
    port = '0'    

    rev_name = reversename.from_address('{}'.format(host))
    try:
        reversed_dns = str(resolver.resolve(rev_name,"PTR")[0])
    except (resolver.NXDOMAIN, resolver.NoAnswer):
        print ("no domain")
        reversed_dns = "no domain"
    except resolver.Timeout:
        print ("timeout")
    except exception.DNSException:
        print ("DNSexception")
    idip += 1
    mysql_query = """INSERT INTO randompings (id, IP, Name, OS, UPDOWN) VALUES (%s, %s, %s, %s, %s)"""
    values = (idip, host, reversed_dns, os, updown)
    cursor = sqlconnection.cursor()
    cursor.execute(mysql_query, values)
    sqlconnection.commit()
