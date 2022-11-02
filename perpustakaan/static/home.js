function bookData(data) {
    if (data.length == 0) {
      // If book is empty
      var pesan = document.createElement('p');
      pesan.innerHTML = 'Mohon maaf atas ketidaknyamanannya! Belum ada buku ditambahkan!';
      pesan.style.margin = "0px 10px";

      $(document.body).append(pesan);

    } else {
      $.each( data, function(key, val) {
          var outerDiv = document.createElement('div');
          outerDiv.classList.add('col-sm-3');

          var card_outer = document.createElement('div');
          card_outer.classList.add('card', 'text-bg-success', 'mb-3');

          var card_body = document.createElement('div');
          card_body.classList.add('card-body');

          card_outer.appendChild(card_body);
          
          var image = document.createElement('img');
          var title = document.createElement('a');
          var titleText = document.createTextNode(val.fields.title);
          var subtitle = document.createElement('h6');
          
          image.setAttribute('src', val.fields.photo);
          
          title.appendChild(titleText);
          title.classList.add('card-title');
          title.classList.add('link-light', 'text-decoration-none');
          title.href = "book/" + val.pk;

          subtitle.classList.add('card-subtitle');

          title.innerHTML = val.fields.title;
          subtitle.innerHTML = "Rate: " + val.fields.rate;
          
          card_body.appendChild(image);
          card_body.appendChild(title);
          card_body.appendChild(subtitle);

          outerDiv.appendChild(card_outer);

          $("#data").append(outerDiv);
      });
    }
  };