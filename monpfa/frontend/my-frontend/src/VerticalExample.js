import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import React from 'react';
import axios from 'axios';



function VerticalExample()
 {
  axios({
    method: "get",
    url: "http://127.0.0.1:5000/uploaded",
    data: {},
    headers: { crossDomain: true },
  })
  return (
   
    <ButtonGroup vertical>
      <Button>Hue</Button>
      <Button>Enhance</Button>

      <DropdownButton
        as={ButtonGroup}
        title="Filtres"
        id="bg-vertical-dropdown-1"
      >
        <Dropdown.Item eventKey="0">BlUR</Dropdown.Item>
        <Dropdown.Item eventKey="1">CONTOUR</Dropdown.Item>
        <Dropdown.Item eventKey="2">DETAIL</Dropdown.Item>
        <Dropdown.Item eventKey="3">EDGE_ENHANCE</Dropdown.Item>
        <Dropdown.Item eventKey="4">EDGE_ENHANCE_MORE</Dropdown.Item>
        <Dropdown.Item eventKey="5">EMBOSS</Dropdown.Item>
        <Dropdown.Item eventKey="6">FIND_EDGES</Dropdown.Item>
        <Dropdown.Item eventKey="7">SMOOTH</Dropdown.Item>
        <Dropdown.Item eventKey="8">SMOOTH8MORE</Dropdown.Item>
        <Dropdown.Item eventKey="9">SHARPEN</Dropdown.Item>
      </DropdownButton>

      <DropdownButton
        as={ButtonGroup}
        title="Flouter"
        id="bg-vertical-dropdown-2"
      >
        <Dropdown.Item eventKey="0">GaussianBlur(4)</Dropdown.Item>
        <Dropdown.Item eventKey="1">BLUR</Dropdown.Item>
        <Dropdown.Item eventKey="2">BoxBlur(1)</Dropdown.Item>
      </DropdownButton>

      <DropdownButton
        as={ButtonGroup}
        title="Transverse"
        id="bg-vertical-dropdown-3"
      >
        <Dropdown.Item eventKey="0">Transpose</Dropdown.Item>
        <Dropdown.Item eventKey="1">Transverse</Dropdown.Item>
        <Dropdown.Item eventKey="2">flip left right</Dropdown.Item>
        <Dropdown.Item eventKey="3">flip top bottom</Dropdown.Item>
      </DropdownButton>
      <DropdownButton
        as={ButtonGroup}
        title="Rotate"
        id="bg-vertical-dropdown-3"
      >
        <Dropdown.Item eventKey="0">90°</Dropdown.Item>
        <Dropdown.Item eventKey="1">180°</Dropdown.Item>
        <Dropdown.Item eventKey="2">270°</Dropdown.Item>
      </DropdownButton>
      <Button>redimensionner</Button>
    </ButtonGroup>
    
  );
}

export default VerticalExample;