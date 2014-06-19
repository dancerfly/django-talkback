(function () {
	"use strict";

	var FORMDATA_SUPPORT = 'FormData' in window,
		$popupTab = $(".zf-popup-tab"),
		$popup = $("#ZenaidaFeedback"),
		$form = $("#ZenaidaFeedback form"),
		$popupBody = $(".zf-body"),
		$submitButton = $("#ZenaidaFeedback form button"),
		bind_submit = function () {
			$form.one("submit", on_submit);
		},
		on_submit = function (e) {
			// If HTML5 FormData support exists, file-uploads will work.
			// Otherwise jQuery.fn.serialize ignores file inputs.
			var form_data = FORMDATA_SUPPORT ? new FormData($form[0]) : $form.serialize();

			$submitButton.attr("disabled", "disabled");
			$submitButton.css({"opacity":.5});
			$submitButton.text("Submitting...");

			$.ajax({
				type: $form.attr('method'),
				url: $form.attr('action'),
				data: form_data,
				dataType: 'json',
				// Let jQuery process the data only if FormData is not supported:
				processData: !FORMDATA_SUPPORT,
				// Content type also depends on FormData support:
				contentType: FORMDATA_SUPPORT ? false : 'application/x-www-form-urlencoded; charset=UTF-8',
				success: function (data) {
					$popupBody.html("<div class='zf-thanks'>Thanks for your feedback!</div>")
				}
			});
		};

	// toggle the feedback form when clicking on the tab
	$popupTab.click(function () {
		$popup.toggleClass("in");
	});

	if (!FORMDATA_SUPPORT) {
		// Asynchronous file upload not supported:
		$('#zf-screenshot-group').hide();
	}

	$form.on("submit", function (e) { e.preventDefault(); }); // always prevent the form from submitting
	bind_submit(); // allow the form to make an ajax call only once

}());
