# app/routes.py

from flask import render_template, redirect, url_for, request
from flask_login import login_required
from app import app, db, login_manager
from app.models import User, Device

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

# Example route for adding a new device
@app.route('/add_device')
@login_required
def add_device():
    # Create a new device
    new_device = Device(name='Example Device', ip_address='192.168.1.1', community_string='public')
    new_device.save()
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Error handler for 500 Internal Server Errors
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# Example route for deleting a device
@app.route('/delete_device/<int:device_id>')
@login_required
def delete_device(device_id):
    # Find the device by ID and delete it
    device = Device.get_by_id(device_id)
    if device:
        device.delete()
    return redirect(url_for('index'))
# Route to display a list of devices with pagination
@app.route('/devices')
def devices():
    page = request.args.get('page', 1, type=int)  # Get the page number from the query parameters (default to 1)
    per_page = 10  # Number of devices to display per page

    devices = Device.query.paginate(page=page, per_page=per_page)

    return render_template('devices.html', devices=devices)

# Route to search devices
@app.route('/search')
@login_required
def search():
    query = request.args.get('query', '')
    devices = Device.query.filter(Device.name.ilike(f'%{query}%')).all()
    return render_template('search_results.html', query=query, devices=devices)
# Route to display device data visualization
@app.route('/visualization')
@login_required
def visualization():
    devices = Device.query.all()
    device_names = [device.name for device in devices]
    device_ip_addresses = [device.ip_address for device in devices]

    # Render a simple bar chart using Plotly
    return render_template('visualization.html', device_names=device_names, device_ip_addresses=device_ip_addresses)