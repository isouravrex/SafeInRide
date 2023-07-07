from flask import Flask, render_template
import amadeus_service
app = Flask(__name__)
@app.route('/')
def safeplace():
    data = amadeus_service.safety_rated_locations()
    print(data)
    return render_template('safeplace.html', safeplaces=data)
if __name__ == '__main__':
   app.run()