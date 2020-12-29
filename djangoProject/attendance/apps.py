.student-profile .card {
  border-radius: 10px;
}

.student-profile .card .card-header .profile_img {
  width: 150px;
  height: 150px;
  object-fit: cover;
  margin: 10px auto;
  border: 10px solid #ccc;
  border-radius: 50%;
  /* align-items: center; */
}

.student-profile .card h3 {
  font-size: 30px;
  font-weight: 700;
  color:#000;
}
h3{
  font-size: 30px;
  font-weight: 700;
  color: #000;
}



.student-profile .card p {
  font-size: 16px;
  color: #000;
}

.student-profile .table th,
.student-profile .table td {
  font-size: 14px;
  padding: 10px 15px;
  color: #000;
}



.button {
  display: inline-block;
  border-radius: 4px;
  background-color: #19b347;
  border: none;
  color: #FFFFFF;
  text-align: center;
  font-size: 16px;

  padding: 10px;
  width: 200px;
  transition: all 0.5s;
  cursor: pointer;
  margin: 5px;
}

.button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.button span:after {
  content: '\00bb';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;
}

.button:hover span {
  padding-right: 25px;
}

.button:hover span:after {
  opacity: 1;
  right: 0;
}

@media screen and (min-width: 1200px) {
  .col-lg-4 {
    width: 71%;

  }
}
