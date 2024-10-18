from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def logout(self):
        self.client.get("/v2/user/logout")

    @task
    def login(self):
        self.client.get("/v2/user/login?username=mugendai3&password=123456")

    @task
    def getUserInfo(self):
        self.client.get("/v2/user/mugendai7")

    @task
    def userCreate(self):
        payload = {
            "id": 1234567,
            "username": "mugendai9",
            "firstName": "ece",
            "lastName": "mertem",
            "email": "nertenece@outlook.com",
            "password": "123456",
            "phone": "05632131636",
            "userStatus": 0
        }
        self.client.post("/v2/user", json=payload)

    @task
    def updateUser(self):
        payload = {
            "id": 1234568,
            "username": "mugendai8",
            "firstName": "ece",
            "lastName": "merten",
            "email": "lertenece@outlook.com",
            "password": "123456",
            "phone": "05632131636",
            "userStatus": 0
        }
        self.client.put("v2/user/mugendai8", json=payload)

    @task
    def deleteUser(self):
        self.client.delete("/v2/user/mugendai9")
