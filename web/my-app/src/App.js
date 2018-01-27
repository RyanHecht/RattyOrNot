import React, { Component } from 'react';
import './App.css';
import Query from './Query.jsx';
import Counter from './Counter.jsx'
import Item from './Item.jsx'


class App extends Component{
  render(){
    return (
      <div className="App">
        <Query/>
        <Counter/>
        <Item name="Apple" vegan={true} vegetarian={true} glutenfree={true} nexttime={{location: "Ratty", time:"Tuesday"}}/>
        <Item name="Eggs" vegan={false} vegetarian={true} glutenfree={true}/>
      </div>
    )
  }
}

export default App; 

