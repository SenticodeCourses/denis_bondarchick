from client import Input


# flask_routes.start()
robot = Input('http://localhost:8080/')
running = 0
while True:
    if input('type "start:"') == 'start':
        robot.start()
        running = 1
        while True:
            if running == 1:
                url = 'http://localhost:8080/' + input("\nhttp://localhost:8080/")
                robot.get(url)

