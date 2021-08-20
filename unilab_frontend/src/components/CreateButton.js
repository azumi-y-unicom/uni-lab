import React, { useState } from 'react';

import Button from 'react-bootstrap/Button'
import Modal from 'react-bootstrap/Modal'
import FormLab from './FormLab'


const CreateButton = (props) => {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const handleSubmit = (e) =>{
    
  }
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [is_active, setIs_active] = useState("");
  
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
              postLab=""
              setTitle=""
              setDescription=""
              setIs_active="1"
            />
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={handleClose}>Cancel</Button>
            <Button variant="primary">Create</Button>
          </Modal.Footer>
        </form>
      </Modal>
    </>
  );

}

export default CreateButton;