import statsd
statsd_client = statsd.StatsClient('localhost', 8125)

def login():
    login_timer = statsd_client.timer('app.login.time')
    login_timer.start()
    if password_valid():
        render_template('welcome.html')
    else:
        render_template('login_failed.html', status=403)
    login_timer.stop()
    login_timer.send()
