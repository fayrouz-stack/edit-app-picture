import React from "react";
import {
  Box,
  Container,
  Row,
  Column,
  FooterLink,
  
} from "./FooterStyles";
  
const Footer = () => {
  return (
    <Box>
      
      <Container>
        <Row>
          <Column>
            <h3>Les options</h3>
            <FooterLink href="#">Enhance,Filtrer,Améliorer</FooterLink>
          </Column>
          <Column>
            <h3>Services</h3>
            <FooterLink href="#">Design,éditer des photos</FooterLink> 
          </Column>
          <Column>
            <h3>Email</h3>
            <FooterLink href="#">Contact@contact.com</FooterLink>
          </Column>
          <Column>
            <h3>Fax</h3>
            <FooterLink href="#">01 23 57 88 66</FooterLink>
          </Column>
        </Row>
      </Container>
    </Box>
  );
};
export default Footer;