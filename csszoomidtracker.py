from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import random, re, smtplib, os, jinja2
from email.mime.text import MIMEText
from email.header import Header

global css1, css2, css3, css4, css5, css6, css7, css8, css9, css10, css1_conf_pulse, css2_conf_pulse, dsam_pulse

otp_data = []


css1 = """
<a href="css1" class="w3-bar-item w3-button w3-padding-large w3-black">
<i class="fa fa-home w3-xxlarge"></i>
<p> css1.pulsesecure.net </p>
</a>

"""

css2 = """
	
<a href="css2" class="w3-bar-item w3-button w3-padding-large w3-black">
<i class="fa fa-home w3-xxlarge"></i>
<p> css2.pulsesecure.net </p>
</a>

"""

css3 = """

<a href="#" class="w3-bar-item w3-button w3-padding-large w3-black">
<i class="fa fa-home w3-xxlarge"></i>
<p> css3.pulsesecure.net </p>
</a>

"""

css4 = """

<a href="#" class="w3-bar-item w3-button w3-padding-large w3-black">
<i class="fa fa-home w3-xxlarge"></i>
<p> css4.pulsesecure.net </p>
</a>

"""

css5 = """
<a href="#" class="w3-bar-item w3-button w3-padding-large w3-black">
<i class="fa fa-home w3-xxlarge"></i>
<p> css5.pulsesecure.net </p>
</a>

"""

css6 = """
<a href="#" class="w3-bar-item w3-button w3-padding-large w3-black">
<i class="fa fa-home w3-xxlarge"></i>
<p> css6.pulsesecure.net </p>
</a>

"""

css7 = """
<a href="#" class="w3-bar-item w3-button w3-padding-large w3-black">
<i class="fa fa-home w3-xxlarge"></i>
<p> css7.pulsesecure.net </p>
</a>
"""

css8 = """
<a href="#" class="w3-bar-item w3-button w3-padding-large w3-black">
<i class="fa fa-home w3-xxlarge"></i>
<p> css8.pulsesecure.net </p>
</a>
"""

css9 = """

<a href="#" class="w3-bar-item w3-button w3-padding-large w3-black">
<i class="fa fa-home w3-xxlarge"></i>
<p> css9.pulsesecure.net </p>
</a>
"""


css10 = """

<a href="#" class="w3-bar-item w3-button w3-padding-large w3-black">
<i class="fa fa-home w3-xxlarge"></i>
<p> css10.pulsesecure.net </p>
</a>

"""

css1_conf_pulse = """

<a href="#" class="w3-bar-item w3-button w3-padding-large w3-black">
<i class="fa fa-home w3-xxlarge"></i>
<p> css1-Conf.pulsesecure.net </p>
</a>
"""

css2_conf_pulse = """

<a href="#" class="w3-bar-item w3-button w3-padding-large w3-black">
<i class="fa fa-home w3-xxlarge"></i>
<p> css2-Conf.pulsesecure.net </p>
</a>
"""

dsam_pulse = """

<a href="#" class="w3-bar-item w3-button w3-padding-large w3-black">
<i class="fa fa-home w3-xxlarge"></i>
<p> dsam.pulsesecure.net </p>
</a>
"""

total_accounts = [css1, css2, css3, css4, css5, css6]
used_accounts = []
available_accounts = [css1, css2, css3, css4, css5, css6]
use_and_name = {}


def generateOTP():	
	OTP = ""	
	for i in range(6):
		OTP += str(random.randint(0,9))
	return OTP

def send_email(address, one_time_password):
	smtp_host = "smtp.gmail.com"
	port = 587
	
	login = "pulsegsclab@gmail.com"
	password = "vreqikgfspuevmxi"

	recipient_mail = address
#	cc = "sramkumar@pulsesecure.net"
	otp = one_time_password
	
	recipient = [recipient_mail]	
	
	msg = MIMEText('Hi', 'Hi', 'utf-8')
	msg['Subject'] = Header(one_time_password, 'utf-8')
	msg['From'] = login
	msg['To'] = recipient_mail
#	msg['cc'] = "sramkumar@pulsesecure.net"

	s = smtplib.SMTP(smtp_host, port)
	try:
		s.starttls()
		s.login(login,password)
		s.sendmail(msg['From'], recipient, msg.as_string())
	finally:
		s.quit()


app = Flask(__name__)

