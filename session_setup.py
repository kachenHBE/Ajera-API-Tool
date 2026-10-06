"""
Filename: session_setup.py
Description: Establish Ajera API connection
Author: Kai Achen
Last Updated: 10/06/2026
Inputs: 
Outputs: 
"""

from dotenv import load_dotenv

load_dotenv()

def create_api_session():
    print("begin create_api_session")
    message = """CreateAPISession {
     Method: 'CreateAPISession',
     Username: os.getenv('ajera_username'),
     Password: os.getenv('ajera_password'),
     APIVersion: os.getenv('api_version'),
     UseSessionCookie: os.getenv('use_session_cookie')
    }
    """
    return message

def main():
    print("main")

if __name__ == "__main__":
    main()