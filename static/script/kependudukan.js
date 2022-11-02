$(document).ready(function() {

    // reference: https://stackoverflow.com/questions/42319247/how-to-compare-two-strings-in-javascript-if-condition
    function areEqual(a, b){
        if (a.length !== b.length) return false;
        return a.localeCompare(b) === 0;
    }

    $.get("/kependudukan/json", function(data) {

        for (i=0;i<data.length;i++){
            if (areEqual(data[i].fields.name, "Beji")) {
                $("#kec-beji").append(
                    `<div class="card kelurahan-card">
                        <div class="card-body">
                            <h5 class="card-title">${data[i].fields.name}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">${data[i].fields.address}</h6>
                        </div>
                    </div>`
                )
            } else if (areEqual(data[i].fields.name, "Pancoran Mas")) {
                $("#kec-pancoran-mas").append(
                    `<div class="card kelurahan-card">
                        <div class="card-body">
                            <h5 class="card-title">${data[i].fields.name}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">${data[i].fields.address}</h6>
                        </div>
                    </div>`
                )
            } else if (areEqual(data[i].fields.name, "Cipayung")) {
                $("#kec-cipayung").append(
                    `<div class="card kelurahan-card">
                        <div class="card-body">
                            <h5 class="card-title">${data[i].fields.name}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">${data[i].fields.address}</h6>
                        </div>
                    </div>`
                )
            } else if (areEqual(data[i].fields.name, "Sukmajaya")) {
                $("#kec-sukmajaya").append(
                    `<div class="card kelurahan-card">
                        <div class="card-body">
                            <h5 class="card-title">${data[i].fields.name}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">${data[i].fields.address}</h6>
                        </div>
                    </div>`
                )
            } else if (areEqual(data[i].fields.name, "Cilodong")) {
                $("#kec-cilodong").append(
                    `<div class="card kelurahan-card">
                        <div class="card-body">
                            <h5 class="card-title">${data[i].fields.name}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">${data[i].fields.address}</h6>
                        </div>
                    </div>`
                )
            } else if (areEqual(data[i].fields.name, "Limo")) {
                $("#kec-limo").append(
                    `<div class="card kelurahan-card">
                        <div class="card-body">
                            <h5 class="card-title">${data[i].fields.name}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">${data[i].fields.address}</h6>
                        </div>
                    </div>`
                )
            } else if (areEqual(data[i].fields.name, "Cinere")) {
                $("#kec-cinere").append(
                    `<div class="card kelurahan-card">
                        <div class="card-body">
                            <h5 class="card-title">${data[i].fields.name}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">${data[i].fields.address}</h6>
                        </div>
                    </div>`
                )
            } else if (areEqual(data[i].fields.name, "Cimanggis")) {
                $("#kec-cimanggis").append(
                    `<div class="card kelurahan-card">
                        <div class="card-body">
                            <h5 class="card-title">${data[i].fields.name}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">${data[i].fields.address}</h6>
                        </div>
                    </div>`
                )
            } else if (areEqual(data[i].fields.name, "Tapos")) {
                $("#kec-tapos").append(
                    `<div class="card kelurahan-card">
                        <div class="card-body">
                            <h5 class="card-title">${data[i].fields.name}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">${data[i].fields.address}</h6>
                        </div>
                    </div>`
                )
            } else if (areEqual(data[i].fields.name, "Sawangan")) {
                $("#kec-sawangan").append(
                    `<div class="card kelurahan-card">
                        <div class="card-body">
                            <h5 class="card-title">${data[i].fields.name}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">${data[i].fields.address}</h6>
                        </div>
                    </div>`
                )
            } else if (areEqual(data[i].fields.name, "Bojong Sari")) {
                $("#kec-bojong-sari").append(
                    `<div class="card kelurahan-card">
                        <div class="card-body">
                            <h5 class="card-title">${data[i].fields.name}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">${data[i].fields.address}</h6>
                        </div>
                    </div>`
                )
            }
            
        }
    })

})