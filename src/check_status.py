import requests as rq

def get_status(url):
    r = rq.get(url)
    return r
if __name__ == "__main__":
    print(get_status('https://e-learning.hcmut.edu.vn/').status_code)