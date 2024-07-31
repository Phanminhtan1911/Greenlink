function performPost() {
    $.ajax({
        type: "POST",
        url: "{{ url_for('create_file') }}",
        data: {"name" : "Jim"},
    })
}