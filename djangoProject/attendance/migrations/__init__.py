/**
* Template Name: Tempo - v2.2.0
* Template URL: https://bootstrapmade.com/tempo-free-onepage-bootstrap-theme/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

/*--------------------------------------------------------------
# General
--------------------------------------------------------------*/
body {
  font-family: "Open Sans", sans-serif;
  color: #444444;
}

a {
  color: #e43c5c;
}

a:hover {
  color: #ea6981;
  text-decoration: none;
}

h1, h2, h3, h4, h5, h6 {
  font-family: "Nunito", sans-serif;
}

/*--------------------------------------------------------------
# Back to top button
--------------------------------------------------------------*/
.back-to-top {
  position: fixed;
  display: none;
  right: 15px;
  bottom: 15px;
  z-index: 99999;
  transition: 0.5s;
}

.back-to-top i {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  width: 40px;
  height: 40px;
  border-radius: 50px;
  background: #e43c5c;
  color: #fff;
  transition: all 0.4s;
}

.back-to-top:hover {
  bottom: 19px;
}

/*--------------------------------------------------------------
# Header
--------------------------------------------------------------*/
#header {
  transition: all 0.5s;
  z-index: 997;
  padding: 20px 0;
}

#header .logo {
  font-size: 32px;
  margin: 0;
  padding: 0;
  line-height: 1;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
}

#header .logo a {
  color: #fff;
}

#header .logo img {
  max-height: 40px;
}

#header.header-scrolled, #header.header-inner-pages {
  background: #fff;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
  padding: 12px 0;
}

#header.header-scrolled .logo a, #header.header-inner-pages .logo a {
  color: #493c3e;
}

@media (max-width: 992px) {
  #header .logo {
    font-size: 28px;
  }
}

/*--------------------------------------------------------------
# Navigation Menu
--------------------------------------------------------------*/
/* Desktop Navigation */
.nav-menu ul {
  margin: 0;
  padding: 0;
  list-style: none;
}

.nav-menu > ul {
  display: flex;
}

.nav-menu > ul > li {
  position: relative;
  white-space: nowrap;
  padding: 10px 0 10px 25px;
}

.nav-menu a {
  display: block;
  position: relative;
  color: #fff;
  transition: 0.3s;
  font-size: 15px;
  padding: 0 4px;
  letter-spacing: 0;
  font-family: "Poppins", sans-serif;
}

.nav-menu > ul > li > a:before {
  content: "";
  position: absolute;
  width: 100%;
  height: 2px;
  bottom: -6px;
  left: 0;
  background-color: #e43c5c;
  visibility: hidden;
  transform: scaleX(0);
  transition: all 0.3s ease-in-out 0s;
}

.nav-menu a:hover:before, .nav-menu li:hover > a:before, .nav-menu .active > a:before {
  visibility: visible;
  transform: scaleX(1);
}

.nav-menu .drop-down ul {
  display: block;
  position: absolute;
  left: 0;
  top: calc(100% + 30px);
  z-index: 99;
  opacity: 0;
  visibility: hidden;
  padding: 10px 0;
  background: #fff;
  box-shadow: 0 0 30px rgba(127, 137, 161, 0.25);
  transition: 0.3s;
}

.nav-menu .drop-down:hover > ul {
  opacity: 1;
  top: 100%;
  visibility: visible;
}

.nav-menu .drop-down li {
  min-width: 180px;
  position: relative;
}

.nav-menu .drop-down ul a {
  padding: 10px 20px;
  font-size: 14px;
  text-transform: none;
  color: #493c3e;
}

.nav-menu .drop-down ul a:hover, .nav-menu .drop-down ul .active > a, .nav-menu .drop-down ul li:hover > a {
  color: #e43c5c;
}

.nav-menu .drop-down > a:after {
  content: "\ea99";
  padding-left: 5px;
}

.nav-menu .drop-down .drop-down ul {
  top: 0;
  left: calc(100% - 30px);
}

.nav-menu .drop-down .drop-down:hover > ul {
  opacity: 1;
  top: 0;
  left: 100%;
}

.nav-menu .drop-down .drop-down > a {
  padding-right: 35px;
}

.nav-menu .drop-down .drop-down > a:after {
  content: "\eaa0";
  position: absolute;
  right: 15px;
}

.header-scrolled .nav-menu > ul > li > a, .header-inner-pages .nav-menu > ul > li > a {
  color: #493c3e;
}

@media (max-width: 1366px) {
  .nav-menu .drop-down .drop-down ul {
    left: -90%;
  }
  .nav-menu .drop-down .drop-down:hover > ul {
    left: -100%;
  }
  .nav-menu .drop-down .drop-down > a:after {
    content: "\ea9d";
  }
}

/* Mobile Navigation */
.mobile-nav-toggle {
  position: fixed;
  right: 15px;
  top: 15px;
  z-index: 9998;
  border: 0;
  background: none;
  font-size: 24px;
  transition: all 0.4s;
  outline: none !important;
  line-height: 1;
  cursor: pointer;
  text-align: right;
}

