import React, { Component } from 'react';
import './App.css';
import Query from './Query.jsx';
import List from './List.jsx';
import FilteredList from './FilteredList.jsx';
import Counter from './Counter.jsx'
import Item from './Item.jsx'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import GoogleButton from './GoogleButton.jsx';



class App extends Component{

  render(){
    return (
      <div className="App">
        <MuiThemeProvider>

          <Query/>
          <GoogleButton/>
          <FilteredList items={[{name:"Apple"}, {name:"Banana"}, {name:"Candy"}]}/>
        </MuiThemeProvider>
      </div>
    )
  }
}

//<Item name="Apple" vegan={true} vegetarian={true} glutenfree={true} nexttime={{location: "Ratty", time:"Tuesday"}}/>
//<Item name="Eggs" vegan={false} vegetarian={true} glutenfree={true}/>


export default App;
