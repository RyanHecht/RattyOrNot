import React, { Component } from 'react';
import List from './List';

class FilteredList extends Component {
   constructor(props) {
       super(props);


       // The state is just a list of key/value pair (like a hashmap)
       this.state = {
           search: ""
       };
   }

   // Sets the state whenever the user types on the search bar
   onSearch = (event) => {
         this.setState({search: event.target.value.toLowerCase()});
   }

   filterItem = (item) => {
       // Checks if the current search term is contained in this item
       return item.name.toLowerCase().search(this.state.search) !== -1;
   }

   render() {
       return (
           <div className="filter-list">
                <h1>Food Search!</h1>
                <p>Set the parameters and type in what you would like to eat for food</p>
               <input type="text" placeholder="Search" onChange={this.onSearch} />

                {/*

                  Here we are taking the items property (which is the list of
                  produce), filtering the content to match the search word, then
                  passing the filtered produce into the List component.

                */}
               <List items={this.props.items.filter(this.filterItem)} />
           </div>
        );
   }
}

export default FilteredList; 