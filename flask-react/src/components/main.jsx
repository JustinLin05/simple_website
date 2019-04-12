import React from 'react'
import './main.sass' //import component style

class Main extends React.Component{
	constructor(props) {
		super(props)
		this.state = {
			content: ''
		}
	}
	componentWillMount() {
		fetch('http://192.168.99.100:2000/api/hello-world').then( res => {
			console.log(res)
			return res.json()
		}).then( data => {
			this.setState({
				content: data.content
			})
		})
	}
	render() {
		return (
			<div id="main-container">
				<h1>{this.state.content}</h1>
			</div>
		)
	}
}

export default Main