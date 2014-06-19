;(function () {
	"use strict";

	var popupTab = document.getElementById("zf-popup-tab"),
		popup = document.getElementById("ZenaidaFeedback");

	popupTab.onclick = function () {
		var popupClass = popup.getAttribute("class");
		if (popupClass !== "in") {
			popup.setAttribute("class", "in");
		} else {
			popup.setAttribute("class", "");
		}
	}
}());
