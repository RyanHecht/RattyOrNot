import React, { Component } from 'react';
import './App.css';
import Query from './Query.jsx';
import Counter from './Counter.jsx'

class App extends Component{
  render(){
    return (
      <div className="App">
        <Query/>
        <Counter/>
      </div>
    )
  }
}

export default App; 

