$(document).ready(function()  {
    showCard();
  });

  async function getData() {
    return fetch("restaurants/json").then((res) => res.json())
  }
  
  async function showCard() {
    const panel = document.getElementById("panel");
    const list = await getData()
    let cards = ``
    list.forEach((item) => {
      cards+=`
      <div class="col-12 col-md-6 col-lg-4 py-2">
        <div class="card .bg-dark .bg-gradient rounded">
          <div class="card-body">
            <img id="card-pic" src="${item.fields.img}" class="card-img-top" alt="...">
              <br><br>
              <h5 class="card-title">${item.fields.name}</h5>
              <p class="card-text">${item.fields.lokasi}</p>
              <p class="card-text"></p> 
              <button class="btn btn-outline-dark btn-lg px-5" onclick="detail(${item.pk})">more</button>
          </div>
        </div>
      </div>
      `;
    });

    panel.innerHTML = cards;

  }

  async function detail(id){
    const list = await getData()
    const detailCard = document.getElementById("detail");
    detailCard.innerHTML = "";
    detailCard.style.transform = "scale(1)";
    panel.style.opacity = 1;
    panel.style.opacity = 0.5;
    detailCard.style.opacity = 1;
    let detail_div = ``

    list.forEach((item) => {
      if(item.pk == id) {
        detail_div = `
        <div class="w-100">
          <span class="close float-end" onclick="closeDetail()">&times;</span>
        </div>

        <div class="col-md-3 border-end p-4">
          <img class="w-100" src="${item.fields.img}" alt="..."/>
          <div>
            <h2 class="display-6 text-center">${item.fields.name}</h2>
          </div>
        </div>

        <div class="col-md-9">
          <div class="container vertical-scrollable">
            <div class="card" style="width: 48rem;">
              <div class="card-body">
                <h5 class="card-title"><b>Deskripsi</b></h5>
                <p class="card-text">${item.fields.desc}</p>
              </div>
            </div>
            
            <br>

            <div class="card" style="width: 48rem;">
              <div class="card-body">
                <h5 class="card-title"><b>Lokasi</b></h5>
                <p class="card-text">${item.fields.lokasi}</p>
              </div>
            </div>
          </div>

          <br>
          <button class="btn btn-outline-dark btn-lg px-5" style = "position:relative; left:300px; " onclick="review(${item.pk})">Lihat Ulasan</button>
          
        `;
      }
    })
    detailCard.innerHTML = detail_div;
  }

  async function review(id){
    const list = await getData()
    const reviewCard = document.getElementById("review");
    reviewCard.innerHTML = "";
    reviewCard.style.transform = "scale(1)";
    panel.style.opacity = 1;
    panel.style.opacity = 0.5;
    reviewCard.style.opacity = 1;
    let review_div = ``
    
    let resto = ""

    list.forEach((item) => {
      if(item.pk == id) {
        resto = item
        console.log(item)
        console.log(resto)

        review_div = `
        <div class="w-100">
          <span class="close float-end" onclick="closeReview()">&times;</span>
          <h1><b>Ulasan</b></h1>
          <button class="btn btn-outline-dark btn-lg px-5" data-bs-toggle="modal" data-bs-target="#exampleModal" >Create Review</button>

        </div>

        
        
        <div class="container vertical-scrollable">
          <div class="row d-flex flex-wrap align-content-center p-3 border" id="reviewcontainer">
        
          </div>
        </div>


           `;
        
      }
    })
    

    document.getElementById("button").onclick = addReview(resto.pk)



    reviewCard.innerHTML = review_div;


  }

  function closeDetail(){
    const detailCard = document.getElementById("detail");
    const panel = document.getElementById("panel");
    detailCard.style.transform = "scale(0)";
    detailCard.style.opacity = 0;
    panel.style.opacity = 1;
  }

  function closeReview(){
    const reviewCard = document.getElementById("review");
    reviewCard.style.transform = "scale(0)";
    reviewCard.style.opacity = 0;
  }

  async function getReviews(id) {
    return fetch("/restaurants/json-rev/" + id).then((res) => res.json())
    
  }

  async function refreshReviews(id) {
    const review = document.getElementById("reviewcontainer");
    review.innerHTML = "";
    const reviews = await getReviews(id)
    let htmlString = ``
    reviews.forEach((item) => {
      if (item.fields.review != "" ) {
        htmlString += `
        <div class="card" style="width: 42rem;">
          <div class="card-body">
            <h5 class="card-title">REVIEW</h5>
            <p class="card-text">${item.fields.review}</p>
          </div>
        </div>`;
      }

    });
    
    review.innerHTML = htmlString
    }
  
    async function addReview(id) {
      const list = await getData();
      let res = ''

      list.forEach((item) => {
        if (item.pk == id) {
          res = item
        }
      })
      console.log(res)
      

      const csrf = document.getElementsByName('csrfmiddlewaretoken')
      var formData = new FormData()
      formData.append('csrfmiddlewaretoken', csrf[0].value)
      formData.append('review', document.getElementById('review-form').value)
      formData.append('pk_resto', id)
      const input = document.getElementById('review-form');
      input.value = '';
      fetch("restaurants/create-review", {
            method: "POST",
            body: formData
        }).then(refreshReviews(id))
      refreshReviews(id)

      return false
    }

    const reviewCard = document.getElementById("review");
    reviewCard.style.transform = "scale(0)";
    reviewCard.style.opacity = 0;
  

    