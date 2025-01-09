import socket
import time
def get_whois_data(domain):

    whois_servers = {
        ".com": "whois.verisign-grs.com",
        ".net": "whois.verisign-grs.com",
        ".org": "whois.pir.org",
        ".info": "whois.afilias.net",
        ".biz": "whois.biz",
        ".co": "whois.nic.co"
    }
    

    tld = '.' + domain.split('.')[-1]
    

    if tld not in whois_servers:
        raise ValueError(f"No WHOIS server found for TLD '{tld}'")
    
    whois_server = whois_servers[tld]
    
    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"Connecting to WHOIS server {whois_server} for domain {domain}")
            s.settimeout(10)
            s.connect((whois_server, 43))  # Port 43 whois port
            s.send((domain + "\r\n").encode())  
            

            response = b""
            while True:
                data = s.recv(4096)  
                if not data:
                    break
                response += data
            
            return response.decode()
    
    except socket.timeout:
        return "Connection timed out"
    except socket.error as e:
        return f"Socket error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    domain = input("Enter domain to look up: ")
    try:
        whois_info = get_whois_data(domain)
        print("\nWHOIS Information:\n")
        print(whois_info)
        time.sleep(100)
    except ValueError as e:
        print(f"Error: {e}")