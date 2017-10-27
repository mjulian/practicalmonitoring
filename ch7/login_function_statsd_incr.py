import statsd
statsd_client = statsd.StatsClient('localhost', 8125)

def login():
    statsd_client.incr('app.login.attempts')
    if password_valid():
        statsd_client.incr('app.login.successes')
        render_template('welcome.html')
    else:
        statsd_client.incr('app.login.failures')
        render_template('login_failed.html', status=403)
