/** 参考 */
/* https://react-bootstrap-table.github.io/react-bootstrap-table2/docs/row-select-props.html */
import React, { Component } from 'react';
import axios from 'axios';

import CreateButton from '../components/CreateButton'



const btn = {
	text: "新規作成"
};

export const createNewLab = (e) =>{
  e.preventDefault();
  alert("Coming Soon!!");
}

class Labs extends Component {
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
				const labs = res.data.list;
        this.setState({ 
					isLoaded: true,
					items: labs
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
			const listItems = this.state.items.map((item) =>
				<div className="box-lab">
					<div>ID： {item.id}</div>
					<div>タイトル：{item.title}</div>
					<div>説明：{item.description}</div>
					<div>登録数：{item.deck_count}</div>
				</div>
			);
			return (
				<div>
					<h2>Lab</h2>
					<div className="create-button-area">
						<CreateButton btn={btn}/>
					</div>
					<div className="">
						{listItems}
				</div>
			</div>
			);
		}
	};
}
export default Labs;