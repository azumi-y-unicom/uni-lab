const FormDeck = (props) => {
  return (
      <form onSubmit={props.setDeck}>
        <table className="table">
          <tr>
            <th>id</th>
            <td>id</td>
          </tr>
          <tr>
            <th>タイトル</th>
            <td>
              <input type="text" name="title" placeholder="タイトル" />
            </td>
          </tr>
          <tr>
            <th>コメント</th>
            <td>
              <input type="text" name="comment" placeholder="説明" />
            </td>
          </tr>
        </table>
      </form>

  );
};

export default FormDeck;