function filemageDelete(button) {
    var id = $(button).attr('id');
    $(button).parents('tr#' + id).remove();
}

function filemageUpload(event) {
    let files = event.target.files;
    let f = files[0];

    var formdata = new FormData();
    formdata.append('file', f, f.name);
    formdata.append('csrfmiddlewaretoken', '{{}}');

    $.ajax({
        url: "/api/filemage/upload/",
        type: 'POST',
        data: formdata,
        processData: false,
        contentType: false,
    });
}

$(function () {
    $("button#filemageUpload").on("click", function () {
        $("input#filemageUpload").trigger("click");
    });
    $("input#filemageUpload").on("change", filemageUpload);
});