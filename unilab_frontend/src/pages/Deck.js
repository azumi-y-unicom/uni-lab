/** 参考 */
/* https://react-bootstrap-table.github.io/react-bootstrap-table2/docs/row-select-props.html */
import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import axios from 'axios';

import CreateButton from '../components/CreateButton'



const btn = {
	text: "新規作成"
};

class Deck extends Component {

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


	constructor(props) {
    super(props);
    this.state = {
      isLoaded: false,
			infomation: {},
			items: [],
    };
	}

	componentDidMount() {

		// 直リンはLabsに戻す
		if(this.props.location.state === undefined){
			this.props.history.push({
				pathname: '/labs'
			});
			return;
		}

		var lab = this.props.location.state.lab_id;
		var url = `http://localhost:8000/lab/` + lab + `/deck/`;
		axios.get(url)
			.then(res =>{
        this.setState({ 
					isLoaded: true,
					infomation: res.data.infomation,
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
			return (
				<div>
					<h2>Deck</h2>
					<div>Now Loading</div>
				</div>
			);
		}else{
			const info = this.state.infomation;
			const listItems = this.state.items.map( (item, i) =>
				<div className="box-lab" key={i} >
					<div className="upper">
						<div className="title">
							<a className="deck-link" href="" onClick={(e) => this.moveDecks(item.id, e)}>{item.title}</a>
								<span className="count">登録件数：{item.card_count}</span>
						</div>
						<button type="button" onClick={(e) => this.editLab(item.id, e)} className="btn btn-outline-success btn-sm">編集</button>
					</div>
					<div>{item.comment}</div>
				</div>
			);

			return (
				<div>
					<h2>説明</h2>
					<div>{info.title}、{info.description}、{info.deck_count}</div>
					<h2>一覧</h2>
					<div className="" >
						{listItems}
					</div>
				</div>
			);
		}
	};
}
export default withRouter(Deck);