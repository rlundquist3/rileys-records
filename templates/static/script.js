$(document).ready(function () {
    $(".genrestab").hover(function () {
        $(".genrelist").slideDown("slow");
    });
});
$(document).ready(function () {
    $(".wishlisttab").hover(function () {
        $(".wishlistlist").slideDown("slow");
    });
});
$(document).ready(function () {
    $(".albumstab").hover(function () {
        $(".albumlist").slideDown("slow");
    });
});
$(document).ready(function () {
    $(".genrelist").hover(function () {
        $(".genrelist").show();
    }, function () {
        $(".genrelist").slideUp("slow");
    });
});
$(document).ready(function () {
    $(".wishlistlist").hover(function () {
        $(".wishlistlist").show();
    }, function () {
        $(".wishlistlist").slideUp("slow");
    });
});
$(document).ready(function () {
    $(".albumlist").hover(function () {
        $(".albumlist").show();
    }, function () {
        $(".albumlist").slideUp("slow");
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
