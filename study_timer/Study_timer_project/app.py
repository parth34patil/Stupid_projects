# Import Flask and render_template to serve HTML pages
from flask import Flask, render_template # type: ignore

# Create an instance of the Flask application
app = Flask(__name__)

# Define the home route (default URL "/")
@app.route('/')
def home():
    # Render the "clock.html" file from the templates folder
    return render_template("clock.html")

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for easier development