.mobile-nav-toggle i {
  color: #e43c5c;
}

.mobile-nav {
  position: fixed;
  top: 55px;
  right: 15px;
  bottom: 15px;
  left: 15px;
  z-index: 9999;
  overflow-y: auto;
  background: #fff;
  transition: ease-in-out 0.2s;
  opacity: 0;
  visibility: hidden;
  border-radius: 10px;
  padding: 10px 0;
}

.mobile-nav * {
  margin: 0;
  padding: 0;
  list-style: none;
}

.mobile-nav a {
  display: block;
  position: relative;
  color: #493c3e;
  padding: 10px 20px;
  font-weight: 500;
  outline: none;
}

.mobile-nav a:hover, .mobile-nav .active > a, .mobile-nav li:hover > a {
  color: #e43c5c;
  text-decoration: none;
}

.mobile-nav .drop-down > a:after {
  content: "\ea99";
  padding-left: 10px;
  position: absolute;
  right: 15px;
}

.mobile-nav .active.drop-down > a:after {
  content: "\eaa1";
}

.mobile-nav .drop-down > a {
  padding-right: 35px;
}

.mobile-nav .drop-down ul {
  display: none;
  overflow: hidden;
}

.mobile-nav .drop-down li {
  padding-left: 20px;
}

.mobile-nav-overly {
  width: 100%;
  height: 100%;
  z-index: 9997;
  top: 0;
  left: 0;
  position: fixed;
  background: rgba(45, 37, 38, 0.6);
  overflow: hidden;
  display: none;
  transition: ease-in-out 0.2s;
}

.mobile-nav-active {
  overflow: hidden;
}

.mobile-nav-active .mobile-nav {
  opacity: 1;
  visibility: visible;
}

.mobile-nav-active .mobile-nav-toggle i {
  color: #fff;
}

/*--------------------------------------------------------------
# Hero Section
--------------------------------------------------------------*/
#hero {
  width: 100%;
  height: 100vh;
  background: url("../../media/default.jpg") top center;
  background-size: cover;
  position: relative;
}

#hero:before {
  content: "";
  background: rgba(0, 0, 0, 0.6);
  position: absolute;
  bottom: 0;
  top: 0;
  left: 0;
  right: 0;
}

#hero .hero-container {
  position: absolute;
  bottom: 0;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  text-align: center;
  padding: 0 15px;
}

#hero h3 {
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  font-size: 26px;
  padding: 10px 30px;
  margin-bottom: 30px;
  border-radius: 50px;
}

#hero h1 {
  margin: 0 0 10px 0;
  font-size: 48px;
  font-weight: 700;
  line-height: 56px;
  text-transform: uppercase;
  color: #fff;
}

#hero h2 {
  color: #eee;
  margin-bottom: 40px;
  font-size: 24px;
}

#hero .btn-get-started {
  font-family: "Poppins", sans-serif;
  text-transform: uppercase;
  font-weight: 400;
  font-size: 13px;
  letter-spacing: 1px;
  display: inline-block;
  padding: 8px 30px 9px 30px;
  border-radius: 50px;
  transition: 0.5s;
  border: 2px solid #fff;
  color: #fff;
}

#hero .btn-get-started:hover {
  background: #e43c5c;
  border: 2px solid #e43c5c;
}

@media (min-width: 1024px) {
  #hero {
    background-attachment: fixed;
  }
}

@media (max-width: 768px) {
  #hero h3 {
    font-size: 22px;
  }
  #hero h1 {
    font-size: 28px;
    line-height: 36px;
  }
  #hero h2 {
    font-size: 18px;
    line-height: 24px;
    margin-bottom: 30px;
  }
}

@media (max-height: 500px) {
  #hero {
    height: 150vh;
  }
}

/*--------------------------------------------------------------
# Sections General
--------------------------------------------------------------*/
section {
  padding: 60px 0;
}

.section-bg {
  background-color: white;
}

.section-title {
  text-align: center;
  padding-bottom: 30px;
}

.section-title h2 {
  font-size: 13px;
  letter-spacing: 1px;
  font-weight: 700;
  padding: 8px 20px;
  line-height: 1;
  margin: 0;
  background: #fdeff2;
  color: #e43c5c;
  display: inline-block;
  text-transform: uppercase;
  border-radius: 50px;
}

.section-title h3 {
  margin: 15px 0 0 0;
  font-size: 32px;
  font-weight: 700;
}

.section-title h3 span {
  color: #e43c5c;
}

.section-title p {
  margin: 15px auto 0 auto;
  font-weight: 600;
}

@media (min-width: 1024px) {
  .section-title p {
    width: 50%;
  }
}

/*--------------------------------------------------------------
# About
--------------------------------------------------------------*/
.about .content h3 {
  font-weight: 600;
  font-size: 26px;
}

.about .content ul {
  list-style: none;
  padding: 0;
}

.about .content ul li {
  padding-left: 28px;
  position: relative;
}

.about .content ul li + li {
  margin-top: 10px;
}

