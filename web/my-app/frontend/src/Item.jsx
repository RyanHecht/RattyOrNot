import React, { Component } from 'react';
import Radium from 'radium';
import './Item.css';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';

class Item extends Component{
    constructor(props){
        super(props)
    }


    render(){
        return (
            <div className="card">
              <Card>
                <CardTitle
                  title={this.props.name}
                />
                <CardText className="cardtext">
            {this.props.vegan ? (<p>Vegan</p>) : null}
            {this.props.vegetarian ? (<p>Vegetarian</p>) : null}
            {this.props.glutenfree ? (<p>Gluten Free</p>) : null}
            {this.props.nexttime == null ? null :
                (<p>
                    Available at {this.props.nexttime.location} on {this.props.nexttime.time}
                </p>)}
              </CardText>
              </Card>


            </div>
        )
    }
}

export default Radium(Item);
