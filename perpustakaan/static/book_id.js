function bookData(data) {
    $.each(data, function(key, val) {        
      var image = document.createElement('img');
      var title = document.getElementById('book-title');
      var synopsis = document.getElementById('book-synopsis');
      var star1 = document.getElementById('star1');
      var star2 = document.getElementById('star2');
      var star3 = document.getElementById('star3');
      var star4 = document.getElementById('star4');
      var star5 = document.getElementById('star5');
      var author = document.getElementById('author');
      var publisher = document.getElementById('publisher');
      var publication_date = document.getElementById('publication_date');
      var isbn = document.getElementById('isbn');
      var edition = document.getElementById('edition');
      var pages = document.getElementById('pages');
      var stock = document.getElementById('stock');

      var borrowBtn = document.getElementById('borrowBtn');
      var returnBtn = document.getElementById('returnBtn');
      var reviewBtn = document.getElementById('reviewBtn');
      
      image.setAttribute('src', "{{ val.fields.photo }}");
      
      title.innerHTML = val.fields.title;

      synopsis.innerHTML = val.fields.synopsis;
      author.innerHTML = "By " + val.fields.author;
      publisher.innerHTML = "Published by " + val.fields.publisher;
      publication_date.innerHTML = val.fields.publication_date;
      isbn.innerHTML = "ISBN " + val.fields.isbn;
      edition.innerHTML = val.fields.edition + " edition";
      pages.innerHTML = val.fields.pages + " pages";
      stock.innerHTML = val.fields.stock + " stocks"; 

      if (Math.round(val.fields.rate) == 1) {
        star1.classList.add('checked');
      }
      else if (Math.round(val.fields.rate) == 2) {
        star1.classList.add('checked');
        star2.classList.add('checked');
      }
      else if(Math.round(val.fields.rate) == 3) {
        star1.classList.add('checked');
        star2.classList.add('checked');
        star3.classList.add('checked');
      }
      else if(Math.round(val.fields.rate) == 4) {
        star1.classList.add('checked');
        star2.classList.add('checked');
        star3.classList.add('checked');
        star4.classList.add('checked');
      }
      else if(Math.round(val.fields.rate) == 5) {
        star1.classList.add('checked');
        star2.classList.add('checked');
        star3.classList.add('checked');
        star4.classList.add('checked');
        star5.classList.add('checked');
      }

      borrowBtn.href = "borrow/" + val.pk;
      reviewBtn.href = "review/" + val.pk;
  });
  };

  function reviewData(data) {
    if (data.length == 0) {
      // If book is empty
      var pesan = document.createElement('p');
      pesan.innerHTML = 'Mohon maaf, belum ada review ditemukan!';
      pesan.style.margin = "0px 10px";

      $(document.body).append(pesan);

    } else {
      $.each(data, function(key, val) {
          var outerDiv1 = document.createElement('div');
          outerDiv1.classList.add('card')

          var outerDiv2 = document.createElement('div');
          outerDiv2.classList.add('container-fluid');

          var outerDiv3 = document.createElement('div');
          outerDiv3.classList.add('wrapper');
          outerDiv3.classList.add('row');

          var innerDiv = document.createElement('div');
          innerDiv.classList.add('details');
          innerDiv.classList.add('col-md-6');

          outerDiv1.append(outerDiv2);
          outerDiv2.append(outerDiv3);
          outerDiv3.append(innerDiv);
        
          
          var user = document.createElement('h3');
          var rate = document.createElement('p');
          var review = document.createElement('p');

          user.classList.add('product-title');
          rate.classList.add('review-no');
          review.classList.add('review-no');
          
          rate.innerHTML = "Rate: " + val.fields.rate + "/5";
          review.innerHTML = val.fields.review;


          innerDiv.append(user);
          innerDiv.append(rate);
          innerDiv.append(review);

          outerDiv = document.getElementById("review_list");
          outerDiv.append(outerDiv1);
      });
    }
  };

  function checkBorrowReturnButton(data) {
    if (data.length == 0) {
      // If no active borrow, can borrow, can't return  
      $("#returnForm").hide();
    }
    else {
      // If there's active borrow, can't borrow, can return  
      $("#borrowForm").hide();
    } 
  };

  function checkReviewButton(data) {
    // If No Book History, can't review
    if (data.length == 0) {
      $("#reviewBtn").hide();
    }
  };

  $("#addReview").submit(function (e) {
    e.preventDefault();
    var serializedData = $(this).serialize();
    $.ajax({
        url: "{% url 'perpustakaan:review' id %}",
        type: "POST",
        data: serializedData,
        dataType: 'text',
        success: function (data) {
            $("#add_modal").modal('hide');
            $('#addReview').each(function () {
                this.reset();
            });
        }
    });    
  });

  
