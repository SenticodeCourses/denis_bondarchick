from client import Input


# flask_routes.start()
robot = Input('http://localhost:8080/')
robot.start()
while True:
    url = 'http://localhost:8080/' + input("http://localhost:8080/")
    robot.get(url)
