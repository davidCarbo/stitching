from flask import Flask, render_template, request, jsonify
import api_utils
from werkzeug.exceptions import HTTPException, MethodNotAllowed, InternalServerError, BadRequest, NotImplemented
from jsonschema import ValidationError
import controller
from subprocess import Popen, PIPE

app = Flask(__name__)
if __name__ == "__main__":
    app.run()

app.register_error_handler(HTTPException, api_utils.handle_error)
app.register_error_handler(ValidationError, api_utils.handle_error)

@api_utils.debug_only
@app.route('/health/', methods=["GET"])
def health():
    """Performs a healthcheck
    
    Parameter:
    testfile (string) -- in which file pytest should collect tests
    """
    # Get Parameters
    file_name = request.args.get("testfile", "", str)
    out = ""
    # Open subprocess for pytest (necessary to reload libraries on hot reload)
    with Popen(['pytest',
                '--tb=short',
                '-x',
                f'src/tests/{file_name}'], stdout=PIPE, bufsize=1,
               universal_newlines=True) as p:
        for line in p.stdout:
            out += line
    return f'<span style="white-space: pre-line">{out}</span>'

@app.route('/train/', methods=["POST"])
def train():
    raise NotImplemented("train method was not implemented.")

@app.route('/start/', methods=["POST"])
def start():
    raise NotImplemented("start method was not implemented.")

@app.route('/predict/', methods=["POST", "GET"])
def predict():
    raise NotImplemented("predict method was not implemented.")


@app.route('/use/<method>/', methods=["GET", "POST"])
def use(method):
    if method == "stitch_images":
        if request.method == 'GET':
            raise MethodNotAllowed("Method 'GET' for stitch_images not allowed.")
        data = request.get_json()          
        if(data):
            try:
                return controller.stitch_images(data) 
            except Exception as e:
                raise InternalServerError(f"Something fails {e}")
        else: 
            raise BadRequest(f"Json data for {method} was missing")