.about .content ul i {
  position: absolute;
  left: 0;
  top: 2px;
  font-size: 20px;
  color: #e43c5c;
  line-height: 1;
}

.about .content p:last-child {
  margin-bottom: 0;
}

.about .content .btn-learn-more {
  font-family: "Nunito", sans-serif;
  font-weight: 600;
  font-size: 14px;
  letter-spacing: 1px;
  display: inline-block;
  padding: 12px 32px;
  border-radius: 50px;
  transition: 0.3s;
  line-height: 1;
  color: #e43c5c;
  -webkit-animation-delay: 0.8s;
  animation-delay: 0.8s;
  margin-top: 6px;
  border: 2px solid #e43c5c;
}

.about .content .btn-learn-more:hover {
  background: #e43c5c;
  color: #fff;
  text-decoration: none;
}

/*--------------------------------------------------------------
# Services
--------------------------------------------------------------*/
.services {
  padding-bottom: 30px;
}

.services .icon-box {
  padding: 60px 30px;
  position: relative;
  overflow: hidden;
  background: #fff;
  box-shadow: 2px 0 35px 0 rgba(68, 88, 144, 0.12);
  transition: all 0.3s ease-in-out;
  border-radius: 8px;
  z-index: 1;
  text-align: center;
}

.services .icon-box::before {
  content: '';
  position: absolute;
  background: #fdeff2;
  right: 0;
  left: 0;
  bottom: 0;
  top: 100%;
  transition: all 0.4s;
  z-index: -1;
}

.services .icon-box:hover::before {
  background: #e43c5c;
  top: 0;
  border-radius: 0;
}

.services .icon {
  margin-bottom: 15px;
}

.services .icon i {
  font-size: 48px;
  line-height: 1;
  color: #e43c5c;
  transition: all 0.3s ease-in-out;
}

.services .title {
  font-weight: 700;
  margin-bottom: 15px;
  font-size: 18px;
}

.services .title a {
  color: #111;
}

.services .description {
  font-size: 15px;
  line-height: 28px;
  margin-bottom: 0;
}

.services .icon-box:hover .title a, .services .icon-box:hover .description {
  color: #fff;
}

.services .icon-box:hover .icon i {
  color: #fff;
}

/*--------------------------------------------------------------
# Features
--------------------------------------------------------------*/
.features {
  padding-top: 0;
}

.features .icon-box {
  display: flex;
  align-items: center;
  padding: 20px;
  transition: ease-in-out 0.3s;
  box-shadow: 2px 0 35px 0 rgba(68, 88, 144, 0.12);
}

.features .icon-box i {
  font-size: 32px;
  padding-right: 10px;
  line-height: 1;
}

.features .icon-box h3 {
  font-weight: 700;
  margin: 0;
  padding: 0;
  line-height: 1;
  font-size: 16px;
}

.features .icon-box h3 a {
  color: #493c3e;
  transition: ease-in-out 0.3s;
}

.features .icon-box:hover a {
  color: #e43c5c;
}

/*--------------------------------------------------------------
# Cta
--------------------------------------------------------------*/
.cta {
  background: linear-gradient(rgba(2, 2, 2, 0.5), rgba(0, 0, 0, 0.8)), url("/media/default.jpg") center center;
  background-size: cover;
  padding: 60px 0;
}

.cta h3 {
  color: #fff;
  font-size: 28px;
  font-weight: 700;
}

.cta p {
  color: #fff;
}

.cta .cta-btn {
  font-family: "Nunito", sans-serif;
  text-transform: uppercase;
  font-weight: 500;
  font-size: 16px;
  letter-spacing: 1px;
  display: inline-block;
  padding: 8px 28px;
  border-radius: 25px;
  transition: 0.5s;
  margin-top: 10px;
  border: 2px solid #fff;
  color: #fff;
}

.cta .cta-btn:hover {
  background: #e43c5c;
  border: 2px solid #e43c5c;
}

@media (min-width: 1024px) {
  .cta {
    background-attachment: fixed;
  }
}

/*--------------------------------------------------------------
# Portfolio
--------------------------------------------------------------*/
.portfolio #portfolio-flters {
  padding: 0;
  margin: 0 auto 25px auto;
  list-style: none;
  text-align: center;
  border-radius: 50px;
}

.portfolio #portfolio-flters li {
  cursor: pointer;
  display: inline-block;
  padding: 7px 17px 9px 17px;
  font-size: 14px;
  font-weight: 500;
  line-height: 1;
  color: #444444;
  margin: 0 3px 10px 3px;
  transition: all ease-in-out 0.3s;
  background: #ede9e9;
  border-radius: 50px;
}

.portfolio #portfolio-flters li:hover, .portfolio #portfolio-flters li.filter-active {
  color: #fff;
  background: #e43c5c;
}

.portfolio #portfolio-flters li:last-child {
  margin-right: 0;
}

.portfolio .portfolio-item {
  margin-bottom: 30px;
  overflow: hidden;
}

