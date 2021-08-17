import React, {useState} from "react";


const FormLab = (props) => {

  return (
    <div>
      <form onSubmit={props.postLab}>
        <table className="table form-table"><tbody>
            <tr>
              <th>タイトル</th>
              <td>
                <input type="text" name="title" placeholder="タイトル"
                  onChange={e => props.setTitle(e.target.value)} />
              </td>
            </tr>
            <tr>
              <th>説明</th>
              <td>
                <textarea name="description" placeholder="説明"
                  onChange={e => props.setDescription(e.target.value)} />
              </td>
            </tr>
            <tr>
              <th>利用状態</th>
              <td>
                <select name="is_active" 
                  onChange={e => props.setIs_active(e.target.value)} >
                  <option value="1">利用中</option>
                  <option value="0">利用停止</option>
                </select>
              </td>
            </tr>
          </tbody>
        </table>
      </form>
    </div>
  );
};

export default FormLab;