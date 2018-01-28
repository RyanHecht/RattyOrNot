import React, { Component } from 'react';
import './App.css';
import Query from './Query.jsx';
import Counter from './Counter.jsx'
import Item from './Item.jsx'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'; 

class App extends Component{
  render(){
    return (
      <div className="App">
        <MuiThemeProvider>
          <Query/>
          <Counter/>
          <Item name="Apple" vegan={true} vegetarian={true} glutenfree={true} nexttime={{location: "Ratty", time:"Tuesday"}}/>
          <Item name="Eggs" vegan={false} vegetarian={true} glutenfree={true}/>
        </MuiThemeProvider>
      </div>
    )
  }
}

export default App;