.portfolio .portfolio-item img {
  position: relative;
  top: 0;
  transition: all 0.6s cubic-bezier(0.645, 0.045, 0.355, 1);
}

.portfolio .portfolio-item .portfolio-info {
  opacity: 0;
  position: absolute;
  left: 15px;
  right: 15px;
  bottom: -50px;
  z-index: 3;
  transition: all ease-in-out 0.3s;
  background: #e43c5c;
  padding: 15px 20px;
}

.portfolio .portfolio-item .portfolio-info h4 {
  font-size: 18px;
  color: #fff;
  font-weight: 600;
}

.portfolio .portfolio-item .portfolio-info p {
  color: #fff;
  font-size: 14px;
  margin-bottom: 0;
}

.portfolio .portfolio-item .portfolio-info .preview-link, .portfolio .portfolio-item .portfolio-info .details-link {
  position: absolute;
  right: 50px;
  font-size: 24px;
  top: calc(50% - 18px);
  color: white;
  transition: ease-in-out 0.3s;
}

.portfolio .portfolio-item .portfolio-info .preview-link:hover, .portfolio .portfolio-item .portfolio-info .details-link:hover {
  color: #f7c2cc;
}

.portfolio .portfolio-item .portfolio-info .details-link {
  right: 15px;
}

.portfolio .portfolio-item:hover img {
  top: -30px;
}

.portfolio .portfolio-item:hover .portfolio-info {
  opacity: 1;
  bottom: 0;
}

/*--------------------------------------------------------------
# Pricing
--------------------------------------------------------------*/
.pricing .box {
  padding: 20px;
  background: #f9f9f9;
  text-align: center;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
  border: 2px solid #f9f9f9;
}

.pricing .box h3 {
  font-weight: 400;
  padding: 15px;
  margin-top: 15px;
  font-size: 20px;
  color: #493c3e;
}

.pricing .box h4 {
  font-size: 42px;
  color: #e43c5c;
  font-weight: 500;
  font-family: "Open Sans", sans-serif;
  margin-bottom: 20px;
}

.pricing .box h4 sup {
  font-size: 20px;
  top: -15px;
  left: -3px;
}

.pricing .box h4 span {
  color: #bababa;
  font-size: 16px;
  font-weight: 300;
}

.pricing .box ul {
  padding: 0;
  list-style: none;
  color: #493c3e;
  text-align: center;
  line-height: 20px;
  font-size: 14px;
}

.pricing .box ul li {
  padding-bottom: 16px;
}

.pricing .box ul i {
  color: #e43c5c;
  font-size: 18px;
  padding-right: 4px;
}

.pricing .box ul .na {
  color: #ccc;
  text-decoration: line-through;
}

.pricing .box .btn-wrap {
  padding: 15px;
  text-align: center;
}

.pricing .box .btn-buy {
  display: inline-block;
  padding: 8px 40px 10px 40px;
  border-radius: 50px;
  border: 2px solid #e43c5c;
  color: #e43c5c;
  font-size: 14px;
  font-family: "Nunito", sans-serif;
  font-weight: 600;
  transition: 0.3s;
}

.pricing .box .btn-buy:hover {
  background: #e43c5c;
  color: #fff;
}

.pricing .recommended {
  border-color: #e43c5c;
}

.pricing .recommended .btn-buy {
  background: #e43c5c;
  color: #fff;
}

.pricing .recommended .btn-buy:hover {
  background: #d91e42;
  border-color: #d91e42;
}

.pricing .recommended-badge {
  position: absolute;
  top: 5px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1;
  font-size: 13px;
  padding: 3px 25px 6px 25px;
  background: #fce6ea;
  color: #e43c5c;
  border-radius: 50px;
}

/*--------------------------------------------------------------
# F.A.Q
--------------------------------------------------------------*/
.faq {
  padding: 60px 0;
}

.faq .faq-list {
  padding: 0;
  list-style:none;
}

.faq .faq-list li {
  padding: 0 0 20px 25px;
}

.faq .faq-list a {
  display: block;
  position: relative;
  font-size: 18px;
  font-weight: 500;
}

.faq .faq-list i {
  font-size: 18px;
  position: absolute;
  left: -25px;
  top: 6px;
}

.faq .faq-list p {
  margin-bottom: 20px;
  font-size: 15px;
}

.faq .faq-list a.collapse {
  color: #e43c5c;
}

.faq .faq-list a.collapsed {
  color: #343a40;
}

.faq .faq-list a.collapsed:hover {
  color: #e43c5c;
}

.faq .faq-list a.collapsed i::before {
  content: "\eab2" !important;
}

@media (min-width: 1280px) {
  .faq .container {
    padding: 0 120px;
  }
}

/*--------------------------------------------------------------
# Team
--------------------------------------------------------------*/
.team {
  background: #fff;
  padding: 60px 0;
}

.team .member {
  margin-bottom: 20px;
  overflow: hidden;
  text-align: center;
  border-radius: 5px;
  background: #fff;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
}

.team .member .member-img {
  position: relative;
  overflow: hidden;
}

