def login():
    if password_valid():
        render_template('welcome.html')
    else:
        render_template('login_failed.html', status=403)
