import React, { Component } from 'react';

class Query extends Component {
    constructor(props){
        super(props)
        this.state = {when: '', food: ''};
        this.handleChange = this.handleChange.bind(this); 
        this.handleSubmit = this.handleSubmit.bind(this);



    }

    handleSubmit(event){
        alert("You did this date! " + this.state.when + " with this food: " + this.state.food)
        event.preventDefault();
    }

    handleChange(event){
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;

        this.setState({
            [name]: value
        });
    }


    render(){
        return (
        <div>
         <h1>Query Page</h1>
            <p>We can have this to query a date, to get a complete listing of all the food</p>
            <form onSubmit={this.handleSubmit}>
                Start Date: 
                <select name="when" onChange={this.handleChange}>
                    <option value="today">Today</option>
                    <option value="tomorrow">Tomorrow</option>
                    <option value="week">This Week</option>
                    <option value="twoweeks">Next Two Weeks</option>
                </select><br/>

                Food: 
                <input type="text" name="food" onChange={this.handleChange}/>
                <input type="submit" value="Submit"/>
            </form>

        </div>
        )
    }
}

export default Query;