.team .member .social {
  position: absolute;
  left: 0;
  bottom: 0;
  right: 0;
  height: 40px;
  opacity: 0;
  transition: ease-in-out 0.3s;
  text-align: center;
  background: rgba(255, 255, 255, 0.85);
}

.team .member .social a {
  transition: color 0.3s;
  color: #493c3e;
  margin: 0 10px;
  padding-top: 8px;
  display: inline-block;
}

.team .member .social a:hover {
  color: #e43c5c;
}

.team .member .social i {
  font-size: 18px;
  margin: 0 2px;
}

.team .member .member-info {
  padding: 25px 15px;
}

.team .member .member-info h4 {
  font-weight: 700;
  margin-bottom: 5px;
  font-size: 18px;
  color: #493c3e;
}

.team .member .member-info span {
  display: block;
  font-size: 13px;
  font-weight: 400;
  color: #aaaaaa;
}

.team .member .member-info p {
  font-style: italic;
  font-size: 14px;
  line-height: 26px;
  color: #777777;
}

.team .member:hover .social {
  opacity: 1;
}

/*--------------------------------------------------------------
# Contact
--------------------------------------------------------------*/
.contact .info {
  width: 100%;
  background: #fff;
}

.contact .info i {
  font-size: 20px;
  color: #e43c5c;
  float: left;
  width: 44px;
  height: 44px;
  background: #fdeff2;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50px;
  transition: all 0.3s ease-in-out;
}

.contact .info h4 {
  padding: 0 0 0 60px;
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 5px;
  color: #493c3e;
}

.contact .info p {
  padding: 0 0 0 60px;
  margin-bottom: 0;
  font-size: 14px;
  color: #816a6e;
}

.contact .info .email, .contact .info .phone {
  margin-top: 40px;
}

.contact .info .email:hover i, .contact .info .address:hover i, .contact .info .phone:hover i {
  background: #e43c5c;
  color: #fff;
}

.contact .php-email-form {
  width: 100%;
  background: #fff;
}

.contact .php-email-form .form-group {
  padding-bottom: 8px;
}

.contact .php-email-form .validate {
  display: none;
  color: red;
  margin: 0 0 15px 0;
  font-weight: 400;
  font-size: 13px;
}

.contact .php-email-form .error-message {
  display: none;
  color: #fff;
  background: #ed3c0d;
  text-align: left;
  padding: 15px;
  font-weight: 600;
}

.contact .php-email-form .error-message br + br {
  margin-top: 25px;
}

.contact .php-email-form .sent-message {
  display: none;
  color: #fff;
  background: #18d26e;
  text-align: center;
  padding: 15px;
  font-weight: 600;
}

.contact .php-email-form .loading {
  display: none;
  background: #fff;
  text-align: center;
  padding: 15px;
}

.contact .php-email-form .loading:before {
  content: "";
  display: inline-block;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  margin: 0 10px -6px 0;
  border: 3px solid #18d26e;
  border-top-color: #eee;
  -webkit-animation: animate-loading 1s linear infinite;
  animation: animate-loading 1s linear infinite;
}

.contact .php-email-form input, .contact .php-email-form textarea {
  border-radius: 0;
  box-shadow: none;
  font-size: 14px;
}

.contact .php-email-form input:focus, .contact .php-email-form textarea:focus {
  border-color: #e43c5c;
}

.contact .php-email-form input {
  height: 44px;
}

.contact .php-email-form textarea {
  padding: 10px 12px;
}

.contact .php-email-form button[type="submit"] {
  background: #e43c5c;
  border: 0;
  padding: 10px 28px;
  color: #fff;
  transition: 0.4s;
  border-radius: 50px;
}

.contact .php-email-form button[type="submit"]:hover {
  background: #d01d3f;
}

