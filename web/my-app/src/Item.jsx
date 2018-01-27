import React, { Component } from 'react';

class Item extends Component{
    constructor(props){
        super(props)
    }


    render(){
        return (
            <div>
                <h1>{this.props.name}</h1>
                    {this.props.vegan ? (<p>Vegan</p>) : null}
                {this.props.vegetarian ? (<p>Vegetarian</p>) : null}
                {this.props.glutenfree ? (<p>Gluten Free</p>) : null}
                {this.props.nexttime == null ? null : 
                    (<p>
                        Available at {this.props.nexttime.location} on {this.props.nexttime.time}
                    </p>)}

            </div>
        )
    }
}

export default Item;
