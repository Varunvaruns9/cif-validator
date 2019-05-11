from locust import HttpLocust, TaskSet, task



class UserBehavior(TaskSet):

    @task(1)
    def index(self):
        attach = open("example.cif", 'r')
        print(self.client.post("/compute/validate", files={'cif': attach}))


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000