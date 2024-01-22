from flask import Flask, request, render_template
from prometheus_flask_exporter import PrometheusMetrics
from gpiozero import OutputDevice, PWMOutputDevice, LED, AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

linus = PiGPIOFactory(host='192.168.0.40')
torvalds = PiGPIOFactory(host='192.168.0.10')

eye = LED(25, pin_factory=torvalds)
en_3 = PWMOutputDevice(12, pin_factory=torvalds)
en_4 = PWMOutputDevice(26, pin_factory=torvalds)
pin1 = OutputDevice(13, pin_factory=torvalds)
pin2 = OutputDevice(21, pin_factory=torvalds)
pin3 = OutputDevice(17, pin_factory=torvalds)
pin4 = OutputDevice(27, pin_factory=torvalds)

led = LED(25, pin_factory=linus)
en_1 = PWMOutputDevice(12, pin_factory=linus)
en_2 = PWMOutputDevice(26, pin_factory=linus)
in1 = OutputDevice(13, pin_factory=linus)
in2 = OutputDevice(21, pin_factory=linus)
in3 = OutputDevice(17, pin_factory=linus)
in4 = OutputDevice(27, pin_factory=linus)
angular_servo = AngularServo(22, min_angle=-90, max_angle=90, pin_factory=linus)
angular_servo2 = AngularServo(23, min_angle=-90, max_angle=90, pin_factory=linus)

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)

# Apply the same metric to all of the endpoints
endpoint_counter = metrics.counter(
    'endpoint_counter', 'Request count by endpoints',
    labels={'endpoint': lambda: request.endpoint}
)

@app.route("/")
@endpoint_counter
def index():
    return render_template("index.html")

@app.route("/forward")
@endpoint_counter
def forward():
    in1.on()
    in2.off()
    in3.on()
    in4.off()
    return render_template("index.html")

@app.route("/backward")
@endpoint_counter
def backward():
    in1.off()
    in2.on()
    in3.off()
    in4.on()
    return render_template("index.html")

@app.route("/left")
@endpoint_counter
def left():
    in1.off()
    in2.on()
    in3.on()
    in4.off()
    return render_template("index.html")

@app.route("/right")
@endpoint_counter
def right():
    in1.on()
    in2.off()
    in3.off()
    in4.on()
    return render_template("index.html")

@app.route("/stop")
@endpoint_counter
def stop():
    in1.off()
    in2.off()
    in3.off()
    in4.off()
    return render_template("index.html")

@app.route("/on")
@endpoint_counter
def on():
    led.on()
    return render_template("index.html")

@app.route("/off")
@endpoint_counter
def off():
    led.off()
    return render_template("index.html")

@app.route("/north")
@endpoint_counter
def north():
    pin1.off()
    pin2.on()
    pin3.off()
    pin4.on()
    return render_template("index.html")

@app.route("/south")
@endpoint_counter
def south():
    pin1.on()
    pin2.off()
    pin3.on()
    pin4.off()
    return render_template("index.html")

@app.route("/west")
@endpoint_counter
def west():
    pin1.off()
    pin2.on()
    pin3.on()
    pin4.off()
    return render_template("index.html")

@app.route("/east")
@endpoint_counter
def east():
    pin1.on()
    pin2.off()
    pin3.off()
    pin4.on()
    return render_template("index.html")

@app.route("/stop2")
@endpoint_counter
def stop2():
    pin1.off()
    pin2.off()
    pin3.off()
    pin4.off()
    return render_template("index.html")

@app.route("/torvaldson")
@endpoint_counter
def torvaldson():
    eye.on()
    return render_template("index.html")

@app.route("/torvaldsoff")
@endpoint_counter
def torvaldsoff():
    eye.off()
    return render_template("index.html")

@app.route("/pwm", methods=['POST'])
@endpoint_counter
def pwm():
    slider = request.form["speed"]
    en_1.value = int(slider) / 10
    en_2.value = int(slider) / 10
    en_3.value = int(slider) / 10
    en_4.value = int(slider) / 10
    return render_template("index.html")

@app.route("/servoarm", methods=['POST'])
@endpoint_counter
def servoarm():
    slider2 = request.form["degree"]
    slider3 = request.form["degree2"]
    angular_servo = int(slider2)
    angular_servo2 = int(slider3)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
