import React, { Component } from 'react';
import './App.css';
import Signin from './Signin/Signin';
import Amplify, { Storage } from 'aws-amplify';
import awsmobile from './aws-exports';

Amplify.configure(awsmobile);

class App extends Component{

  put_dynamodb = async () => {
    //put some shit to dynamodb
    console.log('putting shit on ddb');
    const response = await API.post('dynamodbAPI', '/items', {
      // body: {
      //   id: '1',
      //   name: text
      // }
      body: this.state
    });
  }

  render(){
    return (
      <div className="App">
        {/* todo: pass reference to the signin component
        so that when I click signin, it runs put_dynamodb */}
        <Signin />
      </div>
    );
  }
}

export default App;
