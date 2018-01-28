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
            {this.props.vegan ? (<img className="dot" src="http://legacy.cafebonappetit.com/assets/cor_icons/menu-item-type-c9d18b.png?v=1470070467"/>) : null}
            {this.props.vegetarian ? (<img className="dot" src="http://legacy.cafebonappetit.com/assets/cor_icons/menu-item-type-668e3c.png?v=1470070467"/>) : null}
            {this.props.glutenfree ? (<img className="dot" src="http://legacy.cafebonappetit.com/assets/cor_icons/menu-item-type-ce9d00.png?v=1470070466"/>) : null}
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
