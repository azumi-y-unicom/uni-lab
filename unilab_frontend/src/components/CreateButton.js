import React, { useState } from 'react';

import Button from 'react-bootstrap/Button'
import Modal from 'react-bootstrap/Modal'
import FormLab from './FormLab'
import axios from 'axios';


const CreateButton = (props) => {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const handleSubmit = (e) =>{
    e.preventDefault();
    var url = `http://localhost:8000/lab/`;
    var data ={
      title,
      description,
      is_active
    }
    axios.post(url, data)
    .then(res =>{
      alert("追加しました");
      setShow(false);
      // TODO 再読み込み
    })
    .catch(res => {
      // 500系エラー
      alert("エラー");
      setShow(false);
    })
  }
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [is_active, setIsActive] = useState("1");
  
  return (
    <>
      <button type="button" className="btn btn-primary" onClick={handleShow}>{props.btn.text}</button>
      <Modal
        show={show}
        onHide={handleClose}
        backdrop="static"
        keyboard={false}
      >
        <form onSubmit={handleSubmit}>
          <Modal.Header closeButton>
            <Modal.Title>新規作成</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <FormLab 
              setTitle={setTitle}
              setDescription={setDescription}
              is_active={is_active}
              setIsActive={setIsActive}
            />
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={handleClose}>Cancel</Button>
            <Button variant="primary" type="submit">Create</Button>
          </Modal.Footer>
        </form>
      </Modal>
    </>
  );

}

export default CreateButton;