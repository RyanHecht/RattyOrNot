import React, { Component } from 'react';
import Item from './Item.jsx'
import './List.css'

class List extends Component {
   renderList() {
       
       const items = this.props.items.map(item => {
           return <Item name={item.name} vegan={true} vegetarian={true} glutenfree={true} nexttime={{location: "Ratty", time:"Tuesday"}}/>
       });

       return items;
   }

   render() {
       return (
           <div className="listitem">
               {this.renderList()}
           </div>
       );
   }
}

export default List;