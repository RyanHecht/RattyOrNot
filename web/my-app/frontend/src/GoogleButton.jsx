import React, { Component } from 'react';
import GoogleLogin from 'react-google-login';

const googleStyle = {
  display: 'inline-block',
  background: '#dddddd',
  color: '#000',
  width: 190,
  textAlign: "right",
  paddingTop: 10,
  paddingBottom: 10,
  borderRadius: 2,
  border: '1px solid transparent',
  fontSize: 16,
  fontWeight: 'bold',
  fontFamily: 'Roboto',
  backgroundPosition: "left",
  backgroundSize: "40px 40px",
  backgroundRepeat: "no-repeat",
  backgroundImage: "url('https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/2000px-Google_%22G%22_Logo.svg.png')"
};

const padding = {
  padding: "20px"
};

class GoogleButton extends Component {
  responseGoogle = () => {
    console.log("google");
  };

  render() {
    return (
      <div style={padding}>
        <GoogleLogin
          clientId="658977310896-knrl3gka66fldh83dao2rhgbblmd4un9.apps.googleusercontent.com"
          buttonText="Sign in with Google"
          style={googleStyle}
          onSuccess={this.responseGoogle}
          onFailure={this.responseGoogle}
        />
      </div>

    )
  }
}

export default GoogleButton;
