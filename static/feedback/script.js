(function () {
	"use strict";

	var $popupTab = $(".zf-popup-tab"),
		$popup = $("#ZenaidaFeedback"),
		$form = $("#ZenaidaFeedback form"),
		$popupBody = $(".zf-body"),
		$submitButton = $("#ZenaidaFeedback form button"),
		bind_submit = function () {
			$form.one("submit", on_submit);
		},
		on_submit = function (e) {
			$submitButton.attr("disabled", "disabled");
			$submitButton.css({"opacity":.5});
			$submitButton.text("Submitting...");
			$.ajax({
				type: $form.attr('method'),
				url: $form.attr('action'),
				data: $form.serialize(),
				success: function (data) {
					$popupBody.html("<div class='zf-thanks'>Thanks for your feedback!</div>")
				}
			});
		};

	// toggle the feedback form when clicking on the tab
	$popupTab.click(function () {
		$popup.toggleClass("in");
	});

	$form.on("submit", function (e) { e.preventDefault(); }); // always prevent the form from submitting
	bind_submit(); // allow the form to make an ajax call only once

}());
