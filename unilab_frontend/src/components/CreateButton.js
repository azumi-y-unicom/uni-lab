import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'

import Button from 'react-bootstrap/Button'
import Modal from 'react-bootstrap/Modal'
import FormLab from './FormLab'
import FormDeck from './FormDeck'

const bodycomponent ={
  lab: FormLab,
  deck: FormDeck,
}

// props.btn.title:
// props.btn.comp:
const CreateButton = (props) => {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const postLab = (e) =>{
    console.debug("post");
  }
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [is_active, setIs_active] = useState("");
  const MdlBody = <FormLab 
          postLab={postLab}
          setTitle={setTitle}
          setDescription={setDescription}
          setIs_active={setIs_active}
    />;
  
  return (
    <>
      <button type="button" className="btn btn-primary" onClick={handleShow}>{props.btn.text}</button>
      <Modal
        show={show}
        onHide={handleClose}
        backdrop="static"
        keyboard={false}
      >
        <Modal.Header closeButton>
          <Modal.Title>Modal title</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {MdlBody}
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>Cancel</Button>
          <Button variant="primary">Create</Button>
        </Modal.Footer>
      </Modal>
    </>
  );

}

export default CreateButton;