(function () {
	"use strict";

	var popupTab = $(".zf-popup-tab"),
		popup = $("#ZenaidaFeedback");

	popupTab.click(function () {
		popup.toggleClass("in");
	});

	$("#ZenaidaFeedback form").submit(function (e) {
		e.preventDefault();
	});

}());
