import React, { Component } from 'react';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import FlatButton from 'material-ui/FlatButton';
import './Banner.css'

class Banner extends Component{

    constructor(props){
        super(props)
        this.state = {open: false}
        this.handleToggle = this.handleToggle.bind(this); 

    }

  handleToggle(){
    this.setState({open: !this.state.open});


  }
  handleClick(event){
  }

    render(){
        return(
            
                
            <div className="bar" >
                <button className="menubutton">Home</button>
                <button className="menubutton">About</button>
                <button className="menubutton">Usage</button>

            </div>
                

        )
    }
}

export default Banner