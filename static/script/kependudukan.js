$(document).ready(function() {

    $.get("/kependudukan/request-ktp/json", function(data) {

        for (i=0;i<data.length;i++){
            $(".card-container").append(
            `<div class="card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title">${data[i].fields.title}</h5>
                    <p class="card-text">${data[i].fields.date}</p>
                    <p class="card-text">${data[i].fields.date}</p>
                    <p class="card-text">${data[i].fields.description}</p>
                </div>
            </div>`
            )
        }
    })

    $("#add-task-btn").click(function(){
        $.post("/todolist/add/", 
            {
                title: $("#task-title").val(),
                description:$("#task-desc").val(),
            
            }, function(result, status) {
                    $(".card-container").append(
                        `<div class="card" style="width: 18rem;">
                            <div class="card-body">
                                <h5 class="card-title">${result.fields.title}</h5>
                                <p class="card-text">${result.fields.date}</p>
                                <p class="card-text">${result.fields.description}</p>
                            </div>
                        </div>`
                    )
                    $("#task-title").val('')
                    $("#task-desc").val('')
                }
            )


    })
})