a  = """
    
<!DOCTYPE html>
<!--HTML-->
<html>
<head>
<title>Pulse Secure GSCLAB</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
  <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="stylesheet" type="text/css" href="/static/style.css">
<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700' rel='stylesheet' type='text/css' >
				
<!-- Style Sheet-->
<style>
								body, h1,h2,h3,h4,h5,h6 {font-family: "Montserrat", sans-serif}
								.w3-row-padding img {margin-bottom: 12px}
								/* Set the width of the sidebar to 120px */
								.w3-sidebar {width: 120px;background: #18222b;}
								/* Add a left margin to the "page content" that matches the width of the sidebar (120px) */
								#main {margin-left: 120px}
								/* Remove margins from "page content" on small screens */
								@media only screen and (max-width: 1200px) {#main {margin-left: 0}}
							
							
.button {
  background-color: #008CBA; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
 
 <!--For body-->   
   	body {font-family:"Open Sans", sans-serif;background: black;font-size: 18px}
		.bg {background:url('https://www.pulsesecure.net/base/images/lp/zoom.us/zoom.us-landing-page-background.jpg') top right #000000;background-size:cover;position: absolute;top:0;left:0;right:0;bottom:0}
		h1{color: #5db948;font-weight: 400;margin:0;padding:0 0 30px 0;}
		h2{color:white;font-weight: 300;margin:0;padding:0;}
		.outside {padding:0 1rem;}
		.inside {max-width: 1800px;margin:0 auto;}
		
		.header {min-height:40px;display: table;width: 100%}
		
		@media only screen{
			.c1,.c2,.c3,.c4 {display:block;vertical-align: middle;text-align: center;width: auto;padding-bottom: 20px}
			.c1 {padding-bottom: 100px}
			.header {margin:50px 0 100px 0;}
			h1{font-size:40px;line-height: 40px;}
			h2{font-size:18px;line-height: 24px}
			.page {max-width: 1200px;margin:1 auto;text-align: center}
		}
		@media only screen and (min-width: 1000px) {
			.header {margin:100px 0 220px 0;}
			.c1,.c2,.c3,.c4 {display: table-cell;vertical-align: middle;padding: 0}
			.c1 {text-align: left}
			.c4 {text-align: right}

			.c2 {width: 270px}
			.c3 {width: 270px}
			.c4 {width: 130px}
			h1{font-size:50px;line-height: 50px;}
			h2{font-size:20px;line-height: 28px}
			.page {max-width: 1700px;margin:0 ;text-align: left}
		}
		.c2 a:link,.c2 a:visited {
			border:#5db948 1px solid;border-radius: 40px;height:40px;line-height: 40px;padding:0 40px;display: inline-block;color: #5db948;text-decoration: none
		}
		.c2 a:hover {background: #5db948;color: white}
		
		.c3 a:link,.c3 a:visited {
			background: #5db948;border:#5db948 1px solid;border-radius: 40px;height:40px;line-height: 40px;padding:0 40px;display: inline-block;color: white;text-decoration: none
		}
		.c3 a:hover {background: white;color: #5db948;}
		
		.c4 a:link,.c4 a:visited,.c4 a:hover { text-decoration: none;color:#5db948}
		.c4 img {margin-right: 10px;position: relative;top:7px;}
<!--For label Sheet-->
		.label {
  color: white;
  padding: 8px;
  font-family: Arial;
}
.inactive {background-color: #4CAF50;} /* Green */
.inactive {background-color: #4CAF50;} /* Green */
.active {background-color: #f44336;} /* Red */ 
<!--END Style Sheet-->		
    </style>
  </head>

<!--body-->

<body>
	
<div class="bg">
<div class="outside">
<div class='inside'>
<div class='c1'><img src='https://www.pulsesecure.net/base/images/logo-white.png'> <h2> Zoom's Pro Account Status </h2> </div>


    
    
    """
    
b= """
<form name="RegForm" action="."  method="post">
        <p style="color:white;">Enter your E-mail Address <input type="text" size=55 name="Name"> </p><br>
</form>
"""   

@app.route('/meeting')
def index():
    return a + b

@app.route('/', methods=['POST'])
def getvalue():
    global name
    name = request.form['Name']
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex,name)):
        global otp_value
        otp_value = generateOTP()
        use_and_name.update({name:otp_value})
        send_email(name, otp_value)
        
        c = """
	<form name="RegForm" action="/status"  method="post">
        	<p style="color:white;">Enter OTP sent to email: <input type="text" size=55 name="otp"> </p><br>
        	
        	
    	</form>    
    	"""
        return a + c
    else:
        return a + "<h1>Invalid Email Address</h1>"

@app.route('/status', methods=['POST'])
def status():
    value1 = ""
    user_entered = request.form.to_dict('otp')
    for key, value in user_entered.items():
          value1 = value  
    if name == value1:
        b = a + "<h2>Correct OTP - Please select the available account to proceed meeting  </h2><br></br>" + "".join(available_accounts) + "".join(use_and_name)
        return b
    else:
        return a + "<h1>Incorrect OTP  </h1>"
		    
@app.route('/css1')
def css1():
    if "css1" in used_accounts:
        return a + "<h1>Account Already in Use</h1>"
    else:
        used_accounts.append("css1")
        u_n = "<h1>css1 :" + name + "</h1>"
        use_and_name.append(u_n)
        available_accounts =  list(set(total_accounts) - set(used_accounts))
        return "".join(used_accounts)

@app.route('/css2')
def css2():
    if "css2" in used_accounts:
        return a + "<h1>Account Already in Use</h1>"
    else:
        used_accounts.append("css2")
        u_n = "<h1>css2 :" + name + "</h1>"
        use_and_name.append(u_n)
        available_accounts =  list(set(total_accounts) - set(used_accounts))
        return "".join(used_accounts)
    
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
