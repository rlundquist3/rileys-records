$(document).ready(function () {
    $("#genreButton").hover(function () {
        $("#genreList").slideDown("slow");
    });
});
$(document).ready(function () {
    $("#wishlistButton").hover(function () {
        $("#wishlistList").slideDown("slow");
    });
});
$(document).ready(function () {
    $("#albumButton").hover(function () {
        $("#albumList").slideDown("slow");
    });
});
$(document).ready(function () {
    $("#genreList").hover(function () {
        $("#genreList").show();
    }, function () {
        $("#genreList").slideUp("slow");
    });
});
$(document).ready(function () {
    $("#wishlistList").hover(function () {
        $("#wishlistList").show();
    }, function () {
        $("#wishlistList").slideUp("slow");
    });
});
$(document).ready(function () {
    $("#albumList").hover(function () {
        $("#albumList").show();
    }, function () {
        $("#albumList").slideUp("slow");
    });
});
$(document).ready(function () {
    var line = '<input type="text" name="personnel">';
    $("#addPersonnel").click(function () {
        $("#personnelList").append(line);
        $("#personnelList input").each(function(i) {
            $(this).attr('name', 'personnel'+(i+1));
        });
    });
});
$(document).ready(function () {
    var line = '<input type="text" name="producer">';
    $("#addProducer").click(function () {
        $("#producerList").append(line);
        $("#producerList input").each(function(i) {
            $(this).attr('name', 'producer'+(i+1));
        });
    });
});
$(document).ready(function () {
    var line = '<input type="text" name="track">';
    $("#addTrack").click(function () {
        $("#trackList").append(line);
        $("#trackList input").each(function(i) {
            $(this).attr('name', 'track'+(i+1));
        });
    });
});