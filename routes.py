from app import app

@app.route('/')
def landing():
    from app.controllers.index import controller
    return controller()

@app.route('/admin/login', methods=['POST', 'GET'])
def admin_login():
    from app.controllers.__admin__login import controller
    return controller()

@app.route('/admin/dashboard')
def admin_dashboard():
    from app.controllers.__admin__dash import controller
    return controller()