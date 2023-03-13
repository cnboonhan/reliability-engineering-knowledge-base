from gevent import monkey
monkey.patch_all()
import locust

class LabLoadTestingHandler:
    def __init__(self):
        pass