@-webkit-keyframes animate-loading {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

@keyframes animate-loading {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/*--------------------------------------------------------------
# Breadcrumbs
--------------------------------------------------------------*/
.breadcrumbs {
  padding: 15px 0;
  background: #f6f4f4;
  margin-top: 67px;
}

@media (max-width: 992px) {
  .breadcrumbs {
    margin-top: 50px;
  }
}

.breadcrumbs h2 {
  font-size: 26px;
  font-weight: 600;
}

.breadcrumbs ol {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  padding: 0 0 10px 0;
  margin: 0;
  font-size: 14px;
}

.breadcrumbs ol li + li {
  padding-left: 10px;
}

.breadcrumbs ol li + li::before {
  display: inline-block;
  padding-right: 10px;
  color: #655356;
  content: "/";
}

/*--------------------------------------------------------------
# Portfolio Details
--------------------------------------------------------------*/
.portfolio-details {
  padding-top: 40px;
}

.portfolio-details .portfolio-details-container {
  position: relative;
}

.portfolio-details .portfolio-details-carousel {
  position: relative;
  z-index: 1;
}

.portfolio-details .portfolio-details-carousel .owl-nav, .portfolio-details .portfolio-details-carousel .owl-dots {
  margin-top: 5px;
  text-align: left;
}

.portfolio-details .portfolio-details-carousel .owl-dot {
  display: inline-block;
  margin: 0 10px 0 0;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: #ddd !important;
}

.portfolio-details .portfolio-details-carousel .owl-dot.active {
  background-color: #e43c5c !important;
}

.portfolio-details .portfolio-info {
  padding: 30px;
  position: absolute;
  right: 0;
  bottom: -70px;
  background: #fff;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
  z-index: 2;
}

.portfolio-details .portfolio-info h3 {
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid #eee;
}

.portfolio-details .portfolio-info ul {
  list-style: none;
  padding: 0;
  font-size: 15px;
}

.portfolio-details .portfolio-info ul li + li {
  margin-top: 10px;
}

.portfolio-details .portfolio-description {
  padding-top: 50px;
}

.portfolio-details .portfolio-description h2 {
  width: 50%;
  font-size: 26px;
  font-weight: 700;
  margin-bottom: 20px;
}

.portfolio-details .portfolio-description p {
  padding: 0 0 0 0;
}

@media (max-width: 768px) {
  .portfolio-details .portfolio-info {
    position: static;
    margin-top: 30px;
  }
}

/*--------------------------------------------------------------
# Blog
--------------------------------------------------------------*/
.blog {
  padding: 40px 0 20px 0;
}

.blog .entry {
  padding: 20px;
  margin-bottom: 60px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.blog .entry .entry-img {
  max-height: 400px;
  margin: -20px -20px 20px -20px;
  overflow: hidden;
}

.blog .entry .entry-title {
  font-size: 20px;
  line-height: 26px;
  font-weight: bold;
  padding: 0;
  margin: 0 0 20px 0;
}

.blog .entry .entry-title a {
  color: #493c3e;
  transition: 0.3s;
}

.blog .entry .entry-title a:hover {
  color: #e43c5c;
}

.blog .entry .entry-meta {
  color: #9a8487;
}

.blog .entry .entry-meta ul {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  padding: 0;
  margin: 0;
}

.blog .entry .entry-meta ul li {
  margin-bottom: 15px;
}

.blog .entry .entry-meta ul li + li {
  padding-left: 15px;
}

.blog .entry .entry-meta i {
  font-size: 14px;
  padding-right: 4px;
}

.blog .entry .entry-meta a {
  color: #9a8487;
  font-size: 14px;
  display: inline-block;
  line-height: 1;
}

.blog .entry .entry-content p {
  line-height: 24px;
  font-size: 15px;
}

.blog .entry .entry-content .read-more {
  -moz-text-align-last: right;
  text-align-last: right;
}

.blog .entry .entry-content .read-more a {
  display: inline-block;
  background: #e43c5c;
  color: #fff;
  padding: 5px 20px 7px 20px;
  transition: 0.3s;
  font-size: 14px;
  border-radius: 50px;
}

.blog .entry .entry-content .read-more a:hover {
  background: #d01d3f;
}

.blog .entry .entry-content h3 {
  font-size: 22px;
  margin-top: 30px;
  font-weight: bold;
}

.blog .entry .entry-content blockquote {
  overflow: hidden;
  background-color: #fafafa;
  padding: 60px;
  position: relative;
  text-align: center;
  margin: 20px 0;
}

.blog .entry .entry-content blockquote p {
  color: #444444;
  line-height: 1.6;
  margin-bottom: 0;
  font-style: italic;
  font-weight: 500;
  font-size: 22px;
}

.blog .entry .entry-content blockquote .quote-left {
  position: absolute;
  left: 20px;
  top: 20px;
  font-size: 36px;
  color: #e7e7e7;
}

.blog .entry .entry-content blockquote .quote-right {
  position: absolute;
  right: 20px;
  bottom: 20px;
  font-size: 36px;
  color: #e7e7e7;
}

.blog .entry .entry-content blockquote::after {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background-color: #493c3e;
  margin-top: 20px;
  margin-bottom: 20px;
}

.blog .entry .entry-footer {
  padding-top: 10px;
  border-top: 1px solid #e6e6e6;
}

.blog .entry .entry-footer i {
  color: #9a8487;
  display: inline;
}

.blog .entry .entry-footer a {
  color: #c3b6b8;
  transition: 0.3s;
}

.blog .entry .entry-footer a:hover {
  color: #e43c5c;
}

.blog .entry .entry-footer .cats {
  list-style: none;
  display: inline;
  padding: 0 20px 0 0;
  font-size: 14px;
}

.blog .entry .entry-footer .cats li {
  display: inline-block;
}

.blog .entry .entry-footer .tags {
  list-style: none;
  display: inline;
  padding: 0;
  font-size: 14px;
}

.blog .entry .entry-footer .tags li {
  display: inline-block;
}

.blog .entry .entry-footer .tags li + li::before {
  padding-right: 6px;
  color: #6c757d;
  content: ",";
}

.blog .entry .entry-footer .share {
  font-size: 16px;
}

.blog .entry .entry-footer .share i {
  padding-left: 5px;
}

.blog .entry-single {
  margin-bottom: 30px;
}

.blog .entry-single .entry-title {
  font-size: 36px;
  line-height: 42px;
}

.blog .blog-author {
  padding: 20px;
  margin-bottom: 30px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.blog .blog-author img {
  width: 120px;
}

.blog .blog-author h4 {
  margin-left: 140px;
  font-weight: 600;
  font-size: 22px;
  margin-bottom: 0;
  padding: 0;
}

.blog .blog-author .social-links {
  margin: 0 0 5px 140px;
}

.blog .blog-author .social-links a {
  color: #b1a0a3;
}

.blog .blog-author p {
  margin-left: 140px;
  font-style: italic;
  color: #b7b7b7;
}

.blog .blog-comments {
  margin-bottom: 30px;
}

.blog .blog-comments .comments-count {
  font-weight: bold;
}

.blog .blog-comments .comment {
  margin-top: 30px;
  position: relative;
}

.blog .blog-comments .comment .comment-img {
  width: 50px;
}

.blog .blog-comments .comment h5 {
  margin-left: 65px;
  font-size: 16px;
  margin-bottom: 2px;
}

.blog .blog-comments .comment h5 a {
  font-weight: bold;
  color: #444444;
  transition: 0.3s;
}

.blog .blog-comments .comment h5 a:hover {
  color: #e43c5c;
}

.blog .blog-comments .comment h5 .reply {
  padding-left: 10px;
  color: #493c3e;
}

.blog .blog-comments .comment time {
  margin-left: 65px;
  display: block;
  font-size: 14px;
  color: #b1a0a3;
  margin-bottom: 5px;
}

.blog .blog-comments .comment p {
  margin-left: 65px;
}

.blog .blog-comments .comment.comment-reply {
  padding-left: 40px;
}

.blog .blog-comments .reply-form {
  margin-top: 30px;
  padding: 30px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.blog .blog-comments .reply-form h4 {
  font-weight: bold;
  font-size: 22px;
}

.blog .blog-comments .reply-form p {
  font-size: 14px;
}

.blog .blog-comments .reply-form input {
  border-radius: 0;
  padding: 20px 10px;
  font-size: 14px;
}

.blog .blog-comments .reply-form input:focus {
  box-shadow: none;
  border-color: #f096a7;
}

.blog .blog-comments .reply-form textarea {
  border-radius: 0;
  padding: 10px 10px;
  font-size: 14px;
}

.blog .blog-comments .reply-form textarea:focus {
  box-shadow: none;
  border-color: #f096a7;
}

.blog .blog-comments .reply-form .form-group {
  margin-bottom: 25px;
}

.blog .blog-comments .reply-form .btn-primary {
  padding: 10px 20px;
  border: 0;
  border-radius: 50px;
  background-color: #493c3e;
}

.blog .blog-comments .reply-form .btn-primary:hover {
  background-color: #e43c5c;
}

.blog .blog-pagination {
  color: #816a6e;
}

.blog .blog-pagination ul {
  display: flex;
  padding-left: 0;
  list-style: none;
}

.blog .blog-pagination li {
  border: 1px solid white;
  margin: 0 5px;
  transition: 0.3s;
}

.blog .blog-pagination li.active {
  background: white;
}

.blog .blog-pagination li a {
  color: #aaaaaa;
  padding: 7px 16px;
  display: inline-block;
}

.blog .blog-pagination li.active, .blog .blog-pagination li:hover {
  background: #e43c5c;
  border: 1px solid #e43c5c;
}

.blog .blog-pagination li.active a, .blog .blog-pagination li:hover a {
  color: #fff;
}

.blog .blog-pagination li.disabled {
  background: #fff;
  border: 1px solid white;
}

.blog .blog-pagination li.disabled i {
  color: #f1f1f1;
  padding: 10px 16px;
  display: inline-block;
}

.blog .sidebar {
  padding: 30px;
  margin: 0 0 60px 20px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.blog .sidebar .sidebar-title {
  font-size: 20px;
  font-weight: 700;
  padding: 0 0 0 0;
  margin: 0 0 15px 0;
  color: #493c3e;
  position: relative;
}

.blog .sidebar .sidebar-item {
  margin-bottom: 30px;
}

.blog .sidebar .search-form form {
  background: #fff;
  border: 1px solid #d3cacb;
  padding: 3px 10px;
  position: relative;
  border-radius: 50px;
}

.blog .sidebar .search-form form input[type="text"] {
  border: 0;
  padding: 4px;
  width: calc(100% - 42px);
}

.blog .sidebar .search-form form button {
  position: absolute;
  border-radius: 50px;
  top: 0;
  right: -2px;
  bottom: 0;
  border: 0;
  background: none;
  font-size: 16px;
  padding: 0 20px;
  margin: -1px;
  background: #e43c5c;
  color: #fff;
  transition: 0.3s;
}

.blog .sidebar .search-form form button:hover {
  background: #d01d3f;
}

.blog .sidebar .categories ul {
  list-style: none;
  padding: 0;
}

.blog .sidebar .categories ul li + li {
  padding-top: 10px;
}

.blog .sidebar .categories ul a {
  color: #655356;
}

.blog .sidebar .categories ul a:hover {
  color: #e43c5c;
}

.blog .sidebar .categories ul a span {
  padding-left: 5px;
  color: #b1a0a3;
  font-size: 14px;
}

.blog .sidebar .recent-posts .post-item + .post-item {
  margin-top: 15px;
}

.blog .sidebar .recent-posts img {
  width: 80px;
  float: left;
}

.blog .sidebar .recent-posts h4 {
  font-size: 15px;
  margin-left: 95px;
  font-weight: bold;
}

.blog .sidebar .recent-posts h4 a {
  color: #110e0e;
  transition: 0.3s;
}

.blog .sidebar .recent-posts h4 a:hover {
  color: #e43c5c;
}

.blog .sidebar .recent-posts time {
  display: block;
  margin-left: 95px;
  font-style: italic;
  font-size: 14px;
  color: #b1a0a3;
}

.blog .sidebar .tags {
  margin-bottom: -10px;
}

.blog .sidebar .tags ul {
  list-style: none;
  padding: 0;
}

.blog .sidebar .tags ul li {
  display: inline-block;
}

.blog .sidebar .tags ul a {
  color: #8e767a;
  font-size: 14px;
  padding: 6px 14px;
  margin: 0 6px 8px 0;
  border: 1px solid #ede9e9;
  display: inline-block;
  border-radius: 50px;
  transition: 0.3s;
}

.blog .sidebar .tags ul a:hover {
  color: #fff;
  border: 1px solid #e43c5c;
  background: #e43c5c;
}

.blog .sidebar .tags ul a span {
  padding-left: 5px;
  color: #dfd8d9;
  font-size: 14px;
}

/*--------------------------------------------------------------
# Footer
--------------------------------------------------------------*/
#footer {
  color: #444444;
  font-size: 14px;
  background: #f6f4f4;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
}

#footer .footer-top {
  padding: 60px 0 30px 0;
  background: #fff;
}

#footer .footer-top .footer-contact {
  margin-bottom: 30px;
}

#footer .footer-top .footer-contact h4 {
  font-size: 22px;
  margin: 0 0 30px 0;
  padding: 2px 0 2px 0;
  line-height: 1;
  font-weight: 700;
}

#footer .footer-top .footer-contact p {
  font-size: 14px;
  line-height: 24px;
  margin-bottom: 0;
  font-family: "Nunito", sans-serif;
  color: #777777;
}

#footer .footer-top h4 {
  font-size: 16px;
  font-weight: bold;
  color: #444444;
  position: relative;
  padding-bottom: 12px;
}

