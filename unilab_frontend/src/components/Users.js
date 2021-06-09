/** 参考 */
/* https://react-bootstrap-table.github.io/react-bootstrap-table2/docs/row-select-props.html */

import BootstrapTable from "react-bootstrap-table-next";
/** Todo：フィルター機能 */
import filterFactory, { textFilter } from 'react-bootstrap-table2-filter';

import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';

const columns = [
  { dataField: "id", text: "ID", sort: true, editable: false, hidden: true},
  { dataField: "no", text: "No", sort: true, editable: false,
		style: {backgroundColor: "#F0F0FF", cursor: "pointer"},
		events: {
			onClick: (e, column, columnIndex, row, rowIndex) => {
				alert('Coming Soon!!');
			},
			onMouseEnter: (e, column, columnIndex, row, rowIndex) => {
			}
		}
	},
  { dataField: "user_id", text: "ユーザーID", sort: true, editable: false},
  { dataField: "user_name", text: "表示ユーザ名", sort: true, editable: false},
  { dataField: "mail", text: "メールアドレス", sort: true, editable: false},
  { dataField: "auth", text: "権限", sort: true, editable: false},
  { dataField: "status", text: "状態", sort: true, editable: false},
  { dataField: "create_at", text: "登録日時", sort: true, editable: false },
  { dataField: "update_at", text: "最終更新日時", sort: true, editable: false },
];
const dataSmp = [
	{
		id: "1", 
		no: "1", 
		user_id: "ADMIN", 
		user_name: "ADMIN", 
		mail: "admin@admin.com", 
		auth: "管理者", 
		status: "利用中", 
		create_at: "2021/01/01 00:00:00", 
		update_at: "2021/01/01 00:00:00"
	}, 
	{
		id: "99", 
		no: "2", 
		user_id: "HOGE1" , 
		user_name: "ユーザーほげ１", 
		mail: "hoge1@hoge.com", 
		auth: "一般", 
		status: "利用中", 
		create_at: "2021/01/01 00:00:00", 
		update_at: "2021/01/01 00:00:00", 
	},
	{
		id: "105",
		no: "3", 
		user_id: "HOGE2",
		user_name: "ユーザーほげ２",
		mail: "hoge2@hoge.com", 
		auth: "一般", 
		status: "ロック中", 
		create_at: "2021/01/01 00:00:00",
		update_at: "2021/01/01 00:00:00",
	},
];

const defaultSorted = [{
  dataField: 'no',
  order: 'desc'
}];

const Users = (props) =>{
  return (
      <div>
        <h2>Users</h2>
        <BootstrapTable
          keyField = "id"
          data = {dataSmp}
          columns = {columns}
          bootstrap4 = {true}
          bordered={true}
					striped={true}
					noDataIndication={ 'no results found' }
        />
				</div>
  );
};
  
export default Users;