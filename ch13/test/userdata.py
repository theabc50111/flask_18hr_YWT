def init_app(app):
    @app.route('/auth')
    def auths():
        return 'auth'
