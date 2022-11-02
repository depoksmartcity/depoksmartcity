async function getAspirasi(){
    return fetch("/aspirasi/json/").then((res) => res.json())
  }
 
  async function refreshAspirasi(){
    document.getElementById("output").innerHTML = ""
    const aspirasi = await getAspirasi()
    let htmlString = ``
    htmlString+=`<p><b>List Aspirasi</b></p>`
    aspirasi.forEach(item=> {
      htmlString+=`\n
      <div class="cards" >
        <p>
        <span class="nowrap">${item.fields.aspirasi}</span>
        </p>
      </div>
      `
    });
    document.getElementById("output").innerHTML = htmlString
  }
  
  async function addAspirasi(url) {
    fetch(url, {
          method: "POST",
          body: new FormData(document.querySelector('#postAspirasi'))
      }).then(refreshAspirasi)
    return false
  }
  refreshAspirasi()
 