#footer .footer-top .footer-links {
  margin-bottom: 30px;
}

#footer .footer-top .footer-links ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

#footer .footer-top .footer-links ul i {
  padding-right: 2px;
  color: #ea6981;
  font-size: 18px;
  line-height: 1;
}

#footer .footer-top .footer-links ul li {
  padding: 10px 0;
  display: flex;
  align-items: center;
}

#footer .footer-top .footer-links ul li:first-child {
  padding-top: 0;
}

#footer .footer-top .footer-links ul a {
  color: #777777;
  transition: 0.3s;
  display: inline-block;
  line-height: 1;
}

#footer .footer-top .footer-links ul a:hover {
  text-decoration: none;
  color: #e43c5c;
}

#footer .footer-newsletter {
  font-size: 15px;
}

#footer .footer-newsletter h4 {
  font-size: 16px;
  font-weight: bold;
  color: #444444;
  position: relative;
  padding-bottom: 12px;
}

#footer .footer-newsletter form {
  margin-top: 30px;
  background: #fff;
  padding: 6px 10px;
  position: relative;
  border-radius: 50px;
  text-align: left;
  border: 1px solid #f7c2cc;
}

#footer .footer-newsletter form input[type="email"] {
  border: 0;
  padding: 4px 8px;
  width: calc(100% - 100px);
}

#footer .footer-newsletter form input[type="submit"] {
  position: absolute;
  top: 0;
  right: -2px;
  bottom: 0;
  border: 0;
  background: none;
  font-size: 15px;
  padding: 0 22px;
  background: #e43c5c;
  color: #fff;
  transition: 0.3s;
  border-radius: 50px;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
}

#footer .footer-newsletter form input[type="submit"]:hover {
  background: #d01d3f;
}

#footer .credits {
  padding-top: 5px;
  font-size: 13px;
  color: #444444;
}

#footer .social-links a {
  font-size: 18px;
  display: inline-block;
  background: #e43c5c;
  color: #fff;
  line-height: 1;
  padding: 8px 0;
  margin-right: 4px;
  border-radius: 50%;
  text-align: center;
  width: 36px;
  height: 36px;
  transition: 0.3s;
}

#footer .social-links a:hover {
  background: #d01d3f;
  color: #fff;
  text-decoration: none;
}
