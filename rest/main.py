from client import Input


robot = Input('http://localhost:8080/')
while True:
    if input('type "start":') == 'start':
        robot.start()
        while True:
            url = 'http://localhost:8080/' + input("\nlocalhost:8080/")
            robot.get(url)
