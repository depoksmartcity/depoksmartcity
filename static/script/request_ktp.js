$(document).ready(function() {

    $('#id_schedule_date').addClass('form-control');

    $.get("/kependudukan/request-ktp/json", function(data) {

        for (i=0;i<data.length;i++){
            if (i === 0) $("#no-request").hide();
            $(".requests-card-container").append(
            `<div class="card">
                <div class="card-body">
                    <h5 class="card-title">Request</h5>
                    <h6 class="card-subtitle mb-2 text-muted">${data[i].fields.requested_at}</h6>
                    <p class="card-text">Provinsi: ${data[i].fields.provinsi}</p>
                    <p class="card-text">Kota: ${data[i].fields.kota}</p>
                    <p class="card-text">Kecamatan: ${data[i].fields.kecamatan}</p>
                    <p class="card-text">Kelurahan: ${data[i].fields.kelurahan}</p>
                    <p class="card-text">Permohonan: ${data[i].fields.permohonan}</p>
                    
                    <p class="card-text">Nama Lengkap: ${data[i].fields.nama_lengkap}</p>
                    <p class="card-text">Nomor KK: ${data[i].fields.nomor_kk}</p>
                    <p class="card-text">NIK: ${data[i].fields.nik}</p>
                    <p class="card-text">Alamat: ${data[i].fields.alamat}</p>
                    
                    <p class="card-text">RT: ${data[i].fields.rt}</p>
                    <p class="card-text">RW: ${data[i].fields.rw}</p>
                    <p class="card-text">Kode Pos: ${data[i].fields.kode_pos}</p>
                    
                    <p class="card-text">Nomor HP: ${data[i].fields.nomor_hp}</p>
                    
                    <h6 class="card-text">Jadwal Pemotretan Foto</h6>
                    <p class="card-text">${data[i].fields.schedule_date} ${data[i].fields.schedule_time} WIB</p>
                </div>
            </div>`
            );
        }
    })

    $("#add-request").click(function(){
        $.post("{% url 'kependudukan:add_request' %}", 
            {
                // ini bisa otomatis gak ya?
                title: $("#task-title").val(),
                description:$("#task-desc").val(),
            
            }, function(result, status) {
                    $("#no-request").hide();
                    $(".requests-card-container").append(
                        `<div class="card">
                            <div class="card-body">
                                <h5 class="card-title">Request</h5>
                                <h6 class="card-subtitle mb-2 text-muted">${result.fields.requested_at}</h6>
                                <p class="card-text">Provinsi: ${result.fields.provinsi}</p>
                                <p class="card-text">Kota: ${result.fields.kota}</p>
                                <p class="card-text">Kecamatan: ${result.fields.kecamatan}</p>
                                <p class="card-text">Kelurahan: ${result.fields.kelurahan}</p>
                                <p class="card-text">Permohonan: ${result.fields.permohonan}</p>
                                
                                <p class="card-text">Nama Lengkap: ${result.fields.nama_lengkap}</p>
                                <p class="card-text">Nomor KK: ${result.fields.nomor_kk}</p>
                                <p class="card-text">NIK: ${result.fields.nik}</p>
                                <p class="card-text">Alamat: ${result.fields.alamat}</p>
                                
                                <p class="card-text">RT: ${result.fields.rt}</p>
                                <p class="card-text">RW: ${result.fields.rw}</p>
                                <p class="card-text">Kode Pos: ${result.fields.kode_pos}</p>
                                
                                <p class="card-text">Nomor HP: ${result.fields.nomor_hp}</p>
                                
                                <h6 class="card-text">Jadwal Pemotretan Foto</h6>
                                <p class="card-text">${result.fields.schedule_date} ${result.fields.schedule_time} WIB</p>
                            </div>
                        </div>`
                    )
                    $("#request-ktp-form").reset()
                }
            )
    })
    
})