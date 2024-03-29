/** 参考 */
/* https://react-bootstrap-table.github.io/react-bootstrap-table2/docs/row-select-props.html */
import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import axios from 'axios';

import CreateButton from '../components/CreateButton'



const btn = {
	text: "新規作成"
};

class Labs extends Component {

	editLab = (id, e) => {
		var url = `http://localhost:8000/lab/` + id + '/';
		axios.get(url)
			.then(res =>{
        alert("できた");
			})
			.catch(res => {
				// 500系エラー
				alert("エラー");
			})
	}

	moveDecks = (id, e) => {
		this.props.history.push({
			pathname: '/deck',
			state: {lab_id: id}
		});
	}

	constructor(props) {
    super(props);
    this.state = {
      isLoaded: false,
      items: []
    };
	}

	componentDidMount() {
		axios.get(`http://localhost:8000/lab`)
			.then(res =>{
        this.setState({ 
					isLoaded: true,
					items: res.data.list
				});
			})
			.catch(res => {
				// 500系エラー
				alert("エラー");
			})
	}

	render() {
		if (!this.state.isLoaded) {
			// サーバーと通信中
			return (
				<div>
					<h2>Lab</h2>
					<div>Now Loading</div>
				</div>
			);
		}else{
			// サーバーと通信完了
			// リスト
			const listItems = this.state.items.map( (item, i) =>
				<div className="box-lab" key={i} >
					<div className="upper">
						<div className="title">
							<a className="deck-link" href="" onClick={(e) => this.moveDecks(item.id, e)}>{item.title}</a>
								<span className="count">登録件数：{item.deck_count}</span>
						</div>
						<button type="button" onClick={(e) => this.editLab(item.id, e)} className="btn btn-outline-success btn-sm">編集</button>
					</div>
					<div>{item.description}</div>
				</div>
			);
			return (
				<div>
					<h2>Lab</h2>
					<div className="create-button-area">
						<CreateButton btn={btn}/>
					</div>
					<div className="" >
						{listItems}
					</div>
				</div>
			);
		}
	};
}
export default withRouter(Labs);