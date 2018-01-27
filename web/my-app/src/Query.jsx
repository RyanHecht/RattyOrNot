import React, { Component } from 'react';

class Query extends Component {

    handleSubmit(event){
        alert("ALERT BITCH")
        event.preventDefault();
    }
    handleSubmitTwo(event){
        alert("ALERT 2 BItCH")
        event.preventDefault();
    }

    render(){
        return (
        <div>
         <h1>Query Page</h1>
            <p>We can have this to query a date, to get a complete listing of all the food</p>
            <form onSubmit={this.handleSubmit}>
                Date: <input type="date" name="date"/>
                <input type="submit" value="Submit"/>
            </form>
            <p>We can have this to query a food, to get a list of dates of foods</p>
            <form onSubmit={this.handleSubmitTwo}>
                Food: <input type="text" name="food"/>
                <input type="submit" value="Submit" />
            </form>
        </div>
        )
    }
}

export default Query;